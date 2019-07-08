# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from tina.base.utils.time import timestamp_ms
from tina.projects.due_dates.models import DueDateMixin
from tina.projects.occ import OCCModelMixin
from tina.projects.notifications.mixins import WatchedModelMixin
from tina.projects.mixins.blocked import BlockedMixin
from tina.projects.tagging.models import TaggedMixin


class Task(OCCModelMixin, WatchedModelMixin, BlockedMixin, TaggedMixin, DueDateMixin, models.Model):
    user_story = models.ForeignKey("userstories.UserStory", null=True, blank=True,
                                   related_name="tasks", verbose_name=_("user story"))
    ref = models.BigIntegerField(db_index=True, null=True, blank=True, default=None,
                                 verbose_name=_("ref"))
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, default=None,
                              related_name="owned_tasks", verbose_name=_("owner"))
    status = models.ForeignKey("projects.TaskStatus", null=True, blank=True,
                               related_name="tasks", verbose_name=_("status"))
    project = models.ForeignKey("projects.Project", null=False, blank=False,
                                related_name="tasks", verbose_name=_("project"))
    milestone = models.ForeignKey("milestones.Milestone", null=True, blank=True, on_delete=models.SET_NULL,
                                  default=None, related_name="tasks",
                                  verbose_name=_("milestone"))
    created_date = models.DateTimeField(null=False, blank=False,
                                        verbose_name=_("created date"),
                                        default=timezone.now)
    modified_date = models.DateTimeField(null=False, blank=False,
                                         verbose_name=_("modified date"))
    finished_date = models.DateTimeField(null=True, blank=True,
                                         verbose_name=_("finished date"))
    subject = models.TextField(null=False, blank=False,
                               verbose_name=_("subject"))

    us_order = models.BigIntegerField(null=False, blank=False, default=timestamp_ms,
                                        verbose_name=_("us order"))
    taskboard_order = models.BigIntegerField(null=False, blank=False, default=timestamp_ms,
                                          verbose_name=_("taskboard order"))

    description = models.TextField(null=False, blank=True, verbose_name=_("description"))
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True,
                                    default=None, related_name="tasks_assigned_to_me",
                                    verbose_name=_("assigned to"))
    attachments = GenericRelation("attachments.Attachment")
    is_iocaine = models.BooleanField(default=False, null=False, blank=True,
                                     verbose_name=_("is iocaine"))
    external_reference = ArrayField(models.TextField(null=False, blank=False),
                                    null=True, blank=True, default=None, verbose_name=_("external reference"))
    _importing = None

    class Meta:
        verbose_name = "task"
        verbose_name_plural = "tasks"
        ordering = ["project", "created_date", "ref"]
        # unique_together = ("ref", "project")
        permissions = (
            ("view_task", "Can view task"),
        )

    def save(self, *args, **kwargs):
        if not self._importing or not self.modified_date:
            self.modified_date = timezone.now()

        if not self.status:
            self.status = self.project.default_task_status

        return super().save(*args, **kwargs)

    def __str__(self):
        return "({1}) {0}".format(self.ref, self.subject)

    @property
    def is_closed(self):
        return self.status is not None and self.status.is_closed
