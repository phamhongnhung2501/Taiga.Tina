# -*- coding: utf-8 -*-

from django.core import validators as core_validators
from django.utils.translation import ugettext_lazy as _

from tina.base.api import serializers
from tina.base.api import validators
from tina.base.exceptions import ValidationError
from tina.base.fields import PgArrayField

from .models import User, Role

import re


######################################################
# User
######################################################

class UserValidator(validators.ModelValidator):
    class Meta:
        model = User
        fields = ("username", "full_name", "color", "bio", "lang",
                  "theme", "timezone", "is_active")

    def validate_username(self, attrs, source):
        value = attrs[source]
        validator = core_validators.RegexValidator(re.compile('^[\w.-]+$'), _("invalid username"),
                                                   _("invalid"))

        try:
            validator(value)
        except ValidationError:
            raise ValidationError(_("Required. 255 characters or fewer. Letters, "
                                    "numbers and /./-/_ characters'"))

        if (self.object and
                self.object.username != value and
                User.objects.filter(username=value).exists()):
            raise ValidationError(_("Invalid username. Try with a different one."))

        return attrs


class UserAdminValidator(UserValidator):
    class Meta:
        model = User
        # IMPORTANT: Maintain the UserSerializer Meta up to date
        # with this info (including here the email)
        fields = ("username", "full_name", "color", "bio", "lang",
                  "theme", "timezone", "is_active", "email", "read_new_terms")

    def validate_read_new_terms(self, attrs, source):
        value = attrs[source]
        if not value:
            raise ValidationError(
                _("Read new terms has to be true'"))

        return attrs


class RecoveryValidator(validators.Validator):
    token = serializers.CharField(max_length=200)
    password = serializers.CharField(min_length=6)


class ChangeEmailValidator(validators.Validator):
    email_token = serializers.CharField(max_length=200)


class CancelAccountValidator(validators.Validator):
    cancel_token = serializers.CharField(max_length=200)


######################################################
# Role
######################################################

class RoleValidator(validators.ModelValidator):
    permissions = PgArrayField(required=False)

    class Meta:
        model = Role
        fields = ('id', 'name', 'permissions', 'computable', 'project', 'order')
        i18n_fields = ("name",)


class ProjectRoleValidator(validators.ModelValidator):
    class Meta:
        model = Role
        fields = ('id', 'name', 'slug', 'order', 'computable')
