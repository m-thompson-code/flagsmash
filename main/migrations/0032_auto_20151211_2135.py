# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_challongetournament_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playersync',
            name='final_ranking',
            field=models.IntegerField(),
        ),
    ]
