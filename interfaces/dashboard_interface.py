import flet as ft
from controllers.tarea_controller import TareaController

def dashboard_view(page: ft.Page):
    page.title = "LexiSynapseAI - Dashboard"
    page.bgcolor = ft.colors.GREY_100
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    usuario_id = page.client_storage.get("usuario_id") or "Usuario"

    # Controlador de tareas para traer tareas del usuario
    tarea_controller = TareaController(usuario_id)

    def create_task_item(tarea):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Checkbox(value=tarea.completada, on_change=lambda e, t=tarea: (t.marcar_completada(), cargar_tareas(), page.update())),
                    ft.Text(tarea.nombre, weight=ft.FontWeight.BOLD, size=15, expand=True, no_wrap=True),
                    ft.Text(tarea.fecha_entrega, color=ft.colors.GREY_700),
                ],
                spacing=15,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=ft.padding.symmetric(vertical=8, horizontal=12),
            bgcolor=ft.colors.WHITE,
            border_radius=10,
            shadow=ft.BoxShadow(color=ft.colors.BLACK12, blur_radius=4, offset=ft.Offset(1, 1)),
            margin=ft.margin.only(bottom=8),
        )

    tareas_list_container = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)

    def cargar_tareas():
        tareas_list_container.controls.clear()
        tareas = tarea_controller.obtener_tareas()
        if not tareas:
            tareas_list_container.controls.append(
                ft.Text("No tienes tareas pendientes. ¡Genial!", italic=True, color=ft.colors.GREY_600)
            )
        else:
            # Ordenar por fecha de entrega ascendente
            tareas_ordenadas = sorted(tareas, key=lambda t: t.fecha_entrega)
            for tarea in tareas_ordenadas:
                if not tarea.completada:
                    tareas_list_container.controls.append(create_task_item(tarea))

    def create_action_button(icon, text, on_click=None):
        return ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.IconButton(icon=icon, icon_size=38, tooltip=text, on_click=on_click, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20))),
                ft.Text(text, size=13, text_align=ft.TextAlign.CENTER, color=ft.colors.BLUE_GREY_900)
            ],
            spacing=6,
            width=90,
        )

    cargar_tareas()

    saludo_text = ft.Text(f"¡Hola, {usuario_id}!", size=28, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_GREY_900)

    interface = ft.Column(
        controls=[
            saludo_text,
            ft.Text("Aquí están tus tareas pendientes:", size=18, color=ft.colors.BLUE_GREY_700),
            ft.Container(
                content=tareas_list_container,
                height=300,
                width=480,
                padding=12,
                bgcolor=ft.colors.WHITE,
                border_radius=15,
                shadow=ft.BoxShadow(color=ft.colors.BLACK12, blur_radius=8),
                margin=ft.margin.only(top=12, bottom=24)
            ),
            ft.Text("Acciones rápidas", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_GREY_900, ),
            ft.Row(
                controls=[
                    create_action_button(ft.icons.ADD_CIRCLE_OUTLINE, "Añadir Tarea", lambda e: page.go("/tareas")),
                    create_action_button(ft.icons.CALENDAR_MONTH, "Ver Calendario", lambda e: page.go("/calendario")),
                    create_action_button(ft.icons.NOTIFICATIONS, "Recordatorios", lambda e: page.go("/recordatorios")),
                    create_action_button(ft.icons.ANDROID, "Consultar IA", lambda e: page.go("/asistente")),
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                spacing=30,
                wrap=True
            ),
            ft.Container(
                content=ft.TextButton("Cerrar sesión", on_click=lambda e: cerrar_sesion(page), style=ft.ButtonStyle(text_style=ft.TextStyle(color=ft.colors.RED))),
                alignment=ft.alignment.center,
                margin=ft.margin.only(top=40)
            )
        ],
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    return ft.View(
        "/dashboard",
        [interface],
    )

def cerrar_sesion(page: ft.Page):
    page.client_storage.clear()
    page.go("/login")
    page.update()