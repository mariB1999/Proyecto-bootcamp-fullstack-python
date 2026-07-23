import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from validaciones import validar_descripcion, validar_prioridad, validar_tiempo
from tareas import agregar_tarea, buscar_tarea, eliminar_tarea, actualizar_estado, calcular_tiempo_total, mostrar_tareas

def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar tarea")
    print("2. Buscar tarea")
    print("3. Eliminar tarea")
    print("4. Actualizar estado")
    print("5. Mostrar tareas")
    print("6. Salir")
    print("=====================================")


def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            continue
        
        if 1 <= opcion <= 6:
         return opcion
        
        print("Debe ingresar una opción entre 1 y 6.")

def main():
    tareas = []
    categorias = set()
    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
                agregar_tarea(tareas,categorias)

        elif opcion == 2:
                descripcion = input("Ingrese descripción a buscar: ")
        
                posicion = buscar_tarea(tareas, descripcion)
        
                if posicion != -1:
                    print("\nTarea encontrada")
                    print("Posición:", posicion)
                    print(tareas[posicion])
                else:
                    print("La tarea no existe.")

        elif opcion == 3:
                descripcion = input("Ingrese descripción a eliminar: ")
        
                posicion = buscar_tarea(tareas, descripcion)
        
                if posicion != -1:
                    tareas.pop(posicion)
                    print("Tarea eliminada correctamente.")
                else:
                    print(f"La tarea '{descripcion}' no se encuentra registrada.")

        elif opcion == 4:
                actualizar_estado(tareas)
                print("Estados actualizados correctamente.")
        
        elif opcion == 5:
                mostrar_tareas(tareas)
        
        elif opcion == 6:
            print("Gracias por usar el sistema. Vuelva Pronto")
            break


if __name__ == "__main__":
    main()