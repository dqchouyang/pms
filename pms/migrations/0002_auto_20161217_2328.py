# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-17 15:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='joined',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 17, 23, 28, 40, 739856), verbose_name='入职时间'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='qq',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='QQ号'),
        ),
    ]
