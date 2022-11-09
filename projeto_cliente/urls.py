from django.contrib import admin

from rest_framework import routers
from clientes.views import ClientesViewSet
from django.urls import include, re_path






router = routers.DefaultRouter()
router.register('clientes', ClientesViewSet)

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('', include(router.urls)),
]
