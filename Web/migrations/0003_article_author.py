# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0002_auto_20171209_0520'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=50, null=True, verbose_name='\u4f5c\u8005'),
        ),
    ]
