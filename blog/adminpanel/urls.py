from django.conf.urls import url
import views


urlpatterns = [
    url(r'^users/add/$',views.registerUser.as_view(),name='adduser'),
    url(r'^users/all/$',views.allUsers.as_view(),name='allusers'),
    url(r'^users/(?P<user_id>[0-9]+)/profile/$' , views.userProfile ,name='userProfile'),
    url(r'^users/(?P<pk>[0-9]+)/change/$',views.updateUser.as_view(),name='updateuser'),
    url(r'^users/(?P<user_id>[0-9]+)/delete$',views.deleteUser),
    url(r'^users/block/(?P<user_id>[0-9]+)/$' , views.blockUser),
    url(r'^users/unblock/(?P<user_id>[0-9]+)/$' , views.unblockUser),
]
