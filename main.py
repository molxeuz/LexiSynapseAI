
"""
Archivo principal que configura la navegación y vistas del sistema de registro.
Gestiona rutas y muestra las interfaces correspondientes según la URL.
"""

import flet as ft

from src.interfaces.register_user_interface import registro_view
from src.interfaces.register_acad_interface import academico_view
from src.interfaces.login_interface import login_view
from src.interfaces.tareas_interface import tareas_view
from src.interfaces.calendario_interface import calendario_view
from src.interfaces.dashboard_interface import dashboard_view
from src.interfaces.ia_interface import ia_view
from src.interfaces.profile_interface import perfil_usuario_view  # <-- Importa tu vista perfil

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
        elif route == "/dashboard":
            page.views.append(dashboard_view(page))
        elif route == "/perfil":
            page.views.append(perfil_usuario_view(page))
        elif route == "/tareas":
            page.views.append(tareas_view(page))
        elif route == "/calendario":
            page.views.append(calendario_view(page))
        elif route == "/ia_view":
            page.views.append(ia_view(page))
        else:
            page.views.append(login_view(page))
        page.update()

    page.on_route_change = route_change
    page.go("/login")

ft.app(target=main, view=ft.WEB_BROWSER)