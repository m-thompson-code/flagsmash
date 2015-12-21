from django.db import models
from main.models import ChallongeTournament, Player

class PlayerSync(models.Model):
    tournament = models.ForeignKey(ChallongeTournament, related_name="tournament_sync")
    player = models.ForeignKey(Player, related_name="player_obj", null = True, blank = True, default = None)
    challonge_id = models.CharField(max_length = 75, default = "")
    challonge_name = models.CharField(max_length = 75, default = "")
    final_ranking = models.IntegerField()
    final_elo = models.FloatField(null = True, blank = True, default = None)
    begin_elo = models.FloatField(null = True, blank = True, default = None)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    
    def __unicode__(self):
        if self.player is None:
            player_name = "unknown_player"
        else:
            player_name = self.player.name
        return player_name + " | " + self.challonge_name + self.challonge_id + " " + self.tournament.url