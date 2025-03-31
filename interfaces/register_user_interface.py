import flet as ft
from controllers.usuario_controller import Usuario

def registro_view(page: ft.Page):
    nombre_input = ft.TextField(label="Nombre")
    correo_input = ft.TextField(label="Correo")
    fecha_nacimiento_input = ft.TextField(label="Fecha de Nacimiento (YYYY-MM-DD)")
    contraseña_input = ft.TextField(label="Contraseña", password=True, can_reveal_password=True)
    universidad_input = ft.TextField(label="Universidad")
    carrera_input = ft.TextField(label="Carrera")
    semestre_input = ft.TextField(label="Semestre")
    resultado_text = ft.Text()

    def ir_a_academico(e):
        nombre = nombre_input.value.strip()
        correo = correo_input.value.strip()
        fecha_nacimiento = fecha_nacimiento_input.value.strip()
        contraseña = contraseña_input.value.strip()
        universidad = universidad_input.value.strip()
        carrera = carrera_input.value.strip()
        semestre = semestre_input.value.strip()

        if not all([nombre, correo, fecha_nacimiento, contraseña, universidad, carrera, semestre]):
            resultado_text.value = "Todos los campos son obligatorios."
            resultado_text.color = "red"
            page.update()
            return

        page.go(f"/academico?nombre={nombre}&correo={correo}&fecha_nacimiento={fecha_nacimiento}&contraseña={contraseña}&universidad={universidad}&carrera={carrera}&semestre={semestre}")

    return ft.View(
        "/register",
        controls=[
            ft.Text("Registro de Usuario", size=30, weight="bold"),
            nombre_input,
            correo_input,
            fecha_nacimiento_input,
            contraseña_input,
            universidad_input,
            carrera_input,
            semestre_input,
            ft.ElevatedButton("Siguiente", on_click=ir_a_academico),
            resultado_text
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

"""
Formularios: nombre, correo, fecha nacimiento, contraseña.
Validación de datos.
Conectar a usuario_controller.py para registrar.
Redirigir al registro académico.
"""