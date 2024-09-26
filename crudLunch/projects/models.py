from django.db import models

class Menu(models.Model):
    fecha = models.DateField(unique=True)  # Menú para una fecha específica
    entrada = models.CharField(max_length=255)  # Plato de entrada
    plato_principal = models.CharField(max_length=255)  # Plato principal
    postre = models.CharField(max_length=255)  # Postre

    def __str__(self):
        return f"Menú para {self.fecha}"


class Empleado(models.Model):
    slack_id_usuario = models.CharField(max_length=50, unique=True)  # ID del usuario en Slack
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)  
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)  
    opcion_seleccionada = models.CharField(max_length=255)  
    fecha_pedido = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Pedido de {self.empleado.nombre} para el {self.menu.fecha}"