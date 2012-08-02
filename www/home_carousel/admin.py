from .models import Carousel
from django.contrib import admin
from www.admin_hared.admin import ImageFieldAdmin

    
class CarouselAdmin(ImageFieldAdmin):
    pass
    
    

    
admin.site.register(Carousel,CarouselAdmin)
