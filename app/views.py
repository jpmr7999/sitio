from django.shortcuts import render
from .models import Producto, Orden, Cliente, OrdenItem
from .forms import ProductoForm
from django.shortcuts import get_object_or_404, redirect
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

def loginn(request):
    return render(request, 'dash/login.html')

def register(request):
    return render(request, 'dash/register.html')

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

