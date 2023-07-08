from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from evaluaciones.models import Evaluaciones,Entregas

from evaluaciones.forms import EntregaTestForm

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
        entrega = Entregas.objects.filter(test_id = pk).filter(user_id=request.user.id)

        if(entrega):
             entregado = True
        else:
             entregado = False     

        data = {
            'evaluacion' : test,
            'id':pk,
            'entregado': entrega
        }


        return render(request,'evaluacion.html',data)
    
def entrega(request,pk):
        
        form = EntregaTestForm()

        data = {
             'form' : form,
             'id':pk
        }

        if request.method == 'GET':
             

            return render(request,'entregaform.html',data)
        
        elif request.method == 'POST':
             
             form = EntregaTestForm(request.POST, request.FILES)
            #  datos = request.POST
            #  documento = request.FILES['entrega']
            #  print(datos)
            #  print(documento)    

             if form.is_valid():

                post = form.save(commit = False)
                post.test_id = pk
                post.user_id = request.user.id
                post.save()

                messages.success(request,"Evaluación Enviada!")
                return redirect('evaluaciones')
             else:

                    return render(request,'entregaform.html',{'form':form}) 
             
def calificaciones(request,pk):
     
     if request.method == 'GET':

        calificaciones = Entregas.objects.all().filter(user_id=request.user.id)

        data = {
             'calificaciones':calificaciones
        }
          
     
        return render(request,'calificaciones.html',data)             