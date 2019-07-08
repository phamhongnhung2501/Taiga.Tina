# -*- coding: utf-8 -*-

from tina.base.api import validators

from . import models


class FeedbackEntryValidator(validators.ModelValidator):
    class Meta:
        model = models.FeedbackEntry
