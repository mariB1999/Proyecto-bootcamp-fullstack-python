from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .forms import ProyectoForm, RegistroUsuarioForm, TareaForm
from .models import Proyecto, Tarea


class ProyectoFormTests(TestCase):
    """Validaciones personalizadas de ProyectoForm."""

    def setUp(self):
        self.usuario = User.objects.create_user(username="ana", password="claveSegura123")

    def test_nombre_valido_es_aceptado(self):
        form = ProyectoForm(data={"nombre": "Proyecto Web", "descripcion": ""}, usuario=self.usuario)
        self.assertTrue(form.is_valid(), form.errors)

    def test_nombre_vacio_es_rechazado(self):
        form = ProyectoForm(data={"nombre": "   ", "descripcion": ""}, usuario=self.usuario)
        self.assertFalse(form.is_valid())
        self.assertIn("nombre", form.errors)

    def test_nombre_muy_corto_es_rechazado(self):
        form = ProyectoForm(data={"nombre": "ab", "descripcion": ""}, usuario=self.usuario)
        self.assertFalse(form.is_valid())
        self.assertIn("nombre", form.errors)

    def test_nombre_solo_numeros_es_rechazado(self):
        form = ProyectoForm(data={"nombre": "12345", "descripcion": ""}, usuario=self.usuario)
        self.assertFalse(form.is_valid())
        self.assertIn("nombre", form.errors)

    def test_nombre_duplicado_para_mismo_usuario_es_rechazado(self):
        Proyecto.objects.create(usuario=self.usuario, nombre="Proyecto Web")
        form = ProyectoForm(
            data={"nombre": "proyecto web", "descripcion": ""},  # distinto casing / espacios
            usuario=self.usuario,
        )
        self.assertFalse(form.is_valid())
        self.assertIn("nombre", form.errors)

    def test_nombre_duplicado_para_otro_usuario_es_permitido(self):
        otro_usuario = User.objects.create_user(username="beto", password="claveSegura123")
        Proyecto.objects.create(usuario=otro_usuario, nombre="Proyecto Web")

        form = ProyectoForm(data={"nombre": "Proyecto Web", "descripcion": ""}, usuario=self.usuario)
        self.assertTrue(form.is_valid(), form.errors)

    def test_editar_mismo_proyecto_no_se_marca_como_duplicado(self):
        proyecto = Proyecto.objects.create(usuario=self.usuario, nombre="Proyecto Web")
        form = ProyectoForm(
            data={"nombre": "Proyecto Web", "descripcion": "actualizado"},
            usuario=self.usuario,
            instance=proyecto,
        )
        self.assertTrue(form.is_valid(), form.errors)


