Onirium AI: Multi-Agent Platform for Symbolic Dream Exploration
Onirium AI is a multi-agent application designed for well-being and playful introspection, built under the Vibe Coding and Agentic Engineering paradigms for the Kaggle & Google 5-Day AI Agents Intensive. It combines a strict separation of concerns with a rigorous, deterministic security framework.

The system uses a third‑party API (Free Tier). Due to the quota limits of the free tier, under heavy demand the system may return an error. This is expected behavior designed to protect the integrity of the service.

🛠️ Technical Architecture (ADK 2.0 Simulated Graph)
The application uses a modular, graph-based workflow design to prevent Context Saturation and securely guide agent trajectories:

Central Orchestrator (OniriumWorkflow): Manages the global state and handles intelligent, code-based routing between execution nodes.

Ethical Agent (EthicalAgent): Operates as the primary Pre-LLM Guardrail.

Symbolic Agent (SymbolicAgent): Analyzes cultural, mythological, and archetypal associations within the dream narrative.

Narrative Agent (NarrativeAgent): Rephrases the dream into structured, metaphorized logs and journals.

Integration Layer (Orchestrator): Performs a final Synthesis & Interpretation step, combining symbolic archetypes and narrative structure into a cohesive, actionable, and clinically-safe insight for the user.

🧠 The Logic Flow
The data flow ensures an efficient and secure execution pipeline:

User Input → Ethical Guardrail (Short-circuit if needed) → Parallel Processing (Symbolic + Narrative Agents) → Integration Layer → Structured JSON Response

🛡️ Security & Risk Mitigation (Shift-Left Design)
Following Day 4 guidelines on agent lifecycle protection, Onirium AI embeds security at the inception of the development process:

Context Engineering (CONTEXT.md): Persistent project-level instructions that enforce safe coding standards directly within the development environment.

Deterministic Short-Circuit Router: The Ethical Agent scans the user input first. If any clinical risks (such as depression, self-harm, suicidal ideation, or severe trauma) are detected, the orchestrator immediately short-circuits the execution before triggering any generative LLM nodes. This prevents unauthorized clinical diagnoses and optimizes token consumption.

Data Privacy: Zero persistence or logging of Personally Identifiable Information (PII).

🧪 Evaluation Framework & Local Testing
The project includes an isolated local validation suite under security/evaluacion_local.py that emulates automated trajectory evaluation metrics:

Test Case 1 (Red Teaming): Validates that the pre-LLM guardrail successfully triggers a short-circuit when facing extreme clinical risk inputs.

Test Case 2 (Clean Trajectory): Verifies that safe dream narratives seamlessly navigate through all multi-agent nodes to completion.

Test Case 3 (Integration Coherence): Validates that the final output JSON contains the full synthesis (Symbolic, Narrative, and Integration) without formatting errors or redundant headers.

💡 Why Onirium AI?
Beyond the code, Onirium AI acts as a digital mirror. By bridging the gap between raw subconscious imagery and structured logical analysis, it empowers users to turn dream-states into personal growth tools, ensuring that the "integration" phase moves from abstract thought into real-world action.

Example of Final JSON Output
JSON
{
  "dream_text": "...",
  "analisis": "1) ANÁLISIS SIMBÓLICO: ... \n\n2) ANÁLISIS NARRATIVO: ... \n\n3) INTEGRACIÓN INTERPRETATIVA NARRATIVO-SIMBÓLICA: ...",
  "status": "success"
}