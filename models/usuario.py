
class Usuario:
    #Atributos
    def __init__(self,nombre: str):
        self.nombre: str= nombre
        self.preferencias: list[str]=[]
        self.historial: list[str]=[]

    #Metodos
    def mostrar_usuario(self):
        return f"{self.nombre}-{self.preferencias}-{self.historial}"

"""
Registro, autenticación, edición.
"""