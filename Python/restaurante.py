"""Ejercicio:

Un restaurante necesita un programa para revisar si puede aceptar una reserva. El sistema debe pedir la cantidad de personas, si el cliente tiene reserva previa y si llegará antes de las 22:00 horas. El restaurante solo acepta grupos de hasta 6 personas.

El programa debe verificar primero la cantidad de personas. Si el grupo tiene 6 personas o menos, debe revisar si tiene reserva. Si tiene reserva, debe comprobar si llegará antes de las 22:00 horas. Si todo se cumple, debe mostrar `Reserva aceptada`. Si llega tarde, debe mostrar `Reserva cancelada por atraso`. Si no tiene reserva, debe mostrar `Debe esperar disponibilidad`. Si el grupo tiene más de 6 personas, debe mostrar `No hay mesas disponibles para grupos grandes`."""
personas = int(input("Ingrese la cantidad de personas: "))

if personas <= 6:
    reserva = input("¿Tiene reserva? (si/no): ")
    
    if reserva == "si":
        
        hora = input("¿Llegará antes de las 22:00? (si/no): ")
        if hora == "si":
            print("Reserva aceptada")
        else:
            print("Reserva cancelada por atraso")
    else:
        print("Debe esperar disponibilidad")
else:
    print("No hay mesas disponibles para grupos grandes")

print("¡Gracias por preferir nuestro restaurante!")