# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-17 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phin', '0002_auto_20181216_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icd',
            name='level',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
