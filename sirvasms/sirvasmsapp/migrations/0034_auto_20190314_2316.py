# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-03-14 23:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sirvasmsapp', '0033_auto_20190314_2240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='queue',
            old_name='from_number',
            new_name='provider',
        ),
    ]
