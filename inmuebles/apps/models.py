from django.db import models
from django.contrib.auth.models import User

# Modelo para la comuna
class Usuario(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    rut = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    tipo_usuario = models.CharField(max_length=20, default='arrendatario')

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.tipo_usuario}"

  
# Modelo para el inmueble        
class Inmueble(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('Casa','Casa'),
        ('Departamento','Departamento'),
        ('Parcela','Parcela')
    ]
    nombre = models.CharField(null= False, blank=False, max_length=100)
    descripcion = models.TextField(null= False, blank=False)
    m2_construidos = models.IntegerField(null= False, blank=False)
    m2_totales = models.IntegerField(null= False, blank=False)
    estacionamientos = models.IntegerField(null= False, blank=False)
    habitaciones = models.IntegerField(null= False, blank=False)
    banos = models.IntegerField(null= False, blank=False)
    direccion = models.CharField(max_length=200)
    comuna = models.CharField(max_length=25)
    tipo_inmueble = models.CharField(max_length=20,choices=PROPERTY_TYPE_CHOICES, on_delete=models.CASCADE)
    precio_arriendo = models.IntegerField(null= False, blank=False)
    

    def __str__(self):
        return f"{self.nombre} - {self.comuna} - {self.arrendador}"

# Modelo para la solicitud de arriendo
class SolicitudArriendo(models.Model):
    arrendatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitudes')
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE, related_name='solicitudes')
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    mensaje = models.TextField(blank=True)

    def __str__(self):
        return f'Solicitud de {self.arrendatario.username} para {self.inmueble.nombre}'