"""Ejercicio:

Cree un programa en Python que solicite al usuario ingresar una cantidad de repeticiones. Luego, usando un ciclo for con contador, el programa debe mostrar el mensaje Aprendiendo Python esa cantidad de veces.

Además, en cada repetición debe mostrar el número correspondiente, comenzando desde 1."""

repeticion=int(input("Ingrese cantidad de repeticiones: "))
for contador in range(1,repeticion + 1):
    print(f"{contador} Aprendiendo Python")