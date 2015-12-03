import re
from django.db import models
from jsonfield import JSONField

class Bracket(models.Model):
    name = models.TextField(default = "")
    dataJSON = JSONField()
    
    def __unicode__(self):
        return str(self.pk) + " " + self.name

    def save(self, *args, **kwargs):
        #self.dataJSON = '{"moo":"moo"}'
        #ch = '\'
        #str_dataJSON = str(self.dataJSON)
        #for ch in str_dataJSON:
        #    str_dataJSON = str_dataJSON.replace(ch, "")
        #self.dataJSON = dict(str_dataJSON)
        #for ch in ['&','#']:
        #   if ch in string:
        #      string=string.replace(ch,"\\"+ch)
        #self.dataJSON = str(self.dataJSON).replace("\\", "")

        super(Bracket, self).save(*args, **kwargs)