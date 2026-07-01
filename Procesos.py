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
