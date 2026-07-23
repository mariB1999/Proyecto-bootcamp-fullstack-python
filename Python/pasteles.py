#Una pastelería desea automatizar el cálculo de los ingredientes necesarios para preparar varios pasteles iguales. Para elaborar un pastel se requieren las siguientes cantidades de ingredientes

cantidad_pasteles= int(input("Hola, ingresa la cantidad de pasteles a preparar: "))

# Cantidad de ingredientes para un pastel:

huevos = 3
harina = 250
azucar = 200
mantequilla = 150
leche = 200

cantidad_huevos = cantidad_pasteles * huevos
cantidad_harina = cantidad_pasteles * harina
cantidad_azucar = cantidad_pasteles * azucar
cantidad_mantequilla = cantidad_pasteles * mantequilla
cantidad_leche = cantidad_pasteles * leche 

print(f"\nReceta para {cantidad_pasteles} pasteles: \n{cantidad_huevos} huevos\n{cantidad_harina} gr de harina\n{cantidad_azucar} gr de azúcar\n{cantidad_mantequilla} gr de mantequilla\n{cantidad_leche} ml de leche\n")