from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.RecordRedirectView.as_view(), name='records-root'),
    url(r'^records/$', views.RecordCreateView.as_view(), name='record-list'),
    url(r'^records/(?P<pk>\d+)/$', views.RecordDetailView.as_view(), name='record-detail'),
    url(r'^thanks/$',views.RecordThanksView.as_view(), name='thank-you'),  
]

