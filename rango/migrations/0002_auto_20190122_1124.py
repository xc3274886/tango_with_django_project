# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-22 11:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.RemoveField(
            model_name='category',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='category',
            name='views',
        ),
    ]
