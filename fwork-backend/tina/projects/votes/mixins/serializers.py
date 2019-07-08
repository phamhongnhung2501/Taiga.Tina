# -*- coding: utf-8 -*-

from tina.base.api import serializers
from tina.base.fields import MethodField


class VoteResourceSerializerMixin(serializers.LightSerializer):
    is_voter = MethodField()
    total_voters = MethodField()

    def get_is_voter(self, obj):
        # The "is_voted" attribute is attached in the get_queryset of the viewset.
        return getattr(obj, "is_voter", False) or False

    def get_total_voters(self, obj):
        # The "total_voters" attribute is attached in the get_queryset of the viewset.
        return getattr(obj, "total_voters", 0) or 0
