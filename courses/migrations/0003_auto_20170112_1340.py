# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-12 13:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20161219_1554'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CourseAttendance',
            new_name='CourseEnrolment',
        ),
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(related_name='courses_enrolled', through='courses.CourseEnrolment', to=settings.AUTH_USER_MODEL),
        ),
    ]
