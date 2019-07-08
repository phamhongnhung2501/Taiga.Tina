# -*- coding: utf-8 -*-


from tina.base.api import permissions


class SystemStatsPermission(permissions.TinaResourcePermission):
    global_perms = permissions.AllowAny()


class DiscoverStatsPermission(permissions.TinaResourcePermission):
    global_perms = permissions.AllowAny()
