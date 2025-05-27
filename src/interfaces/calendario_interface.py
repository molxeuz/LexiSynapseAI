
"""
Vista de Calendario Interactivo.
Permite visualizar un calendario mensual, navegar entre meses y asignar tareas por día.
Las tareas se muestran por fecha y pueden agregarse a través de un modal interactivo.
"""

import flet as ft
from datetime import datetime
from src.controllers.calendario_controller import CalendarioController

def calendario_view(page: ft.Page):
    controller = CalendarioController()

    page.title = "Calendario Interactivo"

    mes_ano_label = ft.Text(size=20, weight="bold")
    dia_label = ft.Text()
    tarea_input = ft.TextField(label="Escribe la tarea")
    contenedor_semanas = ft.Column(spacing=8)
    dia_detalle = ft.Column(spacing=10)

    def actualizar_dias():
        contenedor_semanas.controls.clear()
        nombre_mes, anio = controller.obtener_mes_actual()
        mes_ano_label.value = f"{nombre_mes} {anio}"

        encabezados = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=6,
            controls=[ft.Text(dia, weight="bold", width=60, text_align="center")
                      for dia in ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]]
        )
        contenedor_semanas.controls.append(encabezados)

        dias = controller.obtener_dias_del_mes()
        for semana in range(6):
            fila = ft.Row(spacing=6, alignment=ft.MainAxisAlignment.CENTER)
            for i in range(7):
                fecha = dias[semana * 7 + i]
                dia_str = fecha.strftime("%Y-%m-%d")
                es_mes_actual = fecha.month == controller.selected_month
                tareas = controller.obtener_tareas_dia(dia_str)
                tareas_texto = f"\n{len(tareas)} tarea{'s' if len(tareas) != 1 else ''}" if tareas else ""

                def crear_handler(dia_local):
                    return lambda e: abrir_modal(dia_local)

                fila.controls.append(
                    ft.GestureDetector(
                        on_tap=crear_handler(dia_str),
                        content=ft.Container(
                            content=ft.Column([
                                ft.Text(str(fecha.day), text_align="center"),
                                ft.Text(tareas_texto.strip(), size=9, text_align="center")
                            ]),
                            bgcolor="#FFFFFF" if es_mes_actual else "#F0F0F0",
                            border_radius=10,
                            width=65,
                            height=60,
                            padding=6,
                            alignment=ft.alignment.center,
                            shadow=ft.BoxShadow(color=ft.colors.BLACK12, blur_radius=4)
                        )
                    )
                )
            contenedor_semanas.controls.append(fila)
        page.update()

    def abrir_modal(dia_str):
        controller.seleccionar_dia(dia_str)
        dia_label.value = dia_str
        tarea_input.value = ""
        mostrar_dia_detalle()
        dialog.open = True
        page.update()

    def mostrar_dia_detalle():
        dia_detalle.controls.clear()
        selected = controller.obtener_dia_seleccionado()
        if selected:
            fecha_dt = datetime.strptime(selected, "%Y-%m-%d")
            dia_formateado = fecha_dt.strftime("%d de %B de %Y")
            tareas = controller.obtener_tareas_dia(selected)
            dia_detalle.controls.append(ft.Text(dia_formateado, size=20, weight="bold"))
            dia_detalle.controls.append(ft.Divider())
            if tareas:
                for tarea in tareas:
                    dia_detalle.controls.append(ft.Text(f"• {tarea}", size=14))
            else:
                dia_detalle.controls.append(ft.Text("No hay tareas para este día.", italic=True, color=ft.colors.GREY))
        page.update()

    def guardar_tarea(e):
        tarea = tarea_input.value.strip()
        if tarea:
            controller.agregar_tarea(controller.obtener_dia_seleccionado(), tarea)
        tarea_input.value = ""
        dialog.open = False
        actualizar_dias()
        page.update()

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Agregar tarea"),
        content=ft.Column([dia_label, tarea_input], tight=True),
        actions=[
            ft.TextButton("Guardar", on_click=guardar_tarea),
            ft.TextButton("Cancelar", on_click=lambda e: dialog.close())
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )
    page.dialog = dialog

    controles_nav = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        controls=[
            ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=lambda e: [controller.cambiar_mes(False), actualizar_dias()]),
            mes_ano_label,
            ft.IconButton(icon=ft.icons.ARROW_FORWARD, on_click=lambda e: [controller.cambiar_mes(True), actualizar_dias()])
        ]
    )

    actualizar_dias()

    return ft.View(
        route="/calendario",
        bgcolor=ft.colors.GREY_100,
        padding=20,
        controls=[
            ft.Text("Calendario Interactivo", size=32, weight="bold", color=ft.colors.BLUE_GREY_900),
            ft.ResponsiveRow([
                ft.Container(
                    content=ft.Column([
                        controles_nav,
                        ft.Divider(thickness=2, color=ft.colors.BLUE_GREY_200),
                        contenedor_semanas
                    ]),
                    col={"sm": 12, "md": 8},
                    padding=20,
                    bgcolor=ft.colors.WHITE,
                    border_radius=15,
                    shadow=ft.BoxShadow(color=ft.colors.BLACK12, blur_radius=8),
                    height=600
                ),
                ft.Container(
                    content=dia_detalle,
                    col={"sm": 12, "md": 4},
                    padding=20,
                    bgcolor=ft.colors.WHITE,
                    border_radius=15,
                    shadow=ft.BoxShadow(color=ft.colors.BLACK12, blur_radius=8),
                    height=600
                )
            ], spacing=20),
            ft.Row([
                ft.IconButton(icon=ft.icons.ARROW_BACK, tooltip="Volver al Dashboard", on_click=lambda _: page.go("/dashboard")),
                ft.TextButton("Volver al Dashboard", on_click=lambda _: page.go("/dashboard"))
            ], alignment=ft.MainAxisAlignment.START)
        ]
    )