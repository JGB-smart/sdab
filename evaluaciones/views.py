from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required

from evaluaciones.models import Evaluaciones,Entregas

@login_required
def evaluaciones(request):

    if request.method == 'GET':
        test = Evaluaciones.objects.all().exclude(activa = False)

        data = {
            'evaluaciones' : test
        }


    return render(request,'evaluacioneslist.html',data)

@login_required
def evaluacion(request,pk):

    if request.method == 'GET':
        test = get_object_or_404(Evaluaciones,id = pk)

        data = {
            'evaluacion' : test
        }


        return render(request,'evaluacion.html',data)