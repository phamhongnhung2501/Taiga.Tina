# -*- coding: utf-8 -*-

from tina.base.api.permissions import TinaResourcePermission, AllowAny


class LocalesPermission(TinaResourcePermission):
    global_perms = AllowAny()
