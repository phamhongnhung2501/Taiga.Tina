# -*- coding: utf-8 -*-

import pytest
import io
from .. import factories as f

from tina.base.utils import json
from tina.export_import.services import render_project

pytestmark = pytest.mark.django_db


def test_export_issue_finish_date(client):
    issue = f.IssueFactory.create(finished_date="2014-10-22T00:00:00+0000")
    output = io.BytesIO()
    render_project(issue.project, output)
    project_data = json.loads(output.getvalue())
    finish_date = project_data["issues"][0]["finished_date"]
    assert finish_date == "2014-10-22T00:00:00+0000"


def test_export_user_story_finish_date(client):
    user_story = f.UserStoryFactory.create(finish_date="2014-10-22T00:00:00+0000")
    output = io.BytesIO()
    render_project(user_story.project, output)
    project_data = json.loads(output.getvalue())
    finish_date = project_data["user_stories"][0]["finish_date"]
    assert finish_date == "2014-10-22T00:00:00+0000"


def test_export_epic_with_user_stories(client):
    epic = f.EpicFactory.create(subject="test epic export")
    user_story = f.UserStoryFactory.create(project=epic.project)
    f.RelatedUserStory.create(epic=epic, user_story=user_story)
    output = io.BytesIO()
    render_project(user_story.project, output)
    project_data = json.loads(output.getvalue())
    assert project_data["epics"][0]["subject"] == "test epic export"
    assert len(project_data["epics"]) == 1

    assert project_data["epics"][0]["related_user_stories"][0]["user_story"] == user_story.ref
    assert len(project_data["epics"][0]["related_user_stories"]) == 1
