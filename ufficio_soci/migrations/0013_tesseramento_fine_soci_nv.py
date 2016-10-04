# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-04 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ufficio_soci', '0012_auto_20160906_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='tesseramento',
            name='fine_soci_nv',
            field=models.DateField(help_text="La data indicata è inclusa nell'intervallo in cui è permesso il tesseramento", null=True, verbose_name='Data di fine per nuovo volontario'),
        ),
    ]
