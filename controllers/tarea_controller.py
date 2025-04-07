import datetime

class Tarea:
    def __init__(self,id_tarea:int,id_usuario:int, descripcion:str, fecha_entrega:str, estado:bool=False):
        self.id_tarea:int = id_tarea
        self.id_usuario:int = id_usuario
        self.descripcion:str = descripcion
        self.fecha_entrega:str = fecha_entrega
        self.completada:bool = estado

"""
CRUD tareas.

Definir funciones de lógica.
Conectar clases (models) con pantallas (interfaces).
Validaciones y respuestas dinámicas.

"""