# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-03-05 10:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sirvasmsapp', '0015_received_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='received',
            name='body',
        ),
    ]
