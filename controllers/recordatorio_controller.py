
class Recordatorio:
    def __init__(self,id_recordatorio: int, id_usuario: int, titulo_recordatorio: str, descripcion: str, fecha_entrega: str, estado: bool=False):
        self.id_recordatorio: int = id_recordatorio
        self.id_usuario: int = id_usuario
        self.titulo_recordatorio: str = titulo_recordatorio
        self.descripcion: str = descripcion
        self.fecha_entrega: str = fecha_entrega
        self.estado: bool = estado

    def crear_recordatorio(self, titulo: str, materia: str, fecha_entrega: str, descripcion: str):
        pass

    def editar_recordatorio(self, id_recordatorio: int, nuevos_datos: dict):
        pass

    def eliminar_recordatorio(self, id_recordatorio: int):
        pass

    def marcar_completada(self, id_recordatorio: int):
        pass

"""
CRUD recordatorios.

Definir funciones de lógica.
Conectar clases (models) con pantallas (interfaces).
Validaciones y respuestas dinámicas.

"""