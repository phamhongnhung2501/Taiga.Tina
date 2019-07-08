# -*- coding: utf-8 -*-

from tina.base.api.permissions import TinaResourcePermission, IsAuthenticated, DenyAll


class StorageEntriesPermission(TinaResourcePermission):
    enought_perms = IsAuthenticated()
    global_perms = DenyAll()
