# -*- coding: utf-8 -*-

import uuid

from django.core.urlresolvers import reverse
from django.conf import settings

from tina.base.utils.urls import get_absolute_url


# Set this in settings.PROJECT_MODULES_CONFIGURATORS["gitlab"]
def get_or_generate_config(project):
    config = project.modules_config.config
    if config and "gitlab" in config:
        g_config = project.modules_config.config["gitlab"]
    else:
        g_config = {
            "secret": uuid.uuid4().hex,
            "valid_origin_ips": settings.GITLAB_VALID_ORIGIN_IPS,
        }

    url = reverse("gitlab-hook-list")
    url = get_absolute_url(url)
    url = "{}?project={}&key={}".format(url, project.id, g_config["secret"])
    g_config["webhooks_url"] = url
    return g_config
