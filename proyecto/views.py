from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Producto
from proyecto.Carrito import Carrito
from django.contrib.auth import login, authenticate, logout
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def home(request):
    context={
         'username': request.user.username  # Pasar el nombre de usuario al contexto

    }
    return render(request,"proyecto/index.html",context) 

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
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("tienda")  # Asegúrate de que "tienda" sea el nombre correcto de la vista de la tienda

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

