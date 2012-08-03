from django.conf.urls import patterns, include, url
from django.contrib import admin
from www.views.about import AboutView
from www.views.contact import ContactView
from www.views.index import IndexView
from www.views.portfolio import PortfolioView
from www.views.services import ServicesView
from www import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'www.views.home', name='home'),
    # url(r'^www/', include('www.foo.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^resources/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'public/resources'}),
    (r'^uploads/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/?$', ContactView.as_view(), name='contact'),
    url(r'^portfolio/?$', PortfolioView.as_view(), name='portfolio'),
    url(r'^about/?$', AboutView.as_view(), name='about'),
    url(r'^services/?$', ServicesView.as_view(), name='services'),
    url(r'^$', IndexView.as_view(), name='index'),
)
