# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model

from markdown.extensions import Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree, AtomicString


class MentionsExtension(Extension):
    def extendMarkdown(self, md):
        MENTION_RE = r"(@)([\w.-]+)"
        mentionsPattern = MentionsPattern(MENTION_RE)
        mentionsPattern.md = md
        md.inlinePatterns.add("mentions", mentionsPattern, "_end")


class MentionsPattern(Pattern):
    def handleMatch(self, m):
        username = m.group(3)

        try:
            user = get_user_model().objects.get(username=username)
        except get_user_model().DoesNotExist:
            return "@{}".format(username)

        url = "/profile/{}".format(username)

        link_text = "@{}".format(username)

        a = etree.Element('a')
        a.text = AtomicString(link_text)

        a.set('href', url)
        a.set('title', user.get_full_name())
        a.set('class', "mention")

        self.md.extracted_data['mentions'].append(user)

        return a
