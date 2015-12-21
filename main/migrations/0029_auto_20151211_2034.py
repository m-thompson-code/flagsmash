# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20151211_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challongetournament',
            name='name',
            field=models.CharField(max_length=75, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='challongetournament',
            name='updated_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
