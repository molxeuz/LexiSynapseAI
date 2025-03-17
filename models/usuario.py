
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

"""
Registro, autenticación, edición.
"""