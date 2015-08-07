from django.conf.urls import include, url
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

urlpatterns = [
    url(r'^$', lambda request: HttpResponseRedirect(reverse('mypage'))),
    url(r'^mypage$', 'guestbook.views.mypage', name='mypage'),
    url(r'^backend$', 'guestbook.views.backend', name='backend'),
]
