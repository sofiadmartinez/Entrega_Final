from django.contrib import admin
from AppCoder.models import Articulo, Usuario, Envio
from AppCoder.forms import ArticuloForm, UsuarioForm, EnvioForm

admin.site.register(Usuario)
admin.site.register(Articulo)
admin.site.register(Envio)