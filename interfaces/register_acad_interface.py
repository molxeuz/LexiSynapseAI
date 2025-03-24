
import flet as ft
from controllers.usuario_controller import Usuario, Academico

def academico_view(page):
    # Capturar los datos del usuario desde la URL
    parametros = page.route.split("?")
    usuario_data = {}

    if len(parametros) > 1:
        params = dict(p.split("=") for p in parametros[1].split("&"))
        usuario_data["nombre"] = params.get("nombre", "").replace("%20", " ")
        usuario_data["correo"] = params.get("correo", "")
        usuario_data["fecha_nacimiento"] = params.get("fecha_nacimiento", "")
        usuario_data["contraseña"] = params.get("contraseña", "")

    universidad_input = ft.TextField(label="Universidad")
    carrera_input = ft.TextField(label="Carrera")
    semestre_input = ft.TextField(label="Semestre")

    resultado_text = ft.Text()
    materias_inputs = []
    actividades_inputs = []
    materias_container = ft.Column()
    actividades_container = ft.Column()

    dias_semana = [
        ft.dropdown.Option("Lunes"),
        ft.dropdown.Option("Martes"),
        ft.dropdown.Option("Miércoles"),
        ft.dropdown.Option("Jueves"),
        ft.dropdown.Option("Viernes"),
        ft.dropdown.Option("Sábado")
    ]

    def agregar_materia(e):
        nombre_materia = ft.TextField(label="Nombre de la materia")
        dia_materia = ft.Dropdown(label="Día de la semana", options=dias_semana)
        hora_inicio = ft.TextField(label="Hora de inicio (HH:MM)")
        hora_fin = ft.TextField(label="Hora de fin (HH:MM)")

        materia_card = ft.Container(
            content=ft.Column([
                ft.Text(f"Materia {len(materias_inputs) + 1}", weight="bold"),
                nombre_materia,
                dia_materia,
                hora_inicio,
                hora_fin,
                ft.ElevatedButton("Eliminar", on_click=lambda e: eliminar_materia(materia_card))
            ])
        )

        materias_inputs.append(materia_card)
        materias_container.controls.append(materia_card)
        page.update()

    def eliminar_materia(card):
        materias_inputs.remove(card)
        materias_container.controls.remove(card)
        page.update()

    def agregar_actividad(e):
        nombre_actividad = ft.TextField(label="Nombre de la actividad")
        dia_actividad = ft.Dropdown(label="Día de la semana", options=dias_semana)
        hora_inicio = ft.TextField(label="Hora de inicio (HH:MM)")
        hora_fin = ft.TextField(label="Hora de fin (HH:MM)")

        actividad_card = ft.Container(
            content=ft.Column([
                ft.Text(f"Actividad {len(actividades_inputs) + 1}", weight="bold"),
                nombre_actividad,
                dia_actividad,
                hora_inicio,
                hora_fin,
                ft.ElevatedButton("Eliminar", on_click=lambda e: eliminar_actividad(actividad_card))
            ])
        )

        actividades_inputs.append(actividad_card)
        actividades_container.controls.append(actividad_card)
        page.update()

    def eliminar_actividad(card):
        actividades_inputs.remove(card)
        actividades_container.controls.remove(card)
        page.update()

    def guardar_academico(e):
        universidad = universidad_input.value.strip()
        carrera = carrera_input.value.strip()
        semestre = semestre_input.value.strip()

        if not universidad or not carrera or not semestre:
            resultado_text.value = "Debe ingresar la universidad, la carrera y el semestre."
            resultado_text.color = "red"
            page.update()
            return

        if not materias_inputs:
            resultado_text.value = "Debe ingresar al menos una materia."
            resultado_text.color = "red"
            page.update()
            return

        if not actividades_inputs:
            resultado_text.value = "Debe ingresar al menos una actividad."
            resultado_text.color = "red"
            page.update()
            return

        # Registrar usuario con los datos obtenidos de la URL
        mensaje, exito, usuario_id = Usuario.registrar(
            usuario_data["nombre"],
            usuario_data["correo"],
            usuario_data["fecha_nacimiento"],
            usuario_data["contraseña"]
        )

        if not exito:
            resultado_text.value = mensaje
            resultado_text.color = "red"
            page.update()
            return

        # Obtener materias y actividades
        materias = [
            {
                "nombre": card.content.controls[1].value,
                "dia": card.content.controls[2].value,
                "hora_inicio": card.content.controls[3].value,
                "hora_fin": card.content.controls[4].value
            }
            for card in materias_inputs
        ]

        actividades = [
            {
                "nombre": card.content.controls[1].value,
                "dia": card.content.controls[2].value,
                "hora_inicio": card.content.controls[3].value,
                "hora_fin": card.content.controls[4].value
            }
            for card in actividades_inputs
        ]

        # Registrar datos académicos con el usuario correcto
        mensaje, exito = Academico.registrar(usuario_id, universidad, carrera, semestre, materias, actividades)

        resultado_text.value = mensaje
        resultado_text.color = "green" if exito else "red"
        page.update()

    return ft.View(
        "/academico",
        controls=[
            ft.Container(
                expand=True,
                content=ft.Column(
                    controls=[
                        ft.Text("Registro Académico", size=30, weight="bold"),
                        universidad_input,
                        carrera_input,
                        semestre_input,
                        ft.Row([
                            ft.Column([
                                ft.Text("Materias", size=20, weight="bold"),
                                ft.ElevatedButton("Agregar Materia", on_click=agregar_materia),
                                materias_container
                            ]),
                            ft.VerticalDivider(),
                            ft.Column([
                                ft.Text("Actividades Extracurriculares", size=20, weight="bold"),
                                ft.ElevatedButton("Agregar Actividad", on_click=agregar_actividad),
                                actividades_container
                            ])
                        ]),
                        ft.ElevatedButton("Guardar", on_click=guardar_academico),
                        resultado_text
                    ],
                    scroll=ft.ScrollMode.ALWAYS  # HABILITA EL SCROLL
                )
            )
        ]
    )

"""
Formulario universidad, materias, horarios.
Validaciones.
Guardar con materia.py, horario.py.
Redirigir al login o dashboard.
"""