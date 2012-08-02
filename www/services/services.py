from .base import BaseService
from www.models.base import BaseViewModel

class ServicesService(BaseService):
    
    def __init__(self):
        pass

    def services_view_model(self):
        obj = BaseViewModel()
        #obj.services = 
        obj.body_class = 'services'
        return obj
