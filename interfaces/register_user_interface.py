
import flet as ft
from controllers.usuario_controller import registrar_usuario

def registro_view(page: ft.Page):
    nombre_input = ft.TextField(label="Nombre")
    correo_input = ft.TextField(label="Correo")
    fecha_nacimiento_input = ft.TextField(label="Fecha de Nacimiento (YYYY-MM-DD)")
    contraseña_input = ft.TextField(label="Contraseña", password=True, can_reveal_password=True)
    resultado_text = ft.Text()

    def guardar_usuario(e):
        nombre = nombre_input.value.strip()
        correo = correo_input.value.strip()
        fecha_nacimiento = fecha_nacimiento_input.value.strip()
        contraseña = contraseña_input.value.strip()

        mensaje, exito, usuario_id = registrar_usuario(nombre, correo, fecha_nacimiento, contraseña)

        resultado_text.value = mensaje
        resultado_text.color = "green" if exito else "red"
        page.update()

        if exito:
            # ✅ Aquí haces la redirección con el usuario_id recibido:
            page.go(f"/academico?usuario_id={usuario_id}")

    return ft.View(
        "/register",
        [
            ft.Text("Registro de Usuario", size=30, weight="bold"),
            nombre_input,
            correo_input,
            fecha_nacimiento_input,
            contraseña_input,
            ft.ElevatedButton("Registrar", on_click=guardar_usuario),
            resultado_text
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

"""
Formularios: nombre, correo, fecha nacimiento, contraseña.
Validación de datos.
Conectar a usuario_controller.py para registrar.
Redirigir al registro académico.
"""