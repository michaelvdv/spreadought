# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice',
            field=models.BooleanField(default=False),
        ),
    ]
