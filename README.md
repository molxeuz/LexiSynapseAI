# LexiSynapseAI - Asistente de Estudio Inteligente con IA

## Integrantes
- Mateo Molina Gonzalez - [molxeuz](https://github.com/molxeuz)  
- Moises Joshua Herrera Galindo - [Moshua53](https://github.com/Moshua53)  
- Andres David Agudelo Henao - [TheNameAndresWasTaken](https://github.com/TheNameAndresWasTaken)  
- Samuel David Gutierrez Mejia - [samuek1](https://github.com/samuek1)  

## 🚀 Descripción del Proyecto
LexiSynapse es un asistente de estudio inteligente desarrollado en **Python** con **POO** y una interfaz en **Tkinter**. Su objetivo es ayudar a los estudiantes a organizar sus tareas, recibir recordatorios, obtener ayuda en la resolución de problemas y mejorar su aprendizaje con técnicas de IA.

## 🎯 Funcionalidades
- **Gestión de Tareas y Recordatorios** 📅
  - Agregar tareas con fechas de entrega, categorías y nivel de dificultad.
  - La IA organizará las tareas por prioridad y enviará recordatorios.
  - Visualización en un calendario interactivo.

- **Ayuda en la Resolución de Problemas** 🤖
  - Conexión con la API de **DeepSeek** para búsquedas avanzadas.
  - Generación de soluciones paso a paso en matemáticas, ciencias y lenguas.
  - Sugerencias para redacción y gramática.

- **Modo de Repaso Inteligente** 🎓
  - Creación de preguntas de práctica basadas en las tareas del usuario.
  - Personalización de cuestionarios con machine learning.

- **Calendario y Notificaciones Inteligentes** 🔔
  - Organización del estudio según los hábitos del usuario.
  - Envío de recordatorios antes de las fechas límite.

- **Recomendaciones de Recursos** 📚
  - Sugerencia de videos, libros y artículos según la tarea.
  - Posibilidad de tomar notas y organizarlas automáticamente.

## 🛠️ Tecnologías Utilizadas
- **Python (POO)**: Para la estructura del asistente.
- **Tkinter**: Para la interfaz gráfica.
- **SQLite**: Base de datos local para tareas y recordatorios.
- **DeepSeek API**: Para generación de contenido y búsqueda de información.

## 📌 Diagrama de Clases (UML)
```plaintext
+-------------------+
|      Usuario      |
+-------------------+
| - nombre         |
| - preferencias   |
| - historial      |
+-------------------+
| + actualizarDatos() |
+-------------------+
         |
         ▼
+-------------------+
|    Estudiante     |
+-------------------+
| - nivel          |
| - materias       |
+-------------------+

+-------------------+         +------------------+
|     Tarea        |<>------> |  GestorTareas    |
+-------------------+         +------------------+
| - titulo        |          | + agregarTarea() |
| - descripcion   |          | + eliminarTarea()|
| - fecha_entrega |          | + organizar()    |
+-------------------+         +------------------+

+-------------------+         +----------------------+
|   Recordatorio   |<>------> | GestorRecordatorios |
+-------------------+         +----------------------+
| - fecha_hora    |          | + programar()       |
| - tarea_asociada|          | + enviar()          |
+-------------------+         +----------------------+

+-------------------+         +------------------+
|   Pregunta       |<>------> |  Cuestionario   |
+-------------------+         +------------------+
| - enunciado     |          | - preguntas     |
| - opciones      |          | - usuario       |
| - respuesta     |          | + generar()     |
+-------------------+         +------------------+
```

## 📌 Diagrama de Casos de Uso
```plaintext
        +---------------------+
        |     Usuario         |
        +---------------------+
                |
        ------------------
        |                |
+----------------+  +-------------------+
| Gestionar     |  | Consultar IA       |
| Tareas       |  | y Recursos         |
+----------------+  +-------------------+
        |                |
+----------------+  +-------------------+
| Agregar Tarea |  | Resolver Problema |
| Ver Tareas    |  | Sugerencias       |
+----------------+  +-------------------+
```

## 📂 Estructura del Proyecto
```plaintext
lexi_synapse/
│── main.py                  # Archivo principal
│── config.py                # Configuración general
│
├── gui/                     # Interfaz gráfica con Tkinter
│   ├── app.py               # Ventana principal
│   ├── calendario.py        # Vista del calendario
│   ├── tareas.py            # Pantalla de gestión de tareas
│   ├── recordatorios.py     # Manejo de recordatorios
│
├── models/                  # Clases principales (POO)
│   ├── usuario.py           # Clase Usuario y Estudiante
│   ├── tarea.py             # Clase Tarea
│   ├── recordatorio.py      # Clase Recordatorio
│   ├── cuestionario.py      # Cuestionarios y preguntas
│   ├── recurso.py           # Recomendaciones de estudio
│
├── controllers/             # Lógica y comunicación entre módulos
│   ├── gestor_tareas.py     # Manejo de tareas
│   ├── gestor_recordatorios.py  # Notificaciones
│   ├── gestor_consultas.py  # Integración con DeepSeek API
│   ├── gestor_recursos.py   # Sugerencias de recursos
│
├── database/                # Base de datos SQLite
│   ├── db.py                # Conexión con SQLite
│   ├── models.sql           # Definición de tablas
│
└── assets/                  # Archivos estáticos
    ├── icons/               # Iconos para la GUI
    ├── styles/              # Estilos visuales
```

## 🌍 Fases del Desarrollo
### 📌 Primera Fase
✅ Definir estructura y base de datos.  
✅ Implementar gestión de tareas y recordatorios.  
✅ Crear interfaz básica en Tkinter.  

### 📌 Segunda Fase
🔄 Integración con DeepSeek API.  
🔄 Implementar IA para personalización del estudio.  
🔄 Mejorar la experiencia del usuario en la interfaz gráfica.  

## 🎯 Próximos Pasos
📌 **Implementación en la Nube** (API Backend).  
📌 **Desarrollo de una Interfaz Completa** con mejor diseño y accesibilidad.  

🚀 **¡Contribuye al proyecto en GitHub!** 💻


