import csv
import os

#Tupla con las áreas válidas para asignar a un empleado.
AREAS = ('TI', 'Finanzas', 'RRHH', 'Comercial')

#validadores
def validar_identificador(identificador):
    return identificador.isdigit()

def validar_nombre(nombre):
    return nombre.strip() != ""

def validar_edad(edad):
    try:
        valor = int(edad)
    except (TypeError, ValueError):
        return False
    return 18 <= valor <= 99

#Se define la función de listar_empleados en donde si la lista esta vacía,el programa imprime el mensaje y sale sin continuar y sino recorre con for e imprime los datos de cada empleado.
def listar_empleados(empleados):
    if not empleados:
        print("No hay empleados registrados")
        return

    for empleado in empleados:
        print(f'ID {empleado["id"]} | Nombre {empleado["nombre"]} | Edad {empleado["edad"]} | Área {empleado["area"]} | Tecnología {empleado["tecnologia"]}')

 #se solicitan los datos del nuevo empleado.
def agregar_empleado(empleados, tecnologias):
    identificador_input = input("Ingrese un identificador: ")
    if not validar_identificador(identificador_input):
        print("Error: Debe ingresar solo números enteros.")
        return

    identificador = int(identificador_input)
    nombre = input("Ingrese el nombre: ")
    if not validar_nombre(nombre):
        print("Error: Debe ingresar caracteres válidos.")
        return

    edad_input = input("Ingrese la edad: ")
    if not validar_edad(edad_input):
        print("Error: Debe ingresar un número entero entre 18 y 99.")
        return
    edad = int(edad_input)

    # Se recorre el listado de áreas asignando un número a cada valor para mostrar empezando por 1.
    for i, area in enumerate(AREAS, 1):
        print(f"{i} {area}")

    opcion_input = input("Seleccione un área: ")
    if not opcion_input.isdigit():
        print("Error: Selección inválida de área.")
        return

    opcion = int(opcion_input)
    if opcion < 1 or opcion > len(AREAS):
        print("Error: Selección inválida de área.")
        return

    tecnologia = input("Ingrese la tecnología: ")
    if tecnologia.strip() == "":
        print("Error: Debe ingresar una tecnología válida.")
        return

    # Se crea el diccionario para agregar los datos del empleado nuevo y tambien se registra tecnologias en set.
    empleado = {
        "id": identificador,
        "nombre": nombre,
        "edad": edad,
        "area": AREAS[opcion - 1],
        "tecnologia": tecnologia
    }

    empleados.append(empleado)
    tecnologias.add(tecnologia)

def eliminar_empleado(empleados):
    identificador = int(input("Ingrese el ID del empleado a eliminar: "))
 #Búsqueda es a través de ID del empleado en donde si se encuentra se quita con remove y devuelve la información, si no se informa que no existe
    for empleado in empleados:
        if empleado["id"] == identificador:
            empleados.remove(empleado)
            print("Empleado ha sido eliminado")

            return

    print("No se encontró el empleado")
#Muestra la cantidad total de empleados registrados y un listado de las teconologias sin duplicados gracias a set.
def mostrar_resumen(empleados, tecnologias):
    print(f"Total de empleados: { len(empleados) }")

    print("Listado de tecnologías: ")
    for tecnologia in tecnologias:
        print(tecnologia)
#Se abre o en su defecto se crea el archivo CSV en modo escritura.
def guardar_csv(empleados):
    with open("empleados.csv", "w", newline = "", encoding = "utf-8") as archivo:
        campos = ["id", "nombre", "edad", "area", "tecnologia"]
 #csv.DictWrite lee cada fila y la tranforma en un diccionario entregandola como clave:valor.
        escritor = csv.DictWriter(archivo, delimiter=";", fieldnames=campos)

        escritor.writeheader()
        escritor.writerows(empleados)

    print("Se generó el archivo empleados.csv")
#Primero se verifica si el archivo existe,si no se devuelven las listas vacias.
def cargar_csv():
    empleados = []
    tecnologias = set()

    if not os.path.exists("empleados.csv"):
        return empleados, tecnologias

    with open("empleados.csv", "r", newline = "", encoding = "utf-8") as archivo:
        lector = csv.DictReader(archivo, delimiter=";")

        # Se recorre cada fila convirtiendo id y edad de texto a número
        for empleado in lector:
            empleado["id"] = int(empleado["id"])
            empleado["edad"] = int(empleado["edad"])
            tecnologias.add(empleado["tecnologia"])

            empleados.append(empleado)

        print("Se han cargado los datos")

    return empleados, tecnologias