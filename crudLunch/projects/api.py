from .models import Menu, Empleado, Pedido
from rest_framework import viewsets, permissions
from .serializers import MenuSerializer, EmpleadoSerializer, PedidoSerializer
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, time

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if not request.data.get('entrada') \
            or not request.data.get('plato_principal') \
                or not request.data.get('postre'):
            return Response(
                {"detail": "Todos los campos de entrada, plato principal y postre son obligatorios."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if not request.data.get('entrada') or not \
            request.data.get('plato_principal') or not \
                request.data.get('postre'):
            return Response(
                {"detail": "Todos los campos de entrada, plato principal y postre son obligatorios."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().update(request, *args, **kwargs)

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [permissions.IsAuthenticated]

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        now = datetime.now().time()

        start_time = time(11, 30)
        end_time = time(12, 0)

        if not (start_time <= now <= end_time):
            return Response(
                {"detail": "Los pedidos solo pueden realizarse entre las 11:30am y las 12:00pm."},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request, *args, **kwargs)
