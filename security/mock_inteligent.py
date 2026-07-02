import random

class SmartMockModel:
    def generate(self, prompt: str) -> str:
        # Banco de interpretaciones creativas (Simulando Temperatura 0.7)
        respuestas = [
            f"Bajo una lente simbólica, tu sueño sobre '{prompt[:20]}...' sugiere una necesidad de integrar aspectos de tu vida que parecen estar desconectados. Es un llamado a la reconciliación interna.",
            f"Analizando la narrativa de '{prompt[:20]}...', el sistema detecta una fuerte carga de simbolismo emocional. Podría representar un proceso de transición, donde lo antiguo cede paso a una nueva consciencia.",
            f"El sueño que describes ('{prompt[:20]}...') parece actuar como un espejo de tus preocupaciones actuales, proyectando un deseo de encontrar armonía en situaciones donde sientes que el mensaje no logra llegar.",
            f"Desde una perspectiva de psicología analítica, el relato de '{prompt[:20]}...' sugiere que estás explorando un territorio desconocido en tu psique, buscando validar tus propias verdades ante el entorno."
        ]
        
        # Elegimos una interpretación al azar para simular la variabilidad de la temperatura
        return random.choice(respuestas)