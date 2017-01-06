from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^new_user/$', views.new_user, name='new_user'),
    url(r'^user_details/$', views.user_details, name='user_details'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^api/post/$', views.PostList.as_view()),
    url(r'^api/post/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),
    url(r'^api/comment/$', views.CommentList.as_view()),
    url(r'^api/comment/(?P<pk>[0-9]+)/$', views.CommentDetail.as_view()),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
