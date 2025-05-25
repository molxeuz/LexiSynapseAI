# views/tareas_view.py

import flet as ft
from controllers.tarea_controller import tarea_controller

def tareas_view(page: ft.Page):
    page.title = "Gestión de Tareas"

    # ----- Formulario de creación de tareas -----
    nombre_tarea = ft.TextField(label="Nombre de la tarea", width=300)
    fecha_entrega = ft.TextField(label="Fecha de entrega (dd/mm/aa)", width=300)
    prioridad_tarea = ft.Dropdown(
        label="Prioridad",
        width=300,
        options=[
            ft.dropdown.Option("Alta"),
            ft.dropdown.Option("Media"),
            ft.dropdown.Option("Baja"),
        ]
    )
    descripcion_tarea = ft.TextField(label="Descripción", multiline=True, min_lines=2, max_lines=4, width=300)
    asignatura_tarea = ft.TextField(label="Asignatura o categoría", width=300)
    resultado_text = ft.Text()

    # ----- Lista de tareas -----
    tareas_lista = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)

    def get_color_por_prioridad(prioridad):
        if prioridad == "Alta":
            return ft.colors.RED_600
        elif prioridad == "Media":
            return ft.colors.AMBER_700
        else:
            return ft.colors.GREEN_600

    def renderizar_tareas():
        tareas_lista.controls.clear()
        for tarea in tarea_controller.obtener_tareas():
            tarea_item = ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Checkbox(value=tarea.completada, on_change=lambda e, t=tarea: [t.marcar_completada(), page.update()]),
                            ft.Text(tarea.nombre, weight=ft.FontWeight.BOLD, size=18),
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        ft.Text(f"Entrega: {tarea.fecha_entrega}", color=ft.colors.GREY_600),
                        ft.Text(f"Prioridad: {tarea.prioridad}", color=get_color_por_prioridad(tarea.prioridad)),
                        ft.Text(f"Asignatura: {tarea.asignatura}", italic=True),
                        ft.Text(f"Descripción: {tarea.descripcion}", size=13),
                    ]),
                    padding=10,
                )
            )
            tareas_lista.controls.append(tarea_item)
        page.update()

    def agregar_tarea(e):
        exito, mensaje = tarea_controller.agregar_tarea(
            nombre_tarea.value,
            fecha_entrega.value,
            prioridad_tarea.value,
            descripcion_tarea.value,
            asignatura_tarea.value
        )

        resultado_text.value = mensaje
        resultado_text.color = "green" if exito else "red"

        if exito:
            nombre_tarea.value = ""
            fecha_entrega.value = ""
            prioridad_tarea.value = None
            descripcion_tarea.value = ""
            asignatura_tarea.value = ""

        renderizar_tareas()

    renderizar_tareas()

    # ----- Layout en columnas (izquierda y derecha) -----
    formulario = ft.Column([
        ft.Text("Agregar nueva tarea", size=20, weight="bold"),
        nombre_tarea,
        fecha_entrega,
        prioridad_tarea,
        descripcion_tarea,
        asignatura_tarea,
        ft.ElevatedButton("Añadir Tarea", on_click=agregar_tarea),
        resultado_text,
    ], spacing=10)

    contenido = ft.Row(
        controls=[
            ft.Container(formulario, width=350, padding=10),
            ft.VerticalDivider(width=1),
            ft.Container(
                content=ft.Column([
                    ft.Text("Lista de tareas", size=20, weight="bold"),
                    tareas_lista
                ]),
                expand=True,
                padding=10
            )
        ],
        expand=True
    )

    return ft.View(
        route="/tareas",
        controls=[
            ft.Text("Mis Tareas", size=30, weight="bold"),
            ft.Text("Agrega tus tareas académicas importantes", size=16, italic=True, color=ft.colors.GREY_600),
            contenido,
            ft.TextButton("Volver al Dashboard", on_click=lambda _: page.go("/dashboard"))
        ],
        vertical_alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        spacing=20,
        padding=20
    )
