# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-24 12:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qualifications', '0004_auto_20161223_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualification',
            name='date_granted',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]