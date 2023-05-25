from django.contrib import admin
from .models import Materias
from .models import Profesores


admin.site.register(Materias)
admin.site.register(Profesores)