from django.contrib import admin
from .models import Cliente, Perfil, Categoria, Producto, Direccion, Orden, OrdenItem, Pago

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'email', 'telefono')
    search_fields = ('nombre', 'apellidos', 'email')

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha_nacimiento', 'genero')
    search_fields = ('cliente__nombre', 'cliente__apellidos')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'categoria')
    search_fields = ('nombre', 'categoria__nombre')
    list_filter = ('categoria',)

@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'direccion','region', 'ciudad', 'codigo_postal', 'tipo')
    search_fields = ('cliente__nombre', 'cliente__apellidos', 'direccion', 'ciudad', 'estado', 'codigo_postal', 'pais')

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha_creacion', 'completada', 'direccion_envio', 'total')
    search_fields = ('cliente__nombre', 'cliente__apellidos')
    list_filter = ('completada', 'fecha_creacion')

@admin.register(OrdenItem)
class OrdenItemAdmin(admin.ModelAdmin):
    list_display = ('orden', 'producto', 'cantidad', 'precio')
    search_fields = ('orden__cliente__nombre', 'orden__cliente__apellidos', 'producto__nombre')

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('orden', 'metodo', 'transaccion_id', 'monto', 'fecha')
    search_fields = ('orden__cliente__nombre', 'orden__cliente__apellidos', 'transaccion_id')
    list_filter = ('metodo', 'fecha')



# Registramos los modelos sin decoradores
# admin.site.register(Cliente, ClienteAdmin)
# admin.site.register(Perfil, PerfilAdmin)
# admin.site.register(Categoria, CategoriaAdmin)
# admin.site.register(Producto, ProductoAdmin)
# admin.site.register(Direccion, DireccionAdmin)
# admin.site.register(Orden, OrdenAdmin)
# admin.site.register(OrdenItem, OrdenItemAdmin)
# admin.site.register(Pago, PagoAdmin)
# admin.site.register(Inventario, InventarioAdmin)
