from django.db import models

class Service(models.Model):
    title = models.CharField(max_length = 100)
    blurb = models.TextField(max_length = 1000)
    bottom_title = models.CharField(max_length = 100)
    bottom_description = models.CharField(max_length = 200, 
                                          help_text="to add a 'click here' text, link add {click}")
    def get_id(self):
        return self.title.replace(' ','')
    def __unicode__(self):
        return self.title