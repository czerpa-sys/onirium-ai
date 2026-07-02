class SymbolicAgent:
    def __init__(self, model):
        self.model = model
        with open("prompts/symbolic.txt", "r", encoding="utf-8") as f:
            self.prompt = f.read()

    def run(self, dream_text: str) -> dict:
        """
        Genera asociaciones simbólicas y culturales del sueño.
        """
        full_input = f"{self.prompt}\n\nSUEÑO DEL USUARIO:\n{dream_text}"

        response = self.model.generate(full_input)

        return {
            "raw_output": response
        }
