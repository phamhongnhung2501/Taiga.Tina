# -*- coding: utf-8 -*-

from tina.base.api import validators
from tina.base.api import serializers
from tina.projects.notifications.validators import WatchersValidator

from . import models


class WikiPageValidator(WatchersValidator, validators.ModelValidator):
    slug = serializers.CharField()

    class Meta:
        model = models.WikiPage
        read_only_fields = ('modified_date', 'created_date', 'owner')


class WikiLinkValidator(validators.ModelValidator):
    class Meta:
        model = models.WikiLink
        read_only_fields = ('href',)
