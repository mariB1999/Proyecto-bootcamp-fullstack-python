ventas= int(input("Ingrese el monto de ventas realizada: "))

if ventas > 1000000:
    print("No tienes bonos.")
elif 400000 <= ventas <= 1000000: #entre 400 a 1 millon
    print(f"Bono de  50.000: ${ventas+50000} ")    
else: #mas de 1 millon
    print(f"Bono de 75.000: ${ventas+75000}")