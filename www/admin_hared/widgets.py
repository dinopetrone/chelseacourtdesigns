from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe
from www import settings

class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name=str(value)
            output.append(u'<div> <a href="%s" target="_blank"><img src="%s" alt="%s" /></a></div>' % (image_url, image_url, file_name))
        output.append(super(AdminFileWidget, self).render(name, attrs))
        return mark_safe(u''.join(output))


