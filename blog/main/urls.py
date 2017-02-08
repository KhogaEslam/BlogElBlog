from django.conf.urls import url
import views


urlpatterns = [
    url(r'^$',views.homePosts),
    url(r'^subscribe/(?P<cat_id>[0-9]+)/$' , views.subscribe),
    url(r'^unsubscribe/(?P<cat_id>[0-9]+)/$' , views.unsubscribe),
]
