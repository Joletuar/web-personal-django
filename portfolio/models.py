from django.db import models

# Create your models here.

# verbose_name permite cambiar el nombre con el cual se mostran los campos al público sin tener que alterar los nombres de las columnas en la base

# upload_to permite especificar la ruta donde se van a guardar las imagenes
# Esto crea una carpeta nueva dentro de la carpeta general MEDIA que se configuró en el archivo de settings.py

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imagen', upload_to='projects')
    url = models.URLField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de creación') # Se añadirá la hora automaticamente la primera vez que se cree una instancia
    updated = models.DateTimeField(auto_now = True,verbose_name='Fecha de actualización') # Se añade automaticamente la hora cada vez que se interactúe con una instancia de este
    class Meta:
        verbose_name = 'proyecto' #Nombre de como se mostrará al público
        verbose_name_plural = 'proyectos' #Nombre de como se mostrará al público en plural
        ordering =  ["-created"]
    
    def __str__(self) :
        return self.title