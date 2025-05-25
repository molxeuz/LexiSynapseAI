# database/database.py
import sqlite3

conn = sqlite3.connect("app_database.db", check_same_thread=False)
cursor = conn.cursor()

# Crear tablas si no existen
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    correo TEXT UNIQUE,
    fecha_nacimiento TEXT,
    contraseña TEXT,
    universidad TEXT,
    carrera TEXT,
    semestre TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS tareas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER,
    nombre TEXT,
    fecha_entrega TEXT,
    prioridad TEXT,
    descripcion TEXT,
    asignatura TEXT,
    completada INTEGER DEFAULT 0,
    FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS academicos_materias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER,
    materia TEXT,
    dia TEXT,
    hora_inicio TEXT,
    hora_fin TEXT,
    FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS academicos_actividades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER,
    nombre TEXT,
    dia TEXT,
    hora_inicio TEXT,
    hora_fin TEXT,
    FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)
''')

conn.commit()