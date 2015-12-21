# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_auto_20151211_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='playersync',
            name='begin_elo',
            field=models.FloatField(default=None, null=True, blank=True),
        ),
    ]
