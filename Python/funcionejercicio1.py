"""Ejercicio: Se desea implementar una función en Python llamada calcular_descuento.

La función debe recibir dos parámetros:

- monto: el valor original de una compra.

- descuento: el porcentaje de descuento a aplicar (por ejemplo, 20 para un 20%).

La función debe devolver el valor correspondiente al descuento, es decir, la cantidad de dinero que se resta al monto original.

Ejemplo esperado:

Si el monto es 1000 y el descuento es 20, la función debe devolver 200."""

def calcular_descuento(x,y):
    descuento=x*y/100
    return descuento

x=float(input("Ingrese el monto original: "))
y=float(input("Ingrese el porcetaje de descuento: "))

valor_final= calcular_descuento(x,y)
print(valor_final)