"Para generar recordatorios de las tareas creadas en el calendario/tarea_controller.py"
import datetime

class Recordatorio:
    def __init__(self, mensaje, hora):
        self.mensaje = mensaje
        self.hora = hora

    def __str__(self):
        return f" {self.mensaje}, {self.hora.strftime ('%Y-%m-%d %H:%M')}"

    def convertir_a_texto(self):
        return f"Recordatorio, {self.mensaje},{self.hora.isoformat()}"

    @classmethod

    def crear_desde_texo(cls, texto):
        partes = texto.strip().split(',', 2)
        if len(partes) !=3 or partes[0] != " RECORDATORIO":
            return None

        if 'T' not in partes[2] or len(partes[2]) < 16:
            return None

        return cls(mensaje=partes[1],hora=datetime.datetime.fromisoformat(partes[2]))

"""
CRUD recordatorios.

Definir funciones de lógica.
Conectar clases (models) con pantallas (interfaces).
Validaciones y respuestas dinámicas.

"""