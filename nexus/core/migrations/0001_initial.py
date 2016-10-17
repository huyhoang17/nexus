# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True, max_length=512)),
                ('about', models.TextField(blank=True, default='', null=True)),
            ],
        ),
    ]