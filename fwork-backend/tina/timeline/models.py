# -*- coding: utf-8 -*-

from django.db import models
from tina.base.db.models.fields import JSONField
from django.utils import timezone

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from tina.projects.models import Project


class Timeline(models.Model):
    content_type = models.ForeignKey(ContentType, related_name="content_type_timelines")
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    namespace = models.CharField(max_length=250, default="default", db_index=True)
    event_type = models.CharField(max_length=250, db_index=True)
    project = models.ForeignKey(Project, null=True)
    data = JSONField()
    data_content_type = models.ForeignKey(ContentType, related_name="data_timelines")
    created = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        indexes = [
            models.Index(fields=['namespace', '-created']),
            models.Index(fields=['content_type', 'object_id', '-created']),
        ]


# Register all implementations
from .timeline_implementations import *

# Register all signals
from .signals import *
