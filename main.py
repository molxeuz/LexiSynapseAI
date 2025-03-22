
import flet as ft
from interfaces.register_user_interface import registro_view
from interfaces.register_acad_interface import academico_view
from interfaces.login_interface import login_view

def main(page: ft.Page):
    page.title = "Sistema de Registro"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def route_change(e):
        page.views.clear()
        route = page.route

        if route == "/registro":
            page.views.append(registro_view(page))
        elif route.startswith("/academico"):
            page.views.append(academico_view(page))
        elif route == "/login":
            page.views.append(login_view(page))
        else:
            page.views.append(login_view(page))
        page.update()

    page.on_route_change = route_change
    page.go("/login")

ft.app(target=main, view=ft.WEB_BROWSER)

"""
Inicializar la base de datos (llamando a database.py).
Cargar pantallas (interfaces) según navegación.
Controlar navegación: login, registro, dashboard, IA, calendario, etc.
Integrar todas las clases y controladores.
Control de sesión de usuario activo.
"""