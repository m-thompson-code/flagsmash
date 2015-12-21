# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20151208_0221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playersync',
            old_name='challonge_player_id',
            new_name='challonge_id',
        ),
    ]
