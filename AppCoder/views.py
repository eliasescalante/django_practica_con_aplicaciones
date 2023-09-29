from django.shortcuts import render
from AppCoder.models import *
from django.http import HttpResponse
from AppCoder.forms import CursoFormulario, ProfesorFormulario
# Create your views here.
def inicio(request):
    return render(request,"AppCoder\index.html")

def Cursos(request):
    return render(request,"AppCoder\cursos.html")

def profesores(request):
    return render(request,"AppCoder\profesores.html")

def estudiantes(request):
    return render(request,"AppCoder\estudiantes.html")

def entregables(request):
    return render(request,"AppCoder\entregables.html")

def cursoFormulario(request):

    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion['curso'], camada=informacion['camada'])
            curso.save()
            return render(request, "AppCoder\index.html")
    else:
        miFormulario=CursoFormulario()
    return render(request, "AppCoder\cursoFormulario.html", {"miFormulario":miFormulario})

def profesorFormulario(request):
    if request.method =='POST':
        miFormulario = ProfesorFormulario(request.POST)
        informacion = miFormulario.cleaned_data

        profesor = Profesor(nombre=informacion['nombre'],apellido=informacion['apellido'],
                        email=informacion['email'], profesion=informacion['profesion'])
        profesor.save()

        return render(request, "AppCoder\index.html")
    else:
        miFormulario = ProfesorFormulario()
    return render(request,"AppCoder\profesorFormulario.html",{"miFormulario":miFormulario})