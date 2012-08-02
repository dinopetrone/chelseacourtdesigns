from .base import BaseService
from www.home_carousel.models import Carousel
from www.models.base import BaseViewModel

class IndexService(BaseService):
    
    def __init__(self):
        pass

    def index_view_model(self):
        obj = BaseViewModel()
        obj.body_class = 'home'
        obj.images = Carousel.objects.all()
        return obj
