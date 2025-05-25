class Recordatorio:
    def _init_(self, id_recordatorio: int, id_usuario: int, titulo_recordatorio: str,
                 descripcion: str, fecha_entrega: str, estado: bool = False):
        self.id_recordatorio = id_recordatorio
        self.id_usuario = id_usuario
        self.titulo_recordatorio = titulo_recordatorio
        self.descripcion = descripcion
        self.fecha_entrega = fecha_entrega
        self.estado = estado

    def _str_(self):
        return f"{self.titulo_recordatorio} - {self.descripcion} - {self.fecha_entrega}"


class RecordatorioController:
    def _init_(self):
        self.recordatorios = []
        self.counter = 0

    def agregar_recordatorio(self, id_usuario: int, titulo: str, descripcion: str, fecha: str):
        self.counter += 1
        nuevo = Recordatorio(self.counter, id_usuario, titulo, descripcion, fecha)
        self.recordatorios.append(nuevo)
        return nuevo

    def eliminar_recordatorio(self, id_recordatorio: int):
        self.recordatorios = [r for r in self.recordatorios if r.id_recordatorio != id_recordatorio]

    def listar_recordatorios(self, id_usuario: int):
        return [r for r in self.recordatorios if r.id_usuario == id_usuario]

