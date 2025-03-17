
from models.usuario import Usuario

db_usuarios: list[Usuario] = []

def registrar_usuario(nombre, correo, fecha_nacimiento, contraseña):
    if not nombre or not correo or not fecha_nacimiento or not contraseña:
        return "Todos los campos son obligatorios.", False
    if any(user.correo == correo for user in db_usuarios):
        return "Correo ya registrado.", False

    nuevo_usuario = Usuario(nombre, correo, fecha_nacimiento, contraseña)
    db_usuarios.append(nuevo_usuario)
    return "Registro exitoso.", True

def login_usuario(correo, contraseña):
    for usuario in db_usuarios:
        if usuario.correo == correo and usuario.contraseña == contraseña:
            return f"Bienvenido, {usuario.nombre}!", True
    return "Correo o contraseña incorrectos.", False

"""
Registro, login, perfil.

Definir funciones de lógica.
Conectar clases (models) con pantallas (interfaces).
Validaciones y respuestas dinámicas.
"""