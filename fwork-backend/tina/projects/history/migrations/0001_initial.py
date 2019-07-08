# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tina.projects.history.models
import django.utils.timezone
import tina.base.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryEntry',
            fields=[
                ('id', models.CharField(primary_key=True, unique=True, max_length=255, serialize=False, default=tina.projects.history.models._generate_uuid, editable=False)),
                ('user', tina.base.db.models.fields.JSONField(default=None, blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.SmallIntegerField(choices=[(1, 'Change'), (2, 'Create'), (3, 'Delete')])),
                ('is_snapshot', models.BooleanField(default=False)),
                ('key', models.CharField(max_length=255, default=None, blank=True, null=True)),
                ('diff', tina.base.db.models.fields.JSONField(default=None, null=True)),
                ('snapshot', tina.base.db.models.fields.JSONField(default=None, null=True)),
                ('values', tina.base.db.models.fields.JSONField(default=None, null=True)),
                ('comment', models.TextField(blank=True)),
                ('comment_html', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
            bases=(models.Model,),
        ),
    ]
