from django.shortcuts import render
from django.db import models #esto es de la clase 19, parte modelos
from AppCoder.models import Tarea, Persona
from AppCoder.forms import PersonaForm #clase 20

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

#Clase 20:

def mostrar_personas(request):
    personas = Persona.objects.all()
    total_personas = len(personas)
    context= {
        "personas": personas,
        "total_personas": total_personas,
        "form": PersonaForm(),
    }
    return render(request,"AppCoder/personas.html", context)

def crear_persona(request):
    f = PersonaForm(request.POST)
    personas = Persona.objects.all()
    total_personas = len(personas)
    context={
        "personas": personas,
        "total_personas": total_personas,
        "form": f,
    }

    

    if f.is_valid():
        Persona(f.data["nombre"], f.data["apellido"], f.data["fecha_nacimiento"]).save()
    
    return render(request, "AppCoder/personas.html",context)
