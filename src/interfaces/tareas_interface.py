
"""
Vista de gestión de tareas.
Permite agregar, listar y marcar tareas como completadas. Ordena por prioridad y fecha.
Requiere sesión iniciada (usuario_id en client_storage).
"""

import flet as ft
from src.controllers.tarea_controller import TareaController
from datetime import datetime

PRIORIDAD_ORDEN = {"Alta": 0, "Media": 1, "Baja": 2}
PRIORIDAD_COLOR = {
    "Alta": ft.Colors.RED_100,
    "Media": ft.Colors.ORANGE_100,
    "Baja": ft.Colors.GREEN_100,
}

def tareas_view(page: ft.Page):
    usuario_id = page.client_storage.get("usuario_id")
    if not usuario_id:
        return ft.View(
            route="/tareas",
            controls=[
                ft.Text("Error: No has iniciado sesión. Redirigiendo al login...", color="red"),
                ft.ElevatedButton("Ir a Login", on_click=lambda _: page.go("/login"))
            ],
            vertical_alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.MainAxisAlignment.CENTER,
        )

    controller = TareaController(usuario_id)
    page.title = "Gestión de Tareas"

    nombre_tarea = ft.TextField(label="Nombre de la tarea", width=400, border_radius=10, filled=True)
    fecha_entrega = ft.TextField(label="Fecha de entrega (dd/mm/aa)", width=200, border_radius=10, filled=True)
    prioridad = ft.Dropdown(
        label="Prioridad",
        width=150,
        border_radius=10,
        filled=True,
        options=[
            ft.dropdown.Option("Alta"),
            ft.dropdown.Option("Media"),
            ft.dropdown.Option("Baja")
        ]
    )
    descripcion = ft.TextField(label="Descripción", multiline=True, max_lines=3, width=400, border_radius=10, filled=True)
    asignatura = ft.TextField(label="Asignatura", width=200, border_radius=10, filled=True)
    resultado_text = ft.Text()

    tareas_lista = ft.Column(
        scroll=ft.ScrollMode.AUTO,
        spacing=12,
        expand=True
    )

    def parse_fecha(fecha_str):
        try:
            return datetime.strptime(fecha_str, "%d/%m/%y")
        except:
            return datetime.max

    def format_fecha(fecha_str):
        try:
            dt = datetime.strptime(fecha_str, "%d/%m/%y")
            return dt.strftime("%d %b %Y")
        except:
            return fecha_str

    def renderizar_tareas():
        tareas_lista.controls.clear()
        tareas_ordenadas = sorted(
            controller.obtener_tareas(),
            key=lambda t: (PRIORIDAD_ORDEN.get(t.prioridad, 99), parse_fecha(t.fecha_entrega))
        )
        if not tareas_ordenadas:
            tareas_lista.controls.append(
                ft.Text("No tienes tareas registradas.", italic=True, color=ft.colors.GREY_600)
            )
        for tarea in tareas_ordenadas:
            color = PRIORIDAD_COLOR.get(tarea.prioridad, ft.colors.GREY_200)
            tarjeta = ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Checkbox(
                            value=tarea.completada,
                            on_change=lambda e, t=tarea: (t.marcar_completada(), renderizar_tareas(), page.update())
                        ),
                        ft.Text(tarea.nombre, weight="bold", size=16, expand=True),
                        ft.Container(
                            content=ft.Text(tarea.prioridad, weight="bold", size=12),
                            bgcolor=color,
                            padding=ft.padding.symmetric(horizontal=10, vertical=5),
                            border_radius=20,
                        )
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.Row([
                        ft.Text(f"Entrega: {format_fecha(tarea.fecha_entrega)}", color=ft.colors.GREY_700),
                        ft.Text(f"Asignatura: {tarea.asignatura}", color=ft.colors.GREY_700)
                    ], spacing=20),
                    ft.Text(tarea.descripcion, size=13, italic=True, color=ft.colors.GREY_600)
                ]),
                padding=15,
                border_radius=15,
                bgcolor=ft.colors.WHITE,
                animate_opacity=300,
                animate_size=300,
                shadow=ft.BoxShadow(color=ft.colors.BLACK26, blur_radius=6, offset=ft.Offset(2, 2)),
            )
            tareas_lista.controls.append(tarjeta)

    def agregar_tarea(e):
        if not nombre_tarea.value or not fecha_entrega.value or not prioridad.value:
            resultado_text.value = "Por favor completa Nombre, Fecha y Prioridad"
            resultado_text.color = "red"
            page.update()
            return
        try:
            datetime.strptime(fecha_entrega.value.strip(), "%d/%m/%y")
        except ValueError:
            resultado_text.value = "La fecha debe tener el formato dd/mm/aa"
            resultado_text.color = "red"
            page.update()
            return

        exito, mensaje = controller.agregar_tarea(
            nombre_tarea.value.strip(),
            fecha_entrega.value.strip(),
            prioridad.value,
            descripcion.value.strip(),
            asignatura.value.strip()
        )
        resultado_text.value = mensaje
        resultado_text.color = "green" if exito else "red"
        if exito:
            nombre_tarea.value = ""
            fecha_entrega.value = ""
            prioridad.value = None
            descripcion.value = ""
            asignatura.value = ""
        renderizar_tareas()
        page.update()

    renderizar_tareas()

    return ft.View(
        route="/tareas",
        bgcolor=ft.colors.GREY_100,
        padding=20,
        controls=[
            ft.Text("Gestión de Tareas", size=32, weight="bold", color=ft.colors.BLUE_GREY_900),
            ft.ResponsiveRow([
                ft.Container(
                    content=ft.Column([
                        ft.Text("Agregar Nueva Tarea", size=24, weight="bold", color=ft.colors.BLUE_GREY_800),
                        ft.Divider(thickness=2, color=ft.colors.BLUE_GREY_200),
                        nombre_tarea,
                        ft.Row([fecha_entrega, prioridad], spacing=20),
                        descripcion,
                        asignatura,
                        ft.ElevatedButton("Añadir Tarea", icon=ft.icons.ADD, on_click=agregar_tarea),
                        resultado_text,
                    ], spacing=15),
                    col={"sm": 12, "md": 4},
                    padding=20,
                    bgcolor=ft.colors.WHITE,
                    border_radius=15,
                    shadow=ft.BoxShadow(color=ft.colors.BLACK12, blur_radius=8),
                ),
                ft.Container(
                    content=ft.Column([
                        ft.Text("Mis Tareas", size=24, weight="bold", color=ft.colors.BLUE_GREY_800),
                        ft.Divider(thickness=2, color=ft.colors.BLUE_GREY_200),
                        tareas_lista,
                    ], spacing=10),
                    col={"sm": 12, "md": 8},
                    padding=20,
                    bgcolor=ft.colors.WHITE,
                    border_radius=15,
                    shadow=ft.BoxShadow(color=ft.colors.BLACK12, blur_radius=8),
                    height=600,
                )
            ], spacing=20),
            ft.Row([
                ft.IconButton(icon=ft.icons.ARROW_BACK, tooltip="Volver al Dashboard", on_click=lambda _: page.go("/dashboard")),
                ft.TextButton("Volver al Dashboard", on_click=lambda _: page.go("/dashboard"))
            ], alignment=ft.MainAxisAlignment.START)
        ]
    )