from django.contrib import messages
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.db.models import Count, Q
from django.db.models.deletion import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import ClienteForm
from .models import Cliente, Cuenta
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

from .forms import ClienteForm, CuentaForm, TransaccionForm


class AccesoPersonalMixin(
    LoginRequiredMixin,
    UserPassesTestMixin,
):
    def test_func(self):
        return self.request.user.is_staff


class ClienteListView(AccesoPersonalMixin, ListView):
    model = Cliente
    template_name = "gestion/lista_clientes.html"
    context_object_name = "clientes"

    def get_queryset(self):
        clientes = Cliente.objects.annotate(
            total_movimientos=Count("cuenta__transacciones")
        ).order_by("nombre")

        buscar = self.request.GET.get("buscar", "").strip()

        if buscar:
            clientes = clientes.filter(
                Q(nombre__icontains=buscar)
                | Q(email__icontains=buscar)
            )

        return clientes

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)

        contexto["buscar"] = self.request.GET.get(
            "buscar", ""
        )

        return contexto


class ClienteDetailView(AccesoPersonalMixin, DetailView):
    model = Cliente
    template_name = "gestion/detalle_cliente.html"
    context_object_name = "cliente"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)

        cuenta = Cuenta.objects.filter(
            cliente=self.object
        ).first()

        contexto["cuenta"] = cuenta

        contexto["movimientos"] = (
            cuenta.transacciones.all()
            if cuenta
            else []
        )

        return contexto


class ClienteCreateView(AccesoPersonalMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "gestion/form_cliente.html"
    success_url = reverse_lazy("lista_clientes")

    extra_context = {
        "titulo": "Crear cliente",
    }

    def form_valid(self, form):
        respuesta = super().form_valid(form)

        messages.success(
            self.request,
            "Cliente creado correctamente.",
        )

        return respuesta


class ClienteUpdateView(AccesoPersonalMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "gestion/form_cliente.html"
    success_url = reverse_lazy("lista_clientes")

    extra_context = {
        "titulo": "Actualizar cliente",
    }

    def form_valid(self, form):
        respuesta = super().form_valid(form)

        messages.success(
            self.request,
            "Cliente actualizado correctamente.",
        )

        return respuesta


class ClienteDeleteView(AccesoPersonalMixin, DeleteView):
    model = Cliente
    template_name = "gestion/confirmar_eliminar.html"
    context_object_name = "cliente"
    success_url = reverse_lazy("lista_clientes")

    def form_valid(self, form):
        try:
            respuesta = super().form_valid(form)
        except ProtectedError:
            messages.error(
                self.request,
                "No se puede eliminar un cliente "
                "que tiene una cuenta asociada.",
            )

            return redirect(
                "detalle_cliente",
                pk=self.object.pk,
            )

        messages.success(
            self.request,
            "Cliente eliminado correctamente.",
        )

        return respuesta

class CuentaCreateView(AccesoPersonalMixin, CreateView):
    model = Cuenta
    form_class = CuentaForm
    template_name = "gestion/form_cuenta.html"

    def dispatch(self, request, *args, **kwargs):
        self.cliente = get_object_or_404(Cliente, pk=kwargs["cliente_pk"])

        if hasattr(self.cliente, "cuenta"):
            messages.info(
                request,
                "Este cliente ya tiene una cuenta asociada.",
            )
            return redirect("detalle_cliente", pk=self.cliente.pk)

        return super().dispatch(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        # Un cliente no puede autorizarse a sí mismo como contacto.
        form.fields["contactos_autorizados"].queryset = Cliente.objects.exclude(
            pk=self.cliente.pk
        )
        form.fields["contactos_autorizados"].required = False

        return form

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["cliente"] = self.cliente
        contexto["titulo"] = f"Crear cuenta para {self.cliente.nombre}"
        return contexto

    def form_valid(self, form):
        form.instance.cliente = self.cliente
        respuesta = super().form_valid(form)

        messages.success(
            self.request,
            "Cuenta creada correctamente.",
        )

        return respuesta

    def get_success_url(self):
        return reverse("detalle_cliente", kwargs={"pk": self.cliente.pk})


class TransaccionCreateView(AccesoPersonalMixin, CreateView):
    """Permite registrar un ingreso o un egreso sobre la cuenta de un
    cliente. Los egresos se validan contra el saldo disponible."""

    form_class = TransaccionForm
    template_name = "gestion/form_transaccion.html"

    def dispatch(self, request, *args, **kwargs):
        self.cuenta = get_object_or_404(Cuenta, pk=kwargs["cuenta_pk"])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["cuenta"] = self.cuenta
        contexto["titulo"] = f"Registrar movimiento | Cuenta {self.cuenta.numero}"
        return contexto

    def form_valid(self, form):
        form.instance.cuenta = self.cuenta

        if form.instance.tipo == "egreso" and form.instance.monto > self.cuenta.saldo:
            form.add_error(
                "monto",
                "Saldo insuficiente para realizar este egreso.",
            )
            return self.form_invalid(form)

        respuesta = super().form_valid(form)

        messages.success(
            self.request,
            "Transacción registrada correctamente.",
        )

        return respuesta

    def get_success_url(self):
        return reverse("detalle_cliente", kwargs={"pk": self.cuenta.cliente.pk})
