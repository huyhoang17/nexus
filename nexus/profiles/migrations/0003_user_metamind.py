# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20161013_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='metamind',
            field=models.BooleanField(default=False),
        ),
    ]
