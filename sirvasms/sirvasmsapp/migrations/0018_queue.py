# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-03-05 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sirvasmsapp', '0017_auto_20190305_1857'),
    ]

    operations = [
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('from_number', models.CharField(max_length=1000)),
                ('to_number', models.CharField(max_length=1000)),
                ('user', models.CharField(max_length=80)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
    ]
