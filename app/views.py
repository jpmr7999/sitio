from django.shortcuts import render
from .models import Producto, Orden, Cliente, OrdenItem
from .forms import ProductoForm, CrearUsuario
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def perfil(request):
    return render(request, 'app/perfil.html')
def about(request):
    return render(request, 'app/about.html')

def base(request):
    return render(request, 'app/base.html')

def cart(request):
    ordenitem = OrdenItem.objects.all()
    datos = {
        'ordenitem':ordenitem
    }
    return render(request, 'app/cart.html', datos)

def checkout(request):
    return render(request, 'app/checkout.html')

def cliente(request):
    return render(request, 'app/cliente.html')

def contact(request):
    return render(request, 'app/contact.html')

def index(request):
    return render(request, 'app/index.html')

def producto(request):
    return render(request, 'app/producto.html')

def shop(request):
    return render(request, 'app/shop.html')

def thankyou(request):
    return render(request, 'app/thankyou.html')

def dash(request):
    return render(request, 'dash/index.html')

def register(request):
    if request.method == 'POST':
        form = CrearUsuario(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')  # Redirige a la página principal u otra página
    else:
        form = CrearUsuario()
    return render(request, 'dash/register.html', {'form': form})

def password(request):
    return render(request, 'dash/password.html')

def tabla_clientes(request):
    clientes=Cliente.objects.all()
    datos={
        "clientes":clientes
    }
    
    return render(request, 'dash/tabla_clientes.html')

def tabla_ordenes(request):
    ordenes=Orden.objects.all()
    datos={
        "ordenes":ordenes
    }
    return render(request, 'dash/tabla_ordenes.html',datos)

def tabla_producto(request):
    productos=Producto.objects.all()
    
    datos={
        
        "productos":productos
    }

    return render(request, 'dash/tabla_producto.html', datos)

def agregar_producto(request):
    form=ProductoForm()

    if request.method=="POST":
        form=ProductoForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to="tabla_producto")

    datos={
        "form":form
    }
    return render(request, 'dash/agregar_producto.html',datos)

def modificar_producto(request):
    return render(request, 'dash/modificar_producto.html')

def formulario_cliente(request):
    return render(request, 'dash/formulario_cliente.html')

def modificar_cliente(request):
    return render(request, 'dash/modificar_cliente.html')

def agrega(request):
    return render(request, 'dash/agrega.html')

