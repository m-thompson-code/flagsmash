# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20151209_1817'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playermatch',
            old_name='loser_elo_delta',
            new_name='new_loser_elo',
        ),
        migrations.RenameField(
            model_name='playermatch',
            old_name='winner_elo_delta',
            new_name='new_winner_elo',
        ),
        migrations.AddField(
            model_name='playermatch',
            name='old_loser_elo',
            field=models.FloatField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='playermatch',
            name='old_winner_elo',
            field=models.FloatField(default=None, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='playermatch',
            name='video',
            field=embed_video.fields.EmbedVideoField(default='google.com'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playersync',
            name='final_elo',
            field=models.FloatField(default=None, null=True, blank=True),
        ),
    ]
