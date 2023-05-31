from django.urls import path
from usuarios import views


urlpatterns = [
       
    
    path('registro_usuarios/', views.AgregarUsuarios.as_view(), name='registro_usuarios'),
    # path('lista_eventos/', views.ListadoEventos.as_view(), name='lista_eventos'),
       # path('cursos/', views.cursos, name='cursos'),
]
