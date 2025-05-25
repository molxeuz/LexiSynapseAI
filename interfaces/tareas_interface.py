import flet as ft
from controllers.tarea_controller import TareaController
from datetime import datetime

PRIORIDAD_ORDEN = {"Alta": 0, "Media": 1, "Baja": 2}
PRIORIDAD_COLOR = {
    "Alta": ft.colors.RED_200,
    "Media": ft.colors.ORANGE_200,
    "Baja": ft.colors.GREEN_200,
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

    # Campos para agregar tarea
    titulo = ft.Text("Agregar Nueva Tarea", size=24, weight="bold")
    nombre_tarea = ft.TextField(label="Nombre de la tarea", width=350)
    fecha_entrega = ft.TextField(label="Fecha de entrega (dd/mm/aa)", width=150)
    prioridad = ft.Dropdown(
        label="Prioridad",
        options=[
            ft.dropdown.Option("Alta"),
            ft.dropdown.Option("Media"),
            ft.dropdown.Option("Baja")
        ],
        width=150
    )
    descripcion = ft.TextField(label="Descripción", multiline=True, max_lines=3, width=350)
    asignatura = ft.TextField(label="Asignatura", width=200)
    resultado_text = ft.Text()

    tareas_lista = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True, spacing=12)

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

        for tarea in tareas_ordenadas:
            color = PRIORIDAD_COLOR.get(tarea.prioridad, ft.colors.GREY_300)
            tarjeta = ft.Card(
                content=ft.Container(
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
                                border_radius=10,
                            )
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        ft.Row([
                            ft.Text(f"Entrega: {format_fecha(tarea.fecha_entrega)}", color=ft.colors.GREY_700),
                            ft.Text(f"Asignatura: {tarea.asignatura}", color=ft.colors.GREY_700)
                        ], spacing=20),
                        ft.Divider(),
                        ft.Text(tarea.descripcion, size=13, italic=True, color=ft.colors.GREY_600, no_wrap=False)
                    ]),
                    padding=15,
                    border_radius=10,
                    bgcolor=ft.colors.WHITE,
                    shadow=ft.BoxShadow(color=ft.colors.BLACK26, blur_radius=5, offset=ft.Offset(2, 2)),
                ),
                elevation=0
            )
            tareas_lista.controls.append(tarjeta)

    def agregar_tarea(e):
        if not nombre_tarea.value or not fecha_entrega.value or not prioridad.value:
            resultado_text.value = "Por favor completa Nombre, Fecha y Prioridad"
            resultado_text.color = "red"
            page.update()
            return

        # Validar formato de fecha ingresada
        try:
            datetime.strptime(fecha_entrega.value.strip(), "%d/%m/%y")
        except ValueError:
            resultado_text.value = "La fecha debe tener el formato dd/mm/aa"
            resultado_text.color = "red"
            page.update()
            return

        fecha_str = fecha_entrega.value.strip()
        exito, mensaje = controller.agregar_tarea(
            nombre_tarea.value.strip(),
            fecha_str,
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
        controls=[
            ft.Row([
                ft.Container(
                    content=ft.Column([
                        titulo,
                        nombre_tarea,
                        ft.Row([
                            fecha_entrega,
                            prioridad
                        ], spacing=20),
                        descripcion,
                        asignatura,
                        ft.ElevatedButton("Añadir Tarea", on_click=agregar_tarea),
                        resultado_text,
                    ], spacing=15),
                    width=420,
                    padding=20
                ),
                ft.VerticalDivider(width=1),
                ft.Container(
                    content=ft.Column([
                        ft.Text("Mis Tareas", size=24, weight="bold"),
                        tareas_lista,
                    ], spacing=10),
                    expand=True,
                    padding=20
                )
            ]),
            ft.TextButton("Volver al Dashboard", on_click=lambda _: page.go("/dashboard"))
        ],
        padding=20,
        bgcolor=ft.colors.GREY_50
    )
