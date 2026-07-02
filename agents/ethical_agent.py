class EthicalAgent:
    def __init__(self, model):
        # model será el modelo de Antigravity que uses
        self.model = model
        with open("prompts/ethical.txt", "r", encoding="utf-8") as f:
            self.prompt = f.read()

    def run(self, dream_text: str) -> dict:
        """
        Recibe el texto del sueño y devuelve un dict con la evaluación ética.
        """
        # Construimos el mensaje para el modelo
        full_input = f"{self.prompt}\n\nSUEÑO DEL USUARIO:\n{dream_text}"

        # Llamada al modelo (pseudo-código)
        response = self.model.generate(full_input)

        # Aquí asumimos que el modelo devuelve texto en formato JSON
        # En el futuro puedes parsearlo con json.loads(response)
        return {
            "raw_output": response
        }
