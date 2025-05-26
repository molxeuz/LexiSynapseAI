from src.database.database import cursor, conn

class Tarea:
    def __init__(self, id, nombre, fecha_entrega, prioridad, descripcion, asignatura, completada):
        self.id = id
        self.nombre = nombre
        self.fecha_entrega = fecha_entrega
        self.prioridad = prioridad
        self.descripcion = descripcion
        self.asignatura = asignatura
        self.completada = bool(completada)

    def marcar_completada(self):
        nuevo_estado = 1 if not self.completada else 0
        cursor.execute("UPDATE tareas SET completada = ? WHERE id = ?", (nuevo_estado, self.id))
        conn.commit()
        self.completada = not self.completada

class TareaController:
    def __init__(self, usuario_id):
        self.usuario_id = usuario_id

    def agregar_tarea(self, nombre, fecha_entrega, prioridad, descripcion, asignatura):
        if not nombre or not fecha_entrega or not prioridad:
            return False, "Por favor completa los campos obligatorios."

        cursor.execute('''
            INSERT INTO tareas (usuario_id, nombre, fecha_entrega, prioridad, descripcion, asignatura)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (self.usuario_id, nombre, fecha_entrega, prioridad, descripcion, asignatura))
        conn.commit()
        return True, "Tarea agregada correctamente."

    def obtener_tareas(self):
        cursor.execute('''
            SELECT id, nombre, fecha_entrega, prioridad, descripcion, asignatura, completada
            FROM tareas
            WHERE usuario_id = ?
        ''', (self.usuario_id,))
        tareas = cursor.fetchall()
        return [Tarea(*t) for t in tareas]