# -*- coding: utf-8 -*-

from tina.base.api import serializers
from tina.base.fields import Field, MethodField
from tina.base.neighbors import NeighborsSerializerMixin

from tina.mdrender.service import render as mdrender
from tina.projects.attachments.serializers import BasicAttachmentsInfoSerializerMixin
from tina.projects.mixins.serializers import OwnerExtraInfoSerializerMixin
from tina.projects.mixins.serializers import ProjectExtraInfoSerializerMixin
from tina.projects.mixins.serializers import AssignedToExtraInfoSerializerMixin
from tina.projects.mixins.serializers import StatusExtraInfoSerializerMixin
from tina.projects.notifications.mixins import WatchedResourceSerializer
from tina.projects.tagging.serializers import TaggedInProjectResourceSerializer
from tina.projects.votes.mixins.serializers import VoteResourceSerializerMixin


class EpicListSerializer(VoteResourceSerializerMixin, WatchedResourceSerializer,
                         OwnerExtraInfoSerializerMixin, AssignedToExtraInfoSerializerMixin,
                         StatusExtraInfoSerializerMixin, ProjectExtraInfoSerializerMixin,
                         BasicAttachmentsInfoSerializerMixin,
                         TaggedInProjectResourceSerializer, serializers.LightSerializer):

    id = Field()
    ref = Field()
    project = Field(attr="project_id")
    created_date = Field()
    modified_date = Field()
    subject = Field()
    color = Field()
    epics_order = Field()
    client_requirement = Field()
    team_requirement = Field()
    version = Field()
    watchers = Field()
    is_blocked = Field()
    blocked_note = Field()
    is_closed = MethodField()
    user_stories_counts = MethodField()

    def get_is_closed(self, obj):
        return obj.status is not None and obj.status.is_closed

    def get_user_stories_counts(self, obj):
        assert hasattr(obj, "user_stories_counts"), "instance must have a user_stories_counts attribute"
        return obj.user_stories_counts


class EpicSerializer(EpicListSerializer):
    comment = MethodField()
    blocked_note_html = MethodField()
    description = Field()
    description_html = MethodField()

    def get_comment(self, obj):
        return ""

    def get_blocked_note_html(self, obj):
        return mdrender(obj.project, obj.blocked_note)

    def get_description_html(self, obj):
        return mdrender(obj.project, obj.description)


class EpicNeighborsSerializer(NeighborsSerializerMixin, EpicSerializer):
    pass


class EpicRelatedUserStorySerializer(serializers.LightSerializer):
    epic = Field(attr="epic_id")
    user_story = Field(attr="user_story_id")
    order = Field()
