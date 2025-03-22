
import sqlite3

conn = sqlite3.connect('app_database.db', check_same_thread=False)
cursor = conn.cursor()

# Tabla de usuarios
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        correo TEXT UNIQUE NOT NULL,
        fecha_nacimiento TEXT NOT NULL,
        contraseña TEXT NOT NULL
    )
''')

# Crear la tabla academicos SIN la columna 'materias'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS academicos_materias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        universidad TEXT NOT NULL,
        materia TEXT NOT NULL,
        hora_inicio TEXT NOT NULL,
        hora_fin TEXT NOT NULL,
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
    )
''')

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