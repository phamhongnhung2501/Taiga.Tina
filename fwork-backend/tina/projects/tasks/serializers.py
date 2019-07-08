# -*- coding: utf-8 -*-

from tina.base.api import serializers
from tina.base.fields import Field, MethodField
from tina.base.neighbors import NeighborsSerializerMixin

from tina.mdrender.service import render as mdrender
from tina.projects.attachments.serializers import BasicAttachmentsInfoSerializerMixin
from tina.projects.due_dates.serializers import DueDateSerializerMixin
from tina.projects.mixins.serializers import OwnerExtraInfoSerializerMixin
from tina.projects.mixins.serializers import ProjectExtraInfoSerializerMixin
from tina.projects.mixins.serializers import AssignedToExtraInfoSerializerMixin
from tina.projects.mixins.serializers import StatusExtraInfoSerializerMixin
from tina.projects.notifications.mixins import WatchedResourceSerializer
from tina.projects.tagging.serializers import TaggedInProjectResourceSerializer
from tina.projects.votes.mixins.serializers import VoteResourceSerializerMixin
from tina.projects.history.mixins import TotalCommentsSerializerMixin


class TaskListSerializer(VoteResourceSerializerMixin, WatchedResourceSerializer,
                         OwnerExtraInfoSerializerMixin, AssignedToExtraInfoSerializerMixin,
                         StatusExtraInfoSerializerMixin, ProjectExtraInfoSerializerMixin,
                         BasicAttachmentsInfoSerializerMixin, TaggedInProjectResourceSerializer,
                         TotalCommentsSerializerMixin, DueDateSerializerMixin,
                         serializers.LightSerializer):

    id = Field()
    user_story = Field(attr="user_story_id")
    ref = Field()
    project = Field(attr="project_id")
    milestone = Field(attr="milestone_id")
    milestone_slug = MethodField()
    created_date = Field()
    modified_date = Field()
    finished_date = Field()
    subject = Field()
    us_order = Field()
    taskboard_order = Field()
    is_iocaine = Field()
    external_reference = Field()
    version = Field()
    watchers = Field()
    is_blocked = Field()
    blocked_note = Field()
    is_closed = MethodField()
    user_story_extra_info = Field()

    def get_generated_user_stories(self, obj):
        assert hasattr(obj, "generated_user_stories_attr"),\
            "instance must have a generated_user_stories_attr attribute"
        return obj.generated_user_stories_attr

    def get_milestone_slug(self, obj):
        return obj.milestone.slug if obj.milestone else None

    def get_is_closed(self, obj):
        return obj.status is not None and obj.status.is_closed


class TaskSerializer(TaskListSerializer):
    comment = MethodField()
    generated_user_stories = MethodField()
    blocked_note_html = MethodField()
    description = Field()
    description_html = MethodField()

    def get_comment(self, obj):
        return ""

    def get_blocked_note_html(self, obj):
        return mdrender(obj.project, obj.blocked_note)

    def get_description_html(self, obj):
        return mdrender(obj.project, obj.description)


class TaskNeighborsSerializer(NeighborsSerializerMixin, TaskSerializer):
    pass
