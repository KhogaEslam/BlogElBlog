from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.admindashboard),
    url(r'posts/add', views.add_post),
    url(r'^posts$' , views.show_all_posts),
    url(r'posts/(?P<post_id>[0-9]+)/post_details', views.post_details ),
    url(r'posts/(?P<post_id>[0-9]+)/change' , views.edit_post),
    url(r'posts/(?P<post_id>[0-9]+)/delete' , views.delete_post),

]
