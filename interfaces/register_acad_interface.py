
import flet as ft
from controllers.usuario_controller import registrar_academico

def academico_view(page: ft.Page):
    # ✅ Leer el usuario_id desde la URL
    params = page.route.split("?")
    usuario_id = None
    if len(params) > 1:
        query = params[1]
        for p in query.split("&"):
            if p.startswith("usuario_id="):
                usuario_id = p.split("=")[1]
                if usuario_id.isdigit():
                    usuario_id = int(usuario_id)
                else:
                    usuario_id = None

    print("Usuario ID recibido:", usuario_id)  # ⚙️ Verificación temporal

    universidad_input = ft.TextField(label="Universidad")
    materias_input = ft.TextField(label="Materias (separadas por coma)")
    horarios_input = ft.TextField(label="Horarios (separados por coma)")
    resultado_text = ft.Text()

    def guardar_academico(e):
        if not usuario_id:
            resultado_text.value = "Error: Usuario no identificado."
            resultado_text.color = "red"
            page.update()
            return

        universidad = universidad_input.value.strip()
        materias = materias_input.value.strip()
        horarios = horarios_input.value.strip()

        if not universidad or not materias or not horarios:
            resultado_text.value = "Todos los campos son obligatorios."
            resultado_text.color = "red"
        else:
            mensaje, exito = registrar_academico(usuario_id, universidad, materias, horarios)
            resultado_text.value = mensaje
            resultado_text.color = "green" if exito else "red"
            if exito:
                page.go("/login")  # O la ruta que prefieras

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