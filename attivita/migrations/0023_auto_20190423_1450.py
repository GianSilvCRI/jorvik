# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-04-23 14:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attivita', '0022_auto_20190423_1035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nonsonounbersaglio',
            old_name='crentro_formazione',
            new_name='centro_formazione',
        ),
    ]