from .base import BaseView
from www.services.services import ServicesService


class ServicesView(BaseView):
    def get(self, request):
        service = ServicesService()
        model = service.services_view_model()
        return self.view('services.html', model)
