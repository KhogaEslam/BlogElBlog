from django.conf.urls import url ,include
from django.contrib import admin
from . import views
urlpatterns = [
<<<<<<< HEAD
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
=======
    url(r'^forbiddenwords/select/$', views.forbiddenWordsList),
    #url(r'^/forbiddenwords/create', views.forbiddenWordsCreate),
    #url(r'^/forbiddenwords/edit', views.forbiddenWordsEdit),
    #url(r'^/forbiddenwords/delete', views.forbiddenWordsDelete),
    url(r'^users/add$',views.registerUser.as_view(),name='adduser'),
    url(r'^users/all$',views.allUsers,name='allusers'),
    url(r'^category$' , views.showCategory),
    url(r'^category/add$',views.add_category),
    url(r'^category/(?P<id>[0-9]+)/change$', views.edit_category),
    url(r'^category/(?P<id>[0-9]+)/delete$', views.del_category),
>>>>>>> ff138e8d11b30994e03bc1ebe6725d0f571986dc
]
