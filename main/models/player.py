from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.OneToOneField(User)
    tag = models.CharField(max_length = 75)
    email = models.EmailField(max_length = 75)
    elo = models.FloatField(default = 1200.0)
    created = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return str(self.pk) + " " + self.tag