from rest_framework import routers
from .api import MenuViewSet, EmpleadoViewSet, PedidoViewSet

router = routers.DefaultRouter()

router.register('api/menus', MenuViewSet, 'menus')
router.register('api/empleados', EmpleadoViewSet, 'empleados')
router.register('api/pedidos', PedidoViewSet, 'pedidos')

urlpatterns = router.urls
