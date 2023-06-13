from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cursos.models import Cursos
from eventos.models import Eventos
from profesores.models import Profesores
from django.contrib.auth.models import User 


def home(request):

    cursos = Cursos.objects.count()
    eventos = Eventos.objects.count()
    profesores = Profesores.objects.count()
    estudiantes = User.objects.count()

    return render(request,'home.html',{"cursos":cursos, "eventos":eventos, "profesores":profesores,"estudiantes":estudiantes})


def about(request):


    return render(request,'about.html')
