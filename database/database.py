
# database.py
import sqlite3

# Conectar a la base de datos (se creará si no existe)
conn = sqlite3.connect('app_database.db', check_same_thread=False)
cursor = conn.cursor()

# Crear tabla de usuarios
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        correo TEXT UNIQUE NOT NULL,
        fecha_nacimiento TEXT NOT NULL,
        contraseña TEXT NOT NULL
    )
''')

# Tabla para registro académico (si deseas manejarlo desde base)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS academicos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        universidad TEXT NOT NULL,
        materias TEXT NOT NULL,
        horarios TEXT NOT NULL,
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
    )
''')

# Confirmar cambios
conn.commit()

"""
Crear conexión SQLite.
Crear tablas al iniciar app (usuarios, materias, horarios, tareas, recordatorios, eventos).
Definir funciones generales:
 - insertar()
 - seleccionar()
 - actualizar()
 - eliminar()
"""