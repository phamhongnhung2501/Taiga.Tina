# -*- coding: utf-8 -*-

from tina.base import response
from tina.base.api import viewsets

from . import permissions
from . import validators
from . import services

import copy


class FeedbackViewSet(viewsets.ViewSet):
    permission_classes = (permissions.FeedbackPermission,)
    validator_class = validators.FeedbackEntryValidator

    def create(self, request, **kwargs):
        self.check_permissions(request, "create", None)

        data = copy.deepcopy(request.DATA)
        data.update({"full_name": request.user.get_full_name(),
                     "email": request.user.email})

        validator = self.validator_class(data=data)
        if not validator.is_valid():
            return response.BadRequest(validator.errors)

        self.object = validator.save(force_insert=True)

        extra = {
            "HTTP_HOST":  request.META.get("HTTP_HOST", None),
            "HTTP_REFERER": request.META.get("HTTP_REFERER", None),
            "HTTP_USER_AGENT": request.META.get("HTTP_USER_AGENT", None),
        }
        services.send_feedback(self.object, extra, reply_to=[request.user.email])

        return response.Ok(validator.data)
