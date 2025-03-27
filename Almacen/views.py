from django.shortcuts import render,redirect
from .models import Productos

# Create your views here.

def home(request): #index web
    return render(request, 'base.html')

def lista_productos(request): #edicion de productos
    listaprod=Productos.objects.all()
    return render(request, 'lista_productos.html', {'productos':listaprod}) #<<<'productos' ref en lista_prod.

def gestion_prod(request): #LINK REGISTRO PRODUCTOS // FRONTEND // SIN ACCIONES
    return render(request, 'gestion_prod.html')

def reg_productos(request): #REGISTRO DE PRODUCTOS // BACKEND // CON ACCIONES
    codigo=request.POST['txtcodigo']
    nombre=request.POST['txtnombre']
    precio=request.POST['txtprecio']
    cantidad=request.POST['txtcantidad']
    familia=request.POST['txtfamilia']
    subfamilia=request.POST['txtsubfamilia']
    
    n_producto=Productos.objects.create(
        codigo=codigo,nombre=nombre,precio=precio,cantidad=cantidad,familia=familia,subfamilia=subfamilia)   
    return render(request,'gestion_prod.html')

def editar_productos(request,codigo): #LINK REGISTRO PRODUCTOS // FRONTEND // SIN ACCIONES
    edicion_producto=Productos.objects.get(codigo=codigo)
    return render(request, 'editar_producto.html', {'producto':edicion_producto})

def editar_prod(request):
    codigo=request.POST['txtcodigo']
    nombre=request.POST['txtnombre']
    precio=request.POST['txtprecio']
    cantidad=request.POST['txtcantidad']
    familia=request.POST['txtfamilia']
    subfamilia=request.POST['txtsubfamilia']
    
    edicion_producto=Productos.objects.get(codigo=codigo)
    edicion_producto.codigo=codigo
    edicion_producto.nombre=nombre
    edicion_producto.precio=precio
    edicion_producto.cantidad=cantidad
    edicion_producto.familia=familia
    edicion_producto.subfamilia=subfamilia
    edicion_producto.save()
    return redirect('/productos/')

def eliminar_productos(id): #Eliminar productos
    elim_producto=Productos.objects.get(id=id)
    elim_producto.delete()
    return redirect('/productos/') #redirect> carga vista cfg. en urls.py

