# -*- coding: utf-8 -*-

from markdown import Extension
from markdown.inlinepatterns import Pattern
from markdown.treeprocessors import Treeprocessor

from markdown.util import etree

from tina.front.templatetags.functions import resolve
from tina.base.utils.slug import slugify

import re


class WikiLinkExtension(Extension):
    def __init__(self, project, *args, **kwargs):
        self.project = project
        return super().__init__(*args, **kwargs)

    def extendMarkdown(self, md):
        WIKILINK_RE = r"\[\[([\w0-9_ -]+)(\|[^\]]+)?\]\]"
        md.inlinePatterns.add("wikilinks",
                              WikiLinksPattern(md, WIKILINK_RE, self.project),
                              "<not_strong")
        md.treeprocessors.add("relative_to_absolute_links",
                              RelativeLinksTreeprocessor(md, self.project),
                              "<prettify")


class WikiLinksPattern(Pattern):
    def __init__(self, md, pattern, project):
        self.project = project
        self.md = md
        super().__init__(pattern)

    def handleMatch(self, m):
        label = m.group(2).strip()
        url = resolve("wiki", self.project.slug, slugify(label))

        if m.group(3):
            title = m.group(3).strip()[1:]
        else:
            title = label

        a = etree.Element("a")
        a.text = title
        a.set("href", url)
        a.set("title", title)
        a.set("class", "reference wiki")
        return a


SLUG_RE = re.compile(r"^[-a-zA-Z0-9_]+$")


class RelativeLinksTreeprocessor(Treeprocessor):
    def __init__(self, md, project):
        self.project = project
        super().__init__(md)

    def run(self, root):
        links = root.getiterator("a")
        for a in links:
            href = a.get("href", "")

            if SLUG_RE.search(href):
                # [wiki](wiki_page) -> <a href="FRONT_HOST/.../wiki/wiki_page" ...
                url = resolve("wiki", self.project.slug, href)
                a.set("href", url)
                a.set("class", "reference wiki")

            elif href and href[0] == "/":
                # [some link](/some/link) -> <a href="FRONT_HOST/some/link" ...
                url = "{}{}".format(resolve("home"), href[1:])
                a.set("href", url)
