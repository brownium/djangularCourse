# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-14 04:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotedriver', '0011_auto_20180210_0736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='business_value',
        ),
        migrations.RemoveField(
            model_name='card',
            name='story_points',
        ),
    ]
