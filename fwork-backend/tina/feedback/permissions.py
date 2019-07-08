# -*- coding: utf-8 -*-


from tina.base.api.permissions import TinaResourcePermission
from tina.base.api.permissions import IsAuthenticated


class FeedbackPermission(TinaResourcePermission):
    create_perms = IsAuthenticated()
