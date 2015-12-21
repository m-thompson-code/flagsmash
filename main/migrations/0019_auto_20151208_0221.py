# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_playersync_final_ranking'),
    ]

    operations = [
        migrations.AddField(
            model_name='playersync',
            name='challonge_name',
            field=models.CharField(default=b'', max_length=75),
        ),
        migrations.AlterField(
            model_name='playersync',
            name='challonge_player_id',
            field=models.CharField(default=b'', max_length=75),
        ),
    ]
