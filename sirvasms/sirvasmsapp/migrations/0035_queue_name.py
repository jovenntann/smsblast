# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-03-18 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sirvasmsapp', '0034_auto_20190314_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='queue',
            name='name',
            field=models.CharField(default='Joven Tan', max_length=80),
            preserve_default=False,
        ),
    ]
