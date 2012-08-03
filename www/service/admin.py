from .models import Service
from django.contrib import admin
from www.admin_hared.admin import ImageFieldAdmin

    
class ServiceAdmin(ImageFieldAdmin):
    pass
    
    

    
admin.site.register(Service,ServiceAdmin)
