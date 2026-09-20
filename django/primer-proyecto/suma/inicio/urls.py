from django.urls import path
#Importa la función path() de Django, que se encarga de asociar una ruta de texto (URL) con su correspondiente vista.
from . import views
#Importa el archivo views.py ubicado en el mismo directorio (indicado por el punto .). Este archivo contiene la lógica de negocio y la respuesta que se enviará al usuario.

urlpatterns = [
    path('',views.inicio)
]
#"Cuando un usuario visite la página principal de esta app, ejecuta la función inicio definida en views.py".
