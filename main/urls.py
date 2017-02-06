from django.conf.urls import url
import views


urlpatterns = [
    url(r'^$',views.homePosts),
    url(r'^(?P<id>[0-9]+)/post$', views.PostDetails),
]
