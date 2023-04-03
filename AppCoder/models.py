from django.db import models

#Aca vamos a empezar con la parte de modelos, que se encuentra en la clase 19:

class Tarea(models.Model):
    nombre = models.TextField(max_length=100)
    estado = models.TextField(max_length=100, default="por hacer")
    creado_el = models.DateTimeField(auto_now_add=True)
    modificado_el = models.DateTimeField(auto_now=True)

    def terminar(self):
        self.estado = "terminado"

    def __str__(self):
        return f"{self.id} - {self.nombre}"
    