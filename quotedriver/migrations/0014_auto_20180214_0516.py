# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-14 05:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotedriver', '0013_auto_20180214_0510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to='quotedriver.List'),
        ),
    ]