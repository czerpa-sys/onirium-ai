IMPLEMENTATION_AND_SECURITY.md

# Implementation Details & Security Framework

This section details the technical implementation of Onirium AI, focusing on our multi-agent architecture, the integration of the Model Context Protocol (MCP), and our multi-layered safety guardrails.

## 1. Multi-Agent System (ADK) Implementation
The core logic resides in `orchestrator/orchestrator.py`, which implements a centralized `OniriumWorkflow`. We utilize the Antigravity framework to manage specialized agents, each operating with specific system prompts defined in the `prompts/` directory.

### Agent Specialization:
*   EthicalAgent: The primary "Gatekeeper." It executes before any processing occurs. It uses a rigid system prompt to scan inputs for prohibited clinical terminology or self-harm indicators.
*   SymbolicAgent: Extracts archetypes and symbolic nodes from user narratives. It bridges raw text with psychological frameworks (e.g., Jungian/Freudian) without making diagnostic assertions.
*   NarrativeAgent: The final synthesist. It compiles the symbolic data and emotional tone into a structured, reflective narrative output.

The orchestrator logic ensures asynchronous flow control, ensuring that agents only execute in a defined sequence: Input -> Ethical Validation -> Context Enrichment -> Interpretation -> Output.

## 2. MCP Server Integration
To ensure the agents have "grounded" knowledge, we utilize custom MCP Servers. These act as connectors to static and dynamic data sources:
*   Cultural & Folklore MCP: Provides the agents with regional context based on user geography (e.g., specific Latin American mythological motifs), preventing generic or Eurocentric interpretations.
*   Dream Symbology MCP: Connects the agent to public domain dictionaries of symbols, focusing purely on narrative archetypes.
*   Safety Moderation MCP: A dynamic registry of professional help resources that the agent can retrieve and format as a `[Disclaimer Fijo de Seguridad]` if the user input triggers a sensitivity alert.

## 3. Security Features & Guardrails
Security is not an add-on; it is the first layer of our architecture.
*   Lexical Blacklisting: We implement a strict lexical blocking mechanism in `security/test_security.py`. This ensures that terms related to pathology or crisis are caught before they reach the LLM's reasoning engine.
*   Short-Circuit Execution: If `EthicalAgent` returns a "Safety Violation" flag, the `orchestrator` immediately terminates the process. No data is stored, and the user is provided with the standard Disclaimer.
*   Anonymization Layer: As outlined in our V3_Declaración del Proyecto Onirium AI - Acta de Constitución.pdf (Project Charter), all user data is treated via a "Privacy by Design" approach, ensuring that persisted embeddings in our Vector DB contain no Personally Identifiable Information (PII).

### Testing & Validation
Our `security/evaluacion_local.py` script acts as a unit testing suite for our safety prompts. We perform continuous regression testing against our lexical blacklist to ensure that the AI remains within the intended "non-clinical" boundaries during every deployment cycle.