from funciones import listar_empleados, agregar_empleado, eliminar_empleado, mostrar_resumen, guardar_csv, cargar_csv
                        

def mostrar_menu():
    print("\nSistema de Gestión de Datos de Empleados")
    print("1. Agregar empleado")
    print("2. Listar empleados")
    print("3. Eliminar empleado")
    print("4. Mostrar resumen")
    print("5. Exportar datos")
    print("6. Salir")

def main():

    empleados, tecnologias = cargar_csv()
#Se utiliza While True para que cada vez que se ejecute la funcion el  menú aparezca y asi el usuario pueda ingresar una opción  repetiendose en bucle hasta que ingrese la opción de salir terminando con break.
    while True:
        mostrar_menu()

        opcion = input("Ingrese una opción del menú [1-6]: ")

        if opcion == "1":
            print("Agregar empleado")
            agregar_empleado(empleados, tecnologias)
        elif opcion == "2":
            print("Listar empleados")
            
            listar_empleados(empleados)
        elif opcion == "3":
            print("Eliminar empleado")

            eliminar_empleado(empleados)
        elif opcion == "4":
            print("Mostrar resumen")

            mostrar_resumen(empleados, tecnologias)
        elif opcion == "5":
            print("Exportar datos")

            guardar_csv(empleados)
        elif opcion == "6":
            break
        else:
            print("Opción no válida")

    print("Gracias por usar el Sistema de Gestión de Datos de Empleados")

main()