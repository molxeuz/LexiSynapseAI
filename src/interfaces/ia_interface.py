import flet as ft
from src.controllers.asistente_controller import AsistenteIA

asistente = AsistenteIA()

def ia_view(page: ft.Page):
    # Configuración de tema
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.BLUE_800,
            secondary=ft.colors.CYAN_600,
            surface=ft.colors.WHITE,
        ),
    )

    # Campo para consultar_ia
    pregunta_input = ft.TextField(
        label="Ingrese su pregunta",
        multiline=True,
        min_lines=3,
        max_lines=5,
        expand=True,
        border_color=ft.colors.BLUE_GREY_300,
        filled=True,
        fill_color=ft.colors.GREY_50,
        hint_text="Escriba aquí su pregunta para la IA...",
    )

    # Campos para recomendar_documentos
    tema_input = ft.TextField(
        label="Tema de interés",
        expand=True,
        border_color=ft.colors.BLUE_GREY_300,
        filled=True,
        fill_color=ft.colors.GREY_50,
        hint_text="Ej: Machine Learning, Python avanzado...",
    )

    nivel_dropdown = ft.Dropdown(
        label="Nivel de conocimiento",
        options=[
            ft.dropdown.Option("Cualquiera"),
            ft.dropdown.Option("Principiante"),
            ft.dropdown.Option("Intermedio"),
            ft.dropdown.Option("Avanzado"),
        ],
        value="Cualquiera",
        border_color=ft.colors.BLUE_GREY_300,
        filled=True,
        fill_color=ft.colors.GREY_50,
    )

    idioma_dropdown = ft.Dropdown(
        label="Idioma preferido",
        options=[
            ft.dropdown.Option("español"),
            ft.dropdown.Option("inglés"),
            ft.dropdown.Option("francés"),
        ],
        value="español",
        border_color=ft.colors.BLUE_GREY_300,
        filled=True,
        fill_color=ft.colors.GREY_50,
    )

    # Indicador de procesamiento
    processing_indicator = ft.Row(
        [
            ft.ProgressRing(width=20, height=20, stroke_width=2, visible=False),
            ft.Text("Procesando tu pregunta...", visible=False),
        ],
        spacing=10,
        visible=False,
    )

    # Resultados con scroll y mejor visualización
    respuesta_output = ft.Column(
        [
            ft.Text("Respuesta:", size=16, weight="bold", color=ft.colors.BLUE_800),
            ft.Container(
                content=ft.Column(
                    [
                        ft.Markdown(
                            "Aquí aparecerá la respuesta generada por la IA...",
                            selectable=True,
                            extension_set="gitHubWeb",
                        )
                    ],
                    scroll=ft.ScrollMode.AUTO,
                ),
                padding=15,
                border_radius=10,
                bgcolor=ft.colors.GREY_50,
                border=ft.border.all(1, ft.colors.BLUE_GREY_200),
                expand=True,
            ),
        ],
        spacing=10,
        expand=True,
    )

    # Botones
    boton_consultar = ft.ElevatedButton(
        text="Consultar IA",
        icon=ft.icons.SEARCH,
        style=ft.ButtonStyle(
            padding=20,
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
        color=ft.colors.WHITE,
        bgcolor=ft.colors.BLUE_800,
    )

    boton_recomendar = ft.ElevatedButton(
        text="Buscar Documentos",
        icon=ft.icons.BOOK,
        style=ft.ButtonStyle(
            padding=20,
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
        color=ft.colors.WHITE,
        bgcolor=ft.colors.CYAN_600,
    )

    # Funciones de los botones
    async def on_consultar_click(e):
        pregunta = pregunta_input.value.strip()

        if not pregunta:
            respuesta_output.controls[1].content.controls[0].value = "⚠️ Por favor ingresa una pregunta."
            page.update()
            return

        # Mostrar indicador de procesamiento
        processing_indicator.visible = True
        respuesta_output.controls[1].content.controls[0].value = "🔍 Procesando tu consulta..."
        page.update()

        try:
            respuesta = asistente.consultar_ia(pregunta)
            respuesta_output.controls[1].content.controls[0].value = respuesta
        except Exception as ex:
            respuesta_output.controls[1].content.controls[0].value = f"❌ Error al consultar: {str(ex)}"
        finally:
            # Ocultar indicador de procesamiento
            processing_indicator.visible = False
            page.update()

    async def on_recomendar_click(e):
        tema = tema_input.value.strip()
        nivel = nivel_dropdown.value
        idioma = idioma_dropdown.value

        if not tema:
            respuesta_output.controls[1].content.controls[0].value = "⚠️ Por favor ingresa un tema."
            page.update()
            return

        # Mostrar indicador de procesamiento
        processing_indicator.visible = True
        respuesta_output.controls[1].content.controls[0].value = "🔍 Buscando documentos recomendados..."
        page.update()

        try:
            respuesta = asistente.recomendar_documentos(tema, nivel if nivel != "Cualquiera" else None, idioma)
            respuesta_output.controls[1].content.controls[0].value = respuesta
        except Exception as ex:
            respuesta_output.controls[1].content.controls[0].value = f"❌ Error al recomendar: {str(ex)}"
        finally:
            # Ocultar indicador de procesamiento
            processing_indicator.visible = False
            page.update()

    boton_consultar.on_click = on_consultar_click
    boton_recomendar.on_click = on_recomendar_click

    # Diseño de pestañas
    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Consulta IA",
                icon=ft.icons.QUESTION_ANSWER,
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Consulta a la Inteligencia Artificial",
                                   style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                            pregunta_input,
                            processing_indicator,
                            ft.Container(
                                boton_consultar,
                                alignment=ft.alignment.center_right,
                            ),
                        ],
                        spacing=20,
                    ),
                    padding=20,
                ),
            ),
            ft.Tab(
                text="Documentos",
                icon=ft.icons.BOOK,
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Recomendación de Documentos",
                                   style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                            tema_input,
                            ft.Row(
                                [
                                    nivel_dropdown,
                                    idioma_dropdown,
                                ],
                                spacing=20,
                                expand=True,
                            ),
                            ft.Container(
                                boton_recomendar,
                                alignment=ft.alignment.center_right,
                            ),
                        ],
                        spacing=20,
                    ),
                    padding=20,
                ),
            ),
        ],
        expand=1,
    )

    return ft.View(
        route="/ia_view",
        controls=[
            ft.AppBar(
                title=ft.Text("Asistente IA", style=ft.TextThemeStyle.HEADLINE_SMALL),
                center_title=True,
                bgcolor=ft.colors.BLUE_800,
                color=ft.colors.WHITE,
                actions=[
                    ft.IconButton(ft.icons.HELP_OUTLINE, tooltip="Ayuda"),
                ],
            ),
            ft.Column(
                [
                    tabs,
                    ft.Divider(height=1),
                    respuesta_output,
                ],
                expand=True,
                spacing=0,
            ),
        ],
        padding=0,
    )