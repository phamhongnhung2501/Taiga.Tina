# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _

from tina.base.exceptions import ValidationError
from tina.base.api import serializers
from tina.base.api import validators
from tina.projects.notifications.validators import WatchersValidator
from tina.projects.userstories.models import UserStory
from tina.projects.validators import DuplicatedNameInProjectValidator
from tina.projects.validators import ProjectExistsValidator
from . import models


class MilestoneExistsValidator:
    def validate_milestone_id(self, attrs, source):
        value = attrs[source]
        if not models.Milestone.objects.filter(pk=value).exists():
            msg = _("There's no milestone with that id")
            raise ValidationError(msg)
        return attrs


class MilestoneValidator(WatchersValidator, DuplicatedNameInProjectValidator, validators.ModelValidator):
    class Meta:
        model = models.Milestone
        read_only_fields = ("id", "created_date", "modified_date")


# bulk validators
class _UserStoryMilestoneBulkValidator(validators.Validator):
    us_id = serializers.IntegerField()
    order = serializers.IntegerField()


class UpdateMilestoneBulkValidator(MilestoneExistsValidator,
                                   ProjectExistsValidator,
                                   validators.Validator):
    project_id = serializers.IntegerField()
    milestone_id = serializers.IntegerField()
    bulk_stories = _UserStoryMilestoneBulkValidator(many=True)

    def validate_bulk_stories(self, attrs, source):
        filters = {
            "project__id": attrs["project_id"],
            "id__in": [us["us_id"] for us in attrs[source]]
        }

        if UserStory.objects.filter(**filters).count() != len(filters["id__in"]):
            raise ValidationError(_("All the user stories must be from the same project"))

        return attrs
