
"""
Vista de Calendario Interactivo.
Permite visualizar un calendario mensual, navegar entre meses y asignar tareas por día.
Las tareas se muestran por fecha y pueden agregarse a través de un modal interactivo.
"""

import flet as ft
import calendar
from datetime import datetime, timedelta

def calendario_view(page: ft.Page):
    page.title = "Calendario Interactivo"
    current_date = datetime.now()
    selected_year = current_date.year
    selected_month = current_date.month
    dias_tareas = {}
    selected_day = None

    dia_label = ft.Text()
    tarea_input = ft.TextField(label="Escribe la tarea")

    mes_ano_label = ft.Text(size=20, weight="bold")

    def guardar_tarea(e):
        dia = dia_label.value
        tarea = tarea_input.value.strip()
        if tarea:
            if dia not in dias_tareas:
                dias_tareas[dia] = []
            dias_tareas[dia].append(tarea)
        tarea_input.value = ""
        dialog.open = False
        mostrar_dias_del_mes()
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

    contenedor_semanas = ft.Column(spacing=8)

    def abrir_modal(dia_str):
        nonlocal selected_day
        selected_day = dia_str
        dia_label.value = dia_str
        tarea_input.value = ""
        dialog.open = True
        mostrar_dia_detalle()
        page.update()

    def mostrar_dias_del_mes():
        contenedor_semanas.controls.clear()

        mes_ano_label.value = f"{calendar.month_name[selected_month]} {selected_year}"

        encabezados = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=6,
            controls=[
                ft.Text(dia, weight="bold", width=60, text_align="center")
                for dia in ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
            ]
        )
        contenedor_semanas.controls.append(encabezados)

        primer_dia_mes = datetime(selected_year, selected_month, 1)
        inicio_semana = primer_dia_mes.weekday()

        fecha_inicio = primer_dia_mes - timedelta(days=inicio_semana)
        dias = [fecha_inicio + timedelta(days=i) for i in range(42)]

        for semana in range(6):
            fila = ft.Row(spacing=6, alignment=ft.MainAxisAlignment.CENTER)
            for i in range(7):
                fecha_actual = dias[semana * 7 + i]
                es_mes_actual = fecha_actual.month == selected_month
                dia_str = fecha_actual.strftime("%Y-%m-%d")

                def crear_handler(dia_str_local):
                    return lambda e: abrir_modal(dia_str_local)

                tareas = dias_tareas.get(dia_str, [])
                tareas_texto = f"\n{len(tareas)} tarea{'s' if len(tareas) != 1 else ''}" if tareas else ""

                fila.controls.append(
                    ft.GestureDetector(
                        on_tap=crear_handler(dia_str),
                        content=ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.Text(str(fecha_actual.day), text_align="center"),
                                    ft.Text(tareas_texto.strip(), size=9, text_align="center")
                                ],
                                spacing=2,
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            ),
                            bgcolor="#FFFFFF" if es_mes_actual else "#F0F0F0",
                            border_radius=10,
                            width=65,
                            height=60,
                            padding=6,
                            alignment=ft.alignment.center,
                            shadow=ft.BoxShadow(color=ft.colors.BLACK12, blur_radius=4, offset=ft.Offset(1, 1))
                        )
                    )
                )
            contenedor_semanas.controls.append(fila)
        page.update()

    def mostrar_dia_detalle():
        dia_detalle.controls.clear()
        if selected_day:
            fecha_dt = datetime.strptime(selected_day, "%Y-%m-%d")
            dia_formateado = fecha_dt.strftime("%d de %B de %Y")
            tareas = dias_tareas.get(selected_day, [])
            dia_detalle.controls.append(ft.Text(dia_formateado, size=20, weight="bold"))
            dia_detalle.controls.append(ft.Divider())
            if tareas:
                for tarea in tareas:
                    dia_detalle.controls.append(ft.Text(f"• {tarea}", size=14))
            else:
                dia_detalle.controls.append(ft.Text("No hay tareas para este día.", italic=True, color=ft.colors.GREY))
        page.update()

    def siguiente_mes(e):
        nonlocal selected_month, selected_year
        selected_month += 1
        if selected_month > 12:
            selected_month = 1
            selected_year += 1
        mostrar_dias_del_mes()

    def mes_anterior(e):
        nonlocal selected_month, selected_year
        selected_month -= 1
        if selected_month < 1:
            selected_month = 12
            selected_year -= 1
        mostrar_dias_del_mes()

    controles_nav = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        controls=[
            ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=mes_anterior),
            mes_ano_label,
            ft.IconButton(icon=ft.icons.ARROW_FORWARD, on_click=siguiente_mes)
        ]
    )

    dia_detalle = ft.Column(spacing=10)

    mostrar_dias_del_mes()

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
                    ], spacing=15),
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
