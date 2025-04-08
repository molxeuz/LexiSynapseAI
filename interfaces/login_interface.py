
import flet as ft
from controllers.usuario_controller import Usuario

def login_view(page: ft.Page):
    correo_input = ft.TextField(label="Correo")
    contraseña_input = ft.TextField(label="Contraseña", password=True)
    resultado_text = ft.Text()

    def login(e):
        msg, success = Usuario.iniciar_sesion(correo_input.value, contraseña_input.value)
        resultado_text.value = msg
        resultado_text.color = "green" if success else "red"
        page.update()

        if success:
            page.go("/dashboard")

    return ft.View(
        "/login",
        controls=[
            ft.Text("Iniciar Sesión", size=30, weight="bold"),
            correo_input,
            contraseña_input,
            ft.ElevatedButton("Ingresar", on_click=login),
            resultado_text,
            ft.TextButton("¿No tienes cuenta? Registrarse", on_click=lambda _: page.go("/registro"))
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

"""
Formulario correo, contraseña.
Validación y autenticación con usuario_controller.py.
Redirigir a dashboard.
"""