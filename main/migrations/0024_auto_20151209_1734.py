# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20151209_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playermatch',
            name='loser',
            field=models.ForeignKey(related_name='loser_player', default=None, blank=True, to='main.Player', null=True),
        ),
        migrations.AlterField(
            model_name='playermatch',
            name='loser_elo_delta',
            field=models.FloatField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='playermatch',
            name='winner',
            field=models.ForeignKey(related_name='winner_player', default=None, blank=True, to='main.Player', null=True),
        ),
        migrations.AlterField(
            model_name='playermatch',
            name='winner_elo_delta',
            field=models.FloatField(default=None, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='playersync',
            name='player',
            field=models.ForeignKey(related_name='player_obj', default=None, blank=True, to='main.Player', null=True),
        ),
    ]
