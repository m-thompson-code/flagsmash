from django.contrib import admin
from main.models import Player, PlayerMatch, ChallongeTournament, PlayerSync

admin.site.register(Player)
admin.site.register(PlayerMatch)
admin.site.register(ChallongeTournament)
admin.site.register(PlayerSync)