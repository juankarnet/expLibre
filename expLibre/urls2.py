"""expLibre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter

import poemas
import users

from poemas import views
from poemas.api import PoemaListAPI, PoemaDetailAPI, PoemaViewSet
from poemas.views import HomeView, PoemaListView, DetailView, CreateView, UserPoemasView
from users import views
from users.api import UserViewSet
from users.views import LoginView, LogoutView
from users.api2 import UserListAPI, UserDetailAPI

#API Routers
router = DefaultRouter()
router.register(r'api/1.0/poemas', PoemaViewSet )
router.register(r'api/1.0/users', UserViewSet, base_name='user' )

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    #Poemas urls
    #url(r'^$', poemas.views.home, name='poemas_home'),
    url(r'^$', HomeView.as_view(), name='poemas_home'),
    url(r'^poemas/(?P<pk>[0-9]+)$', DetailView.as_view(), name='poemas_detail'),
    url(r'^my-poemas/$', login_required(UserPoemasView.as_view()) , name='user_poemas'),
    url(r'^poemas/$', PoemaListView.as_view(), name='poemas_list'),
    url(r'^poemas/create$', CreateView.as_view(), name='create_poema'),

    url(r'', include(router.urls)),
    #Poema Api URLs
    # url(r'^api/1.0/poemas/$', PoemaListAPI.as_view(), name='poema_list_api'),
    # url(r'^api/1.0/poemas/(?P<pk>[0-9]+)$', PoemaDetailAPI.as_view(), name='poema_detail_api'),

    #Users urls
    # url(r'^users/login$', users.views.login, name='users_login'),
    url(r'^users/login$', LoginView.as_view(), name='users_login'),
    url(r'^users/logout$', LogoutView.as_view(), name='users_logout'),

    #Users API URLs
    # url(r'^api/1.0/users/$', UserListAPI.as_view(), name='user_list_api'),
    # url(r'^api/1.0/users/(?P<pk>[0-9]+)$', UserDetailAPI.as_view(), name='user_detail_api')

]
