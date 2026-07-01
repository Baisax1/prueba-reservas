import sqlite3

def conectar(nombre_db="reservas.db"):
    conn = sqlite3.connect(nombre_db)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def crear_tablas(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            departamento TEXT NOT NULL
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS salas (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            capacidad_maxima INTEGER NOT NULL
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS reservas (
            id INTEGER PRIMARY KEY,
            usuario_id INTEGER NOT NULL,
            sala_id INTEGER NOT NULL,
            fecha TEXT NOT NULL,
            hora_inicio TEXT NOT NULL,
            hora_fin TEXT NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
            FOREIGN KEY (sala_id) REFERENCES salas(id)
        )
    """)
    conn.commit()
    
def seed(conn):
        
    cursor_usuarios = conn.execute("SELECT COUNT(*) FROM usuarios")
    total_usuarios = cursor_usuarios.fetchone()[0]
    
    
    cursor_salas = conn.execute("SELECT COUNT(*) FROM salas")
    total_salas = cursor_salas.fetchone()[0]
    
    
    if total_usuarios >= 3 and total_salas >= 3:
        return 
        
    conn.executemany(
        "INSERT INTO usuarios (nombre, departamento) VALUES (?, ?)",
        [
            ("Ana Torres", "Ventas"),
            ("Luis Pérez", "IT"),
            ("Marta Gómez", "RRHH"),
        ]
    )
    conn.executemany(
        "INSERT INTO salas (nombre, capacidad_maxima) VALUES (?, ?)",
        [
            ("Sala A", 60),
            ("Sala B", 35),
            ("Sala C", 40),
        ]
    )
    conn.executemany(
        "INSERT INTO reservas (usuario_id, sala_id, fecha, hora_inicio, hora_fin, status) VALUES (?, ?, ?, ?, ?, ?)",
        [
            (1, 1, "2026-06-28", "10:00", "11:00", "Confirmada"),
            (2, 2, "2026-06-28", "13:00", "14:00", "Confirmada"),
        ]
    )
    
    
    conn.commit()