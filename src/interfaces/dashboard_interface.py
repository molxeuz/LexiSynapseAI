
"""
Vista del dashboard principal.
Muestra un resumen de tareas próximas y accesos rápidos a otras funcionalidades como tareas, calendario e IA.
Requiere que el usuario haya iniciado sesión (usuario_id en client_storage).
"""

import flet as ft
from src.controllers.tarea_controller import TareaController

def dashboard_view(page: ft.Page):
    usuario_id = page.client_storage.get("usuario_id")
    if not usuario_id:
        return ft.View(
            route="/dashboard",
            controls=[
                ft.Text("Error: No has iniciado sesión. Redirigiendo al login...", color="red"),
                ft.ElevatedButton("Ir a Login", on_click=lambda _: page.go("/login"))
            ],
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    tarea_controller = TareaController(usuario_id)
    page.title = "LexiSynapseAI"

    def format_task(tarea):
        return ft.Row(
            controls=[
                ft.Checkbox(value=tarea.completada, disabled=True),
                ft.Text(tarea.nombre, weight="bold", expand=True),
                ft.Text(str(tarea.fecha_entrega or ""), color=ft.colors.GREY_600)
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

    tareas = tarea_controller.obtener_tareas()[:3]

    tareas_resumen = ft.Column(
        controls=[
            format_task(tarea) for tarea in tareas
        ] if tareas else [
            ft.Text("No hay tareas próximas.", italic=True, color=ft.colors.GREY_600)
        ],
        spacing=10
    )

    def create_action_button(icon, text, on_click):
        return ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.IconButton(icon=icon, icon_size=30, on_click=on_click),
                ft.Text(text, size=12, text_align=ft.TextAlign.CENTER)
            ],
            spacing=5
        )

    return ft.View(
        route="/dashboard",
        bgcolor=ft.colors.GREY_100,
        padding=20,
        controls=[
            ft.Text("Bienvenido a LexiSynapseAI", size=32, weight="bold", color=ft.colors.BLUE_GREY_900),
            ft.ResponsiveRow([
                ft.Container(
                    content=ft.Column([
                        ft.Text("Resumen de Tareas", size=20, weight="bold", color=ft.colors.BLUE_GREY_800),
                        ft.Divider(thickness=2, color=ft.colors.BLUE_GREY_200),
                        tareas_resumen
                    ], spacing=10),
                    col={"sm": 12, "md": 6},
                    padding=20,
                    bgcolor=ft.colors.WHITE,
                    border_radius=15,
                    shadow=ft.BoxShadow(color=ft.colors.BLACK12, blur_radius=8),
                    height=250
                ),
                ft.Container(
                    content=ft.Column([
                        ft.Text("Espacio disponible", size=20, weight="bold", color=ft.colors.BLUE_GREY_800),
                        ft.Divider(thickness=2, color=ft.colors.BLUE_GREY_200),
                        ft.Text("Aquí puedes agregar más funciones o widgets en el futuro.", italic=True, color=ft.colors.GREY_600)
                    ], spacing=10),
                    col={"sm": 12, "md": 6},
                    padding=20,
                    bgcolor=ft.colors.WHITE,
                    border_radius=15,
                    shadow=ft.BoxShadow(color=ft.colors.BLACK12, blur_radius=8),
                    height=250
                )
            ], spacing=20),
            ft.Divider(height=30, color=ft.colors.TRANSPARENT),
            ft.Container(
                content=ft.Row(
                    controls=[
                        create_action_button(ft.icons.ADD_CIRCLE_OUTLINE, "Añadir Tarea", lambda _: page.go("/tareas")),
                        create_action_button(ft.icons.CALENDAR_MONTH, "Calendario", lambda _: page.go("/calendario")),
                        create_action_button(ft.icons.ANDROID, "IA", lambda _: page.go("/ia_view")),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY
                ),
                padding=20,
                bgcolor=ft.colors.WHITE,
                border_radius=15,
                shadow=ft.BoxShadow(color=ft.colors.BLACK12, blur_radius=8)
            )
        ]
    )
