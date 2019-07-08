# -*- coding: utf-8 -*-

from tina.base.api.permissions import (TinaResourcePermission, IsAuthenticated)


class UserProjectSettingsPermission(TinaResourcePermission):
    retrieve_perms = IsAuthenticated()
    create_perms = IsAuthenticated()
    update_perms = IsAuthenticated()
    partial_update_perms = IsAuthenticated()
    destroy_perms = IsAuthenticated()
    list_perms = IsAuthenticated()
