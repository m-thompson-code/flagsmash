# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_delete_playermatch'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerMatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('challonge_winner_id', models.CharField(max_length=75)),
                ('challonge_loser_id', models.CharField(max_length=75)),
                ('loser', models.ForeignKey(related_name='loser_player', to='main.Player', null=True)),
                ('tournament', models.ForeignKey(related_name='tournament', to='main.ChallongeTournament')),
                ('winner', models.ForeignKey(related_name='winner_player', to='main.Player', null=True)),
            ],
        ),
    ]
