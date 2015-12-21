from django.db import models
from main.models import Player, ChallongeTournament
from embed_video.fields import EmbedVideoField

class PlayerMatch(models.Model):
    winner = models.ForeignKey(Player, related_name="winner_player", null = True, blank = True, default = None)
    loser = models.ForeignKey(Player, related_name="loser_player", null = True, blank = True, default = None)
    challonge_winner_id = models.CharField(max_length = 75)
    challonge_loser_id = models.CharField(max_length = 75)
    tournament = models.ForeignKey(ChallongeTournament, related_name="tournament")
    identifier = models.CharField(max_length = 5)
    old_winner_elo = models.FloatField(null = True, blank = True, default = None)
    old_loser_elo = models.FloatField(null = True, blank = True, default = None)
    new_winner_elo = models.FloatField(null = True, blank = True, default = None)
    new_loser_elo = models.FloatField(null = True, blank = True, default = None)
    video = EmbedVideoField(null = True, blank = True, default = None)  # same like models.URLField()
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        if self.winner is None:
            winner_name = "unknown_player1"
        else:
            winner_name = self.winner.name
        if self.loser is None:
            loser_name = "unknown_player2"
        else:
            loser_name = self.loser.name
        return "Match: " + winner_name + " beat " + loser_name + " url: " + self.tournament.url

    def winner_elo_delta(self):
        return self.new_winner_elo - self.old_winner_elo

    def loser_elo_delta(self):
        return self.new_loser_elo - self.old_loser_elo

    class Meta:
           ordering = ['created_at', 'identifier']