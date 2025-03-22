
import flet as ft
from controllers.usuario_controller import registrar_usuario, registrar_academico

def academico_view(page):
    params = page.route.split("?")
    usuario_id = None
    usuario_data = {}

    if len(params) > 1:
        query = params[1]
        for p in query.split("&"):
            key, value = p.split("=")
            usuario_data[key] = value

    universidad_input = ft.TextField(label="Universidad")
    resultado_text = ft.Text()
    materias_inputs = []
    materias_container = ft.Column()

    def agregar_materia(e):
        if len(materias_inputs) >= 10:
            resultado_text.value = "No puedes agregar más de 10 materias."
            resultado_text.color = "red"
            page.update()
            return

        nombre_materia = ft.TextField(label="Nombre de la materia")
        hora_inicio = ft.TextField(label="Hora de inicio (HH:MM)")
        hora_fin = ft.TextField(label="Hora de fin (HH:MM)")

        materias_inputs.append({"nombre": nombre_materia, "hora_inicio": hora_inicio, "hora_fin": hora_fin})
        materias_container.controls.append(ft.Row([nombre_materia, hora_inicio, hora_fin]))

        page.update()

    def guardar_academico(e):
        universidad = universidad_input.value.strip()
        materias = []

        for materia in materias_inputs:
            nombre = materia["nombre"].value.strip()
            hora_inicio = materia["hora_inicio"].value.strip()
            hora_fin = materia["hora_fin"].value.strip()

            if nombre and hora_inicio and hora_fin:
                materias.append({"nombre": nombre, "hora_inicio": hora_inicio, "hora_fin": hora_fin})

        if not universidad or not materias:
            resultado_text.value = "Debe ingresar la universidad y al menos una materia con horarios."
            resultado_text.color = "red"
            page.update()
            return

        # Primero registramos al usuario
        mensaje, exito, usuario_id = registrar_usuario(
            usuario_data.get("nombre"),
            usuario_data.get("correo"),
            usuario_data.get("fecha_nacimiento"),
            usuario_data.get("contraseña")
        )

        if not exito:
            resultado_text.value = mensaje
            resultado_text.color = "red"
            page.update()
            return

        # Luego registramos el académico
        mensaje, exito = registrar_academico(usuario_id, universidad, materias)

        resultado_text.value = mensaje
        resultado_text.color = "green" if exito else "red"

        if exito:
            page.go("/login")

        page.update()

    return ft.View(
        "/academico",
        [
            ft.Text("Registro Académico", size=30, weight="bold"),
            universidad_input,
            ft.ElevatedButton("Agregar Materia", on_click=agregar_materia),
            materias_container,
            ft.ElevatedButton("Guardar", on_click=guardar_academico),
            resultado_text
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