class TareaFormTests(TestCase):
    """Validaciones personalizadas de TareaForm."""

    def setUp(self):
        self.usuario = User.objects.create_user(username="ana", password="claveSegura123")
        self.proyecto = Proyecto.objects.create(usuario=self.usuario, nombre="Proyecto Web")

    def test_titulo_valido_es_aceptado(self):
        form = TareaForm(
            data={"titulo": "Diseñar login", "descripcion": "", "estado": "pendiente"},
            proyecto=self.proyecto,
        )
        self.assertTrue(form.is_valid(), form.errors)

    def test_titulo_muy_corto_es_rechazado(self):
        form = TareaForm(
            data={"titulo": "ab", "descripcion": "", "estado": "pendiente"},
            proyecto=self.proyecto,
        )
        self.assertFalse(form.is_valid())
        self.assertIn("titulo", form.errors)

    def test_titulo_sin_letras_es_rechazado(self):
        form = TareaForm(
            data={"titulo": "12345", "descripcion": "", "estado": "pendiente"},
            proyecto=self.proyecto,
        )
        self.assertFalse(form.is_valid())
        self.assertIn("titulo", form.errors)

    def test_titulo_duplicado_en_mismo_proyecto_es_rechazado(self):
        Tarea.objects.create(proyecto=self.proyecto, titulo="Diseñar login", estado="pendiente")
        form = TareaForm(
            data={"titulo": "diseñar login", "descripcion": "", "estado": "pendiente"},
            proyecto=self.proyecto,
        )
        self.assertFalse(form.is_valid())
        self.assertIn("titulo", form.errors)

    def test_titulo_duplicado_en_otro_proyecto_es_permitido(self):
        otro_proyecto = Proyecto.objects.create(usuario=self.usuario, nombre="Proyecto Móvil")
        Tarea.objects.create(proyecto=otro_proyecto, titulo="Diseñar login", estado="pendiente")

        form = TareaForm(
            data={"titulo": "Diseñar login", "descripcion": "", "estado": "pendiente"},
            proyecto=self.proyecto,
        )
        self.assertTrue(form.is_valid(), form.errors)

    def test_finalizado_sin_descripcion_es_rechazado(self):
        form = TareaForm(
            data={"titulo": "Cerrar sprint", "descripcion": "", "estado": "finalizado"},
            proyecto=self.proyecto,
        )
        self.assertFalse(form.is_valid())
        self.assertIn("__all__", form.errors)

    def test_finalizado_con_descripcion_es_aceptado(self):
        form = TareaForm(
            data={
                "titulo": "Cerrar sprint",
                "descripcion": "Se completaron todas las tareas del sprint.",
                "estado": "finalizado",
            },
            proyecto=self.proyecto,
        )
        self.assertTrue(form.is_valid(), form.errors)


class RegistroUsuarioFormTests(TestCase):
    """Validaciones personalizadas de RegistroUsuarioForm."""

    def test_registro_valido_es_aceptado(self):
        form = RegistroUsuarioForm(data={
            "username": "carla",
            "email": "carla@example.com",
            "password1": "ClaveSegura123",
            "password2": "ClaveSegura123",
        })
        self.assertTrue(form.is_valid(), form.errors)

    def test_email_duplicado_es_rechazado(self):
        User.objects.create_user(username="existente", email="carla@example.com", password="ClaveSegura123")

        form = RegistroUsuarioForm(data={
            "username": "carla2",
            "email": "carla@example.com",
            "password1": "ClaveSegura123",
            "password2": "ClaveSegura123",
        })
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)

    def test_username_con_espacios_es_rechazado(self):
        form = RegistroUsuarioForm(data={
            "username": "carla perez",
            "email": "carla2@example.com",
            "password1": "ClaveSegura123",
            "password2": "ClaveSegura123",
        })
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)


class VistasAccesoTests(TestCase):
    """Control de acceso: todas las vistas de proyectos/tareas exigen login."""

    def setUp(self):
        self.usuario = User.objects.create_user(username="ana", password="claveSegura123")
        self.proyecto = Proyecto.objects.create(usuario=self.usuario, nombre="Proyecto Web")

    def test_lista_de_proyectos_redirige_si_no_hay_login(self):
        respuesta = self.client.get(reverse("proyecto_list"))
        self.assertEqual(respuesta.status_code, 302)
        self.assertIn(reverse("login"), respuesta.url)

    def test_lista_de_proyectos_accesible_con_login(self):
        self.client.login(username="ana", password="claveSegura123")
        respuesta = self.client.get(reverse("proyecto_list"))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, "Proyecto Web")


