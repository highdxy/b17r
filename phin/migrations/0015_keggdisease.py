# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-11 06:55
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chembl', '0001_initial'),
        ('phin', '0014_keggdiseaseclass'),
    ]

    operations = [
        migrations.CreateModel(
            name='KEGGDisease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kegg_id', models.CharField(max_length=64)),
                ('all_gene_accessions', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=32), blank=True, null=True, size=None)),
                ('chembl_mappings', models.ManyToManyField(to='chembl.ComponentSequences')),
                ('kegg_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phin.KEGGDiseaseClass')),
            ],
        ),
    ]