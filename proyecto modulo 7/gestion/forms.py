from django import forms
from .models import Cliente, Cuenta, Transaccion


class ClienteForm(forms.ModelForm):
    ...

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente

        fields = [
            "nombre",
            "email",
            "telefono",
        ]

        labels = {
            "nombre": "Nombre completo",
            "email": "Correo electrónico",
            "telefono": "Teléfono"
        }

        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "telefono": forms.TextInput(attrs={"class": "form-control"}),
        }

class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta

        fields = [
            "numero",
            "contactos_autorizados",
        ]

        labels = {
            "numero": "Número de cuenta",
            "contactos_autorizados": "Contactos autorizados",
        }

        widgets = {
            "numero": forms.TextInput(attrs={"class": "form-control"}),
            "contactos_autorizados": forms.SelectMultiple(
                attrs={"class": "form-select"}
            ),
        }

class TransaccionForm(forms.ModelForm):
    class Meta:
        model=Transaccion

        fields = [
            "tipo",
            "monto",
            "descripcion",
        ]

        labels={
            "tipo": "Tipo de movimiento",
            "monto":"Monto",
            "descripcion":"Descripcion"
        }

        widgets = {
                    "tipo": forms.Select(attrs={"class": "form-select"}),
                    "monto": forms.NumberInput(
                        attrs={"class": "form-control", "step": "0.01", "min": "0.01"}
                    ),
                    "descripcion": forms.TextInput(attrs={"class": "form-control"}),
                }


    