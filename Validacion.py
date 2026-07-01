from datetime import datetime

class OverlapError(Exception):
    pass
class InvalidDateError(Exception):
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

def validar_existencia(usuario_id,sala_id,conn):
    
    usuario=conn.execute(
        "SELECT * FROM usuarios WHERE id = ?", (usuario_id,)
    ).fetchone()
    if usuario is None:
        raise NotFoundError(f"Usuario con ID {usuario_id} no encontrado.")
    
    sala=conn.execute(
        "SELECT * FROM salas WHERE id = ?", (sala_id,)
    ).fetchone()
    if sala is None:
        raise NotFoundError(f"Sala con ID {sala_id} no encontrada.")

def validar_superposicion(sala_id, fecha, hora_inicio, hora_fin, conn):
    reservas_existentes = conn.execute(
        "SELECT hora_inicio, hora_fin FROM reservas WHERE sala_id = ? AND fecha = ? AND status = 'Confirmada'",
        (sala_id, fecha)
    ).fetchall()

    for hora_inicio_existente, hora_fin_existente in reservas_existentes:
        if not (hora_fin <= hora_inicio_existente or hora_inicio >= hora_fin_existente):
            raise OverlapError("La reserva se superpone con otra reserva existente.")
        
def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
    except ValueError:
        raise InvalidDateError(f"Formato de fecha inválido, debe ser YYYY-MM-DD.")
    
def validar_reserva(solicitud, conn):
    usuario_id = solicitud["usuario_id"]
    sala_id = solicitud["sala_id"]
    fecha = solicitud["fecha"]
    hora_inicio = solicitud["hora_inicio"]
    hora_fin = solicitud["hora_fin"]

    validar_existencia(usuario_id, sala_id, conn)
    validar_fecha(fecha)
    validar_duracion(hora_inicio, hora_fin)
    validar_superposicion(sala_id, fecha, hora_inicio, hora_fin, conn)
    
    
    
    
        
        
        