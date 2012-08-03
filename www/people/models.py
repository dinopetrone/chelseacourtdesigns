from django.db import models

class Person(models.Model):
    large_img = models.ImageField(upload_to='photos/%d/%m/%h/%s')
    name = models.CharField(max_length = 100)
    blurb = models.TextField(max_length = 1000)
    def id_class(self):
        return self.name.lower().replace(' ', '')
    def __unicode__(self):
        return self.name