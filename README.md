# Business AI Meeting Companion - Speech to Text

Aplicacion de IA que transcribe audio de reuniones y extrae los puntos clave usando un LLM local.

Basado en el lab de [IBM - Coursera](https://www.coursera.org/), adaptado para ejecutarse completamente en local usando **Ollama** en lugar de IBM WatsonX.

## Stack Tecnologico

| Tecnologia | Uso |
|---|---|
| [OpenAI Whisper](https://github.com/openai/whisper) | Convierte audio a texto (Speech-to-Text) via Hugging Face Transformers |
| [Ollama](https://ollama.ai) + Llama 3.2 | LLM local para resumir y extraer puntos clave (reemplaza IBM WatsonX) |
| [Gradio](https://gradio.app) | Interfaz web para subir audio y ver resultados |

## Estructura del Proyecto

```
business-ia-meeting-companion/
├── simple_speech2text.py   # Step 1: Descarga audio de ejemplo y lo transcribe con Whisper
├── hello.py                # Gradio demo: app "Hello World" para familiarizarse con Gradio
├── speech2text_app.py      # Step 2: App Gradio para subir audio y transcribirlo
├── simple_llm.py           # Step 3: Prueba del LLM (Ollama) con una pregunta simple
├── speech_analyzer.py      # Step 4: App final - audio → transcripcion → puntos clave
├── requirements.txt        # Dependencias Python
└── README.md
```

## Descripcion de Cada Archivo

### `simple_speech2text.py`
Descarga un archivo MP3 de ejemplo desde IBM Cloud y lo transcribe usando el modelo `openai/whisper-tiny.en`. Sirve para verificar que Whisper funciona correctamente.

### `hello.py`
App minima de Gradio que recibe un nombre y devuelve un saludo. Sirve para familiarizarse con la creacion de interfaces web con Gradio.

### `speech2text_app.py`
App de Gradio que permite subir un archivo de audio y devuelve la transcripcion. Combina Whisper con una interfaz web.

### `simple_llm.py`
Script de prueba que envia una pregunta a Ollama (Llama 3.2) via su API REST local y muestra la respuesta. Verifica que el LLM funciona antes de integrarlo con el resto.

### `speech_analyzer.py`
La app final que une todo el flujo:
1. El usuario sube un archivo de audio via Gradio
2. Whisper transcribe el audio a texto
3. El texto se inserta en un prompt template que pide extraer puntos clave
4. Ollama (Llama 3.2) procesa el prompt y devuelve los puntos clave
5. El resultado se muestra en la interfaz web

## Requisitos Previos

- Python 3.10+
- [Ollama](https://ollama.ai) instalado
- ffmpeg instalado

### Instalacion en macOS

```bash
brew install ollama ffmpeg
```

Descargar el modelo Llama 3.2:

```bash
ollama pull llama3.2
```

## Instalacion del Proyecto

```bash
git clone <tu-repositorio>
cd business-ia-meeting-companion
```

Crear y activar el entorno virtual:

```bash
python3 -m venv venv        # crea el entorno virtual en la carpeta venv/
source venv/bin/activate     # activa el entorno virtual (veras "(venv)" en tu terminal)
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

> Cada vez que abras una terminal nueva, necesitas activar el entorno virtual con `source venv/bin/activate` antes de ejecutar los scripts.

## Ejecucion

Antes de ejecutar cualquier script que use el LLM, asegurate de que Ollama este corriendo:

```bash
ollama serve
```

### Step 1: Probar Speech-to-Text

```bash
python3 simple_speech2text.py
```

Descarga un audio de ejemplo y muestra la transcripcion en consola.

### Step 2: Probar Gradio

```bash
python3 hello.py
```

Abre http://localhost:7860 en tu navegador.

### Step 3: App de transcripcion de audio

```bash
python3 speech2text_app.py
```

Abre http://localhost:7860, sube un archivo MP3 y obtendras la transcripcion.

### Step 4: Probar el LLM

```bash
python3 simple_llm.py
```

Muestra la respuesta del modelo a la pregunta "How to read a book effectively?".

### Step 5: App completa

```bash
python3 speech_analyzer.py
```

Abre http://localhost:7860, sube un audio de una reunion y obtendras los puntos clave extraidos por el LLM.

## Diferencias con el Lab Original

| Lab Original (IBM) | Este Proyecto (Local) |
|---|---|
| IBM WatsonX + credenciales cloud | Ollama corriendo localmente, sin API keys |
| `ibm_watson_machine_learning` SDK | Llamadas HTTP directas a Ollama (`requests`) |
| LangChain para orquestar prompts | Prompt template con f-string de Python |
| Entorno Skills Network de IBM | Virtual environment local |
