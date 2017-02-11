from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.admindashboard),
    url(r'posts/add', views.add_post),
    url(r'^posts$' , views.show_all_posts),
    url(r'posts/(?P<post_id>[0-9]+)/post_details', views.post_details ),
    url(r'posts/(?P<post_id>[0-9]+)/change' , views.edit_post),
    url(r'posts/(?P<post_id>[0-9]+)/delete' , views.delete_post),

    url(r'^forbiddenwords/$', views.forbiddenWordsList, name='listWords'),
    url(r'^forbiddenwords/create', views.ForbiddenWord_create.as_view(), name='createNewWord' ),
    url(r'^forbiddenwords/(?P<pk>[0-9]+)/edit', views.ForbiddenWord_edit.as_view() , name='editWord' ),
    url(r'^forbiddenwords/(?P<pk>[0-9]+)/delete', views.ForbiddenWord_delete.as_view(), name='deleteWord' ),

    url(r'^category$' , views.showCategory),
    url(r'^category/add$',views.add_category),
    url(r'^category/(?P<id>[0-9]+)/change$', views.edit_category),
    url(r'^category/(?P<id>[0-9]+)/delete$', views.del_category),
    url(r'^category/(?P<id>[0-9]+)/posts$', views.category_posts),

    url(r'^users/add/$',views.registerUser.as_view(),name='adduser'),
    url(r'^users/$',views.allUsers.as_view(),name='allusers'),
    url(r'^users/(?P<pk>[0-9]+)/change/$',views.updateUser.as_view(),name='updateuser'),
    url(r'^users/(?P<user_id>[0-9]+)/delete$',views.deleteUser),
    url(r'^users/block/(?P<user_id>[0-9]+)/$' , views.blockUser),
    url(r'^users/unblock/(?P<user_id>[0-9]+)/$' , views.unblockUser),
    url(r'^posts/feature/(?P<post_id>[0-9]+)/$' ,views.feature_post),
    url(r'^posts/unfeature/(?P<post_id>[0-9]+)/$' ,views.unfeature_post),
]
