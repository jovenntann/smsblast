# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-03-07 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sirvasmsapp', '0019_queue_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='queue',
            name='tag',
            field=models.CharField(default='Single', max_length=80),
            preserve_default=False,
        ),
    ]
