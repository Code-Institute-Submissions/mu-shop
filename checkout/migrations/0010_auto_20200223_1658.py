# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-23 16:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0009_auto_20200223_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlineitem',
            name='order',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='checkout.Order'),
        ),
    ]