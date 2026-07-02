# orchestrator/orchestrator.py
import sys
import os

from agents.ethical_agent import EthicalAgent
from agents.symbolic_agent import SymbolicAgent
from agents.narrative_agent import NarrativeAgent

class OniriumWorkflow:
    def __init__(self, model):
        self.ethical = EthicalAgent(model)
        self.symbolic = SymbolicAgent(model)
        self.narrative = NarrativeAgent(model)

    def _extract_text(self, result) -> str:
        if isinstance(result, dict):
            return result.get("raw_output", str(result))
        return str(result)

    def execute(self, dream_text: str) -> dict:
        print(f"   [Grafo ADK] Procesando entrada: {dream_text[:50]}...")
        
        # 1. Evaluación Ética (Que ahora incluye la Integración)
        ethical_result = self.ethical.run(dream_text)
        ethical_text = self._extract_text(ethical_result)
        
        print(f"   DEBUG (Agente Ético dijo): {ethical_text}")
        
        # 2. Lógica de seguridad
        block_keywords = ["violencia extrema", "abuso sexual", "peligro inminente"]
        is_blocked = any(kw in ethical_text.lower() for kw in block_keywords)
        
        if is_blocked:
            print("   ⚠️ [BLOQUEO]: Riesgo real detectado.")
            return {
                "dream_text": dream_text,
                "analisis": "Bloqueado por seguridad ética estricta.",
                "status": "blocked"
            }

        # 3. Avanzamos al flujo principal
        print("   ✅ [Nodo Ético Aprobado]: Pasando a nodos de análisis.")
        
        sym_result = self.symbolic.run(dream_text)
        narr_result = self.narrative.run(dream_text)
        
        sym_text = self._extract_text(sym_result)
        narr_text = self._extract_text(narr_result)
        
        # 4. LA SOLUCIÓN: Unimos las tres partes limpiamente para el usuario final
        analisis_final = (
            f"{sym_text}\n"
            f"{narr_text}\n"
            f"{ethical_text}"
        )
        
        return {
            "dream_text": dream_text,
            "analisis": analisis_final,
            "status": "success"
        }