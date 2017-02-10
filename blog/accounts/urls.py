from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    url(r'^login/$', views.custom_login,  name='login'),
    url(r'^logout/$' ,auth_views.logout, {'next_page': '/admin'}, name='logout'),
    url(r'^register/$', views.RegisterView.as_view(), name = 'register'),
]
