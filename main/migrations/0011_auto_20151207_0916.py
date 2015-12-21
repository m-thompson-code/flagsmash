# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_tournament'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerSync',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('challongeID', models.CharField(max_length=75)),
                ('player', models.ForeignKey(related_name='player_obj', to='main.Player')),
            ],
        ),
        migrations.RenameModel(
            old_name='Tournament',
            new_name='ChallongeTournament',
        ),
        migrations.AddField(
            model_name='playersync',
            name='tournament',
            field=models.ForeignKey(related_name='tournament', to='main.ChallongeTournament'),
        ),
    ]
