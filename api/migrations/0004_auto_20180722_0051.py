# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-22 00:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180722_0036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='event',
        ),
        migrations.AddField(
            model_name='location',
            name='event_id',
            field=models.IntegerField(default=100),
        ),
    ]
