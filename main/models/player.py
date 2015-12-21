from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length = 75, unique=True)
    email = models.EmailField(max_length = 75, null = True)
    elo = models.FloatField(default = 1200.0)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.name + " " + str(self.elo) + " {" + self.user.username + ")"