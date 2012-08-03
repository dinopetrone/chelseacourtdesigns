from .models import Person
from django.contrib import admin
from www.admin_hared.admin import ImageFieldAdmin

    
class PersonAmin(ImageFieldAdmin):
    pass
    
    

    
admin.site.register(Person,PersonAmin)
