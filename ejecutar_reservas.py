from Db import conectar, crear_tablas, seed
from Procesos import procesar_reservas


lote_solicitudes = [
    {"usuario_id": 1, "sala_id": 1, "fecha": "2026-06-28", "hora_inicio": "10:30", "hora_fin": "11:30"},
    {"usuario_id": 2, "sala_id": 2, "fecha": "2026-06-28", "hora_inicio": "09:00", "hora_fin": "09:15"},
    {"usuario_id": 3, "sala_id": 1, "fecha": "2026-06-28", "hora_inicio": "14:00", "hora_fin": "15:30"},
    {"usuario_id": 99, "sala_id": 1, "fecha": "2026-06-28", "hora_inicio": "16:00", "hora_fin": "17:00"},
]


def imprimir_reporte(conn):
    resultados = conn.execute(
        """
        SELECT salas.nombre,
               SUM(
                   (CAST(SUBSTR(reservas.hora_fin, 1, 2) AS INTEGER) * 60 + CAST(SUBSTR(reservas.hora_fin, 4, 2) AS INTEGER))
                   -
                   (CAST(SUBSTR(reservas.hora_inicio, 1, 2) AS INTEGER) * 60 + CAST(SUBSTR(reservas.hora_inicio, 4, 2) AS INTEGER))
               ) / 60.0 AS horas_totales
        FROM reservas
        JOIN salas ON reservas.sala_id = salas.id
        WHERE reservas.status = 'Confirmada'
        GROUP BY salas.nombre
        """
    ).fetchall()

    print("\nReporte de horas totales reservadas por salas")
    for nombre_sala, horas in resultados:
        print(f"{nombre_sala}: {horas:.2f} horas")
        
        
def main():
    conn = conectar()
    crear_tablas(conn)
    seed(conn)

    procesar_reservas(lote_solicitudes, conn)

    imprimir_reporte(conn)

    conn.close()


if __name__ == "__main__":
    main()