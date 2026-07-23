import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from validaciones import validar_descripcion, validar_prioridad, validar_tiempo
ESTADOS_VALIDOS = ("PENDIENTE", "COMPLETADA")
def agregar_tarea(lista,categorias):
    descripcion = input("Ingrese descripción: ")
    categoria = input("Ingrese categoría (sistemas,finanzas,legal): ")


    if not validar_descripcion(descripcion):
        print("Error: La descripción no puede estar vacía.")
        return

    prioridad = input("Ingrese prioridad (1-10): ")

    if not validar_prioridad(prioridad):
        print("Error: La prioridad debe ser un entero entre 1 y 10.")
        return

    tiempo = input("Ingrese tiempo estimado (horas): ")

    if not validar_tiempo(tiempo):
        print("Error: El tiempo estimado debe ser mayor que cero.")
        return

    tarea = {
        "descripcion": descripcion,
        "categoria": categoria,
        "prioridad": int(prioridad),
        "tiempo_estimado": float(tiempo),
        "completada": False
    }

    lista.append(tarea)
    categorias.add(categoria)
    print("Tarea registrada correctamente.")


def buscar_tarea(lista, descripcion):
    for i in range(len(lista)):
        if lista[i]["descripcion"] == descripcion:
            return i
    return -1

def eliminar_tarea(lista):
 a_eliminar = input("Ingrese la descripción de la tarea a eliminar ")
 posicion = buscar_tarea(lista, a_eliminar)
 if posicion != -1:
     lista.pop(posicion)
     print("tarea eliminada con exito")
 else:
     print("tarea no encontrada")

def actualizar_estado(lista):
    for tarea in lista:
        if tarea["prioridad"] >= 5:
            tarea["completada"] = ESTADOS_VALIDOS[1] 
        else:
            tarea["completada"] = ESTADOS_VALIDOS[0]  
        

def calcular_tiempo_total(lista, indice=0):
    """
    Suma el tiempo estimado de todas las tareas llamándose a sí misma,
    en vez de usar un bucle for.
    """
    if indice >= len(lista):
        return 0

    tiempo_de_esta_tarea = lista[indice]["tiempo_estimado"]
    resto = calcular_tiempo_total(lista, indice + 1)  

    return tiempo_de_esta_tarea + resto

def mostrar_tareas(lista):
    actualizar_estado(lista)

    if len(lista) == 0:
        print("No existen tareas registradas.")
        return

    print("\n=== LISTA DE TAREAS ===")

    for tarea in lista:
        print(f"Descripción: {tarea['descripcion']}")
        print(f"Categoría: {tarea['categoria']}")
        print(f"Prioridad: {tarea['prioridad']}")
        print(f"Tiempo estimado: {tarea['tiempo_estimado']}")
        print(f"Estado: {tarea['completada']}")


    tiempo_total = calcular_tiempo_total(lista)
    print(f"Tiempo total estimado de todas las tareas: {tiempo_total} horas")
    print("*" * 45)


