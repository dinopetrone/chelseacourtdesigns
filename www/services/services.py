from .base import BaseService
from www.service.models import Service
from www.models.base import BaseViewModel

class ServicesService(BaseService):
    
    def __init__(self):
        pass

    def services_view_model(self):
        obj = BaseViewModel()
        obj.services = Service.objects.all()
        obj.body_class = 'services'
        return obj
