# -*- coding: utf-8 -*-

from tina.base.api import serializers
from tina.base.fields import MethodField


class TaggedInProjectResourceSerializer(serializers.LightSerializer):
    tags = MethodField()

    def get_tags(self, obj):
        if not obj.tags:
            return []

        project_tag_colors = dict(obj.project.tags_colors)
        return [[tag, project_tag_colors.get(tag, None)] for tag in obj.tags]
