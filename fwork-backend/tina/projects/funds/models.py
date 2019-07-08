from django.db import models

# Create your models here.
from django.db import models
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


# Create your models here.

class Fund(models.Model):
    user_story = models.ForeignKey("userstories.UserStory", null=True, blank=True,
                                   related_name="pozits", verbose_name=_("user story"))

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, default=None,
                             related_name="pozits", verbose_name=_("owner"))
    name = models.ForeignKey("projects.Project",max_length=250, null=False, blank=False,
                            verbose_name=_("name"))
    subject = models.ForeignKey("tasks.Task",null=False, blank=False,
                               verbose_name=_("subject"))
    time = models.DateTimeField(null=True, blank=False)

    expense = models.BigIntegerField(null=True, blank=False)

    profit = models.BigIntegerField(null=True, blank=False)

    class Meta:
        verbose_name = "task"

        verbose_name_plural = "funds"