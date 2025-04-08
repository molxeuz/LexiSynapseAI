
import flet as ft
from controllers.usuario_controller import Usuario

def academico_view(page):
    parametros = page.route.split("?")
    usuario_data = {}

    if len(parametros) > 1:
        params = dict(p.split("=") for p in parametros[1].split("&"))
        usuario_data["nombre"] = params.get("nombre", "").replace("%20", " ")
        usuario_data["correo"] = params.get("correo", "")
        usuario_data["fecha_nacimiento"] = params.get("fecha_nacimiento", "")
        usuario_data["contraseña"] = params.get("contraseña", "")
        usuario_data["universidad"] = params.get("universidad", "")
        usuario_data["carrera"] = params.get("carrera", "")
        usuario_data["semestre"] = params.get("semestre", "")

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
        materias = [
            {
                "nombre": card.content.controls[1].value.strip(),
                "dia": card.content.controls[2].value,
                "hora_inicio": card.content.controls[3].value.strip(),
                "hora_fin": card.content.controls[4].value.strip()
            }
            for card in materias_inputs if card.content.controls[1].value.strip()
        ]

        actividades = [
            {
                "nombre": card.content.controls[1].value.strip(),
                "dia": card.content.controls[2].value,
                "hora_inicio": card.content.controls[3].value.strip(),
                "hora_fin": card.content.controls[4].value.strip()
            }
            for card in actividades_inputs if card.content.controls[1].value.strip()
        ]

        mensaje, exito, usuario_id = Usuario.registrar(
            usuario_data["nombre"],
            usuario_data["correo"],
            usuario_data["fecha_nacimiento"],
            usuario_data["contraseña"],
            usuario_data["universidad"],
            usuario_data["carrera"],
            usuario_data["semestre"]
        )

        if not exito:
            resultado_text.value = mensaje
            resultado_text.color = "red"
            page.update()
            return

        mensaje_academico, exito_academico = Usuario.registrar_datos_academicos(usuario_id, materias, actividades)

        if not exito_academico:
            resultado_text.value = mensaje_academico
            resultado_text.color = "red"
        else:
            resultado_text.value = "Registro académico exitoso. Redirigiendo..."
            resultado_text.color = "green"
            page.go("/login")

        page.update()

    return ft.View(
        "/academico",
        controls=[
            ft.Container(
                expand=True,
                content=ft.Column(
                    controls=[
                        ft.Text("Registro Académico", size=30, weight="bold"),
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
                    scroll=ft.ScrollMode.ALWAYS
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