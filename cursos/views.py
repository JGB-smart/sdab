from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from cursos.models import Cursos






class ListadoCursos(ListView):
    model = Cursos
    template_name = 'lista_cursos.html'
    context_object_name = 'cursos'             # permite cambiar de nombre al objetos listview que se llamara en la vista
    queryset=  Cursos.objects.all()           #  Permite realizar filtros a la consulta
                                              # PROBAR:REMPLAZAR QUERYSET por su metodo de este modo:
                                                ## def get_queryset(self):
                                                ##  return self.model.objects.filter(fitrodecampo)   
                                                
    @method_decorator(login_required)             #Puede agrupar decoradores
    def dispatch(self, request, *args, **kwargs):



        return super(ListadoCursos,self).dispatch(request, *args, **kwargs)