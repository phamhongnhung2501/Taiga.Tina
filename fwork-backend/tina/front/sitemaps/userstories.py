# -*- coding: utf-8 -*-

from django.db.models import Q
from django.apps import apps
from datetime import timedelta
from django.utils import timezone

from tina.front.templatetags.functions import resolve

from .base import Sitemap


class UserStoriesSitemap(Sitemap):
    def items(self):
        us_model = apps.get_model("userstories", "UserStory")

        # Get US of public projects OR private projects if anon user can view them
        queryset = us_model.objects.filter(Q(project__is_private=False) |
                                           Q(project__is_private=True,
                                             project__anon_permissions__contains=["view_us"]))

        # Exclude blocked projects
        queryset = queryset.filter(project__blocked_code__isnull=True)

        # Project data is needed
        queryset = queryset.select_related("project")

        return queryset

    def location(self, obj):
        return resolve("userstory", obj.project.slug, obj.ref)

    def lastmod(self, obj):
        return obj.modified_date

    def changefreq(self, obj):
        if (timezone.now() - obj.modified_date) > timedelta(days=90):
            return "monthly"
        return "weekly"

    def priority(self, obj):
        return 0.5
