# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-09 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0004_auto_20180209_0236'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='about',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]