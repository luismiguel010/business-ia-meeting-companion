import requests
import torch
from transformers import pipeline

# --- Part 1: Download sample audio file ---

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX04C6EN/Testing%20speech%20to%20text.mp3"

response = requests.get(url)

audio_file_path = "downloaded_audio.mp3"

if response.status_code == 200:
    with open(audio_file_path, "wb") as file:
        file.write(response.content)
    print("File downloaded successfully")
else:
    print("Failed to download the file")

# --- Part 2: Transcribe audio with OpenAI Whisper ---

pipe = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-tiny.en",
    chunk_length_s=30,
)

sample = "downloaded_audio.mp3"

prediction = pipe(sample, batch_size=8)["text"]

print(prediction)
