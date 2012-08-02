from .base import BaseView
from www.services.index import IndexService


class IndexView(BaseView):
    def get(self, request):
        service = IndexService()
        model = service.index_view_model()
        return self.view('index.html', model)