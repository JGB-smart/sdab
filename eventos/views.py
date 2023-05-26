from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from eventos.models import Eventos




class ListadoEventos(ListView):
    model = Eventos
    template_name = 'lista_eventos.html'
    context_object_name = 'eventos'             # permite cambiar de nombre al objetos listview que se llamara en la vista
    queryset=  Eventos.objects.all()           #  Permite realizar filtros a la consulta
                                              # PROBAR:REMPLAZAR QUERYSET por su metodo de este modo:
                                                ## def get_queryset(self):
                                                ##  return self.model.objects.filter(fitrodecampo)   
                                                
    @method_decorator(login_required)             #Puede agrupar decoradores
    def dispatch(self, request, *args, **kwargs):



        return super(ListadoEventos,self).dispatch(request, *args, **kwargs)