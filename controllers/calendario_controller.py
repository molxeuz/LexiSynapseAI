from controllers.tarea_controller import Tarea
from controllers.recordatorio_controller import Recordatorio

class Calendario:
    def __init__(self, id_usuario: int):
        self.id_usuario: int = id_usuario
        self.Tarea: list[Tarea]
        self.Recordatorio: list[Recordatorio]

    def detalles_calendario(self, id_calendario: int) -> None:
        pass

"""
Integración de eventos.
Definir funciones de lógica.
Conectar clases (models) con pantallas (interfaces).
Validaciones y respuestas dinámicas.
"""