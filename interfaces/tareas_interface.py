
import flet as ft

def tareas_view(page: ft.Page):
    page.title = "Gestión de Tareas"

    titulo = ft.Text("Mis Tareas", size=30, weight="bold")
    descripcion = ft.Text("Agrega tus tareas académicas importantes", size=16, italic=True, color=ft.colors.GREY_600)

    nombre_tarea = ft.TextField(label="Nombre de la tarea", width=300)
    fecha_entrega = ft.TextField(label="Fecha de entrega (dd/mm/aa)", width=300)
    resultado_text = ft.Text()

    tareas_lista = ft.Column(scroll=ft.ScrollMode.AUTO)

    def agregar_tarea(e):
        if not nombre_tarea.value or not fecha_entrega.value:
            resultado_text.value = "Por favor completa todos los campos"
            resultado_text.color = "red"
        else:
            tarea_item = ft.Row(
                controls=[
                    ft.Checkbox(),
                    ft.Text(nombre_tarea.value, weight=ft.FontWeight.BOLD),
                    ft.Text(f"Entrega: {fecha_entrega.value}", color=ft.colors.GREY_600)
                ],
                spacing=15
            )
            tareas_lista.controls.append(tarea_item)
            nombre_tarea.value = ""
            fecha_entrega.value = ""
            resultado_text.value = "Tarea añadida correctamente"
            resultado_text.color = "green"
        page.update()

    return ft.View(
        route="/tareas",
        controls=[
            titulo,
            descripcion,
            nombre_tarea,
            fecha_entrega,
            ft.ElevatedButton("Añadir Tarea", on_click=agregar_tarea),
            resultado_text,
            ft.Divider(height=20),
            tareas_lista,
            ft.TextButton("Volver al Dashboard", on_click=lambda _: page.go("/dashboard"))
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
        padding=20
    )


"""
Listar tareas.
Formulario agregar/editar.
Botones eliminar.
Conexión con tarea_controller.py.
"""