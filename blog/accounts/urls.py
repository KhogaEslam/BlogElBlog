from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    url(r'^login/$', views.custom_login,  name='login'),
    url(r'^logout/$' ,auth_views.logout, {'next_page': '/admin'}, name='logout'),
    url(r'^register/$', views.RegisterView.as_view(), name = 'register'),
    ####### reset password ##########
    url(r'^password/reset/$', auth_views.password_reset, {'post_reset_redirect' : '/accounts/password/reset/done/'}, name='password_reset'),
    url(r'^password/reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        auth_views.password_reset_confirm,  {'post_reset_redirect' : '/accounts/reset/done/'} , name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    ########### Change Password ############
    url(r'^password/change/$', auth_views.password_change, {'post_change_redirect' : '/accounts/password/change/done/'}, name='password_change'),
    url(r'^password/change/done/$', auth_views.password_change_done, name='password_change_done'),

]
