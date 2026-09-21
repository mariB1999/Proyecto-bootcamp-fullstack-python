# 📋 Gestor de Tareas

Aplicación web desarrollada en **Django** para administrar proyectos personales y las tareas asociadas a cada uno. Cada usuario gestiona sus propios proyectos de forma privada: crea proyectos, agrega tareas, actualiza su estado (Pendiente → En proceso → Finalizado) y elimina lo que ya no necesita.

> Proyecto desarrollado como parte del Módulo 6.

---

## ✨ Funcionalidades principales

- **Autenticación de usuarios**: registro, inicio de sesión y cierre de sesión.
- **Gestión de proyectos (CRUD)**: crear, listar, ver el detalle, editar y eliminar proyectos.
- **Gestión de tareas (CRUD)**: crear, editar y eliminar tareas dentro de un proyecto, con 3 estados posibles: `Pendiente`, `En proceso`, `Finalizado`.
- **Privacidad de datos**: cada usuario solo puede ver y modificar sus propios proyectos y tareas (aislamiento por usuario a nivel de consultas).
- **Validaciones personalizadas** en los formularios de registro, proyecto y tarea.
- **Mensajes de confirmación** (Django messages) al crear, actualizar o eliminar un registro.
- **Panel de administración** de Django para gestionar proyectos y tareas desde `/admin/`.

---

## 📸 Capturas de pantalla

| Pantalla | Descripción |
|---|---|
|<img width="2280" height="1301" alt="Captura de pantalla 2026-09-21 180837" src="https://github.com/user-attachments/assets/ddaa1920-6d46-478e-be81-332e2b539f72" />
  | Formulario de registro de usuario |
| <img width="2311" height="672" alt="Captura de pantalla 2026-09-21 181115" src="https://github.com/user-attachments/assets/8047e914-babc-454b-9164-f63110ccc785" />
 | Proyecto creado correctamente |
| <img width="2299" height="950" alt="Captura de pantalla 2026-09-21 181247" src="https://github.com/user-attachments/assets/b7742ecb-160f-4333-9728-4db6d72c7fbc" />
 | Validación personalizada: no se puede finalizar una tarea sin descripción |
|<img width="2294" height="772" alt="Captura de pantalla 2026-09-21 181414" src="https://github.com/user-attachments/assets/10e568a2-557a-4903-98a7-bf5617b1845c" />
 | Detalle de proyecto con tarea finalizada |
| | Formulario de inicio de sesión |
---

## 🛠 Tecnologías 

