from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.GuestPostsCreateView.as_view() , name='guest-book'),
    url(r'^thankyou/$', TemplateView.as_view(template_name="thankyou.html"), name='thank-you'),
]
