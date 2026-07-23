ventas = int(input("ingrese monto de ventas:"))

if ventas < 0:
    print("El valor debe ser mayor a 0")
elif ventas < 400000:
    print("No le corresponde recibir bono")
elif ventas <= 1000000:
    print("Recibe un bono de $50.000")
else:
    print("Recibe un bono de $75.000")