- [Python 3.12+](https://www.python.org/)
- [Django 6.1](https://www.djangoproject.com/)
- SQLite (base de datos por defecto, incluida con Django)
- HTML5 + CSS (plantillas de Django)
---

## 📂 Estructura del proyecto

```
Proyecto modulo #6/
├── gestor_tareas/          # Configuración del proyecto Django (settings, urls)
├── tareas/                 # App principal
│   ├── models.py           # Modelos Proyecto y Tarea
│   ├── forms.py            # Formularios con validaciones personalizadas
│   ├── views.py            # Vistas basadas en clases (CRUD)
│   ├── urls.py              # Rutas de la app
│   ├── admin.py            # Configuración del panel de administración
│   ├── tests.py            # Suite de pruebas automatizadas
│   └── templates/          # Plantillas HTML
├── manage.py
├── requirements.txt         # Dependencias para ejecutar la aplicación
```

---
## 🚀 Instalación

### Requisitos previos

- Python 3.12 o superior instalado.
- `pip` disponible en la línea de comandos.

### Pasos

1. **Clonar el repositorio** (o descomprimir el proyecto):

   ```bash
   git clone https://github.com/<tu-usuario>/<tu-repositorio>.git
   cd "Proyecto modulo #6"
   ```

2. **Crear y activar un entorno virtual**:

   - En Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - En macOS / Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instalar las dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Aplicar las migraciones de la base de datos**:

   ```bash
   python manage.py migrate
   ```

5. **(Opcional) Crear un superusuario** para acceder al panel de administración:

   ```bash
   python manage.py createsuperuser
   ```

6. **Levantar el servidor de desarrollo**:

   ```bash
   python manage.py runserver
   ```

7. Abrir en el navegador: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📖 Uso

1. **Registrarse**: ingresa a `/registro/` y crea una cuenta con usuario, correo y contraseña. Al registrarte, quedas automáticamente autenticado.
2. **Iniciar sesión**: si ya tienes cuenta, ingresa desde `/accounts/login/`.
3. **Crear un proyecto**: desde la pantalla principal, pulsa "Nuevo proyecto", ingresa un nombre (mínimo 3 caracteres, no numérico, no duplicado) y una descripción opcional.
4. **Agregar tareas**: dentro del detalle de un proyecto, pulsa "Nueva tarea" para agregar tareas con título, descripción y estado.
5. **Actualizar el estado de una tarea**: edita la tarea y cambia su estado. Si la marcas como "Finalizado", el sistema exigirá que hayas ingresado una descripción.
6. **Editar o eliminar**: tanto proyectos como tareas se pueden editar o eliminar desde sus respectivas pantallas, con una confirmación antes de eliminar.
7. **Cerrar sesión**: usa el botón "Salir" en la barra de navegación.
8. **Panel de administración**: accede a `/admin/` con un superusuario para administrar todos los proyectos y tareas del sistema.

---

## ✅ Validaciones personalizadas

Todas las validaciones están implementadas en `tareas/forms.py` mediante métodos `clean_<campo>()` y `clean()`, siguiendo el mecanismo estándar de validación de formularios de Django.

### Registro de usuario (`RegistroUsuarioForm`)
- El nombre de usuario no puede contener espacios en blanco.
- El correo electrónico no puede estar ya registrado por otro usuario.

### Proyecto (`ProyectoForm`)
- El nombre no puede estar vacío ni compuesto solo por espacios.
- El nombre debe tener al menos 3 caracteres.
- El nombre no puede ser exclusivamente numérico (ej: `"12345"` es inválido).
- El nombre no puede repetirse entre los proyectos del mismo usuario (comparación insensible a mayúsculas/minúsculas y espacios).

### Tarea (`TareaForm`)
- El título no puede estar vacío ni ser menor a 3 caracteres.
- El título debe contener al menos una letra (no puede ser solo números o símbolos).
- El título no puede repetirse dentro del mismo proyecto.
- **Regla de negocio**: una tarea no puede marcarse como `Finalizado` si no tiene una descripción (validación cruzada entre dos campos, implementada en el método `clean()` del formulario).

Todos los errores de validación se muestran automáticamente en el formulario gracias al renderizado estándar de Django (`{{ form.as_p }}`), sin necesidad de JavaScript adicional.

---

## 🧪 Pruebas

El proyecto incluye pruebas automatizadas en `tareas/tests.py`, organizada en 6 clases:

| Clase | Qué cubre |
|---|---|
| `ProyectoFormTests` | Validaciones del formulario de proyecto (nombre vacío, corto, numérico, duplicado) |
| `TareaFormTests` | Validaciones del formulario de tarea (título corto, duplicado, regla "finalizado sin descripción") |
| `RegistroUsuarioFormTests` | Validaciones del formulario de registro (email duplicado, username con espacios) |
| `VistasAccesoTests` | Verifica que las vistas exigen inicio de sesión |
| `VistasProyectoTests` | CRUD de proyectos y aislamiento de datos entre usuarios distintos |
| `VistasTareaTests` | CRUD de tareas, incluyendo los casos de validación a nivel de vista |

### Ejecutar las pruebas
python manage.py test tareas -v 2
<img width="1110" height="587" alt="Captura de pantalla 2026-09-20 201244" src="https://github.com/user-attachments/assets/142f33a5-6d0e-4c00-915b-3c69c8e7fb6c" />
<img width="1113" height="625" alt="Captura de pantalla 2026-09-20 201221" src="https://github.com/user-attachments/assets/76e70627-3467-4f04-a42f-b230c3464e5f" />
<img width="1102" height="623" alt="Captura de pantalla 2026-09-20 201158" src="https://github.com/user-attachments/assets/e25f8d20-4891-4be4-a9fb-64cd56dac222" />


 
