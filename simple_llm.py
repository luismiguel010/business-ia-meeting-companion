import requests

# Initialize Ollama LLM (replaces IBM WatsonX)
# Make sure Ollama is running: ollama serve
# And the model is pulled: ollama pull llama3.2

OLLAMA_URL = "http://localhost:11434/api/generate"

response = requests.post(OLLAMA_URL, json={
    "model": "llama3.2",
    "prompt": "How to read a book effectively?",
    "stream": False,
    "options": {"temperature": 0.1},
})

print(response.json()["response"])
