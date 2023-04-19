from django import forms

class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    dni = forms.CharField(max_length=50)

class ArticuloForm(forms.Form):
    producto = forms.CharField(max_length=100)
    marca = forms.CharField(max_length=100, initial="samsung")
    cantidad = forms.CharField(max_length=100, initial="1")
    #ingresado_el = forms.DateField()

class EnvioForm(forms.Form):
    direccion = forms.CharField(max_length=100)
    ciudad = forms.CharField(max_length=100, initial=" ")
    provincia = forms.CharField(max_length=100, initial=" ")
    cp =  forms.CharField(max_length=100, initial=" ")
    #fecha_ingreso = forms.DateField()

