# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _

from tina.base.api import serializers
from tina.base.api import validators
from tina.base.exceptions import ValidationError
from tina.base.fields import PgArrayField
from tina.projects.milestones.models import Milestone
from tina.projects.mixins.validators import AssignedToValidator
from tina.projects.notifications.mixins import EditableWatchedResourceSerializer
from tina.projects.notifications.validators import WatchersValidator
from tina.projects.tagging.fields import TagsAndTagsColorsField
from tina.projects.validators import ProjectExistsValidator

from . import models


class IssueValidator(AssignedToValidator, WatchersValidator, EditableWatchedResourceSerializer,
                     validators.ModelValidator):

    tags = TagsAndTagsColorsField(default=[], required=False)
    external_reference = PgArrayField(required=False)

    class Meta:
        model = models.Issue
        read_only_fields = ('id', 'ref', 'created_date', 'modified_date', 'owner')


class IssuesBulkValidator(ProjectExistsValidator, validators.Validator):
    project_id = serializers.IntegerField()
    milestone_id = serializers.IntegerField(required=False)
    bulk_issues = serializers.CharField()


# Milestone bulk validators

class _IssueMilestoneBulkValidator(validators.Validator):
    issue_id = serializers.IntegerField()


class UpdateMilestoneBulkValidator(ProjectExistsValidator, validators.Validator):
    project_id = serializers.IntegerField()
    milestone_id = serializers.IntegerField()
    bulk_issues = _IssueMilestoneBulkValidator(many=True)

    def validate_milestone_id(self, attrs, source):
        filters = {
            "project__id": attrs["project_id"],
            "id": attrs[source]
        }
        if not Milestone.objects.filter(**filters).exists():
            raise ValidationError(_("The milestone isn't valid for the project"))
        return attrs

    def validate_bulk_tasks(self, attrs, source):
        filters = {
            "project__id": attrs["project_id"],
            "id__in": [issue["issue_id"] for issue in attrs[source]]
        }

        if models.Issue.objects.filter(**filters).count() != len(filters["id__in"]):
            raise ValidationError(_("All the issues must be from the same project"))

        return attrs
