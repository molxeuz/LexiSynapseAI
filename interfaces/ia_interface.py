import flet as ft
from controllers.asistente_controller import AsistenteIA


def main(page: ft.Page):
    # Configuración inicial de la página
    page.title = "Asistente DeepSeek"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 800
    page.window_height = 700
    page.padding = 20
    page.scroll = "auto"

    # Intentar inicializar la IA
    try:
        ai = AsistenteIA()
    except ValueError as e:
        page.add(ft.Text(f"Error: {str(e)}", color="red"))
        return

    # Elementos de la interfaz
    historial = []

    # Crear controles
    pregunta_field = ft.TextField(
        label="Tu pregunta",
        multiline=True,
        min_lines=3,
        max_lines=5,
        expand=True,
        hint_text="Escribe tu consulta aquí...",
        autofocus=True
    )

    contexto_field = ft.TextField(
        label="Contexto (opcional)",
        multiline=True,
        min_lines=2,
        max_lines=4,
        expand=True,
        hint_text="Contexto adicional para la consulta"
    )

    nivel_dropdown = ft.Dropdown(
        label="Nivel",
        options=[ft.dropdown.Option(o) for o in ["principiante", "intermedio", "avanzado"]],
        visible=False
    )

    idioma_dropdown = ft.Dropdown(
        label="Idioma",
        options=[ft.dropdown.Option(o) for o in ["español", "inglés", "francés", "alemán"]],
        value="español",
        visible=False
    )

    mode_switch = ft.Switch(label="Modo recomendación de documentos", value=False)

    respuesta_area = ft.Column(scroll="auto", expand=True)

    progress_bar = ft.ProgressBar(visible=False, width=400)

    historial_dialog = ft.AlertDialog(
        title=ft.Text("Historial"),
        content=ft.Column(scroll="auto", height=400),
        actions=[ft.TextButton("Cerrar", on_click=lambda e: cerrar_dialogo())]
    )

    # Funciones de eventos
    def toggle_mode(e):
        if mode_switch.value:
            nivel_dropdown.visible = True
            idioma_dropdown.visible = True
            contexto_field.visible = False
            pregunta_field.label = "Tema de estudio"
            pregunta_field.hint_text = "Ej: Inteligencia Artificial, Filosofía..."
        else:
            nivel_dropdown.visible = False
            idioma_dropdown.visible = False
            contexto_field.visible = True
            pregunta_field.label = "Tu pregunta"
            pregunta_field.hint_text = "Escribe tu consulta aquí..."
        page.update()

    def enviar_consulta(e):
        if not pregunta_field.value:
            mostrar_error("Por favor escribe una pregunta o tema")
            return

        progress_bar.visible = True
        enviar_btn.disabled = True
        respuesta_area.controls.append(ft.Text("Procesando...", italic=True))
        page.update()

        try:
            if mode_switch.value:
                respuesta = ai.recomendar_documentos(
                    pregunta_field.value,
                    nivel=nivel_dropdown.value,
                    idioma=idioma_dropdown.value
                )
            else:
                respuesta = ai.consultar_ia(
                    pregunta_field.value,
                    contexto=contexto_field.value
                )

            respuesta_area.controls.clear()
            respuesta_area.controls.append(ft.Text("Respuesta:", weight="bold"))
            respuesta_area.controls.append(ft.Text(respuesta, selectable=True))

            historial.append({
                "pregunta": pregunta_field.value,
                "respuesta": respuesta
            })

        except Exception as ex:
            mostrar_error(f"Error: {str(ex)}")
        finally:
            progress_bar.visible = False
            enviar_btn.disabled = False
            page.update()

    def mostrar_historial(e):
        historial_dialog.content.controls = [
            ft.Text(f"{i + 1}. {item['pregunta']}", weight="bold")
            for i, item in enumerate(historial)
        ]
        historial_dialog.open = True
        page.update()

    def cerrar_dialogo():
        historial_dialog.open = False
        page.update()

    def mostrar_error(mensaje):
        page.snack_bar = ft.SnackBar(
            ft.Text(mensaje, color="white"),
            bgcolor="red"
        )
        page.snack_bar.open = True
        page.update()

    # Configurar eventos
    mode_switch.on_change = toggle_mode
    enviar_btn = ft.ElevatedButton("Enviar", icon="send", on_click=enviar_consulta)

    # Diseño de la interfaz
    page.add(
        ft.Column([
            ft.Container(
                ft.Column([
                    ft.Row([
                        ft.Icon("rocket_launch", color="blue"),
                        ft.Text("DeepSeek AI", size=24, weight="bold")
                    ], alignment="center"),
                    ft.Text("Asistente de consultas inteligentes", italic=True, color="blue")
                ], horizontal_alignment="center"),
                padding=20
            ),
            mode_switch,
            ft.Divider(),
            pregunta_field,
            contexto_field,
            ft.Row([nivel_dropdown, idioma_dropdown]),
            ft.Row([
                enviar_btn,
                ft.IconButton("history", on_click=mostrar_historial)
            ], alignment="spaceBetween"),
            progress_bar,
            ft.Text("Respuesta:", weight="bold"),
            ft.Container(
                respuesta_area,
                border=ft.border.all(1),
                padding=10,
                expand=True
            )
        ], expand=True)
    )

    page.dialog = historial_dialog