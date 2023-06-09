"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppCoder.views import (cargar_articulos, crear_usuario, envio_realizado, base, BuscarUsuarios)



urlpatterns = [
    path('',base),
    path('admin/', admin.site.urls),
    path('articulos/create', cargar_articulos, name="articulos-create"),
    path('usuarios/create', crear_usuario, name="usuarios-create"),
    path('envios/create', envio_realizado, name="envios-create"),
    path('usuarios/list', BuscarUsuarios.as_view(), name="usuarios-list" ), #importamos una clase no una funcion. as.view lo que hace es convertir una class review en una function review. que es lo que necesita para funcionar
    
    ]
