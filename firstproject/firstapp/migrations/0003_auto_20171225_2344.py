# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-25 20:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_pizza'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pizzashop',
            options={'verbose_name': 'Пиццерия', 'verbose_name_plural': 'Пиццерии'},
        ),
    ]