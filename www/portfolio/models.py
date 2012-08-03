from django.db import models

class Portfolio(models.Model):
    large_img = models.ImageField(upload_to='photos/%d/%m/%h/%s')
    small_img = models.ImageField(upload_to='photos/%d/%m/%h/%s')
    def __unicode__(self):
        return 'Portfolio item: '+ str(self.pk)