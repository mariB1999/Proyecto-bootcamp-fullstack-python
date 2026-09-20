from django.db import models
from django.conf import settings
from django.urls import reverse

class Proyecto(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='proyectos')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("proyecto_detail", kwargs ={"pk": self.pk})

class Tarea(models.Model):
    ESTADOS = [
        #uno es el dato como se almacenara y otro es como se vera
        ("pendiente","Pendiente"),
        ("en_proceso","En proceso"),
        ("finalizado","Finalizado")
    ]

    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE,related_name='tareas')
    #estados posibles son solo los que estan disponibles en la lista
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,#establece los valores posibles
        default='pendiente' #valor por defecto
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.titulo
    




