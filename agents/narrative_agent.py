class NarrativeAgent:
    def __init__(self, model):
        self.model = model
        with open("prompts/narrative.txt", "r", encoding="utf-8") as f:
            self.prompt = f.read()

    def run(self, dream_text: str) -> dict:
        """
        Crea una narrativa alternativa del sueño.
        """
        full_input = f"{self.prompt}\n\nSUEÑO DEL USUARIO:\n{dream_text}"

        response = self.model.generate(full_input)

        return {
            "raw_output": response
        }
