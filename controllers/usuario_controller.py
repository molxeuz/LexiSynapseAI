
from database.database import conn, cursor

class Usuario:
    def __init__(self, nombre: str, correo: str, fecha_nacimiento: str, contraseña: str):
        self.nombre = nombre
        self.correo = correo
        self.fecha_nacimiento = fecha_nacimiento
        self.contraseña = contraseña
        self.preferencias = []
        self.historial = []

    def mostrar_usuario(self):
        return f"{self.nombre} - {self.correo} - {self.fecha_nacimiento}"

    @staticmethod
    def registrar(nombre, correo, fecha_nacimiento, contraseña):
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
            usuario_id = cursor.lastrowid
            return "Registro exitoso.", True, usuario_id
        except Exception as e:
            return f"Error al registrar: {e}", False, None

    @staticmethod
    def login(correo, contraseña):
        cursor.execute(
            "SELECT nombre FROM usuarios WHERE correo = ? AND contraseña = ?",
            (correo, contraseña)
        )
        usuario = cursor.fetchone()
        if usuario:
            return f"Bienvenido, {usuario[0]}!", True
        return "Correo o contraseña incorrectos.", False

class Academico:
    @staticmethod
    def registrar(usuario_id, universidad, materias):
        if not usuario_id or not universidad or not materias:
            return "Todos los campos son obligatorios.", False

        cursor.execute("SELECT * FROM usuarios WHERE id = ?", (usuario_id,))
        if not cursor.fetchone():
            return "Usuario no encontrado.", False

        try:
            for materia in materias:
                nombre = materia.get("nombre", "").strip()
                hora_inicio = materia.get("hora_inicio", "").strip()
                hora_fin = materia.get("hora_fin", "").strip()

                if not nombre or not hora_inicio or not hora_fin:
                    return f"Todos los campos de la materia '{nombre}' son obligatorios.", False

                cursor.execute(
                    "INSERT INTO academicos_materias (usuario_id, universidad, materia, hora_inicio, hora_fin) VALUES (?, ?, ?, ?, ?)",
                    (usuario_id, universidad, nombre, hora_inicio, hora_fin)
                )
            conn.commit()
            return "Registro académico exitoso.", True
        except Exception as e:
            print("Error al registrar datos académicos:", e)
            return f"Error al registrar datos académicos: {e}", False

"""
Registro, login, perfil.

Definir funciones de lógica.
Conectar clases (models) con pantallas (interfaces).
Validaciones y respuestas dinámicas.
"""