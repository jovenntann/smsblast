# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-08 09:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sirvasmsapp', '0003_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sms',
            old_name='messageID',
            new_name='MessageSid',
        ),
    ]
