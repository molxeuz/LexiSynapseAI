
import flet as ft

def dashboard_view(page: ft.Page):
    page.title = "LexiSynapseAI"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def create_task_item(task_name, due_date):
        return ft.Row(
            controls=[
                ft.Checkbox(),
                ft.Text(task_name, style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                ft.Text(due_date, color=ft.colors.GREY_600),
            ],
            spacing=15
        )

    def create_action_button(icon, text, on_click=None):
        return ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.IconButton(icon=icon, icon_size=30, on_click=on_click),
                ft.Text(text, size=12, text_align=ft.TextAlign.CENTER)
            ],
            spacing=5
        )

    interface = ft.Container(
        padding=20,
        content=ft.Column(
            controls=[
                ft.Text("Hola, Usuario", size=24, weight=ft.FontWeight.BOLD),
                ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                create_task_item("Examen de cálculo", "18/04/25"),
                create_task_item("Entrega Proyecto POO", "19/04/25"),
                create_task_item("Taller Álgebra Lineal", "21/04/25"),
                ft.Divider(height=40),
                ft.Row(
                    controls=[
                        create_action_button(ft.icons.ADD_CIRCLE_OUTLINE, "Añadir Tarea", lambda e: page.go("/tareas")),
                        create_action_button(ft.icons.ASSIGNMENT, "Cuestionarios"),
                        create_action_button(ft.icons.CALENDAR_MONTH, "Ver calendario", on_click=lambda _: page.go("/calendario")),
                        create_action_button(ft.icons.NOTIFICATIONS, "Recordatorios"),
                        create_action_button(ft.icons.ANDROID, "Consultar IA"),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY
                )
            ]
        )
    )

    return ft.View("/dashboard", [interface])

def main(page: ft.Page):
    page.title = "LexiSynapseAI"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def create_task_item(task_name, due_date):
        return ft.Row(
            controls=[
                ft.Checkbox(),
                ft.Text(task_name, style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                ft.Text(due_date, color=ft.colors.GREY_600),
            ],
            spacing=15
        )

    def create_action_button(icon, text, on_click=None):
        return ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.IconButton(icon=icon, icon_size=30, on_click=on_click),
                ft.Text(text, size=12, text_align=ft.TextAlign.CENTER)
            ],
            spacing=5
        )

    interface = ft.Container(
        padding=20,
        content=ft.Column(
            controls=[
                ft.Text("Hola, Usuario", size=24, weight=ft.FontWeight.BOLD),
                ft.Divider(height=20, color=ft.colors.TRANSPARENT),
                create_task_item("Examen de calculo", "18/04/25"),
                create_task_item("Entrega Proyecto Poo", "19/04/25"),
                create_task_item("Taller Algebra Lineal", "21/04/25"),
                ft.Divider(height=40),
                ft.Row(
                    controls=[
                        create_action_button(ft.icons.ADD_CIRCLE_OUTLINE, "Añadir Tarea"),
                        create_action_button(ft.icons.ASSIGNMENT, "Cuestionarios"),
                        create_action_button(ft.icons.CALENDAR_MONTH, "Ver calendario"),
                        create_action_button(ft.icons.NOTIFICATIONS, "Recordatorios"),
                        create_action_button(ft.icons.ANDROID, "Consultar IA"),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY
                )
            ]
        )
    )

    page.add(interface)

"""
Mostrar datos usuario, tareas, recordatorios.
Conectar con tarea_controller.py, recordatorio_controller.py.
Acceso a IA (conexión directa con asistente_controller.py).
"""