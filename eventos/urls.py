from django.urls import path
from eventos import views


urlpatterns = [
       
    path('lista_eventos/', views.ListadoEventos.as_view(), name='lista_eventos'),
       # path('cursos/', views.cursos, name='cursos'),
]
