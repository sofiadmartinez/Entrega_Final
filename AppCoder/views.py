from django.shortcuts import render
from django.db import models 
from AppCoder.models import Articulo, Usuario, Envio
from AppCoder.forms import UsuarioForm, ArticuloForm, EnvioForm, BuscarUsuariosForm
from django.views.generic import ListView #vistas basadas en clases. Clase 21, 1:30:00

def base(request):
    return render(request, "AppCoder/base.html")

#Asi estaba hasta el min 1:20:00 / 1:27:00
def crear_usuario(request):
    f = UsuarioForm(request.POST)
    usuarios = Usuario.objects.all()
    total_usuarios = len(usuarios)
    context={
        "usuarios": usuarios,
        "total_usuarios": total_usuarios,
        "form": f,
    }
   
    if f.is_valid():
        Usuario(nombre=f.data["nombre"], apellido=f.data["apellido"], dni=f.data["dni"]).save()
    
    return render(request, "AppCoder/usuarios.html", context)

#Asi esta ahora: De esta forma si yo pongo un valor invalido me va a tirar en el formulario un cartel que dice que ponga un valor valido
# def crear_usuario(request):
#      f = UsuarioForm(request.POST)
#      context = {
#         "form": f
#      }
#      if f.is_valid():
#          Usuario(nombre=f.data["nombre"], apellido=f.data["apellido"], dni=f.data["dni"]).save()
#          context['form'] = UsuarioForm()

#     context["usuarios"] = Usuario.objects.all()
#     context["total_usuarios"] = len(Usuario.objects.all())
   
#     return render(request, "AppCoder/usuarios.html", context)  

    
def cargar_articulos(request):
     f = ArticuloForm(request.POST)
     articulos = Articulo.objects.all()
     total_articulos = len(articulos)
     context={
         "articulos": articulos,
         "total_articulos": total_articulos,
         "form": f,
     }

     if f.is_valid():
         Articulo(producto=f.data["producto"], marca=f.data["marca"], cantidad=f.data["cantidad"]).save()

     return render(request, "AppCoder/articulos.html", context)



def envio_realizado(request):
    f = EnvioForm(request.POST)
    envios = Envio.objects.all()
    total_envios = len(envios)
    context = {
        "envios": envios,
        "total_envios": total_envios,
        "form": f,
    }

    if f.is_valid():
        Envio(direccion=f.data["direccion"], ciudad=f.data ["ciudad"], provincia=f.data ["provincia"], cp=f.data ["cp"]).save()
        context ['form'] = EnvioForm()
    
    return render(request, "AppCoder/envios.html", context)



class BuscarUsuarios(ListView):
    model = Usuario
    context_object_name = "usuarios"
    #este usuario matchea con el {% for usuario in usuarios %} del html. aca no se pone la url

    def get_queryset(self): #utilizado para buscar. Aca no tenemos request. pero se invoca en el self cuando utilizamos el queryset. ya viene inyectado
        f= BuscarUsuariosForm(self.request.GET) #aca metemos el formulario
        if f.is_valid(): #si el formulario es valido entonces ejecutamos la busqueda
            return Usuario.objects.filter(nombre__icontains=f.data["criterio_nombre"]).all() #Esto es una consulta sobre nombre. vamos a ocupar un filtro icontains. Icontains quiere decir que cualquier substring que se busque me va tirar la opcion. Ej busco SOF y me va a tirar SOFIA
        return Usuario.objects.none()
