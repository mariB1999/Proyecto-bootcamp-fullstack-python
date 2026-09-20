"""
URL configuration for ejemplo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#Su función es centralizar las rutas de todo el sitio web y redirigir el tráfico hacia el panel de administración o hacia las distintas aplicaciones que conforman tu proyecto.

from django.contrib import admin
from django.urls import path, include
#from django.contrib import admin: Importa el módulo del panel de administración que viene integrado en Django por defecto.
# from django.urls import path, include: Importa la función path (para definir rutas) e include (que permite vincular las rutas creadas en los archivos urls.py de tus aplicaciones individuales).
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('inicio.urls'))

    #'' (cadena vacía): Captura las peticiones a la ruta raíz de la web (por ejemplo, [midominio.com/](https://midominio.com/)).include('inicio.urls'): Le dice a Django: "Para responder a las peticiones que lleguen aquí, ve a buscar las rutas definidas dentro del archivo urls.py de la app llamada inicio".De esta manera, conectas la URL raíz con la vista views.inicio que configuraste previamente en esa aplicación.

]
