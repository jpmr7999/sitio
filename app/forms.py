from django import forms
from .models import Producto
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CrearUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['imagen','nombre','descripcion','precio','stock','categoria',]


