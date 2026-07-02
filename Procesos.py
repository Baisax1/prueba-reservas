import logging
from Validacion import (
    validar_reserva,
    OverlapError,
    InvalidDurationError,
    InvalidDateError,
    NotFoundError,
)

logging.basicConfig(
    filename="reservas.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def guardar_reserva(solicitud,status,conn):
    conn.execute(
        "INSERT INTO reservas (usuario_id,sala_id,fecha,hora_inicio,hora_fin,status) VALUES (?,?,?,?,?,?)",
        (
            solicitud["usuario_id"],
            solicitud["sala_id"],
            solicitud["fecha"],
            solicitud["hora_inicio"],
            solicitud["hora_fin"],
            status
        )
    )
    conn.commit()
    
def procesar_reserva(solicitud, conn):
    try:
        validar_reserva(solicitud, conn)
        guardar_reserva(solicitud, "Confirmada", conn)
        logging.info(f"Reserva aprobada: {solicitud}")
        return "Reserva aprobada"
    
    # Para Resolver el Error del Usuario o Sala cuyo Id no existe y no se rompa la tabla
    #agregue esta excepcion para capturar el error de NotFoundError y registrar un mensaje de advertencia en
    #el log, sin guardar la reserva en la base de datos.
    #Solo habria que cambiar el codigo de abajo por el siguiente
    #except NotFoundError as e:
    #    logging.warning(f"Reserva rechazada: {solicitud} - Motivo: {str(e)}")
    #except (OverlapError, InvalidDurationError, InvalidDateError) as e:
    #   guardar_reserva(solicitud, "Rechazada", conn)
    #   logging.warning(f"Reserva rechazada: {solicitud} - Motivo: {str(e)}")
    
    except (OverlapError, InvalidDurationError, InvalidDateError, NotFoundError) as e:
        guardar_reserva(solicitud, "Rechazada", conn)
        logging.warning(f"Reserva rechazada: {solicitud} - Motivo: {str(e)}")
        
        
        
def procesar_reservas(solicitudes, conn):#
    for solicitud in solicitudes:
        procesar_reserva(solicitud, conn)
        