from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.poll_list,name='poll_list'),
    url(r'^$/(?P<question_id>\d+)/upvote',views.upvote,name='upvote'),
    url(r'^like_category/$', views.like_category, name='like_category'),
    url(r'^like/(\d+)/$',views.like),
    url(r'^sorted/',views.sorted,name='sorted'),
    #url(r'^poll/new/$',views.poll_new,name='poll_new'),
]
