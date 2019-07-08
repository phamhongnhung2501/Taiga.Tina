# -*- coding: utf-8 -*-

from django.utils.translation import ugettext as _

from tina.base.api import serializers
from tina.base.api import validators
from tina.base.exceptions import ValidationError
from tina.base.fields import PgArrayField
from tina.projects.mixins.validators import AssignedToValidator
from tina.projects.notifications.mixins import EditableWatchedResourceSerializer
from tina.projects.notifications.validators import WatchersValidator
from tina.projects.tagging.fields import TagsAndTagsColorsField
from tina.projects.validators import ProjectExistsValidator
from . import models


class EpicExistsValidator:
    def validate_epic_id(self, attrs, source):
        value = attrs[source]
        if not models.Epic.objects.filter(pk=value).exists():
            msg = _("There's no epic with that id")
            raise ValidationError(msg)
        return attrs


class EpicValidator(AssignedToValidator, WatchersValidator, EditableWatchedResourceSerializer,
                    validators.ModelValidator):
    tags = TagsAndTagsColorsField(default=[], required=False)
    external_reference = PgArrayField(required=False)

    class Meta:
        model = models.Epic
        read_only_fields = ('id', 'ref', 'created_date', 'modified_date', 'owner')


class EpicsBulkValidator(ProjectExistsValidator, EpicExistsValidator,
                         validators.Validator):
    project_id = serializers.IntegerField()
    status_id = serializers.IntegerField(required=False)
    bulk_epics = serializers.CharField()


class CreateRelatedUserStoriesBulkValidator(ProjectExistsValidator, EpicExistsValidator,
                                            validators.Validator):
    project_id = serializers.IntegerField()
    bulk_userstories = serializers.CharField()


class EpicRelatedUserStoryValidator(validators.ModelValidator):
    class Meta:
        model = models.RelatedUserStory
        read_only_fields = ('id',)
