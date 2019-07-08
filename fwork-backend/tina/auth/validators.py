# -*- coding: utf-8 -*-

from django.core import validators as core_validators
from django.utils.translation import ugettext as _

from tina.base.api import serializers
from tina.base.api import validators
from tina.base.exceptions import ValidationError

import re


class BaseRegisterValidator(validators.Validator):
    full_name = serializers.CharField(max_length=256)
    email = serializers.EmailField(max_length=255)
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(min_length=4)

    def validate_username(self, attrs, source):
        value = attrs[source]
        validator = core_validators.RegexValidator(re.compile('^[\w.-]+$'), _("invalid username"), "invalid")

        try:
            validator(value)
        except ValidationError:
            raise ValidationError(_("Required. 255 characters or fewer. Letters, numbers "
                                    "and /./-/_ characters'"))
        return attrs


class PublicRegisterValidator(BaseRegisterValidator):
    pass


class PrivateRegisterValidator(BaseRegisterValidator):
    token = serializers.CharField(max_length=255, required=True)
