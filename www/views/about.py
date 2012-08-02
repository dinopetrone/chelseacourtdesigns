from .base import BaseView
from www.services.about import AboutService


class AboutView(BaseView):
    def get(self, request):
        service = AboutService()
        model = service.about_view_model()
        return self.view('about.html', model)
