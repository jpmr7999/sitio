from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Orden, Cliente, OrdenItem, Direccion
from .forms import ProductoForm, CrearUsuario, CategoriaForm, OrdenForm,UpdateClienteForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


def detalleorden(request,id):
    orden=get_object_or_404(Orden, id=id)
    items = OrdenItem.objects.filter(orden=orden)
    datos={
         "orden":orden,
         'items':items
     }
    return render(request, 'app/detalleorden.html',datos)

def misordenes(request):
    cliente = Cliente.objects.get(user=request.user)
    ordenes = Orden.objects.filter(cliente=cliente)
    datos={
        'cliente':cliente,
        'ordenes':ordenes
    }
    
    return render(request, 'app/misordenes.html',datos)

def misdirecciones(request):
    cliente = Cliente.objects.get(user=request.user)
    direcciones = Direccion.objects.filter(cliente=cliente)
    datos={
        'cliente':cliente,
        'direcciones':direcciones
    }
    return render(request, 'app/misdirecciones.html', datos)

def perfil(request):
    cliente = Cliente.objects.get(user=request.user)

    form=UpdateClienteForm(instance=cliente)
    datos={
        "form":form,
        "cliente":cliente
    }

    if request.method=="POST":
        form=UpdateClienteForm(data=request.POST, files=request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            messages.warning(request,'Datos Modificados')
            return redirect(to='perfil')
    
    return render(request, 'app/perfil.html',datos)

def about(request):
    return render(request, 'app/about.html')


def base(request):
    return render(request, 'app/base.html')


@login_required
def cart(request):
    if request.method == 'POST':
        accion = request.POST.get('accion')
        
        if accion == 'actualizar':
            try:
                ordenitem_id = request.POST.get('ordenitemid')
                product_id = request.POST.get('productoid')
                cantidad = int(request.POST.get('cantidad'))
                
                # Obtener el producto y calcular el precio del item
                producto = Producto.objects.get(id=product_id)
                precio_item = producto.precio * cantidad
                
                # Obtener o crear el OrdenItem y actualizarlo
                ordenitem = OrdenItem.objects.get(id=ordenitem_id)
                ordenitem.cantidad = cantidad
                ordenitem.precio = precio_item
                ordenitem.save()
                
                messages.success(request, 'El item ha sido actualizado correctamente.')
                return redirect("cart")
            except (KeyError, Producto.DoesNotExist, OrdenItem.DoesNotExist):
                messages.error(request, 'Error al actualizar el item.')
                return redirect("cart")
            
        elif accion == 'eliminar':
            try:
                ordenitem_id = request.POST.get('ordenitemid')
                ordenitem = get_object_or_404(OrdenItem, id=ordenitem_id)
                ordenitem.delete()
                
                messages.success(request, 'El item ha sido eliminado correctamente.')
                return redirect("cart")
            except (KeyError, OrdenItem.DoesNotExist):
                messages.error(request, 'Error al eliminar el item.')
                return redirect("cart")
                
        else:  # Añadir nuevo item al carrito
            try:
                cliente = Cliente.objects.get(user=request.user)
                product_id = request.POST.get('productoid')
                cantidad = int(request.POST.get('cantidad'))
                producto = Producto.objects.get(id=product_id)
                
                # Calcular el precio del item
                precio_item = producto.precio * cantidad
                
                orden_incompleta = Orden.objects.filter(cliente=cliente, completada=False).first()
                
                if orden_incompleta:
                    item = OrdenItem.objects.create(orden=orden_incompleta, producto=producto, cantidad=cantidad, precio=precio_item)
                else:
                    nueva_orden = Orden.objects.create(cliente=cliente)
                    item = OrdenItem.objects.create(orden=nueva_orden, producto=producto, cantidad=cantidad, precio=precio_item)
                
                messages.success(request, 'El item ha sido añadido al carrito.')
                return redirect("cart")
            except KeyError:
                messages.error(request, 'Falta información en el formulario.')
                return redirect("cart")
            except Cliente.DoesNotExist:
                messages.error(request, 'Debe iniciar sesión como cliente.')
                return redirect("cart")
            except Producto.DoesNotExist:
                messages.error(request, 'El producto seleccionado no existe.')
                return redirect("cart")
    
    cliente = Cliente.objects.get(user=request.user)
    ordenitems = OrdenItem.objects.filter(orden__cliente=cliente, orden__completada=False)
    datos = {'ordenitems': ordenitems}
    return render(request, 'app/cart.html', datos)

def checkout(request):
    cliente = Cliente.objects.get(user=request.user)
    orden_incompleta = Orden.objects.filter(cliente=cliente, completada=False).first()
    orden_incompleta.calcular_total()
    orden_incompleta.completada = True
    orden_incompleta.save()
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
    
    return render(request, 'dash/tabla_clientes.html', datos)

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

def agregar_categoria(request):
    form=CategoriaForm()

    if request.method=="POST":
        form=CategoriaForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to="tabla_producto")

    datos={
        "form":form
    }
    return render(request, 'dash/agregar_producto.html',datos)
def agregar_orden(request):
    form=OrdenForm()

    if request.method=="POST":
        form=OrdenForm(data=request.POST, files=request.FILES)
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

