# -*- coding: utf-8 -*-

from tina.base.api import validators

from . import models


class ContactEntryValidator(validators.ModelValidator):

    class Meta:
        model = models.ContactEntry
        read_only_fields = ("user", "created_date", )
