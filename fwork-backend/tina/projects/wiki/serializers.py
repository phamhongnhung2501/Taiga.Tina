# -*- coding: utf-8 -*-

from tina.base.api import serializers
from tina.base.fields import Field, MethodField
from tina.projects.history import services as history_service
from tina.projects.mixins.serializers import ProjectExtraInfoSerializerMixin
from tina.projects.notifications.mixins import WatchedResourceSerializer
from tina.mdrender.service import render as mdrender


class WikiPageSerializer(
    WatchedResourceSerializer, ProjectExtraInfoSerializerMixin,
    serializers.LightSerializer
):
    id = Field()
    project = Field(attr="project_id")
    slug = Field()
    content = Field()
    owner = Field(attr="owner_id")
    last_modifier = Field(attr="last_modifier_id")
    created_date = Field()
    modified_date = Field()

    html = MethodField()
    editions = MethodField()

    version = Field()

    def get_html(self, obj):
        return mdrender(obj.project, obj.content)

    def get_editions(self, obj):
        return history_service.get_history_queryset_by_model_instance(obj).count() + 1  # +1 for creation


class WikiLinkSerializer(serializers.LightSerializer):
    id = Field()
    project = Field(attr="project_id")
    title = Field()
    href = Field()
    order = Field()