class VistasProyectoTests(TestCase):
    """Flujo CRUD de proyectos y aislamiento de datos entre usuarios."""

    def setUp(self):
        self.usuario = User.objects.create_user(username="ana", password="claveSegura123")
        self.otro_usuario = User.objects.create_user(username="beto", password="claveSegura123")
        self.proyecto_ana = Proyecto.objects.create(usuario=self.usuario, nombre="Proyecto de Ana")
        self.proyecto_beto = Proyecto.objects.create(usuario=self.otro_usuario, nombre="Proyecto de Beto")
        self.client.login(username="ana", password="claveSegura123")

    def test_usuario_no_ve_proyectos_de_otros(self):
        respuesta = self.client.get(reverse("proyecto_list"))
        self.assertContains(respuesta, "Proyecto de Ana")
        self.assertNotContains(respuesta, "Proyecto de Beto")

    def test_usuario_no_puede_ver_detalle_de_proyecto_ajeno(self):
        respuesta = self.client.get(reverse("proyecto_detail", kwargs={"pk": self.proyecto_beto.pk}))
        self.assertEqual(respuesta.status_code, 404)

    def test_crear_proyecto_con_datos_validos(self):
        respuesta = self.client.post(
            reverse("proyecto_create"),
            data={"nombre": "Proyecto Nuevo", "descripcion": "Descripción de prueba"},
        )
        self.assertEqual(respuesta.status_code, 302)
        self.assertTrue(Proyecto.objects.filter(usuario=self.usuario, nombre="Proyecto Nuevo").exists())

    def test_crear_proyecto_con_nombre_invalido_no_guarda(self):
        respuesta = self.client.post(
            reverse("proyecto_create"),
            data={"nombre": "ab", "descripcion": ""},
        )
        self.assertEqual(respuesta.status_code, 200)  # vuelve a mostrar el formulario con errores
        self.assertFalse(Proyecto.objects.filter(nombre="ab").exists())

    def test_eliminar_proyecto(self):
        respuesta = self.client.post(reverse("proyecto_delete", kwargs={"pk": self.proyecto_ana.pk}))
        self.assertEqual(respuesta.status_code, 302)
        self.assertFalse(Proyecto.objects.filter(pk=self.proyecto_ana.pk).exists())


class VistasTareaTests(TestCase):
    """Flujo CRUD de tareas."""

    def setUp(self):
        self.usuario = User.objects.create_user(username="ana", password="claveSegura123")
        self.proyecto = Proyecto.objects.create(usuario=self.usuario, nombre="Proyecto Web")
        self.client.login(username="ana", password="claveSegura123")

    def test_crear_tarea_con_datos_validos(self):
        respuesta = self.client.post(
            reverse("tarea_create", kwargs={"proyecto_id": self.proyecto.pk}),
            data={"titulo": "Diseñar interfaz", "descripcion": "", "estado": "pendiente"},
        )
        self.assertEqual(respuesta.status_code, 302)
        self.assertTrue(Tarea.objects.filter(proyecto=self.proyecto, titulo="Diseñar interfaz").exists())

    def test_crear_tarea_finalizada_sin_descripcion_no_guarda(self):
        respuesta = self.client.post(
            reverse("tarea_create", kwargs={"proyecto_id": self.proyecto.pk}),
            data={"titulo": "Cerrar sprint", "descripcion": "", "estado": "finalizado"},
        )
        self.assertEqual(respuesta.status_code, 200)
        self.assertFalse(Tarea.objects.filter(titulo="Cerrar sprint").exists())

    def test_actualizar_estado_de_tarea(self):
        tarea = Tarea.objects.create(proyecto=self.proyecto, titulo="Diseñar interfaz", estado="pendiente")
        respuesta = self.client.post(
            reverse("tarea_update", kwargs={"pk": tarea.pk}),
            data={"titulo": "Diseñar interfaz", "descripcion": "Wireframes listos", "estado": "en_proceso"},
        )
        self.assertEqual(respuesta.status_code, 302)
        tarea.refresh_from_db()
        self.assertEqual(tarea.estado, "en_proceso")

    def test_eliminar_tarea(self):
        tarea = Tarea.objects.create(proyecto=self.proyecto, titulo="Diseñar interfaz", estado="pendiente")
        respuesta = self.client.post(reverse("tarea_delete", kwargs={"pk": tarea.pk}))
        self.assertEqual(respuesta.status_code, 302)
        self.assertFalse(Tarea.objects.filter(pk=tarea.pk).exists())