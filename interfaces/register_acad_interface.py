
import flet as ft
from controllers.usuario_controller import Usuario, Academico

def academico_view(page):
    params = page.route.split("?")
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

            if not nombre or not hora_inicio or not hora_fin:
                resultado_text.value = "Todos los campos de cada materia son obligatorios."
                resultado_text.color = "red"
                page.update()
                return

            materias.append({"nombre": nombre, "hora_inicio": hora_inicio, "hora_fin": hora_fin})

        if not universidad or not materias:
            resultado_text.value = "Debe ingresar la universidad y al menos una materia con horarios."
            resultado_text.color = "red"
            page.update()
            return

        nombre = usuario_data.get("nombre", "").strip()
        correo = usuario_data.get("correo", "").strip()
        fecha_nacimiento = usuario_data.get("fecha_nacimiento", "").strip()
        contraseña = usuario_data.get("contraseña", "").strip()

        if not nombre or not correo or not fecha_nacimiento or not contraseña:
            resultado_text.value = "Error: Datos de usuario incompletos."
            resultado_text.color = "red"
            page.update()
            return

        mensaje_usuario, exito_usuario, usuario_id = Usuario.registrar(nombre, correo, fecha_nacimiento, contraseña)

        if not exito_usuario:
            resultado_text.value = mensaje_usuario
            resultado_text.color = "red"
            page.update()
            return

        mensaje_academico, exito_academico = Academico.registrar(usuario_id, universidad, materias)

        resultado_text.value = mensaje_academico
        resultado_text.color = "green" if exito_academico else "red"

        if exito_academico:
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

"""
Formulario universidad, materias, horarios.
Validaciones.
Guardar con materia.py, horario.py.
Redirigir al login o dashboard.
"""