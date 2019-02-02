import admin_tools
from django.conf.urls import url, include
from django.contrib import admin
from users import urls as users_urls, api_urls as users_api_urls
from poemas import urls as poema_urls, api_urls as poema_api_urls

urlpatterns = [
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #users urls
    url(r'', include(users_urls)),
    url(r'api/', include(users_api_urls)),

    #poemas urls
    url(r'', include(poema_urls)),
    url(r'api/', include(poema_api_urls))

]
