from django.urls import path
from cursos import views


urlpatterns = [
       
       path('lista_cursos/', views.ListadoCursos.as_view(), name='lista_cursos'),
       # path('cursos/', views.cursos, name='cursos'),
]
