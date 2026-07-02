from ethical_agent import EthicalAgent
from symbolic_agent import SymbolicAgent
from narrative_agent import NarrativeAgent

# Aquí "model" sería el objeto del modelo de Antigravity
model = ...  # lo que el codelab te indique

ethical = EthicalAgent(model)
symbolic = SymbolicAgent(model)
narrative = NarrativeAgent(model)

dream = "Anoche soñé que caminaba por un bosque oscuro y encontraba una luz al final."

print(ethical.run(dream))
print(symbolic.run(dream))
print(narrative.run(dream))
