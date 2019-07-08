# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _

from tina.base.api import serializers
from tina.base.api import validators
from tina.base.exceptions import ValidationError
from tina.base.fields import PgArrayField
from tina.base.fields import PickledObjectField
from tina.base.utils import json
from tina.projects.milestones.models import Milestone
from tina.projects.mixins.validators import AssignedToValidator
from tina.projects.models import UserStoryStatus
from tina.projects.notifications.mixins import EditableWatchedResourceSerializer
from tina.projects.notifications.validators import WatchersValidator
from tina.projects.tagging.fields import TagsAndTagsColorsField
from tina.projects.userstories.models import UserStory
from tina.projects.validators import ProjectExistsValidator

from . import models


class UserStoryExistsValidator:
    def validate_us_id(self, attrs, source):
        value = attrs[source]
        if not models.UserStory.objects.filter(pk=value).exists():
            msg = _("There's no user story with that id")
            raise ValidationError(msg)
        return attrs


class RolePointsField(serializers.WritableField):
    def to_native(self, obj):
        return {str(o.role.id): o.points.id for o in obj.all()}

    def from_native(self, obj):
        if isinstance(obj, dict):
            return obj
        return json.loads(obj)


class UserStoryValidator(AssignedToValidator, WatchersValidator,
                         EditableWatchedResourceSerializer, validators.ModelValidator):
    tags = TagsAndTagsColorsField(default=[], required=False)
    external_reference = PgArrayField(required=False)
    points = RolePointsField(source="role_points", required=False)
    tribe_gig = PickledObjectField(required=False)

    class Meta:
        model = models.UserStory
        depth = 0
        read_only_fields = ('id', 'ref', 'created_date', 'modified_date', 'owner')


class UserStoriesBulkValidator(ProjectExistsValidator, validators.Validator):
    project_id = serializers.IntegerField()
    status_id = serializers.IntegerField(required=False)
    bulk_stories = serializers.CharField()

    def validate_status_id(self, attrs, source):
        filters = {
            "project__id": attrs["project_id"],
            "id": attrs[source]
        }

        if not UserStoryStatus.objects.filter(**filters).exists():
            raise ValidationError(_("Invalid user story status id. The status must belong to "
                                    "the same project."))

        return attrs


# Order bulk validators

class _UserStoryOrderBulkValidator(validators.Validator):
    us_id = serializers.IntegerField()
    order = serializers.IntegerField()


class UpdateUserStoriesOrderBulkValidator(ProjectExistsValidator, validators.Validator):
    project_id = serializers.IntegerField()
    status_id = serializers.IntegerField(required=False)
    milestone_id = serializers.IntegerField(required=False)
    bulk_stories = _UserStoryOrderBulkValidator(many=True)

    def validate_status_id(self, attrs, source):
        filters = {
            "project__id": attrs["project_id"],
            "id": attrs[source]
        }

        if not UserStoryStatus.objects.filter(**filters).exists():
            raise ValidationError(_("Invalid user story status id. The status must belong "
                                    "to the same project."))

        return attrs

    def validate_milestone_id(self, attrs, source):
        filters = {
            "project__id": attrs["project_id"],
            "id": attrs[source]
        }

        if not Milestone.objects.filter(**filters).exists():
            raise ValidationError(_("Invalid milestone id. The milistone must belong to the "
                                    "same project."))

        return attrs

    def validate_bulk_stories(self, attrs, source):
        filters = {"project__id": attrs["project_id"]}
        if "milestone_id" in attrs:
            filters["milestone__id"] = attrs["milestone_id"]

        filters["id__in"] = [us["us_id"] for us in attrs[source]]

        if models.UserStory.objects.filter(**filters).count() != len(filters["id__in"]):
            raise ValidationError(_("Invalid user story ids. All stories must belong to the same project "
                                    "and, if it exists, to the same status and milestone."))

        return attrs


# Milestone bulk validators

class _UserStoryMilestoneBulkValidator(validators.Validator):
    us_id = serializers.IntegerField()
    order = serializers.IntegerField()


class UpdateMilestoneBulkValidator(ProjectExistsValidator, validators.Validator):
    project_id = serializers.IntegerField()
    milestone_id = serializers.IntegerField()
    bulk_stories = _UserStoryMilestoneBulkValidator(many=True)

    def validate_milestone_id(self, attrs, source):
        filters = {
            "project__id": attrs["project_id"],
            "id": attrs[source]
        }
        if not Milestone.objects.filter(**filters).exists():
            raise ValidationError(_("The milestone isn't valid for the project"))
        return attrs

    def validate_bulk_stories(self, attrs, source):
        filters = {
            "project__id": attrs["project_id"],
            "id__in": [us["us_id"] for us in attrs[source]]
        }

        if UserStory.objects.filter(**filters).count() != len(filters["id__in"]):
            raise ValidationError(_("All the user stories must be from the same project"))

        return attrs
