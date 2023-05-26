from django.db import models
from profesores.models import Profesores
class Eventos(models.Model):
    evento = models.CharField(max_length=150,verbose_name='evento')
    tematica = models.CharField(max_length=150,verbose_name='tematica ')
    profesor = models.ForeignKey(Profesores,on_delete=models.CASCADE,related_name = 'exponente')
    descripcion = models.CharField(max_length=150,verbose_name='descripcion')
    Fevento = models.DateField()


    def __str__(self):
        return self.evento

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'