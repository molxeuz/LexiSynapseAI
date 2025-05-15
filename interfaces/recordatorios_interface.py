"""
Listar recordatorios.
Formulario agregar/editar.
Botón eliminar.
Conexión con recordatorio_controller.py.
"""

#recordatorios, tareas etc

import flet as ft

def main(page:ft.Page):
    page.tittle = "tablero de Recordatorios"
    page.padding = 20
    page.bgcolor = ft.colors.BLACK
    note = ft.TextField(value = "mi primera nota", multiline =True)

    def add_note(e):
        new_note = create_note("Nueva Tarea")
        grid.controls.append(new_note)
        page.update()


    def delete_note(note):
        grid.controls.remove(note)
        page.update()



    def create_note (text):
       note_content=ft.TextField(value=text,multiline=True,
                                 bgcolor=ft.colors.GREY)
       note=ft.Container(
           content=ft.Column([note_content,ft.IconButton(icon=ft.icons.DELETE,
                                                         on_click=lambda _: delete_note(note))]),
           width=200,
           height=200,
           bgcolor=ft.colors.WHITE,
           border_radius=10,
           padding=10,
       )
       return note
    grid = ft.GridView(
        expand = True,
        max_extent=220,
        horizontal = False,
        child_aspect_ratio=1,
        spacing=20,
        run_spacing=20
    )

    notes=[
        "Nueva Tarea",
        "Nueva Tarea",
        "Nueva Tarea",
    ]
    for note in notes:
        grid.controls.append(create_note(note))
    page.add(
        ft.Row([
            ft.Text("Mis Tareas Pendientes", size=30, weight="bold",
                    color=ft.colors.WHITE),
            ft.IconButton(icon=ft.icons.ADD , on_click = add_note , icon_color = ft.colors.WHITE)
            ]),grid

    )


ft.app(target=main)

