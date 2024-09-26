from rest_framework import serializers
from .models import Menu, Empleado, Pedido

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'fecha', 'entrada', 'plato_principal', 'postre']


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ['id', 'slack_id_usuario', 'nombre']


class PedidoSerializer(serializers.ModelSerializer):
    empleado = EmpleadoSerializer()  
    menu = MenuSerializer()  

    class Meta:
        model = Pedido
        fields = ['id', 'empleado', 'menu', 'opcion_seleccionada', 'fecha_pedido']
