# -*- coding: utf-8 -*-


from tina.base.api.permissions import TinaResourcePermission, AllowAny


class AuthPermission(TinaResourcePermission):
    create_perms = AllowAny()
    register_perms = AllowAny()
