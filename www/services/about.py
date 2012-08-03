from .base import BaseService
from www.models.base import BaseViewModel
from www.people.models import Person

class AboutService(BaseService):
    
    def __init__(self):
        pass

    def about_view_model(self):
        obj = BaseViewModel()
        obj.body_class = 'about'
        obj.people = Person.objects.all()
        return obj
