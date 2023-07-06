from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Evaluaciones(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=150)
    image = models.ImageField(null= True, blank=True, upload_to='images/')
    documento = models.FileField(upload_to='files/')
    activa = models.BooleanField(default=True)
    fecha_inicial = models.DateField(auto_now_add=True)
    fecha_final = models.DateField()

    def __str__(self):
        return "Titulo: " + str(self.titulo)
    
    class Meta:
        verbose_name = 'Evaluación'
        verbose_name_plural = 'Evaluaciones'
        ordering = ['id']    

class Entregas(models.Model):
    test = models.ForeignKey(Evaluaciones, on_delete= models.CASCADE, related_name='evaluacion')
    entrega = models.FileField(upload_to='files/')
    mensaje = models.CharField(max_length=150)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='estudiante')
    puntaje = models.IntegerField()
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Evaluación: " + str(self.user) + " " + "Alumno:" + str(self.user)
    
    class Meta:
        verbose_name = 'Entrega'
        verbose_name_plural = 'Entregas'
        ordering = ['id']    