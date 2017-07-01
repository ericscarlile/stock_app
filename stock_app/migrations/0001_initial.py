# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 20:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ticker', models.CharField(max_length=5, unique=True)),
                ('is_bullish', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=24, unique=True)),
                ('password', models.CharField(max_length=150)),
            ],
        ),
    ]
