from django.conf.urls import url
import views


urlpatterns = [
    url(r'^$',views.homePosts),
    url(r'^subscribe/(?P<cat_id>[0-9]+)/$' , views.subscribe),
    url(r'^unsubscribe/(?P<cat_id>[0-9]+)/$' , views.unsubscribe),
<<<<<<< HEAD
=======
    url(r'^select/(?P<model_name>[a-zA-Z]+)/$', views.modelSelect),
    #url(r'^$',views.sidebar),
    url(r'^(?P<id>[0-9]+)/post$', views.PostDetails),
    url(r'^(?P<postID>[0-9]+)/addComment$', views.addComment),
    url(r'^(?P<postID>[0-9]+)/(?P<commentID>[0-9]+)/addReply$', views.addReply),
>>>>>>> ff138e8d11b30994e03bc1ebe6725d0f571986dc
]
