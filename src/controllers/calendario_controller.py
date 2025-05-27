


from datetime import datetime, timedelta
import calendar

class CalendarioController:
    def __init__(self):
        self.current_date = datetime.now()
        self.selected_year = self.current_date.year
        self.selected_month = self.current_date.month
        self.selected_day = None
        self.dias_tareas = {}

    def obtener_mes_actual(self):
        return calendar.month_name[self.selected_month], self.selected_year

    def cambiar_mes(self, siguiente=True):
        if siguiente:
            self.selected_month += 1
            if self.selected_month > 12:
                self.selected_month = 1
                self.selected_year += 1
        else:
            self.selected_month -= 1
            if self.selected_month < 1:
                self.selected_month = 12
                self.selected_year -= 1

    def obtener_dias_del_mes(self):
        primer_dia_mes = datetime(self.selected_year, self.selected_month, 1)
        inicio_semana = primer_dia_mes.weekday()
        fecha_inicio = primer_dia_mes - timedelta(days=inicio_semana)
        return [fecha_inicio + timedelta(days=i) for i in range(42)]

    def agregar_tarea(self, fecha, tarea):
        if fecha not in self.dias_tareas:
            self.dias_tareas[fecha] = []
        self.dias_tareas[fecha].append(tarea)

    def obtener_tareas_dia(self, fecha):
        return self.dias_tareas.get(fecha, [])

    def seleccionar_dia(self, dia):
        self.selected_day = dia

    def obtener_dia_seleccionado(self):
        return self.selected_day