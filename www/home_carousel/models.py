from django.db import models

class Carousel(models.Model):
    large_img = models.ImageField(upload_to='photos/%d/%m/%h/%s')
    def __unicode__(self):
        return 'Carousel Item ' + str(self.pk)