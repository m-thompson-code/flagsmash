# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_player_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerMatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('loser', models.ForeignKey(related_name='loser_set', to='main.Player')),
                ('winner', models.ForeignKey(related_name='winner_set', to='main.Player')),
            ],
        ),
    ]
