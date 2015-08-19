from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from guestbook import urls as guestbook_urls

urlpatterns = [
    url(r'^guestbook/', include(guestbook_urls, namespace='guestbook')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', TemplateView.as_view(template_name="index.html")),
]
