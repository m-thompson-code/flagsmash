# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20151208_0012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playermatch',
            old_name='challonge_loser_id',
            new_name='moo',
        ),
        migrations.RemoveField(
            model_name='playermatch',
            name='challonge_winner_id',
        ),
        migrations.RemoveField(
            model_name='playermatch',
            name='loser',
        ),
        migrations.RemoveField(
            model_name='playermatch',
            name='tournament',
        ),
        migrations.RemoveField(
            model_name='playermatch',
            name='winner',
        ),
    ]
