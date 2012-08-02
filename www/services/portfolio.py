from .base import BaseService
from www.models.base import BaseViewModel

class PortfolioService(BaseService):
    
    def __init__(self):
        pass

    def portfolio_view_model(self):
        obj = BaseViewModel()
        #obj.portfolio_items = 
        return obj
