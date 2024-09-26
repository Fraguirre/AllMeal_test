from .models import Menu, Empleado, Pedido
from rest_framework import viewsets, permissions
from .serializers import MenuSerializer, EmpleadoSerializer, PedidoSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]  # Cambia si necesitas otros permisos


class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [permissions.IsAuthenticated]  # Cambia si necesitas otros permisos


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [permissions.IsAuthenticated]  # Cambia si necesitas otros permisos
