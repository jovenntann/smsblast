# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-03-14 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sirvasmsapp', '0032_goip_prefix_prov'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='dateSent',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]