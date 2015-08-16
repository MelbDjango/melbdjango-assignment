from django.conf.urls import patterns, url

from . import views

urlpatterns =[

    url(r'^(?P<pk>[0-9]+)/$',
        views.UserCommentDetail.as_view(),
        name='comments_detail'),
    url(r'^create/$',
        views.UserCommentCreate.as_view(),
        name='comments_create'),
    url(r'^(?P<pk>[0-9]+)/update/$',
        views.UserCommentUpdate.as_view(),
        name='comments_edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$',
        views.UserCommentDelete.as_view(),
        name='comments_delete'),
    url(r'^user/$',
        views.UserCommentList.as_view(),
        name='user_comments_list'),
    url(r'^',
        views.AllCommentList.as_view(),
        name='all_comments_list'),
]
