from django.urls import path
from AppCoder import views

urlpatterns = [
    path('',views.inicio,name="Inicio"),
    path('cursos', views.Cursos, name="Cursos"),
    path('profesores', views.profesores,name="Profesores"),
    path('estudiantes',views.estudiantes,name="Estudiantes"),
    path('entregables', views.entregables, name="Entregables"),
]