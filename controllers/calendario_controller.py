import datetime
from tarea_controller import Tarea
from recordatorio_controller import Recordatorio

class Evento:
    def __init__(self, nombre, inicio, fin):
        self.nombre = nombre
        self.inicio = inicio
        self.fin = fin

    def __str__(self):
        return f"{self.nombre} ({self.inicio} a {self.fin})"

    def convertir_a_texto(self):
        return f"EVENTO, {self.nombre},{self.inicio.isoformat()}, {self.fin.isoformat()}"

    @classmethod
    def crear_desde_texto(cls, texto):
        partes = texto.strip().split(',', 3)
        if len(partes) !=4 or partes[0] != "EVENTO":
            return None
"""
Integración de eventos.

Definir funciones de lógica.
Conectar clases (models) con pantallas (interfaces).
Validaciones y respuestas dinámicas.

"""