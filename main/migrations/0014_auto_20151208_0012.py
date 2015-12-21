# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20151207_2343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playersync',
            old_name='challongeID',
            new_name='challonge_player_id',
        ),
        migrations.RemoveField(
            model_name='playermatch',
            name='loser_elo_delta',
        ),
        migrations.RemoveField(
            model_name='playermatch',
            name='winner_elo_delta',
        ),
        migrations.AddField(
            model_name='playermatch',
            name='challonge_loser_id',
            field=models.CharField(default='moo', max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playermatch',
            name='challonge_winner_id',
            field=models.CharField(default='moo', max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playermatch',
            name='tournament',
            field=models.ForeignKey(related_name='tournament', default=None, to='main.ChallongeTournament'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='playermatch',
            name='loser',
            field=models.ForeignKey(related_name='loser_player', to='main.Player', null=True),
        ),
        migrations.AlterField(
            model_name='playermatch',
            name='winner',
            field=models.ForeignKey(related_name='winner_player', to='main.Player', null=True),
        ),
        migrations.AlterField(
            model_name='playersync',
            name='tournament',
            field=models.ForeignKey(related_name='tournament_sync', to='main.ChallongeTournament'),
        ),
    ]
