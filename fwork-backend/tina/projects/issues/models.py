# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
from django.utils import timezone
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from tina.projects.due_dates.models import DueDateMixin
from tina.projects.occ import OCCModelMixin
from tina.projects.notifications.mixins import WatchedModelMixin
from tina.projects.mixins.blocked import BlockedMixin
from tina.projects.tagging.models import TaggedMixin


class Issue(OCCModelMixin, WatchedModelMixin, BlockedMixin, TaggedMixin, DueDateMixin, models.Model):
    ref = models.BigIntegerField(db_index=True, null=True, blank=True, default=None,
                                 verbose_name=_("ref"))
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, default=None,
                              related_name="owned_issues", verbose_name=_("owner"))
    status = models.ForeignKey("projects.IssueStatus", null=True, blank=True,
                               related_name="issues", verbose_name=_("status"))
    severity = models.ForeignKey("projects.Severity", null=True, blank=True,
                                 related_name="issues", verbose_name=_("severity"))
    priority = models.ForeignKey("projects.Priority", null=True, blank=True,
                                 related_name="issues", verbose_name=_("priority"))
    type = models.ForeignKey("projects.IssueType", null=True, blank=True,
                             related_name="issues", verbose_name=_("type"))
    milestone = models.ForeignKey("milestones.Milestone", null=True, blank=True,
                                  default=None, related_name="issues",
                                  verbose_name=_("milestone"))
    project = models.ForeignKey("projects.Project", null=False, blank=False,
                                related_name="issues", verbose_name=_("project"))
    created_date = models.DateTimeField(null=False, blank=False,
                                        verbose_name=_("created date"),
                                        default=timezone.now)
    modified_date = models.DateTimeField(null=False, blank=False,
                                         verbose_name=_("modified date"))
    finished_date = models.DateTimeField(null=True, blank=True,
                                         verbose_name=_("finished date"))
    subject = models.TextField(null=False, blank=False,
                               verbose_name=_("subject"))
    description = models.TextField(null=False, blank=True, verbose_name=_("description"))
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True,
                                    default=None, related_name="issues_assigned_to_me",
                                    verbose_name=_("assigned to"))
    attachments = GenericRelation("attachments.Attachment")
    external_reference = ArrayField(models.TextField(null=False, blank=False),
                                    null=True, blank=True, default=None, verbose_name=_("external reference"))
    _importing = None

    class Meta:
        verbose_name = "issue"
        verbose_name_plural = "issues"
        ordering = ["project", "-id"]
        permissions = (
            ("view_issue", "Can view issue"),
        )

    def save(self, *args, **kwargs):
        if not self._importing or not self.modified_date:
            self.modified_date = timezone.now()

        if not self.status_id:
            self.status = self.project.default_issue_status

        if not self.type_id:
            self.type = self.project.default_issue_type

        if not self.severity_id:
            self.severity = self.project.default_severity

        if not self.priority_id:
            self.priority = self.project.default_priority

        return super().save(*args, **kwargs)

    def __str__(self):
        return "({1}) {0}".format(self.ref, self.subject)

    @property
    def is_closed(self):
        return self.status is not None and self.status.is_closed
