# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-15 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_categorie_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price_currency',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
