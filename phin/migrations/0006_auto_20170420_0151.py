# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 01:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phin', '0005_auto_20170420_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='targetinteraction',
            name='first_target',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='as_first', to='phin.Target'),
        ),
        migrations.AlterField(
            model_name='targetinteraction',
            name='second_target',
            field=models.ForeignKey(db_index=False, on_delete=django.db.models.deletion.CASCADE, related_name='as_second', to='phin.Target'),
        ),
    ]