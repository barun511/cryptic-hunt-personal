# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-05 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunt', '0009_submission'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='accepted',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
