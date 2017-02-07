from django.conf.urls import url
import views
urlpatterns = [

    url(r'^category$' , views.showCategory),
    url(r'^category/add$',views.add_category),
    url(r'^category/(?P<id>[0-9]+)/change$', views.edit_category),
    url(r'^category/(?P<id>[0-9]+)/delete$', views.del_category)
]