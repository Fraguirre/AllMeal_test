from rest_framework import routers
from .api import MenuViewSet, EmpleadoViewSet, PedidoViewSet

router = routers.DefaultRouter()

# Registrar los viewsets para los modelos Menu, Empleado y Pedido
router.register('api/menus', MenuViewSet, 'menus')
router.register('api/empleados', EmpleadoViewSet, 'empleados')
router.register('api/pedidos', PedidoViewSet, 'pedidos')

# Generar las URLS automáticamente
urlpatterns = router.urls
