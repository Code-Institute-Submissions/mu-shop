# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-24 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0256_auto_20200224_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description_line_four',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='product',
            name='description_line_three',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='product',
            name='description_line_two',
            field=models.CharField(default='', max_length=254),
        ),
    ]