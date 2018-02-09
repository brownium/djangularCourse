# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-08 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0002_auto_20180208_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='firstname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='list',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='list',
            unique_together=set([('title', 'firstname', 'lastname')]),
        ),
    ]