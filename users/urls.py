
from django.conf.urls import url, include
from users.views import LoginView, LogoutView

urlpatterns = [

    #Users urls
    url(r'^users/login$', LoginView.as_view(), name='users_login'),
    url(r'^users/logout$', LogoutView.as_view(), name='users_logout'),

]
