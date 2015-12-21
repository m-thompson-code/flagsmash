# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20151207_0929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challongetournament',
            name='created',
        ),
        migrations.AddField(
            model_name='challongetournament',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 8, 6, 43, 23, 741000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
