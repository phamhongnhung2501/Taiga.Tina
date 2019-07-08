# -*- coding: utf-8 -*-


from tina.base import exceptions as exc
from tina.base.api.utils import get_object_or_404

from django.apps import apps
from django.utils.translation import ugettext as _

import json

def get_user_for_application_token(token:str) -> object:
    """
    Given an application token it tries to find an associated user
    """
    app_token = apps.get_model("external_apps", "ApplicationToken").objects.filter(token=token).first()
    if not app_token:
        raise exc.NotAuthenticated(_("Invalid token"))
    return app_token.user


def authorize_token(application_id:int, user:object, state:str) -> object:
    ApplicationToken = apps.get_model("external_apps", "ApplicationToken")
    Application = apps.get_model("external_apps", "Application")
    application = get_object_or_404(Application, id=application_id)
    token, _ = ApplicationToken.objects.get_or_create(user=user, application=application)
    token.update_auth_code()
    token.state = state
    token.save()
    return token
