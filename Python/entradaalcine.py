#Ejercicio: Realice un programa que calcule el valor de una entrada al cine. Debe leer la edad de una persona y a partir de ese dato, calcule el valor de la entrada:
#Si es menor de edad, el valor es $1.000.
#Si es mayor, el valor es $5.000

edad= int(input("Ingrese su edad: "))

if edad >= 18:
    print("El valor de la entrada es $1.000")

else:
    print("El valor de la entrada es $5.000")