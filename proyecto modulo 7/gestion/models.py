from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.db.models import Sum

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

class Cuenta(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.PROTECT, related_name="cuenta")
    numero = models.CharField(max_length=20, unique=True)
    contactos_autorizados = models.ManyToManyField(Cliente, blank=True, related_name="cuentas_autorizadas")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente.nombre} | {self.numero}"

    @property
    def saldo(self):
        ingresos = self.transacciones.filter(tipo="ingreso").aggregate(total=Sum("monto"))["total"] or Decimal("0.00")

        egresos = self.transacciones.filter(tipo="egreso").aggregate(total=Sum("monto"))["total"] or Decimal("0.00")

        return ingresos - egresos

class Transaccion(models.Model):
    TIPOS = [
        ("ingreso", "Ingreso"),
        ("egreso", "Egreso"),
    ]

    cuenta = models.ForeignKey(Cuenta, on_delete=models.PROTECT, related_name="transacciones")
    tipo = models.CharField(max_length=10, choices=TIPOS)
    monto = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(Decimal("0.01"))],)
    descripcion = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-fecha", "-pk"]

    def __str__(self):
        return f"{self.get_tipo_display()} | {self.monto}"

