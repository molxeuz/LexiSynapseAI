from database.database import conn, cursor


class Usuario:
    def __init__(self, nombre: str, correo: str, fecha_nacimiento: str, contraseña: str):
        self.nombre = nombre
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento
        self.contraseña = contraseña

    @staticmethod
    def registrar(nombre, correo, fecha_nacimiento, contraseña):
        if not all([nombre, correo, fecha_nacimiento, contraseña]):
            return "Todos los campos son obligatorios.", False, None

        cursor.execute("SELECT id FROM usuarios WHERE correo = ?", (correo,))
        if cursor.fetchone():
            return "Correo ya registrado.", False, None

        try:
            cursor.execute(
                "INSERT INTO usuarios (nombre, correo, fecha_nacimiento, contraseña) VALUES (?, ?, ?, ?)",
                (nombre, correo, fecha_nacimiento, contraseña)
            )
            conn.commit()
            usuario_id = cursor.lastrowid  # 🔹 Obtenemos el ID del usuario registrado
            return "Registro exitoso.", True, usuario_id
        except Exception as e:
            return f"Error al registrar: {e}", False, None

    @staticmethod
    def login(correo, contraseña):
        cursor.execute("SELECT id, nombre FROM usuarios WHERE correo = ? AND contraseña = ?", (correo, contraseña))
        usuario = cursor.fetchone()
        if usuario:
            return {"id": usuario[0], "nombre": usuario[1]}, True
        return "Correo o contraseña incorrectos.", False


class Academico:
    @staticmethod
    def registrar(usuario_id, universidad, carrera, semestre, materias, actividades):
        if not all([usuario_id, universidad, carrera, semestre]):
            return "Todos los campos son obligatorios.", False

        cursor.execute("SELECT id FROM usuarios WHERE id = ?", (usuario_id,))
        if not cursor.fetchone():
            return "Usuario no encontrado.", False

        try:
            for materia in materias:
                if not all([materia.get("nombre"), materia.get("dia"), materia.get("hora_inicio"),
                            materia.get("hora_fin")]):
                    return "Todos los campos de las materias son obligatorios.", False
                cursor.execute(
                    "INSERT INTO academicos_materias (usuario_id, universidad, carrera, semestre, materia, dia, hora_inicio, hora_fin) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                    (usuario_id, universidad, carrera, semestre, materia["nombre"], materia["dia"],
                     materia["hora_inicio"], materia["hora_fin"])
                )

            for actividad in actividades:
                if not all([actividad.get("nombre"), actividad.get("dia"), actividad.get("hora_inicio"),
                            actividad.get("hora_fin")]):
                    return "Todos los campos de las actividades son obligatorios.", False
                cursor.execute(
                    "INSERT INTO academicos_actividades (usuario_id, nombre, dia, hora_inicio, hora_fin) VALUES (?, ?, ?, ?, ?)",
                    (usuario_id, actividad["nombre"], actividad["dia"], actividad["hora_inicio"], actividad["hora_fin"])
                )

            conn.commit()
            return "Registro académico exitoso.", True
        except Exception as e:
            return f"Error al registrar datos académicos: {e}", False

"""
Registro, login, perfil.

Definir funciones de lógica.
Conectar clases (models) con pantallas (interfaces).
Validaciones y respuestas dinámicas.
"""