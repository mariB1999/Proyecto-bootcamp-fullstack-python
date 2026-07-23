"""Ejercicio: Registro de una película

Una plataforma de streaming necesita almacenar la información de una película mediante un diccionario en Python.

El diccionario debe contener inicialmente:

- Título
- Género
- Duración en minutos
- Año de estreno

Luego, el programa debe realizar las siguientes acciones:

1. Mostrar cada dato accediendo mediante su clave.
2. Recorrer el diccionario con un ciclo y mostrar todas las claves junto con sus valores.
3. Mostrar la cantidad de elementos almacenados.
4. Mostrar por separado las claves, los valores y los pares clave-valor.
Intentar obtener la calificación de la película usando get().
5. Agregar la clave "director" con su respectivo valor.
6. Actualizar la duración de la película.
7. Eliminar el año de estreno.
8. Eliminar el último elemento agregado.
9. Mostrar el diccionario después de cada modificación."""

pelicula = {
    "titulo": "Interstellar",
    "genero": "Ciencia ficción",
    "duracion": 169,
    "anio_estreno": 2014
}

print(pelicula)

#1.Mostrar cada dato accediendo mediante su clave
print("titulo:",pelicula["titulo"])
print("genero:",pelicula["genero"])
print("duracion:",pelicula["duracion"])
print("anio_estreno:",pelicula["anio_estreno"])
print("===========================================")
#2.Recorrer el diccionario en un ciclo y mostrar todas las claves junto con sus valores
for clave in pelicula:
    print(f"{clave}: {pelicula[clave]}")

print("==================================")

#Mostar la cantidad de elementos almacenados
print("Cantidad de elementos:",len(pelicula))
print("=====================================")

#Mostraer por separado las claves,los valores y los pares clave-valor
print("claves")
print(pelicula.keys())
print("Valores")
print(pelicula.values())
print("Clave-valor")
print(pelicula.items())

print("calificacion",pelicula.get("calificacion"))
print("================================================")
#Agregar la clave "director" con su respectivo
pelicula.update({"director":"James Cameron"})
print(pelicula)
print("=================================================")
#Actualizar la duracion de la pelicula 
pelicula.update({"duracion":"170"})
print(pelicula) 
print("==================================================")
#Eliminare el ano de estreno
pelicula.pop("anio_estreno")
print(pelicula)
print("===================================================")
#Eliminar el ultimo elemento agregado
pelicula.popitem()
print(pelicula)
