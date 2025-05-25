import flet as ft
from controllers.usuario_controller import Usuario

def login_view(page: ft.Page):
    page.title = "Bienvenido de nuevo"
    page.padding = 0
    page.bgcolor = "#f0f4ff"

    correo_input = ft.TextField(
        label="Correo electrónico",
        icon=ft.icons.EMAIL,
        width=300,
        border_radius=10,
        bgcolor="#ffffff",
    )

    contraseña_input = ft.TextField(
        label="Contraseña",
        icon=ft.icons.LOCK,
        password=True,
        can_reveal_password=True,
        width=300,
        border_radius=10,
        bgcolor="#ffffff",
    )

    resultado_text = ft.Text(size=14)

    def login(e):
        msg, success = Usuario.iniciar_sesion(correo_input.value, contraseña_input.value)
        resultado_text.value = msg
        resultado_text.color = "#00c853" if success else "#d50000"
        page.update()

        if success:
            page.go("/dashboard")

    login_button = ft.ElevatedButton(
        " Ingresar",
        on_click=login,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=20,
            bgcolor="#4a90e2",
            color="white"
        ),
    )

    card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("Bienvenido de nuevo", size=32, weight="bold", color="#1e3a8a"),
                    ft.Text("Ingresa tus credenciales para continuar", size=16, color="#4b5563"),
                    ft.Divider(),
                    correo_input,
                    contraseña_input,
                    login_button,
                    resultado_text,
                    ft.TextButton(
                        "¿No tienes cuenta? Registrarse",
                        on_click=lambda _: page.go("/registro"),
                        style=ft.ButtonStyle(
                            color="#4a90e2",
                            overlay_color="#dbeafe",
                        ),
                    ),
                ],
                tight=True,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=40,
            width=500,
            bgcolor="white",
            border_radius=20,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=15,
                color=ft.colors.GREY_300,
                offset=ft.Offset(0, 4),
            ),
        )
    )

    return ft.View(
        "/login",
        controls=[ft.Row([card], alignment=ft.MainAxisAlignment.CENTER)],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
