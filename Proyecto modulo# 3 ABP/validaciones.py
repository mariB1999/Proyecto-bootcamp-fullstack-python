def validar_descripcion (descripcion):
    return descripcion.strip() != ""


def validar_prioridad (prioridad):
    return prioridad.isdigit() and 1 <= int(prioridad) <= 10


def validar_tiempo (tiempo):
    try:
        return float(tiempo) > 0
    except ValueError:
        return False