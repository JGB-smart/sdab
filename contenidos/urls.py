from django.urls import path
from contenidos import views


urlpatterns = [

       path('introduccion/', views.tema1, name='introduccion'),
]
