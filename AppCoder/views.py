from django.shortcuts import render
from django.db import models #esto es de la clase 19, parte modelos
from AppCoder.models import Tarea

def mostrar_mi_template(request, nombre, apellido):
    context={ 
        "nombre":nombre,
        "apellido":apellido,
        "notas":[5,6,7,8,9,10]
    }
    return render(request,"AppCoder/index.html", context)

#aca empieza la parte del video de la clase 19, modelos

def mostrar_mis_tareas(request,criterio):
    tareas = Tarea.objects.filter(nombre=criterio).all()
    return render(request,"AppCoder/index.html", {"tareas":tareas})
