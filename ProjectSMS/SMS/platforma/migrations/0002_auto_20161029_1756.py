# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 15:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platforma', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 29, 17, 56, 19, 322017)),
        ),
        migrations.AlterField(
            model_name='user',
            name='expired',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 30, 17, 56, 19, 322017)),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=256),
        ),
    ]
