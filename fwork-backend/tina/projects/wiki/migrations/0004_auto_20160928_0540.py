# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-28 05:40
from __future__ import unicode_literals

from django.db import migrations, models
import tina.base.utils.time


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0003_auto_20160615_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wikilink',
            name='order',
            field=models.BigIntegerField(default=tina.base.utils.time.timestamp_ms, verbose_name='order'),
        ),
    ]
