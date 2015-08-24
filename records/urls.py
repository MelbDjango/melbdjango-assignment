from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    #url(r'^$', views.RootRedirectView.as_view(), name='client-list'),
    url(r'^records/$', views.RecordCreateView.as_view(), name='record-list'),
    url(r'^records/(?P<pk>\d+)/$', views.RecordDetailView.as_view(), name='record-detail'),
    url(r'^thanks/$', TemplateView.as_view(template_name='thank_you.html'), name='thank-you'),  
]

