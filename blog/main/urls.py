from django.conf.urls import url
import views


urlpatterns = [
    url(r'^$',views.homePosts),
    #url(r'^$',views.sidebar),
    url(r'^(?P<id>[0-9]+)/post$', views.PostDetails),
    url(r'^(?P<postID>[0-9]+)/addComment$', views.addComment),
    url(r'^(?P<postID>[0-9]+)/(?P<commentID>[0-9]+)/addReply$', views.addReply),
]
