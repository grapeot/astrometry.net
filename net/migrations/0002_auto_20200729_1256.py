# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-29 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('net', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='display_name',
            field=models.CharField(max_length=256),
        ),
    ]