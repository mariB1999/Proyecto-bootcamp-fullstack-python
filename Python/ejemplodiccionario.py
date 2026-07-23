producto = {
    "nombre": "celular",
    "marca": "samsung",
    "modelo": "s25"
}

# Muestra los valores al referencialos mediante clave
print(producto["nombre"], producto["marca"], producto["modelo"])

# Recorro el diccionario
for clave in producto:
    print(clave, ':', producto[clave])

# Largo o cantidad de elementos (pares clave|valor)
print(len(producto))

# Devuelve una lista con las claves (llaves) del diccionario
print(producto.keys())

# Devuelve una lista con los valores del diccionario
print(producto.values())

# Devuelve una lista de tuplas con los elementos del diccionario 
print(producto.items())

# Obtiene el valor asociado a la llave indicada; si no existe la llave, no se 'cae' la aplicación
print("Modelo", producto.get("precio"))

# Limpia (o vacía) el diccionario
# producto.clear()

# Agrega un nuevo ítem al diccionario
producto.update({"precio": 300000})
print(producto)

# Actualiza el valor del ítem indicado
producto.update({"nombre": "smartphone"})
print(producto)

# Elimina el ítem correspondiente a la llave indicada
producto.pop("modelo")
print(producto)

# Elimina el último ítem del diccionario
producto.popitem()
print(producto)