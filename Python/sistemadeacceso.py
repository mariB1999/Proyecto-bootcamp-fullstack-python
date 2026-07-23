""" 
Ejercicio:
Un instituto necesita implementar un pequeño sistema de acceso para su plataforma educativa. El programa debe solicitar al usuario que ingrese su nombre de usuario y su contraseña. Para este ejercicio, se puede considerar que el usuario correcto es alumno y la contraseña correcta es python123.

El sistema debe validar primero si el nombre de usuario ingresado es correcto. Si el usuario existe, entonces debe revisar si la contraseña también es correcta. Si ambos datos son válidos, debe mostrar el mensaje Acceso permitido. Si el usuario es correcto pero la contraseña no coincide, debe mostrar Contraseña incorrecta. En cambio, si el usuario ingresado no corresponde al usuario registrado, debe mostrar Usuario no registrado.
"""
usuario=input("Ingrese su usuario: ")
clave=input("Ingrese su contraseña: ")
if usuario=="alumno":
    if clave=="python123":
        print("Bienvenido al sistema")
    else:
        print("Contraseña incorrecta")
else:
    print("Usuario no registrado")
    
print("¡Gracias por utilizar el sistema! :)")