# -*- coding: utf-8 -*-

from django.core import mail
from django.core.urlresolvers import reverse

from tests import factories as f

from tina.base.utils import json

import pytest
pytestmark = pytest.mark.django_db


# Members can comment on a private project
# if the project has the contact activated
def test_member_create_comment_on_private_project(client):
    user = f.UserFactory.create()
    project = f.ProjectFactory.create(is_private=True)
    project.is_contact_activated = True
    m1 = f.MembershipFactory(user=project.owner, project=project)
    m2 = f.MembershipFactory(project=project, is_admin=True)
    m3 = f.MembershipFactory(user=user, project=project, is_admin=False)

    url = reverse("contact-list")

    contact_data = json.dumps({
        "project": project.id,
        "comment": "Testing comment"
    })

    client.login(user)

    assert len(mail.outbox) == 0
    response = client.post(url, contact_data, content_type="application/json")
    assert response.status_code == 201
    assert len(mail.outbox) == 1
    assert set(mail.outbox[0].to[0].split(", ")) == set([project.owner.email, m2.user.email])


# Non members user cannot comment on a private project
# even if the project has the contact activated
def test_guest_create_comment_on_private_project(client):
    user = f.UserFactory.create()
    project = f.ProjectFactory.create(is_private=True)
    project.is_contact_activated = True

    url = reverse("contact-list")

    contact_data = json.dumps({
        "project": project.id,
        "comment": "Testing comment"
    })

    client.login(user)

    response = client.post(url, contact_data, content_type="application/json")
    assert response.status_code == 403
    assert len(mail.outbox) == 0


# All user can comment on a public project
# if the project has the contact activated
def test_create_comment_on_public_project(client):
    user = f.UserFactory.create()
    project = f.ProjectFactory.create(is_private=False)
    project.is_contact_activated = True
    m1 = f.MembershipFactory(user=project.owner, project=project)
    m2 = f.MembershipFactory(project=project, is_admin=True)
    url = reverse("contact-list")

    contact_data = json.dumps({
        "project": project.id,
        "comment": "Testing comment"
    })

    client.login(user)

    assert len(mail.outbox) == 0
    response = client.post(url, contact_data, content_type="application/json")
    assert response.status_code == 201
    assert len(mail.outbox) == 1
    assert set(mail.outbox[0].to[0].split(", ")) == set([project.owner.email, m2.user.email])


# No user can comment on a project
# if the project does not have the contact activated
def test_create_comment_disabled(client):
    user = f.UserFactory.create()
    project = f.ProjectFactory.create()
    project.is_contact_activated = False
    project.save()
    f.MembershipFactory(user=project.owner, project=project, is_admin=True)

    url = reverse("contact-list")

    contact_data = json.dumps({
        "project": project.id,
        "comment": "Testing comment"
    })

    client.login(user)

    response = client.post(url, contact_data, content_type="application/json")
    assert response.status_code == 403
