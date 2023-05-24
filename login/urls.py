from django.urls import path
from login import views


urlpatterns = [
        path('salir/', views.salir, name='salir'),
    #    path('introduccion/', views.tema1, name='introduccion'),
]