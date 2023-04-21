from django.shortcuts import render
from django.db import models 
from AppCoder.models import Articulo, Usuario, Envio
from AppCoder.forms import UsuarioForm, ArticuloForm, EnvioForm

def base(request):
    return render(request, "AppCoder/base.html")

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
        Usuario(f.data["nombre"], f.data["apellido"], f.data["dni"]).save()
    
    return render(request, "AppCoder/usuarios.html", context)

def cargar_articulos(request):
    f= ArticuloForm(request.POST)
    if f.is_valid():
        data = f.cleaned_data
        articulo = Articulo(
            producto= data["producto"],
            marca= data["marca"],
            cantidad= data["cantidad"]
        )
        articulo.save()
        return redirect("articulos-create")
    
    f= ArticuloForm()
    articulos = Articulo.objects.all()
    total_articulos = len(articulos)
    context={
        "articulos": articulos,
        "total_articulos": total_articulos,
        "form": f
    }

    return render(request, "AppCoder/articulos.html", context)
    
# def cargar_articulos(request):
#     f = ArticuloForm(request.POST)
#     articulos = Articulo.objects.all()
#     total_articulos = len(articulos)
#     context={
#         "articulos": articulos,
#         "total_articulos": total_articulos,
#         "form": f,
#     }

#     if f.is_valid():
#         Articulo(f.data["producto"], f.data["marca"], f.data["cantidad"]).save()

#     return render(request, "AppCoder/articulos.html", context)



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
        Envio(f.data["direccion"], f.data ["ciudad"], f.data ["provincia"], f.data ["cp"]).save()
    
    return render(request, "AppCoder/envios.html", context)


#def busqueda(request):
#    return render(request, "AppCoder/busqueda.html")

#def buscar(request):
#    respuesta = f"Estos son los resultados del usuario"
#    return HttpResponse(respuesta)