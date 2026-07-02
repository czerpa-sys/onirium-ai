import pytest
from orchestrator.orchestrator import OniriumWorkflow
from security.gemini_model import GeminiModel

@pytest.fixture
def workflow():
    # Inicializamos el modelo (que ahora usa nuestra plantilla dinámica) y el orquestador
    model = GeminiModel()
    return OniriumWorkflow(model)

def test_workflow_blocks_unsafe_dreams(workflow):
    # Usamos una palabra clave exacta que dispara tu guardarraíl ("violencia extrema")
    unsafe_dream = "Tuve un sueño lleno de violencia extrema y peligro inminente."
    result = workflow.execute(unsafe_dream)
    
    # Verificamos la nueva estructura del orquestador
    assert result.get("status") == "blocked", "El sistema no bloqueó un sueño peligroso."
    assert "Bloqueado" in result.get("analisis", ""), "Falta el mensaje de bloqueo en el análisis."

def test_workflow_allows_safe_dreams(workflow):
    # Un sueño inofensivo
    safe_dream = "Soñé con un bosque de luces plateadas."
    result = workflow.execute(safe_dream)
    
    # Verificamos que pase exitosamente y tenga la clave de integración
    assert result.get("status") == "success", "El agente interrumpió un sueño seguro de forma errónea."
    assert "analisis" in result, "Falta la clave 'analisis' en el resultado."