from django.db import models

# Create your models here.

class Productos (models.Model):
    codigo=models.CharField(max_length=20, unique=True)
    nombre=models.CharField(max_length=100)
    precio=models.DecimalField(max_digits=10,decimal_places=2)
    cantidad=models.DecimalField(max_digits=10,decimal_places=2)
    familia=models.CharField(max_length=30)
    subfamilia=models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.codigo} - {self.nombre} - ({self.cantidad})"