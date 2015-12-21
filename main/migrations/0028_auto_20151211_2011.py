# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20151211_0309'),
    ]

    operations = [
        migrations.AddField(
            model_name='playermatch',
            name='identifier',
            field=models.CharField(default=datetime.datetime(2015, 12, 12, 3, 11, 44, 311000, tzinfo=utc), max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playermatch',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 12, 3, 11, 57, 478000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
