# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 19:21
from __future__ import unicode_literals

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('platforma', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scszkola',
            name='telefon',
            field=phonenumber_field.modelfields.PhoneNumberField(default=0, max_length=128),
            preserve_default=False,
        ),
    ]
