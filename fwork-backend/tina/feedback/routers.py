# -*- coding: utf-8 -*-

from tina.base import routers
from . import api


router = routers.DefaultRouter(trailing_slash=False)
router.register(r"feedback", api.FeedbackViewSet, base_name="feedback")
