# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20151209_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challongetournament',
            name='url',
            field=models.CharField(unique=True, max_length=75),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(unique=True, max_length=75),
        ),
    ]
