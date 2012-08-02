from .base import BaseService
from www.models.base import BaseViewModel

class ContactService(BaseService):
    
    def __init__(self):
        pass

    def contact_view_model(self):
        obj = BaseViewModel()
        obj.body_class = 'contact'
        return obj
