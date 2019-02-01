from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from poemas.api import PoemaListAPI, PoemaDetailAPI, PoemaViewSet

#API Routers
router = DefaultRouter()
router.register(r'poemas', PoemaViewSet )

urlpatterns = [

    url(r'1.0/', include(router.urls)),

]
