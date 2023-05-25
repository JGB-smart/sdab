from django.db import models


class Materias(models.Model):
    materia = models.CharField(max_length=150,verbose_name='materia')

    def __str__(self):
        return self.materia

    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'  



class Profesores(models.Model):
    nombre = models.CharField(max_length=150,verbose_name='nombre')
    apellido = models.CharField(max_length=150,verbose_name='apellido')
    materia = models.ForeignKey(Materias,on_delete=models.CASCADE,related_name = 'materias')
    
    def __str__(self):
        return self.nombre + " " + self.apellido

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'


   
