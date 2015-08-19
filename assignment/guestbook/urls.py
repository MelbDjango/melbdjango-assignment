from django.conf.urls import url
from .views import PostCreateList

urlpatterns = [
    url(r'^', PostCreateList.as_view(), name='post-create-list'),
]
