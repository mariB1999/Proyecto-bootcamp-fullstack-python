# Billetera digital

Aplicación web desarrollada en **Django** para la gestión de clientes, sus cuentas bancarias y las transacciones (ingresos/egresos) asociadas a cada cuenta.

## Funcionalidades

- **Autenticación**: acceso mediante login/logout, restringido a usuarios del tipo *staff*.
- **Gestión de clientes**: listar (con buscador por nombre o correo), crear, editar y eliminar.
- **Gestión de cuentas**: cada cliente puede tener **una cuenta** (relación 1 a 1), con número de cuenta, saldo calculado automáticamente y contactos autorizados (otros clientes).
- **Gestión de transacciones**: registro de ingresos y egresos sobre una cuenta, con validación de saldo disponible para evitar egresos que dejen el saldo en negativo.
- **Vista de detalle de cliente**: muestra en una sola pantalla los datos del cliente, el estado de su cuenta (saldo, número, fecha de creación, contactos autorizados) y el historial completo de transacciones.
- **Interfaz** basada en Bootstrap 5 con una paleta de colores turquesa.

## Tecnologías

- Python 3.14
- Django 6.1.1
- SQLite (base de datos por defecto)
- Bootstrap 5 (CDN)

## Estructura del proyecto

```
proyecto7/
├── config/                 # Configuración del proyecto (settings, urls, wsgi/asgi)
├── gestion/                 # App principal
│   ├── models.py            # Modelos: Cliente, Cuenta, Transaccion
│   ├── forms.py              # Formularios: ClienteForm, CuentaForm, TransaccionForm
│   ├── views.py               # Vistas basadas en clases (CRUD)
│   ├── urls.py                 # Rutas de la app
│   ├── admin.py                 # Registro de modelos en el panel de administración
│   ├── static/css/styles.css      # Hoja de estilos con la paleta de colores
│   └── templates/                  # Plantillas HTML
├── manage.py
└── requirements.txt
```

## Modelo de datos

- **Cliente**: nombre, email (único), teléfono, fecha de registro.
- **Cuenta**: pertenece a un único `Cliente` (1 a 1), tiene un número único, contactos autorizados (M2M a `Cliente`) y un saldo calculado a partir de sus transacciones.
- **Transaccion**: pertenece a una `Cuenta`, tiene tipo (`ingreso`/`egreso`), monto, descripción y fecha.

## Instalación y ejecución local

1. Clonar el repositorio:
   ```bash
   git clone <url-del-repositorio>
   cd alke-wallet
   ```

2. Crear y activar un entorno virtual:
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # Linux / macOS
   source venv/bin/activate
   ```

3. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Aplicar las migraciones:
   ```bash
   python manage.py migrate
   ```

5. Crear un superusuario (necesario porque el acceso está restringido a usuarios `staff`):
   ```bash
   python manage.py createsuperuser
   ```

6. Levantar el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

7. Abrir el navegador en `http://127.0.0.1:8000/` e iniciar sesión con el superusuario creado.

## Flujo de uso

1. Iniciar sesión.
2. Crear un cliente desde el botón **"Crear cliente"**.
3. Entrar al detalle del cliente y crear su cuenta con **"Crear cuenta"**.
4. Registrar movimientos (ingresos/egresos) con **"Registrar movimiento"**; el sistema no permite un egreso mayor al saldo disponible.
5. Revisar en la misma vista de detalle el saldo actualizado y el historial de transacciones.
