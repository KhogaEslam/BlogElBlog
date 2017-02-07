from django.conf.urls import url ,include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^forbiddenwords/select/$', views.forbiddenWordsList),
    #url(r'^/forbiddenwords/create', views.forbiddenWordsCreate),
    #url(r'^/forbiddenwords/edit', views.forbiddenWordsEdit),
    #url(r'^/forbiddenwords/delete', views.forbiddenWordsDelete),
    url(r'^users/add$',views.registerUser.as_view(),name='adduser'),
    url(r'^users/all$',views.allUsers,name='allusers'),
]
