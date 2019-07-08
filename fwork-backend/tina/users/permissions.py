# -*- coding: utf-8 -*-

from tina.base.api.permissions import TinaResourcePermission
from tina.base.api.permissions import IsSuperUser
from tina.base.api.permissions import AllowAny
from tina.base.api.permissions import IsAuthenticated
from tina.base.api.permissions import HasProjectPerm
from tina.base.api.permissions import IsProjectAdmin
from tina.base.api.permissions import PermissionComponent


class IsTheSameUser(PermissionComponent):
    def check_permissions(self, request, view, obj=None):
        return obj and request.user.is_authenticated() and request.user.pk == obj.pk


class UserPermission(TinaResourcePermission):
    enought_perms = IsSuperUser()
    global_perms = None
    retrieve_perms = AllowAny()
    by_username_perms = retrieve_perms
    update_perms = IsTheSameUser()
    partial_update_perms = IsTheSameUser()
    destroy_perms = IsTheSameUser()
    list_perms = AllowAny()
    stats_perms = AllowAny()
    password_recovery_perms = AllowAny()
    change_password_from_recovery_perms = AllowAny()
    change_password_perms = IsAuthenticated()
    change_avatar_perms = IsAuthenticated()
    me_perms = IsAuthenticated()
    remove_avatar_perms = IsAuthenticated()
    change_email_perms = AllowAny()
    contacts_perms = AllowAny()
    liked_perms = AllowAny()
    voted_perms = AllowAny()
    watched_perms = AllowAny()


class RolesPermission(TinaResourcePermission):
    retrieve_perms = HasProjectPerm('view_project')
    create_perms = IsProjectAdmin()
    update_perms = IsProjectAdmin()
    partial_update_perms = IsProjectAdmin()
    destroy_perms = IsProjectAdmin()
    list_perms = AllowAny()
