from orchestrator import Orchestrator

# Modelo placeholder (cuando uses Antigravity, aquí va el modelo real)
class ModeloFalso:
    def generate(self, prompt):
        return "Salida simulada del modelo para pruebas."

model = ModeloFalso()

orq = Orchestrator(model)

sueño = "Soñé que caminaba por un puente que se movía como si estuviera vivo."

resultado = orq.run(sueño)

print(resultado)

