from .models import Portfolio
from django.contrib import admin
from www.admin_hared.admin import ImageFieldAdmin

    
class PortfolioAmin(ImageFieldAdmin):
    pass
    
admin.site.register(Portfolio,PortfolioAmin)
