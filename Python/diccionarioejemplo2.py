"""Ejercicio: Registro de libros

Una biblioteca necesita almacenar información de varios libros. Cada libro debe representarse mediante un diccionario y todos deben guardarse dentro de una lista.

Cada libro debe tener:

- Título
- Autor
- Año de publicación

Crea una lista con al menos cuatro libros y desarrolla un programa que permita:

1. Mostrar todos los libros usando un ciclo.
2. Mostrar solamente el título de cada libro.
3. Agregar un nuevo libro a la lista.
4. Mostrar la cantidad total de libros registrados.

Guía: Recordar que la lista contendrá varios diccionarios. Para mostrar la información, debe recorrer la lista con un ciclo for y acceder a los valores de cada libro mediante sus claves. Para agregar un nuevo libro, primero cree un diccionario y luego incorpórelo a la lista."""

#Diccionario
libros = [
    {
        "titulo": "El principe cruel",
        "autor": "Holly Black",
        "año": 2018
    },
    {
        "titulo": "La Metamorfosis",
        "autor": "Franz Kafka",
        "año": 1915
    },
    {
        "titulo": "Alas de Onix",
        "autor": "Rebecca Yarros",
        "año": 2025
    },
    {
        "titulo": "Orgullo y Prejuicio",
        "autor": "Jane Austen",
        "año": 1813
    },
    {
        "titulo": "Proyect hail Mary",
        "autor": "Andy Weir",
        "año": 2021
    }
]   

print(" Registro de libros")
# 1. Mostrar todos los libros 
print("=== Libros registrados: ===")
for libro in libros:
    print(libro)

# 2. Mostrar solamente el títuLo de cada libro

print("=== Títulos de los libros: ===")
for libro in libros:
    print(libro["titulo"])

# 3. Agregar un nuevo libro
nuevo_libro = {
    "titulo": "La casa de los espiritus",
    "autor": "Isabel Allende",
    "año": 1982
}
libros.append(nuevo_libro)

print("=== Lista de libros actualizada: ===")
for libro in libros:
    print(libro)

# 4. Mostrar la cantidad de libros registrados
print("Cantidad de libros registrados:", len(libros))

