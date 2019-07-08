# -*- coding: utf-8 -*-

from tina.base.exceptions import BaseException

from django.utils.translation import ugettext_lazy as _


class ConnectorBaseException(BaseException):
    status_code = 400
    default_detail = _("Connection error.")
