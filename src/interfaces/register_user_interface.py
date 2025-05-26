
import flet as ft


def registro_view(page: ft.Page):
    page.title = "Registro de Usuario"
    page.bgcolor = "#f0f4ff"

    # Inputs estilizados
    nombre_input = ft.TextField(label="Nombre completo", width=350, bgcolor="#f9fafb", border_radius=10, border_color="#e0e0e0")
    correo_input = ft.TextField(label="Correo electrónico", width=350, bgcolor="#f9fafb", border_radius=10, border_color="#e0e0e0")
    fecha_nacimiento_input = ft.TextField(label="Fecha de nacimiento (YYYY-MM-DD)", width=350, bgcolor="#f9fafb", border_radius=10, border_color="#e0e0e0")
    contraseña_input = ft.TextField(label="Contraseña", width=350, password=True, can_reveal_password=True, bgcolor="#f9fafb", border_radius=10, border_color="#e0e0e0")
    universidad_input = ft.TextField(label="Universidad", width=350, bgcolor="#f9fafb", border_radius=10, border_color="#e0e0e0")
    carrera_input = ft.TextField(label="Carrera", width=350, bgcolor="#f9fafb", border_radius=10, border_color="#e0e0e0")
    semestre_input = ft.TextField(label="Semestre", width=350, bgcolor="#f9fafb", border_radius=10, border_color="#e0e0e0")

    resultado_text = ft.Text(size=14)

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
            resultado_text.color = "#c62828"
            page.update()
            return

        # Redirigir con datos en la URL
        page.go(
            f"/academico?nombre={nombre}&correo={correo}&fecha_nacimiento={fecha_nacimiento}&contraseña={contraseña}"
            f"&universidad={universidad}&carrera={carrera}&semestre={semestre}"
        )

    return ft.View(
        "/register",
        controls=[
            ft.Container(
                padding=30,
                width=450,
                content=ft.Column(
                    controls=[
                        ft.Text("Registro de Usuario", size=30, weight="bold", color="#1565c0"),
                        ft.Text("Crea tu cuenta para continuar", size=16, color="#757575"),
                        ft.Divider(height=20, color="transparent"),
                        nombre_input,
                        correo_input,
                        fecha_nacimiento_input,
                        contraseña_input,
                        universidad_input,
                        carrera_input,
                        semestre_input,
                        ft.Divider(height=10, color="transparent"),
                        ft.ElevatedButton("Siguiente", on_click=ir_a_academico, style=ft.ButtonStyle(
                            bgcolor="#1976d2", color="white", shape=ft.RoundedRectangleBorder(radius=10),
                            padding=ft.padding.symmetric(horizontal=20, vertical=14)
                        )),
                        resultado_text
                    ],
                    width=400,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    scroll=ft.ScrollMode.AUTO
                ),
                alignment=ft.alignment.center,
                bgcolor="#ffffff",
                border_radius=15,
                shadow=ft.BoxShadow(blur_radius=20, color="#e0e0e0", offset=ft.Offset(0, 4)),
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

"""
Formularios: nombre, correo, fecha nacimiento, contraseña.
Validación de datos.
Conectar a usuario_controller.py para registrar.
Redirigir al registro académico.
"""