# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_playermatch'),
    ]

    operations = [
        migrations.AddField(
            model_name='playersync',
            name='final_ranking',
            field=models.CharField(default=b'', max_length=75),
        ),
    ]
