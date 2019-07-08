# -*- coding: utf-8 -*-

from tina.base.api.permissions import (TinaResourcePermission, HasProjectPerm,
                                       IsProjectAdmin, AllowAny)


class ResolverPermission(TinaResourcePermission):
    list_perms = HasProjectPerm('view_project')
