import flet as ft
from src.controllers.usuario_controller import Usuario


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

    def crear_materia_card(idx=None):
        nombre_materia = ft.TextField(label="Nombre de la materia")
        dia_materia = ft.Dropdown(label="Día de la semana", options=dias_semana)
        hora_inicio = ft.TextField(label="Hora de inicio (HH:MM)")
        hora_fin = ft.TextField(label="Hora de fin (HH:MM)")

        def eliminar_materia(e):
            materias_inputs.remove(materia_card)
            materias_container.controls.remove(materia_card)
            page.update()

        materia_card = ft.Container(
            padding=10,
            margin=ft.margin.only(bottom=15),
            border=ft.border.all(1, ft.colors.BLUE_GREY),
            border_radius=8,
            content=ft.Column([
                ft.Text(f"Materia {idx if idx else len(materias_inputs) + 1}", weight="bold", size=16),
                nombre_materia,
                dia_materia,
                hora_inicio,
                hora_fin,
                ft.ElevatedButton("Eliminar", on_click=eliminar_materia,
                                  style=ft.ButtonStyle(bgcolor=ft.colors.RED_400))
            ])
        )
        return materia_card

    def crear_actividad_card(idx=None):
        nombre_actividad = ft.TextField(label="Nombre de la actividad")
        dia_actividad = ft.Dropdown(label="Día de la semana", options=dias_semana)
        hora_inicio = ft.TextField(label="Hora de inicio (HH:MM)")
        hora_fin = ft.TextField(label="Hora de fin (HH:MM)")

        def eliminar_actividad(e):
            actividades_inputs.remove(actividad_card)
            actividades_container.controls.remove(actividad_card)
            page.update()

        actividad_card = ft.Container(
            padding=10,
            margin=ft.margin.only(bottom=15),
            border=ft.border.all(1, ft.colors.BLUE_GREY),
            border_radius=8,
            content=ft.Column([
                ft.Text(f"Actividad {idx if idx else len(actividades_inputs) + 1}", weight="bold", size=16),
                nombre_actividad,
                dia_actividad,
                hora_inicio,
                hora_fin,
                ft.ElevatedButton("Eliminar", on_click=eliminar_actividad,
                                  style=ft.ButtonStyle(bgcolor=ft.colors.RED_400))
            ])
        )
        return actividad_card

    def agregar_materia(e=None):
        materia_card = crear_materia_card()
        materias_inputs.append(materia_card)
        materias_container.controls.append(materia_card)
        page.update()

    def agregar_actividad(e=None):
        actividad_card = crear_actividad_card()
        actividades_inputs.append(actividad_card)
        actividades_container.controls.append(actividad_card)
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

        mensaje, exito, usuario_id = Usuario.registrar_usuario(
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

        mensaje_academico, exito_academico = Usuario.registrar_academico(usuario_id, materias, actividades)

        if not exito_academico:
            resultado_text.value = mensaje_academico
            resultado_text.color = "red"
        else:
            resultado_text.value = "Registro académico exitoso. Redirigiendo..."
            resultado_text.color = "green"
            page.go("/login")

        page.update()

    # Aquí se agregan 1 materia y 1 actividad desde el inicio
    agregar_materia()
    agregar_actividad()

    return ft.View(
        "/academico",
        controls=[
            ft.Container(
                padding=30,
                alignment=ft.alignment.center,
                content=ft.Column(
                    spacing=30,
                    scroll=ft.ScrollMode.AUTO,
                    controls=[
                        ft.Text("Registro Académico", size=28, weight="bold", text_align="center"),

                        ft.Row(
                            spacing=30,
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.START,
                            controls=[
                                ft.Container(
                                    expand=1,
                                    alignment=ft.alignment.top_center,
                                    content=ft.Column([
                                        ft.Text("Materias", size=22, weight="bold"),
                                        ft.ElevatedButton("Agregar Materia", on_click=agregar_materia),
                                        materias_container
                                    ])
                                ),
                                ft.VerticalDivider(width=30),
                                ft.Container(
                                    expand=1,
                                    alignment=ft.alignment.top_center,
                                    content=ft.Column([
                                        ft.Text("Actividades Extracurriculares", size=22, weight="bold"),
                                        ft.ElevatedButton("Agregar Actividad", on_click=agregar_actividad),
                                        actividades_container
                                    ])
                                )
                            ]
                        ),

                        ft.ElevatedButton(
                            "Guardar Registro Académico",
                            on_click=guardar_academico,
                            style=ft.ButtonStyle(bgcolor=ft.colors.BLUE, color=ft.colors.WHITE)
                        ),

                        resultado_text
                    ]
                )
            )
        ]
    )
