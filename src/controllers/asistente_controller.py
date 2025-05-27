
"""
Clase AsistenteIA para consultas con API Deepseek.
Manejo de interacción con modelo IA y generación de recomendaciones.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class AsistenteIA:
    def __init__(self):
        api_key = os.getenv("DEEPSEEK_API_KEY")
        if not api_key:
            raise ValueError("No se encontró DEEPSEEK_API_KEY en las variables de entorno")
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com"
        )
        self.default_model = "deepseek-chat"
        self.default_temperature = 0.7
        self.default_max_tokens = 512

    def consultar_ia(self, pregunta, contexto=None, stream=False) -> None:
        messages = [
            {"role": "system", "content": contexto or "Eres un asistente útil y das respuestas cortas"},
            {"role": "user", "content": pregunta}
        ]

        response = self.client.chat.completions.create(
            model=self.default_model,
            messages=messages,
            max_tokens=self.default_max_tokens,
            temperature=self.default_temperature,
            stream=stream
        )

        if stream:
            return self._handle_stream_response(response)
        return response.choices[0].message.content

    def recomendar_documentos(self, tema, nivel=None, idioma="español"):
        prompt = (
            f"Por favor recomienda documentos, libros, artículos académicos o recursos en línea "
            f"para estudiar {tema}"
        )

        if nivel:
            prompt += f" a nivel {nivel}"

        prompt += (
            f". Preferiblemente en {idioma}. Incluye títulos, autores (si aplica), "
            f"y enlaces cuando sea posible. Organiza las recomendaciones por tipo de recurso."
        )

        return self.consultar_ia(prompt)

"""
Consultas IA.
Definir funciones de lógica.
Conectar clases (models) con pantallas (interfaces).
Validaciones y respuestas dinámicas.
"""