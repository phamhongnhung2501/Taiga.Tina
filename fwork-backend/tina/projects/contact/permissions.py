# -*- coding: utf-8 -*-

from tina.base.api.permissions import PermissionComponent
from tina.base.api.permissions import TinaResourcePermission


class IsContactActivated(PermissionComponent):
    def check_permissions(self, request, view, obj=None):
        if not request.user.is_authenticated() or not obj.project.is_contact_activated:
            return False

        if obj.project.is_private:
            return obj.project.cached_memberships_for_user(request.user)

        return True


class ContactPermission(TinaResourcePermission):
    create_perms = IsContactActivated()
