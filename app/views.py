from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Orden, Cliente, OrdenItem
from .forms import ProductoForm, CrearUsuario
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

def perfil(request):
    return render(request, 'app/perfil.html')
def about(request):
    return render(request, 'app/about.html')


def base(request):
    return render(request, 'app/base.html')


@login_required
def cart(request):
    if request.method == 'POST':
        accion = request.POST['accion']
        
        
        if accion == 'actualizar':
            try:
                ordenidi = request.POST['ordenitemid']
                product_id = request.POST['productoid']
                cantidad = int(request.POST['cantidad'])
                
                # Obtener el producto y calcular el precio del item
                producto = Producto.objects.get(id=product_id)
                precio_item = producto.precio * cantidad
                
                # Obtener o crear el OrdenItem y actualizarlo
                ordenit, created = OrdenItem.objects.get_or_create(id=ordenidi)
                ordenit.cantidad = cantidad
                ordenit.precio = precio_item
                ordenit.save()
                
                return redirect("cart")  # Redirigir al carrito si todo está correcto
            except (KeyError, Producto.DoesNotExist):
                # Manejar errores de datos incorrectos o productos no existentes
                return redirect("cart")  # Redirigir al carrito en caso de error
            
        elif accion == 'eliminar':
            ordenidi = request.POST['ordenitemid']
            orden = get_object_or_404(OrdenItem, id=ordenidi)
            orden.delete()
            print("eliminado")
            return redirect("cart")  # Redirigir al carrito si todo está correcto
        else:
            try:
                cliente = Cliente.objects.get(user=request.user)
                ordenes = Orden.objects.filter(cliente=cliente)
                product_id = request.POST['productoid']
                cantidad = int(request.POST['cantidad'])
                producto = Producto.objects.get(id=product_id)
                
                # Calcular el precio del item
                precio_item = producto.precio * cantidad
                
                tiene_ordenes_incompletas = any(not orden.completada for orden in ordenes)
                
                if tiene_ordenes_incompletas:
                    orden_incompleta = Orden.objects.filter(cliente=cliente, completada=False).first()
                    # Crear el OrdenItem con precio calculado
                    item = OrdenItem.objects.create(orden=orden_incompleta, producto=producto, cantidad=cantidad, precio=precio_item)
                else:
                    nueva_orden = Orden.objects.create(cliente=cliente)
                    # Crear el OrdenItem con precio calculado
                    item = OrdenItem.objects.create(orden=nueva_orden, producto=producto, cantidad=cantidad, precio=precio_item)
                    
                return redirect("cart")
        
            except KeyError:
                # Redirigir a 'cart' si falta información en el formulario
                messages.error(request, 'Falta información en el formulario.')
                return redirect("cart")
            
            except Cliente.DoesNotExist:
                # Redirigir a 'cart' si el cliente no existe
                messages.error(request, 'Debe iniciar sesión como cliente.')
                return redirect("cart")
            
            except Producto.DoesNotExist:
                # Redirigir a 'cart' si el producto no existe
                messages.error(request, 'El producto seleccionado no existe.')
                return redirect("cart")
    
    ordenitems = OrdenItem.objects.filter(orden__cliente__user=request.user)
    datos = {'ordenitems': ordenitems}
    return render(request, 'app/cart.html', datos)

def checkout(request):
    cliente = Cliente.objects.get(user=request.user)
    orden_incompleta = Orden.objects.filter(cliente=cliente, completada=False).first()
    orden_incompleta.calcular_total()
    ordenes=OrdenItem.objects.filter(orden=orden_incompleta)
    datos={
        'cliente':cliente,
        'orden':orden_incompleta,
        'ordenes':ordenes
    }
    return render(request, 'app/checkout.html',datos)

def cliente(request):
    return render(request, 'app/cliente.html')

def contact(request):
    return render(request, 'app/contact.html')

def index(request):
    return render(request, 'app/index.html')

def producto(request,id):
    producto = get_object_or_404(Producto, id=id)
    datos={
        'p':producto
    }
    return render(request, 'app/producto.html', datos)

def shop(request):
    productos=Producto.objects.all()
    
    datos={
        
        "productos":productos
    }
    return render(request, 'app/shop.html', datos)

def thankyou(request):
    if request.method == 'POST':
        id = request.POST['orden']
    orden = Orden.objects.filter(id=id).first()
    orden.completada = True
    orden.save()
    datos={
        'orden':orden
    }
    print(orden)
    return render(request, 'app/thankyou.html',datos)

def dash(request):
    return render(request, 'dash/index.html')

def register(request):
    if request.method == 'POST':
        form = CrearUsuario(request.POST)
        if form.is_valid():
            user = form.save()
            Cliente.objects.create(
                user=user,
                nombre=user.first_name,
                apellidos=user.last_name,
                email=user.email
            )
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

