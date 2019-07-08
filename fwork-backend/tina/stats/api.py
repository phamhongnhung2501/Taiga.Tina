# -*- coding: utf-8 -*-

from collections import OrderedDict

from django.conf import settings
from django.views.decorators.cache import cache_page

from tina.base import response
from tina.base.api import viewsets

from . import permissions
from . import services


CACHE_TIMEOUT = getattr(settings, "STATS_CACHE_TIMEOUT", 0)


class BaseStatsViewSet(viewsets.ViewSet):
    @property
    def _cache_timeout(self):
        return CACHE_TIMEOUT

    def dispatch(self, *args, **kwargs):
        return cache_page(self._cache_timeout)(super().dispatch)(*args, **kwargs)


class SystemStatsViewSet(BaseStatsViewSet):
    permission_classes = (permissions.SystemStatsPermission,)

    def list(self, request, **kwargs):
        stats = OrderedDict()
        stats["users"] = services.get_users_public_stats()
        stats["projects"] = services.get_projects_public_stats()
        stats["userstories"] = services.get_user_stories_public_stats()
        return response.Ok(stats)


class DiscoverStatsViewSet(BaseStatsViewSet):
    permission_classes = (permissions.DiscoverStatsPermission,)

    def list(self, request, **kwargs):
        stats = OrderedDict()
        stats["projects"] = services.get_projects_discover_stats(user=request.user)
        return response.Ok(stats)
