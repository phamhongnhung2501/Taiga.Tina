# -*- coding: utf-8 -*-

import pytest

from django.contrib.contenttypes.models import ContentType

from tina.projects.votes import services as votes, models

from .. import factories as f

pytestmark = pytest.mark.django_db


def test_add_vote():
    project = f.ProjectFactory()
    project_type = ContentType.objects.get_for_model(project)
    user = f.UserFactory()
    votes_qs = models.Votes.objects.filter(content_type=project_type, object_id=project.id)

    votes.add_vote(project, user)

    assert votes_qs.get().count == 1

    votes.add_vote(project, user)  # add_vote must be idempotent

    assert votes_qs.get().count == 1


def test_remove_vote():
    user = f.UserFactory()
    project = f.ProjectFactory()
    project_type = ContentType.objects.get_for_model(project)
    votes_qs = models.Votes.objects.filter(content_type=project_type, object_id=project.id)
    f.VotesFactory(content_type=project_type, object_id=project.id, count=1)
    f.VoteFactory(content_type=project_type, object_id=project.id, user=user)

    assert votes_qs.get().count == 1

    votes.remove_vote(project, user)

    assert votes_qs.get().count == 0

    votes.remove_vote(project, user)  # remove_vote must be idempotent

    assert votes_qs.get().count == 0


def test_get_votes():
    project = f.ProjectFactory()
    project_type = ContentType.objects.get_for_model(project)
    f.VotesFactory(content_type=project_type, object_id=project.id, count=4)

    assert votes.get_votes(project) == 4


def test_get_voters():
    f.UserFactory()
    project = f.ProjectFactory()
    project_type = ContentType.objects.get_for_model(project)
    vote = f.VoteFactory(content_type=project_type, object_id=project.id)

    assert list(votes.get_voters(project)) == [vote.user]


def test_get_voted():
    f.ProjectFactory()
    project = f.ProjectFactory()
    project_type = ContentType.objects.get_for_model(project)
    vote = f.VoteFactory(content_type=project_type, object_id=project.id)

    assert list(votes.get_voted(vote.user, type(project))) == [project]
