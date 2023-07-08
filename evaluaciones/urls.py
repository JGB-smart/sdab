from django.urls import path
from evaluaciones import views


urlpatterns = [
       path('evaluaciones/', views.evaluaciones, name='evaluaciones'),
       path('evaluacion/<int:pk>', views.evaluacion, name='evaluacion'),
       path('entregar/<int:pk>', views.entrega, name='entrega'),
       path('calificaciones/<int:pk>', views.calificaciones, name='calificaciones')
]
