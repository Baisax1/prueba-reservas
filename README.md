CODIGO-RETO: LIBELULA-77

# Sistema para reservas de Salas
Sistema en Python que se encarga de validar y procesar solicitudes de reservas de salas de reuniones para evitar solapamientos

## Requisitos
- Python 3.13.3
- No requiere Librerias Externas

## Como ejecutarlo

1. Clona el repositorio
    git clone https://github.com/Baisax1/prueba-reservas.git
    cd prueba-reservas

3. (Opcional) Crear un entorno virtual
    py -m venv venv

4. Ejecuta el Programa
    py ejecutar_reservas.py

5. Esto generara de manera automatica un db con sqlite3 llamada "reservas.db" con las tablas planteadas en DB.py y posteriormente usara la seed en este mismo archivo para añadir 3 usuarios, 3 salas y 2 reservas.

6. Se evaluara el lote de reservas planteado en el archivo ejecutar_reservas y uno por uno se evaluaran, para posteriormente ser Confirmadas o Rechazadas.

7. Todas las reservas confirmadas o rechazadas seran guardados en la base de datos junto con un registro en el archivo de reservas.log para su posterior analisis en caso de error.

## Reglas Implementadas 

1. **Regla de Superposición:** Una sala no puede ser reservada si ya existe una reserva *Confirmada* para esa misma sala en la misma fecha cuyos horarios se crucen.
   - *Ejemplo:* Si hay una reserva de 10:00 a 11:00, una nueva de 10:30 a 11:30 debe ser rechazada.
2. **Regla de Duración:** La reserva debe ser de al menos 30 minutos y no puede exceder las 4 horas.
3. **Regla de Existencia:** El usuario y la sala deben existir en la base de datos.

## Manejo de Errores Utilizado

El sistema usa excepciones personalizadas (`OverlapError`, `InvalidDurationError`, `InvalidDateError`, `NotFoundError`) para capturar cada tipo de fallo. Si una solicitud es rechazada, el sistema continúa procesando el resto del lote sin interrumpirse, y registra el motivo en `reservas.log`

## Reflexión

Me enfocaria principalmente en mejorar las consultas de SQL y enfocarlas mas al trabajo con lotes grandes en lugar de selects generales, esto para reducir la sobrecarga y no saturar al servidor con las peticiones.

## Autor

Balam López Jaramillo
