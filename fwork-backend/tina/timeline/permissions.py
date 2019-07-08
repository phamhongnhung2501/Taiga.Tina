# -*- coding: utf-8 -*-

from tina.base.api.permissions import TinaResourcePermission, AllowAny, IsSuperUser
from tina.permissions.permissions import HasProjectPerm, IsProjectAdmin


class UserTimelinePermission(TinaResourcePermission):
    enought_perms = IsSuperUser()
    global_perms = None
    retrieve_perms = AllowAny()


class ProjectTimelinePermission(TinaResourcePermission):
    enought_perms = IsProjectAdmin() | IsSuperUser()
    global_perms = None
    retrieve_perms = HasProjectPerm('view_project')
