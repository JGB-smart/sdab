from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.views.generic import View
from django.contrib import messages

from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from usuarios.forms import RegistrationForm







class AgregarUsuarios(View):
    
    template = 'agg_usuarios.html'

    def get(self,request):
        form = RegistrationForm()

        return render(request,self.template,{"form":form})


    def post(self,request):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            
            usuario = form.save()
            usuario.groups.add(1)
            login(request, usuario)
            return redirect('home')
        
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request,self.template,{"form":form})
