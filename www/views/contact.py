from .base import BaseView
from www.services.contact import ContactService


class ContactView(BaseView):
    def get(self, request):
        service = ContactService()
        model = service.contact_view_model()
        return self.view('contact.html', model)
