# -*- coding: utf-8 -*-

from django.forms import widgets
from django.utils.translation import ugettext as _
from tina.base.api import serializers, ISO_8601
from tina.base.api.settings import api_settings

import serpy


####################################################################
# DRF Serializer fields (OLD)
####################################################################
# NOTE: This should be in other place, for example tina.base.api.serializers


class JSONField(serializers.WritableField):
    """
    Json objects serializer.
    """
    widget = widgets.Textarea

    def to_native(self, obj):
        return obj

    def from_native(self, data):
        return data


class PgArrayField(serializers.WritableField):
    """
    PgArray objects serializer.
    """
    widget = widgets.Textarea

    def to_native(self, obj):
        return obj

    def from_native(self, data):
        return data


class PickledObjectField(serializers.WritableField):
    """
    PickledObjectField objects serializer.
    """
    widget = widgets.Textarea

    def to_native(self, obj):
        return obj

    def from_native(self, data):
        return data


class WatchersField(serializers.WritableField):
    def to_native(self, obj):
        return obj

    def from_native(self, data):
        return data


####################################################################
# Serpy fields (NEW)
####################################################################

class Field(serpy.Field):
    pass


class MethodField(serpy.MethodField):
    pass


class I18NField(Field):
    def to_value(self, value):
        ret = super(I18NField, self).to_value(value)
        return _(ret)


class I18NJSONField(Field):
    """
    Json objects serializer.
    """
    def __init__(self, i18n_fields=(), *args, **kwargs):
        super(I18NJSONField, self).__init__(*args, **kwargs)
        self.i18n_fields = i18n_fields

    def translate_values(self, d):
        i18n_d = {}
        if d is None:
            return d

        for key, value in d.items():
            if isinstance(value, dict):
                i18n_d[key] = self.translate_values(value)

            if key in self.i18n_fields:
                if isinstance(value, list):
                    i18n_d[key] = [e is not None and _(str(e)) or e for e in value]
                if isinstance(value, str):
                    i18n_d[key] = value is not None and _(value) or value
            else:
                i18n_d[key] = value

        return i18n_d

    def to_native(self, obj):
        i18n_obj = self.translate_values(obj)
        return i18n_obj


class FileField(Field):
    def to_value(self, value):
        if value:
            return value.name
        return None


class DateTimeField(Field):
    format = api_settings.DATETIME_FORMAT

    def to_value(self, value):
        if value is None or self.format is None:
            return value

        if self.format.lower() == ISO_8601:
            ret = value.isoformat()
            if ret.endswith("+00:00"):
                ret = ret[:-6] + "Z"
            return ret
        return value.strftime(self.format)
