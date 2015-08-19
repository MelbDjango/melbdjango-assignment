from django.conf.urls import include, url
from django.contrib import admin
from guestbook import urls as guestbook_urls

urlpatterns = [
    url(r'^guestbook/', include(guestbook_urls, namespace='guestbook')),
    url(r'^admin/', include(admin.site.urls)),
]
