# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_playermatch'),
    ]

    operations = [
        migrations.AddField(
            model_name='playermatch',
            name='loser_elo_delta',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='playermatch',
            name='winner_elo_delta',
            field=models.FloatField(default=0.0),
        ),
    ]
