from app.models import Cancion, Disco
from django.shortcuts import redirect, render

from datetime import date

# Create your views here.

def Inicio(request):
    discos = Disco.objects.all()
    try:
        cancion = Cancion.objects.get(id=2)
    except:
        cancion = None

    contexto = {'discos': discos, 'cancion': cancion}

    return render(request, 'inicio.html', contexto)


def agregarDisco(request):
    fecha = date.today()
    disco = Disco(nombre = 'Evolve', fecha=fecha)
    disco.save()

    return redirect('Inicio')

def agregarCancion(request):
    nombre   = request.POST.get('nombre-cancion', '')
    artista  = request.POST.get('artista-cancion', '')
    id_disco = request.POST.get('disco-cancion', '')
    duracion = request.POST.get('duracion-cancion', '')

    disco   = Disco.objects.get(id=id_disco)

    cancion = Cancion(artista=artista, nombre=nombre, disco=disco, duracion = duracion)
    cancion.save()

    return redirect('Inicio')

def modificarCancion(request, id):
    nombre   = request.POST.get('nombre-cancion', '')
    artista  = request.POST.get('artista-cancion', '')
    id_disco = request.POST.get('disco-cancion', '')
    duracion = request.POST.get('duracion-cancion', '')

    disco   = Disco.objects.get(id=id_disco)
    cancion = Cancion. objects.get(id = id)

    cancion.artista  = artista
    cancion.nombre   = nombre
    cancion.disco    = disco
    cancion.duracion = duracion

    cancion.save()

    return redirect('Inicio')

def eliminarCancion(request, id):
    cancion = Cancion.objects.get(id = id)
    cancion.delete()

    return redirect('Inicio')

def listarCancion(request, id):
    cancion   = Cancion.objects.get(id = id)
    return redirect('Inicio')

def listarCanciones(request):
    canciones = Cancion.objects.all()
    return redirect('Inicio')