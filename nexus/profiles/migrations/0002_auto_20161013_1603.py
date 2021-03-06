# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='reposted',
            field=models.ManyToManyField(blank=True, related_name='reposters', to='posts.Post'),
        ),
        migrations.AddField(
            model_name='user',
            name='upvoted',
            field=models.ManyToManyField(blank=True, related_name='upvoters', to='posts.Post'),
        ),
    ]
