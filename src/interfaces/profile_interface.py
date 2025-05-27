
"""
Vista "Perfil de Usuario" en Flet: muestra datos personales y académicos del usuario,
permite editarlos mediante campos ocultos que se activan con botones, y ofrece secciones vacías para materias y actividades.
Incluye botones para cerrar sesión y volver al dashboard.
"""

import flet as ft

def perfil_usuario_view(page: ft.Page):
    page.title = "Perfil de Usuario"

    def cerrar_sesion(e):
        page.client_storage.clear()
        page.go("/login")

    def volver_dashboard(e):
        page.go("/dashboard")

    # Estado de edición
    estado_edicion_personal = {"activo": False}
    estado_edicion_academico = {"activo": False}

    def toggle_editar_personal(e):
        estado_edicion_personal["activo"] = not estado_edicion_personal["activo"]
        nombre.visible = estado_edicion_personal["activo"]
        correo.visible = estado_edicion_personal["activo"]
        fecha_nacimiento.visible = estado_edicion_personal["activo"]
        btn_guardar_personal.visible = estado_edicion_personal["activo"]
        page.update()

    def toggle_editar_academico(e):
        estado_edicion_academico["activo"] = not estado_edicion_academico["activo"]
        universidad.visible = estado_edicion_academico["activo"]
        carrera.visible = estado_edicion_academico["activo"]
        semestre.visible = estado_edicion_academico["activo"]
        btn_guardar_academico.visible = estado_edicion_academico["activo"]
        page.update()

    # Campos de edición
    nombre = ft.TextField(label="Nombre completo", width=400, filled=True, border_radius=10, visible=False)
    correo = ft.TextField(label="Correo electrónico", width=400, filled=True, border_radius=10, visible=False)
    fecha_nacimiento = ft.TextField(label="Fecha de nacimiento", width=200, filled=True, border_radius=10, visible=False)
    universidad = ft.TextField(label="Universidad", width=300, filled=True, border_radius=10, visible=False)
    carrera = ft.TextField(label="Carrera", width=300, filled=True, border_radius=10, visible=False)
    semestre = ft.TextField(label="Semestre", width=100, filled=True, border_radius=10, visible=False)

    # Visualización
    nombre_text = ft.Text("", size=16, weight="bold")
    correo_text = ft.Text("", size=16)
    fecha_text = ft.Text("", size=16)
    universidad_text = ft.Text("", size=16)
    carrera_text = ft.Text("", size=16)
    semestre_text = ft.Text("", size=16)

    # Botones individuales por sección
    btn_editar_personal = ft.OutlinedButton("Editar Datos Personales", icon=ft.icons.EDIT, on_click=toggle_editar_personal)
    btn_guardar_personal = ft.ElevatedButton("Guardar Cambios", icon=ft.icons.SAVE, visible=False)

    btn_editar_academico = ft.OutlinedButton("Editar Datos Académicos", icon=ft.icons.EDIT, on_click=toggle_editar_academico)
    btn_guardar_academico = ft.ElevatedButton("Guardar Cambios", icon=ft.icons.SAVE, visible=False)

    # Datos personales
    datos_personales = ft.Container(
        content=ft.Column([
            ft.Text("Datos Personales", size=20, weight="bold", color=ft.colors.BLUE_900),
            ft.Divider(),
            ft.Row([ft.Text("Nombre:", width=150), nombre_text, nombre], spacing=10),
            ft.Row([ft.Text("Correo:", width=150), correo_text, correo], spacing=10),
            ft.Row([ft.Text("Fecha de nacimiento:", width=150), fecha_text, fecha_nacimiento], spacing=10),
            ft.Row([btn_editar_personal, btn_guardar_personal], spacing=10)
        ], spacing=10),
        padding=20,
        bgcolor=ft.colors.WHITE,
        border_radius=15,
        shadow=ft.BoxShadow(color=ft.colors.BLACK12, blur_radius=8),
    )

    # Datos académicos
    datos_academicos = ft.Container(
        content=ft.Column([
            ft.Text("Datos Académicos", size=20, weight="bold", color=ft.colors.BLUE_900),
            ft.Divider(),
            ft.Row([ft.Text("Universidad:", width=150), universidad_text, universidad], spacing=10),
            ft.Row([ft.Text("Carrera:", width=150), carrera_text, carrera], spacing=10),
            ft.Row([ft.Text("Semestre:", width=150), semestre_text, semestre], spacing=10),
            ft.Row([btn_editar_academico, btn_guardar_academico], spacing=10)
        ], spacing=10),
        padding=20,
        bgcolor=ft.colors.WHITE,
        border_radius=15,
        shadow=ft.BoxShadow(color=ft.colors.BLACK12, blur_radius=8),
    )

    # Materias
    materias_academicas = ft.Container(
        content=ft.Column([
            ft.Text("Materias Inscritas", size=20, weight="bold", color=ft.colors.BLUE_900),
            ft.Divider(),
            ft.Text("No hay materias registradas.", italic=True)
        ], spacing=10),
        padding=20,
        bgcolor=ft.colors.WHITE,
        border_radius=15,
        shadow=ft.BoxShadow(color=ft.colors.BLACK12, blur_radius=8),
    )

    # Actividades
    actividades_extra = ft.Container(
        content=ft.Column([
            ft.Text("Actividades Extracurriculares", size=20, weight="bold", color=ft.colors.BLUE_900),
            ft.Divider(),
            ft.Text("No hay actividades registradas.", italic=True)
        ], spacing=10),
        padding=20,
        bgcolor=ft.colors.WHITE,
        border_radius=15,
        shadow=ft.BoxShadow(color=ft.colors.BLACK12, blur_radius=8),
    )

    # Footer con botones grandes y bonitos
    footer = ft.Row([
        ft.Container(
            content=ft.FilledButton(
                text="Volver al Dashboard",
                icon=ft.icons.ARROW_BACK,
                on_click=volver_dashboard,
                style=ft.ButtonStyle(
                    padding=20,
                    bgcolor=ft.colors.BLUE_700,
                    color=ft.colors.WHITE,
                    shape=ft.RoundedRectangleBorder(radius=12),
                    elevation=4
                )
            ),
            expand=1,
            alignment=ft.alignment.center_left
        ),
        ft.Container(
            content=ft.FilledButton(
                text="Cerrar Sesión",
                icon=ft.icons.LOGOUT,
                on_click=cerrar_sesion,
                style=ft.ButtonStyle(
                    padding=20,
                    bgcolor=ft.colors.RED_600,
                    color=ft.colors.WHITE,
                    shape=ft.RoundedRectangleBorder(radius=12),
                    elevation=4
                )
            ),
            expand=1,
            alignment=ft.alignment.center_right
        )
    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN, spacing=30)

    # Vista principal
    return ft.View(
        route="/perfil",
        bgcolor=ft.colors.GREY_100,
        padding=30,
        controls=[
            ft.Text("Perfil de Usuario", size=32, weight="bold", color=ft.colors.BLUE_GREY_900),
            ft.ResponsiveRow([
                ft.Column([datos_personales], col={"sm": 12, "md": 6}),
                ft.Column([datos_academicos], col={"sm": 12, "md": 6}),
            ], spacing=20),
            ft.ResponsiveRow([
                ft.Column([materias_academicas], col={"sm": 12, "md": 6}),
                ft.Column([actividades_extra], col={"sm": 12, "md": 6}),
            ], spacing=20),
            footer
        ]
    )
