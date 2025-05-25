"""
Listar recordatorios.
Formulario agregar/editar.
Botón eliminar.
Conexión con recordatorio_controller.py.
"""

# recordatorios_interface.py

import flet as ft

def recordatorios_view(page: ft.Page):
    page.title = "🎯 Tablero de Recordatorios"
    page.padding = 30
    page.bgcolor = ft.colors.BLUE_GREY_900
    page.scroll = "auto"

    notes = [
        "Estudiar para el examen de Python 🐍",
        "Revisar apuntes de lógica 💡",
        "Terminar proyecto final 🚀",
    ]

    grid = ft.GridView(
        expand=True,
        max_extent=240,
        horizontal=False,
        child_aspect_ratio=1,
        spacing=25,
        run_spacing=25,
    )

    def delete_note(note):
        grid.controls.remove(note)
        page.update()

    def create_note(text):
        note_content = ft.TextField(
            value=text,
            multiline=True,
            border_radius=10,
            bgcolor=ft.colors.BLUE_GREY_50,
            text_style=ft.TextStyle(size=14),
            border_color=ft.colors.BLUE_GREY_300,
            filled=True,
        )

        delete_button = ft.IconButton(
            icon=ft.icons.DELETE_OUTLINE,
            icon_color=ft.colors.RED_400,
            tooltip="Eliminar tarea",
            on_click=lambda _: delete_note(note)
        )

        note = ft.Container(
            content=ft.Column([
                ft.Text("📝 Recordatorio", weight="bold", size=16),
                note_content,
                delete_button,
            ], spacing=10),
            width=220,
            height=250,
            padding=15,
            bgcolor=ft.colors.AMBER_100,
            border_radius=20,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=8,
                color=ft.colors.BLACK26,
                offset=ft.Offset(2, 4)
            )
        )
        return note

    def add_note(e):
        new_note = create_note("Nueva Tarea ✏️")
        grid.controls.append(new_note)
        page.update()

    for note in notes:
        grid.controls.append(create_note(note))

    return ft.View(
        route="/recordatorios",
        controls=[
            ft.Row([
                ft.Text("📌 Mis Tareas Pendientes", size=28, weight="bold", color=ft.colors.WHITE),
                ft.IconButton(icon=ft.icons.ADD_CIRCLE_OUTLINE, on_click=add_note, icon_color=ft.colors.LIGHT_GREEN_300),
            ], alignment="spaceBetween"),
            ft.Divider(height=10, color=ft.colors.TRANSPARENT),
            grid
        ]
    )
