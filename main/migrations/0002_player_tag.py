# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='tag',
            field=models.CharField(default=datetime.datetime(2015, 11, 27, 5, 19, 43, 946000, tzinfo=utc), max_length=75),
            preserve_default=False,
        ),
    ]
