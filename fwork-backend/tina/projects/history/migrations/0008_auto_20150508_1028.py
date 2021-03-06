# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tina.base.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0007_set_bloked_note_and_is_blocked_in_snapshots'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historyentry',
            name='diff',
            field=tina.base.db.models.fields.JSONField(null=True, default=None, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historyentry',
            name='snapshot',
            field=tina.base.db.models.fields.JSONField(null=True, default=None, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='historyentry',
            name='values',
            field=tina.base.db.models.fields.JSONField(null=True, default=None, blank=True),
            preserve_default=True,
        ),
    ]
