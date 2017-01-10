# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-16 00:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('anagrafica', '0041_auto_20160513_0954'),
        ('formazione', '0014_partecipazionecorsobase_automatica'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvitoCorsoBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creazione', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('ultima_modifica', models.DateTimeField(auto_now=True, db_index=True)),
                ('corso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='inviti', to='formazione.CorsoBase')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inviti_corsi', to='anagrafica.Persona')),
            ],
            options={
                'verbose_name': 'Invito di partecipazione a corso base',
                'permissions': (('view_invitocorsobase', 'Can view invito partecipazione corso base'),),
                'verbose_name_plural': 'Inviti di partecipazione a corso base',
                'ordering': ('persona__nome', 'persona__cognome', 'persona__codice_fiscale'),
            },
        ),
    ]