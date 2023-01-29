from django.contrib import admin
from . import models

# Register your models here.

# Se crea un clase adicional que extiende de la clase principal del panel de admin
# Se especifican los campos que no se muestran para que se muestren como de lectura
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') # Campos a mostrar

admin.site.register(models.Project, ProjectAdmin)