"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url ,include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^admin/', admin.site.urls),
    url(r'^adminpanel/', include('adminpanel.urls',namespace='adminpanel')),
    #url(r'^admin/',admin.site.urls),
    url(r'^main/',include('main.urls')),
    url(r'^admin/', include('adminpanel.urls')),
    url(r'^home/', include('main.urls')),
    url(r'^accounts/', include("accounts.urls", namespace= 'accounts') ),
<<<<<<< HEAD
    url(r'^adminpanel/', include("adminpanel.urls", namespace="adminpanel") ),
=======
    #url(r'^accounts/', include('django.contrib.auth.urls')),

>>>>>>> ff138e8d11b30994e03bc1ebe6725d0f571986dc
]
