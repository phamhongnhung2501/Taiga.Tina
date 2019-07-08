# -*- coding: utf-8 -*-

from django.conf import settings

from tina.base.utils.thumbnails import get_thumbnail_url, get_thumbnail


def get_timeline_image_thumbnail_name(attachment):
    if attachment.attached_file:
        thumbnail = get_thumbnail(attachment.attached_file, settings.THN_ATTACHMENT_TIMELINE)
        return thumbnail.name if thumbnail else None
    return None


def get_card_image_thumbnail_url(attachment):
    if attachment.attached_file:
        return get_thumbnail_url(attachment.attached_file, settings.THN_ATTACHMENT_CARD)
    return None


def get_attachment_image_preview_url(attachment):
    if attachment.attached_file:
        return get_thumbnail_url(attachment.attached_file, settings.THN_ATTACHMENT_PREVIEW)
    return None
