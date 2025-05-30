
"""
Clase Usuario para manejar registro, inicio de sesión y datos académicos.
Incluye validaciones y operaciones con la base de datos SQLite.
"""

from src.database.database import conn, cursor

class UsuarioData:
    """
    Clase auxiliar para representar los datos de un usuario.
    """
    def __init__(self, row):
        self.nombre = row[0]
        self.correo = row[1]
        self.fecha_nacimiento = row[2]
        self.universidad = row[3]
        self.carrera = row[4]
        self.semestre = row[5]

class Usuario:
    def __init__(self, nombre=None, correo=None, fecha_nacimiento=None, contraseña=None,
                 universidad=None, carrera=None, semestre=None, usuario_id=None):
        self.nombre = nombre
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento
        self.contraseña = contraseña
        self.universidad = universidad
        self.carrera = carrera
        self.semestre = semestre
        self.usuario_id = usuario_id

    def obtener_usuario(self):
        cursor.execute(
            "SELECT nombre, correo, fecha_nacimiento, universidad, carrera, semestre FROM usuarios WHERE id = ?",
            (self.usuario_id,))
        row = cursor.fetchone()
        if row:
            return UsuarioData(row)
        return None

    def actualizar_usuario_completo(self, nombre, correo, fecha_nacimiento, universidad, carrera, semestre):
        try:
            cursor.execute("""
                UPDATE usuarios 
                SET nombre = ?, correo = ?, fecha_nacimiento = ?, universidad = ?, carrera = ?, semestre = ?
                WHERE id = ?
            """, (nombre, correo, fecha_nacimiento, universidad, carrera, semestre, self.usuario_id))
            conn.commit()
            return True, "Datos actualizados correctamente."
        except Exception as e:
            return False, f"Error al actualizar: {e}"

    @staticmethod
    def registrar_usuario(nombre, correo, fecha_nacimiento, contraseña, universidad, carrera, semestre):
        if not all([nombre, correo, fecha_nacimiento, contraseña, universidad, carrera, semestre]):
            return "Todos los campos son obligatorios.", False, None

        cursor.execute("SELECT id FROM usuarios WHERE correo = ?", (correo,))
        if cursor.fetchone():
            return "Correo ya registrado.", False, None

        try:
            cursor.execute("""
                INSERT INTO usuarios 
                (nombre, correo, fecha_nacimiento, contraseña, universidad, carrera, semestre) 
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (nombre, correo, fecha_nacimiento, contraseña, universidad, carrera, semestre))
            conn.commit()
            usuario_id = cursor.lastrowid
            return "Registro exitoso.", True, usuario_id
        except Exception as e:
            return f"Error al registrar: {e}", False, None

    @staticmethod
    def iniciar_sesion(correo, contraseña):
        cursor.execute("""
            SELECT id, nombre, universidad, carrera, semestre 
            FROM usuarios 
            WHERE correo = ? AND contraseña = ?
        """, (correo, contraseña))
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
                cursor.execute("""
                    INSERT INTO academicos_materias 
                    (usuario_id, materia, dia, hora_inicio, hora_fin) 
                    VALUES (?, ?, ?, ?, ?)
                """, (usuario_id, materia["nombre"], materia["dia"], materia["hora_inicio"], materia["hora_fin"]))

            for actividad in actividades:
                if not all([actividad.get("nombre"), actividad.get("dia"), actividad.get("hora_inicio"), actividad.get("hora_fin")]):
                    return "Todos los campos de las actividades son obligatorios.", False
                cursor.execute("""
                    INSERT INTO academicos_actividades 
                    (usuario_id, nombre, dia, hora_inicio, hora_fin) 
                    VALUES (?, ?, ?, ?, ?)
                """, (usuario_id, actividad["nombre"], actividad["dia"], actividad["hora_inicio"], actividad["hora_fin"]))

            conn.commit()
            return "Registro académico exitoso.", True
        except Exception as e:
            return f"Error al registrar datos académicos: {e}", False
