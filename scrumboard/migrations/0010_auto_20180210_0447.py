# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-10 04:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0009_auto_20180210_0130'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'ordering': ['list', 'category']},
        ),
        migrations.AlterModelOptions(
            name='list',
            options={'ordering': ['lastname']},
        ),
    ]