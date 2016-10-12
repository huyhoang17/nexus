# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-08 01:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0023_post_fictionhub'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.SlugField(blank=True, default='', max_length=256),
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='post',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='post',
            name='daily',
        ),
        migrations.RemoveField(
            model_name='post',
            name='fictionhub',
        ),
        migrations.RemoveField(
            model_name='post',
            name='imported',
        ),
        migrations.RemoveField(
            model_name='post',
            name='number',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_type',
        ),
        migrations.RemoveField(
            model_name='post',
            name='published',
        ),
        migrations.RemoveField(
            model_name='post',
            name='rational',
        ),
        migrations.RemoveField(
            model_name='post',
            name='reddit_url',
        ),
        migrations.RemoveField(
            model_name='post',
            name='state',
        ),
    ]
