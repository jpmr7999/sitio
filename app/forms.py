from django import forms
from .models import Producto, Direccion, Categoria, Direccion, Orden
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class OrdenForm(forms.ModelForm):

    class Meta:
        model = Orden
        fields = '__all__'

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = '__all__'

class CrearUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']
class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'

class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = '__all__'




