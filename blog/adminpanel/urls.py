from django.conf.urls import url ,include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^forbiddenwords/select/$', views.forbiddenWordsList, name="listWords"),
    url(r'^forbiddenwords/create', views.ForbiddenWord_create.as_view(), name="createNewWord"),
    url(r'^forbiddenwords/edit/(?P<pk>[0-9]+)/$', views.ForbiddenWord_edit.as_view() , name="editWord"),
    url(r'^forbiddenwords/delete/(?P<pk>[0-9]+)/$', views.ForbiddenWord_delete.as_view(), name="deleteWord"),
    url(r'^users/add$',views.registerUser.as_view(),name='adduser'),
    url(r'^users/all$',views.allUsers.as_view(),name='allusers'),
    url(r'^users/(?P<user_id>[0-9]+)/profile/$' , views.userProfile ,name='userProfile'),
    #url(r'^users/(?P<user_id>[0-9]+)/delete$',views.deleteUser.as_view(),name='deleteuser'),
    url(r'^users/block/(?P<user_id>[0-9]+)/$' , views.blockUser),
    url(r'^users/unblock/(?P<user_id>[0-9]+)/$' , views.unblockUser),
]
