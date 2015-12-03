from django.db import models
from main.models import Player

class PlayerMatch(models.Model):
    winner = models.ForeignKey(Player, related_name="winner_set")
    loser = models.ForeignKey(Player, related_name="loser_set")
    winner_elo_delta = models.FloatField(default = 0.0)
    loser_elo_delta = models.FloatField(default = 0.0)

    def __unicode__(self):
        return str(self.pk) + " " + self.winner.tag + " " + str(self.winner_elo_delta) + " beat " + self.loser.tag + " " + str(self.loser_elo_delta)