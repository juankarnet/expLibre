from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from poemas.views import HomeView, PoemaListView, DetailView, CreateView, UserPoemasView

urlpatterns = [

    #Poemas urls
    #url(r'^$', poemas.views.home, name='poemas_home'),
    url(r'^$', HomeView.as_view(), name='poemas_home'),
    url(r'^poemas/(?P<pk>[0-9]+)$', DetailView.as_view(), name='poemas_detail'),
    url(r'^my-poemas/$', login_required(UserPoemasView.as_view()) , name='user_poemas'),
    url(r'^poemas/$', PoemaListView.as_view(), name='poemas_list'),
    url(r'^poemas/create$', CreateView.as_view(), name='create_poema'),
]
