# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-10 01:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0007_auto_20180210_0125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='description',
            new_name='text',
        ),
    ]