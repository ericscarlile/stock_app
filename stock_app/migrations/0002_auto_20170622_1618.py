# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 21:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='last_updated',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stock',
            name='price_target',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
