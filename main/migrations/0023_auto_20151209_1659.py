# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20151209_1620'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bracket',
        ),
        migrations.AlterField(
            model_name='challongetournament',
            name='name',
            field=models.CharField(default=b'', max_length=75),
        ),
        migrations.AlterField(
            model_name='player',
            name='email',
            field=models.EmailField(max_length=75, null=True),
        ),
    ]
