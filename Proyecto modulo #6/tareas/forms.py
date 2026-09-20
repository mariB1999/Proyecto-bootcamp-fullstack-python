import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Proyecto, Tarea


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_username(self):
        username = self.cleaned_data.get("username", "").strip()
        if " " in username:
            raise forms.ValidationError("El nombre de usuario no puede contener espacios.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email", "").strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "Ya existe una cuenta registrada con este correo electrónico."
            )
        return email


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ["nombre", "descripcion"]

    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop("usuario", None)
        super().__init__(*args, **kwargs)

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre", "").strip()

        if not nombre:
            raise forms.ValidationError("El nombre del proyecto es obligatorio.")

        if len(nombre) < 3:
            raise forms.ValidationError(
                "El nombre del proyecto debe tener al menos 3 caracteres."
            )

        if nombre.isdigit():
            raise forms.ValidationError(
                "El nombre del proyecto no puede estar compuesto solo por números."
            )

        if self.usuario is not None:
            duplicados = Proyecto.objects.filter(
                usuario=self.usuario,
                nombre__iexact=nombre,
            )
            if self.instance.pk:
                duplicados = duplicados.exclude(pk=self.instance.pk)
            if duplicados.exists():
                raise forms.ValidationError(
                    "Ya tienes un proyecto registrado con este nombre."
                )

        return nombre

    def clean_descripcion(self):
        return self.cleaned_data.get("descripcion", "").strip()


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ["titulo", "descripcion", "estado"]

    def __init__(self, *args, **kwargs):
        self.proyecto = kwargs.pop("proyecto", None)
        super().__init__(*args, **kwargs)

    def clean_titulo(self):
        titulo = self.cleaned_data.get("titulo", "").strip()

        if not titulo:
            raise forms.ValidationError("El título de la tarea es obligatorio.")

        if len(titulo) < 3:
            raise forms.ValidationError(
                "El título de la tarea debe tener al menos 3 caracteres."
            )

        if not re.search(r"[a-zA-ZÁÉÍÓÚÑáéíóúñ]", titulo):
            raise forms.ValidationError(
                "El título de la tarea debe contener al menos una letra."
            )

        proyecto = getattr(self, "proyecto", None) or getattr(self.instance, "proyecto", None)
        if proyecto is not None:
            duplicados = Tarea.objects.filter(proyecto=proyecto, titulo__iexact=titulo)
            if self.instance.pk:
                duplicados = duplicados.exclude(pk=self.instance.pk)
            if duplicados.exists():
                raise forms.ValidationError(
                    "Ya existe una tarea con este título en este proyecto."
                )

        return titulo

    def clean_descripcion(self):
        return self.cleaned_data.get("descripcion", "").strip()

    def clean(self):
        cleaned_data = super().clean()
        estado = cleaned_data.get("estado")
        descripcion = cleaned_data.get("descripcion")

        if estado == "finalizado" and not descripcion:
            raise forms.ValidationError(
                "Debes indicar una descripción antes de marcar la tarea como finalizada."
            )

        return cleaned_data
