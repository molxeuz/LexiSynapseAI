from src.database.database import conn, cursor

class Usuario:
    def __init__(self, nombre, correo, fecha_nacimiento, contraseña, universidad, carrera, semestre):
        self.nombre = nombre
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento
        self.contraseña = contraseña
        self.universidad = universidad
        self.carrera = carrera
        self.semestre = semestre

    @staticmethod
    def registrar_usuario(nombre, correo, fecha_nacimiento, contraseña, universidad, carrera, semestre):
        if not all([nombre, correo, fecha_nacimiento, contraseña, universidad, carrera, semestre]):
            return "Todos los campos son obligatorios.", False, None

        cursor.execute("SELECT id FROM usuarios WHERE correo = ?", (correo,))
        if cursor.fetchone():
            return "Correo ya registrado.", False, None

        try:
            cursor.execute(
                "INSERT INTO usuarios (nombre, correo, fecha_nacimiento, contraseña, universidad, carrera, semestre) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (nombre, correo, fecha_nacimiento, contraseña, universidad, carrera, semestre)
            )
            conn.commit()
            usuario_id = cursor.lastrowid
            return "Registro exitoso.", True, usuario_id
        except Exception as e:
            return f"Error al registrar: {e}", False, None

    @staticmethod
    def iniciar_sesion(correo, contraseña):
        cursor.execute("SELECT id, nombre, universidad, carrera, semestre FROM usuarios WHERE correo = ? AND contraseña = ?", (correo, contraseña))
        usuario = cursor.fetchone()
        if usuario:
            return {
                "id": usuario[0],
                "nombre": usuario[1],
                "universidad": usuario[2],
                "carrera": usuario[3],
                "semestre": usuario[4]
            }, True
        return "Correo o contraseña incorrectos.", False

    @staticmethod
    def registrar_academico(usuario_id, materias, actividades):
        if not usuario_id:
            return "Usuario no encontrado.", False

        try:
            for materia in materias:
                if not all([materia.get("nombre"), materia.get("dia"), materia.get("hora_inicio"), materia.get("hora_fin")]):
                    return "Todos los campos de las materias son obligatorios.", False
                cursor.execute(
                    "INSERT INTO academicos_materias (usuario_id, materia, dia, hora_inicio, hora_fin) VALUES (?, ?, ?, ?, ?)",
                    (usuario_id, materia["nombre"], materia["dia"], materia["hora_inicio"], materia["hora_fin"])
                )

            for actividad in actividades:
                if not all([actividad.get("nombre"), actividad.get("dia"), actividad.get("hora_inicio"), actividad.get("hora_fin")]):
                    return "Todos los campos de las actividades son obligatorios.", False
                cursor.execute(
                    "INSERT INTO academicos_actividades (usuario_id, nombre, dia, hora_inicio, hora_fin) VALUES (?, ?, ?, ?, ?)",
                    (usuario_id, actividad["nombre"], actividad["dia"], actividad["hora_inicio"], actividad["hora_fin"])
                )

            conn.commit()
            return "Registro académico exitoso.", True
        except Exception as e:
            return f"Error al registrar datos académicos: {e}", False