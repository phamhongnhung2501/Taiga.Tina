# -*- coding: utf-8 -*-

import uuid

from django.core.urlresolvers import reverse

from tina.base.utils.urls import get_absolute_url


# Set this in settings.PROJECT_MODULES_CONFIGURATORS["github"]
def get_or_generate_config(project):
    config = project.modules_config.config
    if config and "github" in config:
        g_config = project.modules_config.config["github"]
    else:
        g_config = {"secret": uuid.uuid4().hex}

    url = reverse("github-hook-list")
    url = get_absolute_url(url)
    url = "%s?project=%s" % (url, project.id)
    g_config["webhooks_url"] = url
    return g_config
