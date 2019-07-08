# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-28 07:55
from __future__ import unicode_literals

from django.db import migrations, models
import tina.base.utils.time


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_auto_20160614_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='taskboard_order',
            field=models.BigIntegerField(default=tina.base.utils.time.timestamp_ms, verbose_name='taskboard order'),
        ),
        migrations.AlterField(
            model_name='task',
            name='us_order',
            field=models.BigIntegerField(default=tina.base.utils.time.timestamp_ms, verbose_name='us order'),
        ),
    ]
