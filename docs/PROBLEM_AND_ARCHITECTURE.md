# Problem Statement & Solution Architecture

## 1. Problem Statement: The Cultural and Ethical Void
While generative AI models have democratized content, they have also amplified a dangerous trend in Latin American and Brazilian digital spaces: the proliferation of irresponsible, "prophetic" dream interpretation websites.

*   The Problem of "Premonitory Divination": Many platforms exploit ingrained cultural beliefs by presenting dream interpretations as literal "premonitions" or "prophecies." This creates unnecessary anxiety and distorts the user's reality, often leading to superstition-based distress.
*   The Hallucination of Clinical Diagnosis: Beyond divination, mainstream models frequently provide unsolicited medical advice, creating ethical liabilities.
*   Lack of Contextual Depth: Without external knowledge grounding, interpretations remain superficial, failing to connect user narratives with established symbolic or cultural frameworks that respect the user's specific regional background.

Onirium AI was built to reclaim this space for responsible introspection. We offer a "safe container" where users can explore symbolic meaning without the risk of inappropriate clinical assessments or exploitative divination claims.


## 2. Solution Architecture: The Multi-Agent Orchestrator
To address these challenges, Onirium AI implements a robust multi-agent topology designed for resilience and ethical compliance, as detailed in our V3_Declaración del Proyecto Onirium AI - Acta de Constitución.pdf [Project Charter].

The architecture utilizes an asynchronous flow, as visualized in Gemini_Generated_Image_3djf2f3djf2f3djf.png, following these operational stages:

| Stage | Component | Responsibility |
| :--- | :--- | :--- |
| **Ingestion** | API Gateway & Ethical Layer | Intercepts input, applies strict lexical blacklists, and validates age/safety compliance. |
| **Routing** | Pub/Sub Event Router | Ensures asynchronous handling of user requests. |
| **Orchestration**| Multi-Agent Orchestrator (Antigravity) | The central brain. Coordinates specialized agents (Symbolic, Narrative, Ethical)[cite: 5]. |
| **Context** | MCP Servers | Dynamically fetches cultural, symbolic, and safety contexts to ground agent responses. |
| **Storage** | Vector DB & BigQuery | Manages persistent embeddings for pattern recognition (recurrence detection) while maintaining data anonymization. |


By decoupling the Safety Layer from the Interpretation Engine via an Orchestrator, we ensure that no narrative output reaches the user without first passing through the moderation gates. This design leverages MCP (Model Context Protocol) to provide agents with the necessary cultural nuance, ensuring that interpretations are based on symbolic archetypes rather than fabricated clinical observations.