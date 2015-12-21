from django.db import models

class ChallongeTournament(models.Model):
    name = models.CharField(max_length = 75, default="", blank=True)
    description = models.CharField(max_length = 200, default="", blank=True)
    url = models.CharField(max_length = 75, unique=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.name + " url:" + self.url