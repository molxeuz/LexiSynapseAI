import datetime

class Tarea:
    def __int__(self, descripcion, fecha_limite, completada=False):
        self.descripcion = descripcion
        self.fecha_limite = fecha_limite
        self.completada = completada

    def __str__(self):
        estado = "v" if self.completada else " "
        return f"[{estado}] {self.descripcion} (Para: {self.fecha_limite})"

    def convertir_a_texto(self):
        return f"TAREA,{self.descripcion},{self.fecha_limite},{int(self.completada)}"

    @classmethod
    def crear_desde_texto(cls, texto):
        try:
            partes = texto.strip().split(',')
            if len(partes) != 4 or partes[0] != "TAREA":
                raise ValueError("Formato incorrecto")

            return cls(
                descripcion=partes[1],
                fecha_limite=datetime.date.fromisoformat(partes[2]),
                completada=bool(int(partes[3]))
            )
        except Exception as error:
            print(f"Error al crear tarea: {error}")
            return None
"""
CRUD tareas.

Definir funciones de lógica.
Conectar clases (models) con pantallas (interfaces).
Validaciones y respuestas dinámicas.

"""