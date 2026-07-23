# Enunciado del ejercicio
# Un videojuego de aventuras necesita calcular la energía perdida de un personaje cuando recibe daño. Implementa una función en Python llamada calcular_daño.

# La función debe recibir dos parámetros:
# - energia_inicial: la cantidad de energía que tiene el personaje al comenzar.
# - impacto: el porcentaje de daño recibido (por ejemplo, 30 significa que pierde un 30% de su energía).

# La función debe:
# - Validar que la energía inicial sea mayor que cero.
# - Validar que el impacto esté en el rango de 0 a 100.
# - Si los valores no son válidos, devolver "Error: valores inválidos".
# - Calcular la energía perdida.

# Función para calcular daño de un jugador
def calcular_daño(energia_inicial, impacto):
   
    # Validar que la energía inicial sea mayor a 0
    if energia_inicial <= 0:
        return "GAME OVER: El héroe no tiene energía para iniciar la batalla."
   
    # Validar que el impacto sea entre 0 y 100
    if impacto < 0 or impacto > 100:
        return "ATAQUE RECHAZADO: El daño recibido debe estar entre 0 y 100."
   
    # Calcular energía perdida
    energia_perdida = energia_inicial * (impacto / 100)
    return energia_perdida