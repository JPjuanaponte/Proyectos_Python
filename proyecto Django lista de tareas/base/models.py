from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tarea(models.Model): # logica de dfatos uno a varios - un solo elemento pude tener multiples tareas.
    usuario = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 null=True,
                                 blank= True) # cascade si se elimina el usuario se elimina sus tareas. 
    titulo = models.CharField(max_length=200) 
    descripcion = models.TextField(null=True,
                                   blank=True)
    completo = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['completo']


