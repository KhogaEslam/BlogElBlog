from django.conf.urls import url
import views


urlpatterns = [
    url(r'^$',views.homePosts , name='homeurl'),
    url(r'^subscribe/(?P<cat_id>[0-9]+)/$' , views.subscribe),
    url(r'^unsubscribe/(?P<cat_id>[0-9]+)/$' , views.unsubscribe),
    url(r'^select/(?P<model_name>[a-zA-Z]+)/$', views.modelSelect),
]
