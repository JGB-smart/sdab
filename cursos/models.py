from django.db import models
from profesores.models import Materias,Profesores

# Create your models here.

class Cursos(models.Model):
    curso = models.CharField(max_length=150,verbose_name='curso')
    descripcion = models.CharField(max_length=150,verbose_name='descripcion')
    Fcurso = models.DateField()
    materia = models.ForeignKey(Materias,on_delete=models.CASCADE,related_name = 'categoria')
    profesor = models.ForeignKey(Profesores,on_delete=models.CASCADE,related_name = 'encargado')

    def __str__(self):
        return self.curso

    class Meta:
        verbose_name = 'Cursos'
        verbose_name_plural = 'Cursos'  