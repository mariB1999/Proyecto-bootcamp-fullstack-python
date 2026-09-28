from django.urls import path

from .views import (
    ClienteCreateView,
    ClienteDeleteView,
    ClienteDetailView,
    ClienteListView,
    ClienteUpdateView,
    CuentaCreateView,
    TransaccionCreateView,
)

urlpatterns = [
    path("", ClienteListView.as_view(), name="lista_clientes"),
    path("clientes/crear/", ClienteCreateView.as_view(), name="crear_cliente"),
    path("clientes/<int:pk>/", ClienteDetailView.as_view(), name="detalle_cliente"),
    path("clientes/<int:pk>/editar/", ClienteUpdateView.as_view(), name="editar_cliente"),
    path("clientes/<int:pk>/eliminar/", ClienteDeleteView.as_view(), name="eliminar_cliente"),

    path(
        "clientes/<int:cliente_pk>/cuentas/crear/",
        CuentaCreateView.as_view(),
        name="crear_cuenta",
    ),
    path(
        "cuentas/<int:cuenta_pk>/transacciones/crear/",
        TransaccionCreateView.as_view(),
        name="crear_transaccion",
    ),
]