from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Producto, Compra
from proyecto.Carrito import Carrito
from django.contrib.auth import login, authenticate, logout
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db import transaction
from decimal import Decimal


# Create your views here.

def home(request):
    context = {
        'username': request.user.username if request.user.is_authenticated else None
    }
    return render(request, "proyecto/index.html", context)

def moca(request):
    context={

    }
    return render(request,"proyecto/moca.html",context)

def login_t(request):

    if request.method== "POST":
        usuario= request.POST["username"]
        contrasena= request.POST["password"]
        user= authenticate(request, username= usuario, password= contrasena)
    
        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            return redirect('login_t') 
    else:

        context={ 
        }   
        return render(request,"proyecto/login.html",context)

def beneficio(request):
    context={

    }
    return render(request,"proyecto/beneficio.html",context)

def expreso(request):
    context={

    }
    return render(request,"proyecto/expreso.html",context)

def capuchino(request):
    context={

    }
    return render(request,"proyecto/capuchino.html",context)

def carrito(request):
    # Lógica de la vista carrito aquí
    return render(request, 'proyecto/carrito.html', {})  # Ejemplo de renderización de un template



def agregar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    carrito = request.session.get('carrito', {})
    
    # Convertir el precio (Decimal) a float antes de almacenarlo
    precio_float = float(producto.precio)
    
    # Guardar en la sesión
    carrito[producto_id] = {
        'producto_id': producto_id,
        'nombre': producto.nombre,
        'precio': precio_float,  # Convertir a float antes de almacenarlo
        'cantidad': 1,
        'acumulado': precio_float,  # Convertir a float si es necesario
    }
    request.session['carrito'] = carrito
    request.session.modified = True
    
    return redirect('tienda') # Asegúrate de que "tienda" sea el nombre correcto de la vista de la tienda

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("tienda")

def tienda(request):
    productos = Producto.objects.all()
    return render(request, "proyecto/tienda.html", {'productos': productos})

def nosotros(request):
    # Aquí puedes agregar información sobre la cafetería
    informacion = {
        'nombre_cafeteria': 'Baristas',
        'descripcion': 'Matias Gonzalez - Dueño De Baristas.',
        'direccion': 'Calle Principal Grecia, Santiago, Chile',
        'telefono': '+56934567890',
        'email': 'info@cafeteriaBarista.com',
        'imagen_url': '/static/img/chico.jpg',  # Ruta de la imagen en tu proyecto
    }
    return render(request, 'proyecto/nosotros.html', informacion)

def generar_factura(request):
    # Obtener los datos del carrito desde la sesión
    carrito = request.session.get('carrito', {})
    
    # Calcular el total de la factura
    total_carrito = sum(item['acumulado'] for item in carrito.values())

    # Aquí podrías agregar más lógica para generar tu factura
    # Por ejemplo, crear un objeto de factura en la base de datos, etc.

    # Renderizar la plantilla de la factura
    return render(request, 'proyecto/factura.html', {
        'carrito': carrito,
        'total_carrito': total_carrito,
    })