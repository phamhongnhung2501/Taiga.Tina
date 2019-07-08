# -*- coding: utf-8 -*-

from markdown.extensions import Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree

from tina.projects.references.services import get_instance_by_ref
from tina.front.templatetags.functions import resolve


class TinaReferencesExtension(Extension):
    def __init__(self, project, *args, **kwargs):
        self.project = project
        return super().__init__(*args, **kwargs)

    def extendMarkdown(self, md):
        Tina_REFERENCE_RE = r'(?<=^|(?<=[^a-zA-Z0-9-\[]))#(\d+)'
        referencesPattern = TinaReferencesPattern(Tina_REFERENCE_RE, self.project)
        referencesPattern.md = md
        md.inlinePatterns.add('tina-references', referencesPattern, '_begin')


class TinaReferencesPattern(Pattern):
    def __init__(self, pattern, project):
        self.project = project
        super().__init__(pattern)

    def handleMatch(self, m):
        obj_ref = m.group(2)

        instance = get_instance_by_ref(self.project.id, obj_ref)
        if instance is None or instance.content_object is None:
            return "#{}".format(obj_ref)

        subject = instance.content_object.subject

        if instance.content_type.model == "epic":
            html_classes = "reference epic"
        elif instance.content_type.model == "userstory":
            html_classes = "reference user-story"
        elif instance.content_type.model == "task":
            html_classes = "reference task"
        elif instance.content_type.model == "issue":
            html_classes = "reference issue"
        else:
            return "#{}".format(obj_ref)

        url = resolve(instance.content_type.model, self.project.slug, obj_ref)

        link_text = "&num;{}".format(obj_ref)

        a = etree.Element('a')
        a.text = link_text
        a.set('href', url)
        a.set('title', "#{} {}".format(obj_ref, subject))
        a.set('class', html_classes)

        self.md.extracted_data['references'].append(instance.content_object)

        return a
