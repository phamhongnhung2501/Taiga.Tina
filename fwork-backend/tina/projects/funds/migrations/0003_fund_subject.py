# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-05 12:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_add_due_date'),
        ('funds', '0002_auto_20190705_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='fund',
            name='subject',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.Task', verbose_name='subject'),
            preserve_default=False,
        ),
    ]
