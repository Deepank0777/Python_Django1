# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-28 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='time',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
    ]
