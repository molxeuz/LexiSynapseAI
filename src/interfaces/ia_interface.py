
"""
Vista del Asistente Inteligente (IA).
Permite realizar consultas a un modelo de IA y obtener recomendaciones de documentos basados en tema, nivel e idioma.
Incluye dos secciones: consulta general y recomendación de recursos de aprendizaje.
Requiere el controlador AsistenteIA.
"""

import flet as ft
from src.controllers.asistente_controller import AsistenteIA

asistente = AsistenteIA()

def ia_view(page: ft.Page):
    page.title = "Asistente Inteligente"
    page.bgcolor = ft.colors.GREY_100

    pregunta_input = ft.TextField(
        label="Pregunta a la IA",
        multiline=True,
        min_lines=3,
        max_lines=5,
        filled=True,
        expand=True,
        border_radius=10,
        fill_color=ft.colors.GREY_50,
        border_color=ft.colors.BLUE_GREY_200,
        hint_text="Ej: ¿Qué es una red neuronal?"
    )

    respuesta_ia_output = ft.Container(
        content=ft.Markdown("Aquí aparecerá la respuesta de la IA...", selectable=True),
        padding=15,
        border_radius=10,
        width=700,
        bgcolor=ft.colors.GREY_50,
        border=ft.border.all(1, ft.colors.BLUE_GREY_200),
        expand=True
    )

    tema_input = ft.TextField(
        label="Tema de interés",
        filled=True,
        expand=True,
        border_radius=10,
        fill_color=ft.colors.GREY_50,
        border_color=ft.colors.BLUE_GREY_200,
        hint_text="Ej: Python, Machine Learning, Redes Neuronales..."
    )

    nivel_dropdown = ft.Dropdown(
        label="Nivel",
        filled=True,
        border_radius=10,
        value="Cualquiera",
        fill_color=ft.colors.GREY_50,
        border_color=ft.colors.BLUE_GREY_200,
        options=[
            ft.dropdown.Option("Cualquiera"),
            ft.dropdown.Option("Principiante"),
            ft.dropdown.Option("Intermedio"),
            ft.dropdown.Option("Avanzado"),
        ]
    )

    idioma_dropdown = ft.Dropdown(
        label="Idioma",
        filled=True,
        border_radius=10,
        value="español",
        fill_color=ft.colors.GREY_50,
        border_color=ft.colors.BLUE_GREY_200,
        options=[
            ft.dropdown.Option("español"),
            ft.dropdown.Option("inglés"),
            ft.dropdown.Option("francés"),
        ]
    )

    respuesta_docs_output = ft.Container(
        content=ft.Markdown("Aquí aparecerán los documentos recomendados...", selectable=True),
        padding=15,
        border_radius=10,
        width=700,
        bgcolor=ft.colors.GREY_50,
        border=ft.border.all(1, ft.colors.BLUE_GREY_200),
        expand=True
    )

    ia_loading = ft.Row([
        ft.ProgressRing(width=20, height=20, stroke_width=3, visible=False),
        ft.Text("Consultando la IA...", visible=False),
    ], spacing=10)

    docs_loading = ft.Row([
        ft.ProgressRing(width=20, height=20, stroke_width=3, visible=False),
        ft.Text("Buscando recomendaciones...", visible=False),
    ], spacing=10)

    def toggle_loading(row, show: bool, mensaje: str = ""):
        row.controls[0].visible = show
        row.controls[1].value = mensaje
        row.controls[1].visible = show
        page.update()

    async def on_consultar_click(e):
        pregunta = pregunta_input.value.strip()
        if not pregunta:
            respuesta_ia_output.content.value = "⚠️ Ingresa una pregunta válida."
            page.update()
            return

        toggle_loading(ia_loading, True, "Consultando la IA...")
        respuesta_ia_output.content.value = "⏳ Procesando tu consulta..."
        page.update()

        try:
            respuesta = asistente.consultar_ia(pregunta)
            respuesta_ia_output.content.value = respuesta
        except Exception as ex:
            respuesta_ia_output.content.value = f"❌ Error al consultar la IA: {str(ex)}"
        toggle_loading(ia_loading, False)

    async def on_recomendar_click(e):
        tema = tema_input.value.strip()
        if not tema:
            respuesta_docs_output.content.value = "⚠️ Ingresa un tema válido."
            page.update()
            return

        nivel = nivel_dropdown.value if nivel_dropdown.value != "Cualquiera" else None
        idioma = idioma_dropdown.value

        toggle_loading(docs_loading, True, "Buscando recomendaciones...")
        respuesta_docs_output.content.value = "⏳ Procesando tu solicitud..."
        page.update()

        try:
            respuesta = asistente.recomendar_documentos(tema, nivel, idioma)
            respuesta_docs_output.content.value = respuesta
        except Exception as ex:
            respuesta_docs_output.content.value = f"❌ Error al buscar documentos: {str(ex)}"
        toggle_loading(docs_loading, False)

    return ft.View(
        route="/ia_view",
        padding=20,
        controls=[
            ft.Text("Asistente Inteligente", size=32, weight="bold", color=ft.colors.BLUE_GREY_900),
            ft.ResponsiveRow([

                ft.Container(
                    content=ft.Column([
                        ft.Text("Consulta a la IA", size=20, weight="bold", color=ft.colors.BLUE_GREY_800),
                        ft.Divider(thickness=1),
                        pregunta_input,
                        ft.ElevatedButton("Consultar IA", icon=ft.icons.PSYCHOLOGY_ALT, on_click=on_consultar_click),
                        ia_loading,
                        ft.Text("Respuesta", size=16, weight="w600"),
                        respuesta_ia_output
                    ], spacing=15),
                    padding=20,
                    col={"sm": 12, "md": 6},
                    bgcolor=ft.colors.WHITE,
                    border_radius=15,
                    shadow=ft.BoxShadow(color=ft.colors.BLACK12, blur_radius=8),
                ),

                ft.Container(
                    content=ft.Column([
                        ft.Text("Recomendación de Documentos", size=20, weight="bold", color=ft.colors.BLUE_GREY_800),
                        ft.Divider(thickness=1),
                        tema_input,
                        ft.Row([nivel_dropdown, idioma_dropdown], spacing=10),
                        ft.ElevatedButton("Buscar Documentos", icon=ft.icons.BOOK, on_click=on_recomendar_click),
                        docs_loading,
                        ft.Text("Resultados", size=16, weight="w600"),
                        respuesta_docs_output
                    ], spacing=15),
                    padding=20,
                    col={"sm": 12, "md": 6},
                    bgcolor=ft.colors.WHITE,
                    border_radius=15,
                    shadow=ft.BoxShadow(color=ft.colors.BLACK12, blur_radius=8),
                ),
            ], spacing=20),

            ft.Row([
                ft.IconButton(icon=ft.icons.ARROW_BACK, tooltip="Volver", on_click=lambda _: page.go("/dashboard")),
                ft.TextButton("Volver al Dashboard", on_click=lambda _: page.go("/dashboard"))
            ], alignment=ft.MainAxisAlignment.START)
        ]
    )