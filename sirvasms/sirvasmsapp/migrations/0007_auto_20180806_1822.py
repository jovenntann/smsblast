# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-06 10:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sirvasmsapp', '0006_daterange'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='buy',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='email',
            name='sell',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sms',
            name='buy',
            field=models.DecimalField(decimal_places=6, default='0', max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sms',
            name='sell',
            field=models.DecimalField(decimal_places=6, default=2, max_digits=8),
            preserve_default=False,
        ),
    ]
