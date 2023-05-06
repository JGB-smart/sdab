from django.urls import path
from cursos import views


urlpatterns = [
       path('cursos/', views.cursos, name='cursos'),
]
