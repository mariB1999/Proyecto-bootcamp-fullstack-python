from django.db import models
#Define una clase que Django convertirá automáticamente en una tabla de base de datos por defecto llamada app.categorias
class Categoria(models.Model):
    #los nombres no pueden ir en plural porque aunque sean categorias el modelo que representa la tabla debe ser singular Crea una columna llamada nombre de tipo texto (varchar).max_length=100: Limita el texto a un máximo de 100 caracteres (nota: en tu código original dice max_leght, lo cual generará un error; debe ser max_length).unique=True: Asegura que no se puedan registrar dos categorías con el mismo nombre.
    nombre = models.CharField(max_lenght=100,unique = True)

    class Meta:
        #Meta permite ajustar configuraciones adicionales del modelo
        ordering = ['nombre']
        #Hace que las consultas a la base de datos devuelvan siempre los resultados ordenados alfabéticamente por el campo nombre.
        verbose_name = 'Categorias'
        #Define un nombre legible en singular para el panel de administración de Django osea el usuario.
        verbose_name_plural = 'Categorias'
        #Define el nombre legible en plural

    def __str__(self):
       return self.nombre

    class Libro(models.Model):
        titulo = models.CharField(max_lenght = 100,unique=True)
        autor = models.CharField(max_lenght = 100,unique=True)

    


