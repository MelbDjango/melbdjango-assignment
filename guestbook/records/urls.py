from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.RootRedirectView.as_view(), name='client-list'),
    url(r'^records/$', views.RecordCreateView.as_view(), name='record-list'),
]

