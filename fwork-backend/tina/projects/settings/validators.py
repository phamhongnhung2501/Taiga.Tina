# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _

from tina.base.api import validators
from tina.base.exceptions import ValidationError
from tina.projects.settings.utils import get_allowed_sections

from . import models


class UserProjectSettingsValidator(validators.ModelValidator):

    class Meta:
        model = models.UserProjectSettings
        read_only_fields = ('id', 'created_at', 'modified_at', 'project',
                            'user')

    def validate_homepage(self, attrs, source):
        if attrs[source] not in get_allowed_sections(self.object):
            msg = _("You don't have access to this section")
            raise ValidationError(msg)
        return attrs
