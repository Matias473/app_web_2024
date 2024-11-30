from django.urls import path
from . import views

# aqui iran todas las urls del sistema o vistas
urlpatterns = [
    path('inicio/', views.index, name='inicio'),
    path('', views.index, name='inicio'),
    path('acercade/', views.about, name='acercade'),
    path('mision/', views.mision, name='mision'),
    path('vision/', views.vision, name='vision'),
    path('login/', views.inicio_sesion, name='inicio_sesion'),
    path('registrarse/', views.registrarse, name='registrarse'),
]