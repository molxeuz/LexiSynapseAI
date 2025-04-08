from controllers.tarea_controller import Tarea

class Calendario:
    def __init__(self, id_usuario: int):
        self.id_usuario: int = id_usuario
        self.recordatorios:list[str]
        self.Tareas:list[Tarea]

    def mostrar_calendario(self, vista: str) -> None:
        pass

    def detalles_evento(self, id_evento: int) -> None:
        pass

    def editar_evento(self, id_evento: int) -> None:
        pass

    def eliminar_eventos(self, id_evento: int) -> None:
        pass

"""
Integración de eventos.

Definir funciones de lógica.
Conectar clases (models) con pantallas (interfaces).
Validaciones y respuestas dinámicas.

"""