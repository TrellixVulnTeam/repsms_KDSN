# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 15:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platforma', '0002_auto_20161029_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 30, 16, 15, 13, 498708)),
        ),
        migrations.AlterField(
            model_name='user',
            name='expired',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 31, 16, 15, 13, 498708)),
        ),
        migrations.AlterField(
            model_name='user',
            name='phoneNumber',
            field=models.CharField(max_length=15),
        ),
    ]