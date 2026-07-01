class OverlapError(Exception):
    pass
class InvalidDateError(Exception):
    pass
class InvalidTimeError(Exception):
    pass
class InvalidDurationError(Exception):
    pass
class NotFoundError(Exception):
    pass

def conversion_a_minutos(hora_str):
    horas, minutos = hora_str.split(":")
    return int(horas) * 60 + int(minutos)

def validar_duracion(hora_inicio, hora_fin):
    duracion = conversion_a_minutos(hora_fin) - conversion_a_minutos(hora_inicio)
    if duracion <= 0:
        raise InvalidDurationError("La hora de fin debe ser posterior a la hora de inicio.")
    if duracion > 240:
        raise InvalidDurationError("La duración de la reserva no puede exceder las 4 horas.")
    if duracion < 30:
        raise InvalidDurationError("La duración de la reserva no puede ser menor a 30 minutos.")
    return duracion

def vaalidar_existencia(usuario_id,sala_id,conn):
    
    usuario=conn.execute(
        "SELECT * FROM usuarios WHERE id = ?", (usuario_id,)
    ).fetchone()
    if usuario is None:
        raise NotFoundError(f"Usuario con ID {usuario_id} no encontrado.")
    