import flet as ft

def perfil_usuario_view(page: ft.Page):
    page.title = "Perfil de Usuario"

    # Redirección al cerrar sesión o volver
    def cerrar_sesion(e):
        page.client_storage.clear()
        page.go("/login")

    def volver_dashboard(e):
        page.go("/dashboard")

    # Acciones de edición
    def editar_datos_personales(e):
        nombre.visible = True
        correo.visible = True
        fecha_nacimiento.visible = True
        btn_guardar.visible = True
        page.update()

    def editar_datos_academicos(e):
        universidad.visible = True
        carrera.visible = True
        semestre.visible = True
        btn_guardar.visible = True
        page.update()

    # Campos de edición (inicialmente ocultos)
    nombre = ft.TextField(label="Nombre completo", width=400, filled=True, border_radius=10, visible=False)
    correo = ft.TextField(label="Correo electrónico", width=400, filled=True, border_radius=10, visible=False)
    fecha_nacimiento = ft.TextField(label="Fecha de nacimiento", width=200, filled=True, border_radius=10, visible=False)
    universidad = ft.TextField(label="Universidad", width=300, filled=True, border_radius=10, visible=False)
    carrera = ft.TextField(label="Carrera", width=300, filled=True, border_radius=10, visible=False)
    semestre = ft.TextField(label="Semestre", width=100, filled=True, border_radius=10, visible=False)

    # Visualización de datos (vacíos por defecto)
    nombre_text = ft.Text("", size=16, weight="bold")
    correo_text = ft.Text("", size=16)
    fecha_text = ft.Text("", size=16)
    universidad_text = ft.Text("", size=16)
    carrera_text = ft.Text("", size=16)
    semestre_text = ft.Text("", size=16)

    # Botones
    btn_editar_personal = ft.OutlinedButton("Editar Datos Personales", icon=ft.icons.EDIT, on_click=editar_datos_personales)
    btn_editar_academico = ft.OutlinedButton("Editar Datos Académicos", icon=ft.icons.EDIT, on_click=editar_datos_academicos)
    btn_guardar = ft.ElevatedButton("Guardar Cambios", icon=ft.icons.SAVE, visible=False)

    # Datos personales
    datos_personales = ft.Container(
        content=ft.Column([
            ft.Text("Datos Personales", size=20, weight="bold", color=ft.colors.BLUE_900),
            ft.Divider(),
            ft.Row([ft.Text("Nombre:", width=150), nombre_text, nombre], spacing=10),
            ft.Row([ft.Text("Correo:", width=150), correo_text, correo], spacing=10),
            ft.Row([ft.Text("Fecha de nacimiento:", width=150), fecha_text, fecha_nacimiento], spacing=10),
            ft.Row([btn_editar_personal])
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
            ft.Row([btn_editar_academico])
        ], spacing=10),
        padding=20,
        bgcolor=ft.colors.WHITE,
        border_radius=15,
        shadow=ft.BoxShadow(color=ft.colors.BLACK12, blur_radius=8),
    )

    # Materias inscritas
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

    # Actividades extracurriculares
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

    # Botones de acción
    botones_accion = ft.Row([btn_guardar], spacing=10)

    # Opciones extra
    opciones_extra = ft.Column([
        ft.Text("Opciones", size=20, weight="bold"),
        ft.Divider(),
        ft.TextButton("Cerrar sesión", on_click=cerrar_sesion)
    ], spacing=10)

    # Botón de volver
    volver = ft.Row([
        ft.IconButton(icon=ft.icons.ARROW_BACK, tooltip="Volver al Dashboard", on_click=volver_dashboard),
        ft.TextButton("Volver al Dashboard", on_click=volver_dashboard)
    ], alignment=ft.MainAxisAlignment.START, spacing=5)

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
            botones_accion,
            ft.ResponsiveRow([
                ft.Column([materias_academicas], col={"sm": 12, "md": 6}),
                ft.Column([actividades_extra], col={"sm": 12, "md": 6}),
            ], spacing=20),
            opciones_extra,
            volver
        ]
    )
