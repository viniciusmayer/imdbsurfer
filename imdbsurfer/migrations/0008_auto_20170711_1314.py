# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdbsurfer', '0007_auto_20170709_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='minutes',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
