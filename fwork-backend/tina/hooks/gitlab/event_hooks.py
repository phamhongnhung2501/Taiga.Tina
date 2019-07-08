# -*- coding: utf-8 -*-

import re
import os

from tina.hooks.event_hooks import BaseNewIssueEventHook, BaseIssueCommentEventHook, BasePushEventHook


class BaseGitLabEventHook():
    platform = "GitLab"
    platform_slug = "gitlab"

    def replace_gitlab_references(self, project_url, wiki_text):
        if wiki_text is None:
            wiki_text = ""

        template = "\g<1>[GitLab#\g<2>]({}/issues/\g<2>)\g<3>".format(project_url)
        return re.sub(r"(\s|^)#(\d+)(\s|$)", template, wiki_text, 0, re.M)


class IssuesEventHook(BaseGitLabEventHook, BaseNewIssueEventHook):
    def ignore(self):
        return self.payload.get('object_attributes', {}).get("action", "") != "open"

    def get_data(self):
        description = self.payload.get('object_attributes', {}).get('description', None)
        project_url = self.payload.get('repository', {}).get('homepage', "")
        user_name = self.payload.get('user', {}).get('username', None)
        return {
            "number": self.payload.get('object_attributes', {}).get('iid', None),
            "subject": self.payload.get('object_attributes', {}).get('title', None),
            "url": self.payload.get('object_attributes', {}).get('url', None),
            "user_id": None,
            "user_name": user_name,
            "user_url": os.path.join(os.path.dirname(os.path.dirname(project_url)), "u", user_name),
            "description": self.replace_gitlab_references(project_url, description),
        }


class IssueCommentEventHook(BaseGitLabEventHook, BaseIssueCommentEventHook):
    def ignore(self):
        return self.payload.get('object_attributes', {}).get("noteable_type", None) != "Issue"

    def get_data(self):
        comment_message = self.payload.get('object_attributes', {}).get('note', None)
        project_url = self.payload.get('repository', {}).get('homepage', "")
        number = self.payload.get('issue', {}).get('iid', None)
        user_name = self.payload.get('user', {}).get('username', None)
        return {
            "number": number,
            "url": os.path.join(project_url, "issues", str(number)),
            "user_id": None,
            "user_name": user_name,
            "user_url": os.path.join(os.path.dirname(os.path.dirname(project_url)), "u", user_name),
            "comment_url": self.payload.get('object_attributes', {}).get('url', None),
            "comment_message": self.replace_gitlab_references(project_url, comment_message),
        }


class PushEventHook(BaseGitLabEventHook, BasePushEventHook):
    def get_data(self):
        result = []
        for commit in self.payload.get("commits", []):
            user_name = commit.get('author', {}).get('name', None)
            result.append({
                "user_id": None,
                "user_name": user_name,
                "user_url": None,
                "commit_id": commit.get("id", None),
                "commit_url": commit.get("url", None),
                "commit_message": commit.get("message").strip(),
                "commit_short_message": commit.get("message").split("\n")[0].strip(),
            })
        return result
