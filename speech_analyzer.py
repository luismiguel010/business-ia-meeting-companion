import gradio as gr
from transformers import pipeline
import requests

#######------------- LLM -------------####

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"


def query_llm(prompt):
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.1},
    })
    return response.json()["response"]


#######------------- Prompt Template -------------####

PROMPT_TEMPLATE = """List the key points with details from the context:

The context: {context}"""

#######------------- Speech2text -------------####


def transcript_audio(audio_file):
    pipe = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-tiny.en",
        chunk_length_s=30,
    )
    transcript_txt = pipe(audio_file, batch_size=8)["text"]
    prompt = PROMPT_TEMPLATE.format(context=transcript_txt)
    result = query_llm(prompt)
    return result


#######------------- Gradio -------------####

audio_input = gr.Audio(sources="upload", type="filepath")
output_text = gr.Textbox()

iface = gr.Interface(
    fn=transcript_audio,
    inputs=audio_input,
    outputs=output_text,
    title="Audio Transcription App",
    description="Upload the audio file",
)

iface.launch(server_name="0.0.0.0", server_port=7860)
