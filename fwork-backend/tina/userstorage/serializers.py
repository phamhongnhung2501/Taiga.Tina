# -*- coding: utf-8 -*-

from tina.base.api import serializers
from tina.base.fields import Field


class StorageEntrySerializer(serializers.LightSerializer):
    key = Field()
    value = Field()
    created_date = Field()
    modified_date = Field()
