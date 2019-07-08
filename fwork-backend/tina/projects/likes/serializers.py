# -*- coding: utf-8 -*-

from tina.base.api import serializers
from tina.base.fields import Field, MethodField


class FanSerializer(serializers.LightSerializer):
    id = Field()
    username = Field()
    full_name = MethodField()

    def get_full_name(self, obj):
        return obj.get_full_name()
