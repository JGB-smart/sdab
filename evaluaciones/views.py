from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def evaluaciones(request):


    return render(request,'evaluacioneslist.html')

