
import flet as ft
from controllers.usuario_controller import registrar_usuario

def registro_view(page: ft.Page):
    nombre_input = ft.TextField(label="Nombre")
    correo_input = ft.TextField(label="Correo")
    fecha_input = ft.TextField(label="Fecha de nacimiento (YYYY-MM-DD)")
    contraseña_input = ft.TextField(label="Contraseña", password=True)
    resultado_text = ft.Text()

    def registrar(e):
        msg, success = registrar_usuario(
            nombre_input.value,
            correo_input.value,
            fecha_input.value,
            contraseña_input.value
        )
        resultado_text.value = msg
        resultado_text.color = "green" if success else "red"
        page.update()
        if success:
            page.go("/academico")  # Redirigir al registro académico

    return ft.View(
        "/registro",
        [
            ft.Text("Registro de Usuario", size=30, weight="bold"),
            nombre_input,
            correo_input,
            fecha_input,
            contraseña_input,
            ft.ElevatedButton("Registrar", on_click=registrar),
            resultado_text,
            ft.TextButton("¿Ya tienes cuenta? Iniciar sesión", on_click=lambda _: page.go("/login"))
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