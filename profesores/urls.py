from django.urls import path
from profesores import views


urlpatterns = [
       path('profesores/', views.profesores, name='profesores'),
]
