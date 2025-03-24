class Tarea:
    def __int__(self, descripcion, fecha_limite, completada=False):
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite
        self.completada = completada

    def __str__(self):
        estado = "v" if self.completada else " "
        return f"[{estado}] {self.descripcion} (Para: {self.fecha_limite})"

    def devolver(self):
        return f"TAREA, {self.descripcion},{self.fecha_limite}, {int(self.completada)}"

"""
CRUD tareas.

Definir funciones de lógica.
Conectar clases (models) con pantallas (interfaces).
Validaciones y respuestas dinámicas.

"""