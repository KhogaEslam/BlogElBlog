from django.conf.urls import url
import views


urlpatterns = [
    url(r'^.$',views.homePosts),
    url(r'^$',views.homePosts , name='homeurl'),
    url(r'^subscribe/(?P<cat_id>[0-9]+)/$' , views.subscribe),
    url(r'^unsubscribe/(?P<cat_id>[0-9]+)/$' , views.unsubscribe),
    url(r'^select/(?P<model_name>[a-zA-Z]+)/$', views.modelSelect),
    #url(r'^$',views.sidebar),
    url(r'^(?P<id>[0-9]+)/post$', views.PostDetails),
    url(r'^(?P<postID>[0-9]+)/addComment$', views.addComment),
    url(r'^(?P<postID>[0-9]+)/(?P<commentID>[0-9]+)/addReply$', views.addReply),
    url(r'^(?P<postID>[0-9]+)/(?P<commentID>[0-9]+)/deleteComment$', views.deleteComment),
    url(r'^category/(?P<cat_id>[0-9]+)/posts$', views.category_posts),
    

]
