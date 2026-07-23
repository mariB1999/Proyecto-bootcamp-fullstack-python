horas = int(input("Ingrese las horas: "))
minutos = int(input("Ingrese los minutos: "))
segundos = int(input("Ingrese los segundos: "))

#Calculamos el total convirtiendo todo a segundos
resultado = (horas * 3600)+ (minutos * 60) + segundos

print("El total en segundos es: ", resultado)
