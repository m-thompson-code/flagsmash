# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20151208_0223'),
    ]

    operations = [
        migrations.AddField(
            model_name='playermatch',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 9, 23, 5, 12, 528000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
