# -*- coding: utf-8 -*-

import pytest
from unittest.mock import patch
from unittest.mock import Mock

from .. import factories as f

from tina.projects.history import services


pytestmark = pytest.mark.django_db(transaction=True)


from tina.base.utils import json

def test_webhooks_when_create_milestone(settings):
    settings.WEBHOOKS_ENABLED = True
    project = f.ProjectFactory()
    f.WebhookFactory.create(project=project)
    f.WebhookFactory.create(project=project)

    obj = f.MilestoneFactory.create(project=project)

    with patch('tina.webhooks.tasks._send_request') as send_request_mock:
        services.take_snapshot(obj, user=obj.owner)
        assert send_request_mock.call_count == 2

        (webhook_id, url, key, data) = send_request_mock.call_args[0]
        assert data["action"] == "create"
        assert data["type"] == "milestone"
        assert data["by"]["id"] == obj.owner.id
        assert "date" in data
        assert data["data"]["id"] == obj.id


def test_webhooks_when_update_milestone(settings):
    settings.WEBHOOKS_ENABLED = True
    project = f.ProjectFactory()
    f.WebhookFactory.create(project=project)
    f.WebhookFactory.create(project=project)

    obj = f.MilestoneFactory.create(project=project)

    with patch('tina.webhooks.tasks._send_request') as send_request_mock:
        services.take_snapshot(obj, user=obj.owner)
        assert send_request_mock.call_count == 2

    obj.name = "test webhook update"
    obj.save()

    with patch('tina.webhooks.tasks._send_request') as send_request_mock:
        services.take_snapshot(obj, user=obj.owner, comment="test_comment")
        assert send_request_mock.call_count == 2

        (webhook_id, url, key, data) = send_request_mock.call_args[0]
        assert data["action"] == "change"
        assert data["type"] == "milestone"
        assert data["by"]["id"] == obj.owner.id
        assert "date" in data
        assert data["data"]["id"] == obj.id
        assert data["data"]["name"] == obj.name
        assert data["change"]["comment"] == "test_comment"
        assert data["change"]["diff"]["name"]["to"] == data["data"]["name"]
        assert data["change"]["diff"]["name"]["from"] !=  data["data"]["name"]


def test_webhooks_when_delete_milestone(settings):
    settings.WEBHOOKS_ENABLED = True
    project = f.ProjectFactory()
    f.WebhookFactory.create(project=project)
    f.WebhookFactory.create(project=project)

    obj = f.MilestoneFactory.create(project=project)

    with patch('tina.webhooks.tasks._send_request') as send_request_mock:
        services.take_snapshot(obj, user=obj.owner, delete=True)
        assert send_request_mock.call_count == 2

        (webhook_id, url, key, data) = send_request_mock.call_args[0]
        assert data["action"] == "delete"
        assert data["type"] == "milestone"
        assert data["by"]["id"] == obj.owner.id
        assert "date" in data
        assert "data" in data
