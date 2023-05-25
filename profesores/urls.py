from django.urls import path
from profesores import views


urlpatterns = [
       path('lista_profesores/', views.ListadoProfesores.as_view(), name='lista_profesores'),
       # path('profesores/', views.profesores, name='profesores'),
]
