# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from tina.base.utils.colors import generate_random_predefined_hex_color
from tina.base.utils.time import timestamp_ms
from tina.projects.tagging.models import TaggedMixin
from tina.projects.occ import OCCModelMixin
from tina.projects.notifications.mixins import WatchedModelMixin
from tina.projects.mixins.blocked import BlockedMixin


class Epic(OCCModelMixin, WatchedModelMixin, BlockedMixin, TaggedMixin, models.Model):
    ref = models.BigIntegerField(db_index=True, null=True, blank=True, default=None,
                                 verbose_name=_("ref"))
    project = models.ForeignKey("projects.Project", null=False, blank=False,
                                related_name="epics", verbose_name=_("project"))
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,
                              related_name="owned_epics", verbose_name=_("owner"),
                              on_delete=models.SET_NULL)
    status = models.ForeignKey("projects.EpicStatus", null=True, blank=True,
                               related_name="epics", verbose_name=_("status"),
                               on_delete=models.SET_NULL)
    epics_order = models.BigIntegerField(null=False, blank=False, default=timestamp_ms,
                                      verbose_name=_("epics order"))

    created_date = models.DateTimeField(null=False, blank=False,
                                        verbose_name=_("created date"),
                                        default=timezone.now)
    modified_date = models.DateTimeField(null=False, blank=False,
                                         verbose_name=_("modified date"))

    subject = models.TextField(null=False, blank=False,
                               verbose_name=_("subject"))
    description = models.TextField(null=False, blank=True, verbose_name=_("description"))
    color = models.CharField(max_length=32, null=False, blank=True,
                             default=generate_random_predefined_hex_color,
                             verbose_name=_("color"))
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True,
                                    default=None, related_name="epics_assigned_to_me",
                                    verbose_name=_("assigned to"))
    client_requirement = models.BooleanField(default=False, null=False, blank=True,
                                             verbose_name=_("is client requirement"))
    team_requirement = models.BooleanField(default=False, null=False, blank=True,
                                           verbose_name=_("is team requirement"))

    user_stories = models.ManyToManyField("userstories.UserStory", related_name="epics",
                                          through='RelatedUserStory',
                                          verbose_name=_("user stories"))
    external_reference = ArrayField(models.TextField(null=False, blank=False),
                                    null=True, blank=True, default=None, verbose_name=_("external reference"))

    attachments = GenericRelation("attachments.Attachment")

    _importing = None

    class Meta:
        verbose_name = "epic"
        verbose_name_plural = "epics"
        ordering = ["project", "epics_order", "ref"]

    def __str__(self):
        return "#{0} {1}".format(self.ref, self.subject)

    def __repr__(self):
        return "<Epic %s>" % (self.id)

    def save(self, *args, **kwargs):
        if not self._importing or not self.modified_date:
            self.modified_date = timezone.now()

        if not self.status:
            self.status = self.project.default_epic_status

        super().save(*args, **kwargs)


class RelatedUserStory(WatchedModelMixin, models.Model):
    user_story = models.ForeignKey("userstories.UserStory", on_delete=models.CASCADE)
    epic = models.ForeignKey("epics.Epic", on_delete=models.CASCADE)

    order = models.BigIntegerField(null=False, blank=False, default=timestamp_ms,
                                verbose_name=_("order"))

    class Meta:
        verbose_name = "related user story"
        verbose_name_plural = "related user stories"
        ordering = ["user_story", "order", "id"]
        unique_together = (("user_story", "epic"), )

    def __str__(self):
        return "{0} - {1}".format(self.epic_id, self.user_story_id)

    @property
    def project(self):
        return self.epic.project

    @property
    def project_id(self):
        return self.epic.project_id

    @property
    def owner(self):
        return self.epic.owner

    @property
    def owner_id(self):
        return self.epic.owner_id

    @property
    def assigned_to_id(self):
        return self.epic.assigned_to_id
