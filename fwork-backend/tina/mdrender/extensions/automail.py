# -*- coding: utf-8 -*-

import markdown


# We can't re-use the built-in AutomailPattern because we need to add mailto:.
# We also don't care about HTML-encoding the email.
class AutomailPattern(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        el = markdown.util.etree.Element("a")
        el.set('href', self.unescape('mailto:' + m.group(2)))
        el.text = markdown.util.AtomicString(m.group(2))
        return el


class AutomailExtension(markdown.Extension):
    """An extension that turns all email addresses into links."""

    def extendMarkdown(self, md):
        mail_re = r'\b(?i)([a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]+)\b'
        automail = AutomailPattern(mail_re, md)
        md.inlinePatterns.add('gfm-automail', automail, '_end')
