# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-14 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_resolver', '0002_auto_20200504_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='CivilStructure',
            fields=[
                ('id', models.CharField(max_length=19, primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=12)),
                ('location', models.CharField(max_length=100)),
                ('basically_intact_square', models.CharField(max_length=6)),
                ('damaged_square', models.CharField(max_length=6)),
                ('destroyed_square', models.CharField(max_length=6)),
                ('note', models.CharField(max_length=200)),
                ('reporting_unit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CollapseRecord',
            fields=[
                ('id', models.CharField(max_length=19, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=12)),
                ('type', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=10)),
                ('note', models.CharField(max_length=200)),
                ('picture', models.BinaryField(max_length=8388608)),
                ('reporting_unit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DeathStatics',
            fields=[
                ('id', models.CharField(max_length=19, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=12)),
                ('number', models.IntegerField(max_length=5)),
                ('reporting_unit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DisasterRequest',
            fields=[
                ('id', models.CharField(max_length=19, primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=12)),
                ('disasterType', models.CharField(max_length=3)),
                ('status', models.CharField(max_length=1)),
                ('o_URL', models.CharField(max_length=200)),
                ('requestunit', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DisatserPrediction',
            fields=[
                ('id', models.CharField(max_length=19, primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=12)),
                ('location', models.CharField(max_length=100)),
                ('longtitude', models.FloatField(max_length=100)),
                ('latitude', models.FloatField(max_length=100)),
                ('depth', models.FloatField(max_length=100)),
                ('magnitude', models.FloatField(max_length=100)),
                ('Intensity', models.CharField(max_length=6)),
                ('type', models.CharField(max_length=2)),
                ('note', models.CharField(max_length=200)),
                ('picture', models.BinaryField(max_length=8388608)),
                ('reporting_unit', models.CharField(max_length=50)),
            ],
        ),
    ]