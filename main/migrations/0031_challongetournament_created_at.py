# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_auto_20151211_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='challongetournament',
            name='created_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
