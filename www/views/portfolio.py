from .base import BaseView
from www.services.portfolio import PortfolioService


class PortfolioView(BaseView):
    def get(self, request):
        service = PortfolioService()
        model = service.portfolio_view_model()
        return self.view('portfolio.html', model)
