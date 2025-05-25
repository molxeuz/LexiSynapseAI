import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class AsistenteIA:
    def __init__(self):
        api_key = os.getenv("DEEPSEEK_API_KEY")
        if not api_key:
            raise ValueError("No se encontró DEEPSEEK_API_KEY en las variables de entorno")
        

    def consultar_ia(self, consulta: str) -> None:
        pass

    def sugerencias_estudio(self, id_usuario: int) -> None:
        pass

"""
Consultas IA.
Definir funciones de lógica.
Conectar clases (models) con pantallas (interfaces).
Validaciones y respuestas dinámicas.
"""