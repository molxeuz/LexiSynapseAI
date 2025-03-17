
import flet as ft

def academico_view(page: ft.Page):
    universidad_input = ft.TextField(label="Universidad")
    materias_input = ft.TextField(label="Materias (separadas por coma)")
    horarios_input = ft.TextField(label="Horarios (separados por coma)")
    resultado_text = ft.Text()

    def guardar_academico(e):
        if not universidad_input.value or not materias_input.value or not horarios_input.value:
            resultado_text.value = "Todos los campos son obligatorios."
            resultado_text.color = "red"
        else:
            resultado_text.value = "Registro académico completado. Ahora inicia sesión."
            resultado_text.color = "green"
            page.update()
            page.go("/login")
        page.update()

    return ft.View(
        "/academico",
        [
            ft.Text("Registro Académico", size=30, weight="bold"),
            universidad_input,
            materias_input,
            horarios_input,
            ft.ElevatedButton("Guardar", on_click=guardar_academico),
            resultado_text
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

"""
Formulario universidad, materias, horarios.
Validaciones.
Guardar con materia.py, horario.py.
Redirigir al login o dashboard.
"""