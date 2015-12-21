# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_playermatch_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='playermatch',
            name='loser_elo_delta',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='playermatch',
            name='winner_elo_delta',
            field=models.FloatField(null=True),
        ),
    ]
