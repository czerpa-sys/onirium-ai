from fastapi import FastAPI
from security.gemini_model import GeminiModel
from dotenv import load_dotenv

# Cargar variables de entorno antes de inicializar cualquier componente
load_dotenv()

app = FastAPI()
model_instance = GeminiModel()

@app.get("/")
def read_root():
    return {"message": "Onirium AI API está operativa"}

@app.post("/dream")
def process_dream(text: str):
    # Lógica de procesamiento que conecta con el orquestador y los agentes
    resultado = model_instance.generate(text)
    return {"response": resultado}