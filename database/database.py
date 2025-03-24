
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

# Tabla de materias académicas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS academicos_materias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        universidad TEXT NOT NULL,
        carrera TEXT NOT NULL,
        semestre TEXT NOT NULL,
        materia TEXT NOT NULL,
        dia TEXT NOT NULL,
        hora_inicio TEXT NOT NULL,
        hora_fin TEXT NOT NULL,
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id) ON DELETE CASCADE
    )
''')

# Tabla de actividades extracurriculares
cursor.execute('''
    CREATE TABLE IF NOT EXISTS academicos_actividades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        nombre TEXT NOT NULL,
        dia TEXT NOT NULL,
        hora_inicio TEXT NOT NULL,
        hora_fin TEXT NOT NULL,
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id) ON DELETE CASCADE
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