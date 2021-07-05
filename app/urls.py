from app.views import Inicio, agregarCancion, agregarDisco, eliminarCancion, listarCancion, listarCanciones, modificarCancion
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', Inicio, name="Inicio"),
    path('agregar-disco/', agregarDisco, name="agregarDisco"),
    path('agregar-cancion/', agregarCancion, name="agregarCancion"),
    path('modificar-cancion/<int:id>/', modificarCancion, name="modificarCancion"),
    path('eliminar-cancion/<int:id>/', eliminarCancion, name="eliminarCancion"),

    path('listar-cancion/<int:id>/', listarCancion, name="listarCancion"),
    path('listar-canciones/', listarCanciones, name="listarCanciones"),
]
