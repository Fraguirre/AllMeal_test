from django.contrib import admin
from django.urls import path, include
from projects.api import MenuViewSet, EmpleadoViewSet, PedidoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/menus', MenuViewSet, 'menus')
router.register('api/empleados', EmpleadoViewSet, 'empleados')
router.register('api/pedidos', PedidoViewSet, 'pedidos')

urlpatterns = [
    path("admin/", admin.site.urls),  
    path('', include(router.urls)),
]
