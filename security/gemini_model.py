import os
import google.generativeai as genai
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env en la raíz
load_dotenv()

class GeminiModel:
    def __init__(self):
        # Obtener la API KEY de forma segura
        self.api_key = os.getenv("GEMINI_API_KEY")
        
        if not self.api_key:
            raise ValueError("⚠️ ERROR: No se encontró la variable GEMINI_API_KEY en el archivo .env")
        
        print("✅ Configurando API Key desde variable de entorno...")
        genai.configure(api_key=self.api_key)
        
        # Usar el modelo validado en tu diagnóstico previo
        self.model_name = 'models/gemini-2.0-flash'
        self.model = genai.GenerativeModel(self.model_name)
        print(f"✅ Gemini inicializado con: {self.model_name}")

    def generate(self, text: str):
        try:
            response = self.model.generate_content(text)
            return response.text
        except Exception as e:
            return f"Error en la generación: {e}"