from django.contrib import admin

# Register your models here.
from Academic.models import *

@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre')
    search_fields = ['nombre']
    list_filter = ['duracion', 'nombre']
    list_per_page = 1

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
	list_display = ('ci', 'nombreCompleto','fechaNace','sexo')
	search_fields = ['dni']
	list_filter = ['nombres','apellidoPaterno']
	list_per_page = 1

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
	list_display = ('codigo','nombre','creditos','docente')

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
	list_display = ('id','estudiante','curso','fecha')
