# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_auto_20151211_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challongetournament',
            name='name',
            field=models.CharField(default=b'', max_length=75, blank=True),
        ),
    ]
