# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-08 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sirvasmsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sms',
            name='messageID',
            field=models.CharField(max_length=80),
        ),
    ]
