# -*- coding: utf-8 -*-

from tina.base.api.permissions import TinaResourcePermission
from tina.base.api.permissions import IsAuthenticated
from tina.base.api.permissions import PermissionComponent


class ApplicationPermission(TinaResourcePermission):
    retrieve_perms = IsAuthenticated()
    token_perms = IsAuthenticated()
    list_perms = IsAuthenticated()


class CanUseToken(PermissionComponent):
    def check_permissions(self, request, view, obj=None):
        if not obj:
            return False

        return request.user == obj.user


class ApplicationTokenPermission(TinaResourcePermission):
    retrieve_perms = IsAuthenticated() & CanUseToken()
    by_application_perms = IsAuthenticated()
    create_perms = IsAuthenticated()
    update_perms = IsAuthenticated() & CanUseToken()
    partial_update_perms = IsAuthenticated() & CanUseToken()
    destroy_perms = IsAuthenticated() & CanUseToken()
    list_perms = IsAuthenticated()
