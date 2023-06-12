from django.urls import path
from contenidos import views


urlpatterns = [
       path('introduccion/', views.intro, name='introduccion'),
       path('tema1/', views.tema1, name='tema1'),
]
