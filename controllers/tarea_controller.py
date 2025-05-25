# controllers/tarea_controller.py

class Tarea:
    def __init__(self, nombre, fecha_entrega, prioridad, descripcion, asignatura):
        self.nombre = nombre
        self.fecha_entrega = fecha_entrega
        self.prioridad = prioridad
        self.descripcion = descripcion
        self.asignatura = asignatura
        self.completada = False

    def marcar_completada(self):
        self.completada = not self.completada


class TareaController:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, nombre, fecha_entrega, prioridad, descripcion, asignatura):
        if not nombre or not fecha_entrega or not prioridad or not descripcion or not asignatura:
            return False, "Por favor completa todos los campos"

        nueva_tarea = Tarea(nombre, fecha_entrega, prioridad, descripcion, asignatura)
        self.tareas.append(nueva_tarea)
        return True, "Tarea añadida correctamente"

    def obtener_tareas(self):
        return self.tareas


# Instancia global del controlador
tarea_controller = TareaController()
