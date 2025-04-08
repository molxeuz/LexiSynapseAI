
class Tarea:
    def __init__(self,id_tarea: int, id_usuario: int, descripcion: str, fecha_entrega: str, estado: bool=False):
        self.id_tarea: int = id_tarea
        self.id_usuario: int = id_usuario
        self.descripcion: str = descripcion
        self.fecha_entrega: str = fecha_entrega
        self.estado: bool = estado

    def crear_tarea(self, titulo: str, materia: str, fecha_entrega: str, descripcion: str):
        pass

    def editar_tarea(self, id_tarea: int, nuevos_datos: dict):
        pass

    def eliminar_tarea(self, id_tarea: int):
        pass

    def marcar_completada(self, id_tarea: int):
        pass

"""
CRUD tareas.
Definir funciones de lógica.
Conectar clases (models) con pantallas (interfaces).
Validaciones y respuestas dinámicas.
"""