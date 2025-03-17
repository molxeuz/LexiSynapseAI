
from database.database import conn, cursor

def registrar_usuario(nombre, correo, fecha_nacimiento, contraseña):
    if not nombre or not correo or not fecha_nacimiento or not contraseña:
        return "Todos los campos son obligatorios.", False, None

    cursor.execute("SELECT * FROM usuarios WHERE correo = ?", (correo,))
    if cursor.fetchone():
        return "Correo ya registrado.", False, None

    try:
        cursor.execute(
            "INSERT INTO usuarios (nombre, correo, fecha_nacimiento, contraseña) VALUES (?, ?, ?, ?)",
            (nombre, correo, fecha_nacimiento, contraseña)
        )
        conn.commit()
        usuario_id = cursor.lastrowid  # 👈 obtener el ID recién creado
        return "Registro exitoso.", True, usuario_id
    except Exception as e:
        return f"Error al registrar: {e}", False, None

def registrar_academico(usuario_id, universidad, materias, horarios):
    if not usuario_id or not universidad or not materias or not horarios:
        return "Todos los campos son obligatorios.", False

    # Verificar si el usuario existe
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (usuario_id,))
    if not cursor.fetchone():
        return "Usuario no encontrado.", False

    try:
        cursor.execute(
            "INSERT INTO academicos (usuario_id, universidad, materias, horarios) VALUES (?, ?, ?, ?)",
            (usuario_id, universidad, materias, horarios)
        )
        conn.commit()
        return "Registro académico exitoso.", True
    except Exception as e:
        print("Error al registrar datos académicos:", e)  # Log de error detallado
        return f"Error al registrar datos académicos: {e}", False

def login_usuario(correo, contraseña):
    cursor.execute(
        "SELECT nombre FROM usuarios WHERE correo = ? AND contraseña = ?",
        (correo, contraseña)
    )
    usuario = cursor.fetchone()
    if usuario:
        return f"Bienvenido, {usuario[0]}!", True
    return "Correo o contraseña incorrectos.", False

"""
Registro, login, perfil.

Definir funciones de lógica.
Conectar clases (models) con pantallas (interfaces).
Validaciones y respuestas dinámicas.
"""