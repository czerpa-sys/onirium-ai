Onirium AI: Multi-Agent Platform for Symbolic Dream Exploration
Onirium AI is a specialized multi-agent system designed to facilitate secure, non-clinical dream exploration through narrative and symbolic analysis. It serves as a responsible alternative to exploitative "premonitory" websites by providing a safe, introspection-focused container for users to explore symbolic meaning.

Executive Summary
Onirium AI addresses the cultural gap in digital spaces where users are frequently exposed to unverified prophetic claims. By adopting a "Privacy by Design" and "Safety-First" architecture, the system transforms raw dream input into structured, insightful, and safe narrative outputs for introspection.

Architecture
The system utilizes an orchestrator-based multi-agent topology to manage task delegation.

Orchestration: The core logic resides in orchestrator/orchestrator.py, implementing an OniriumWorkflow that manages agent sequences.

Specialized Agents:

EthicalAgent (Gatekeeper): Scans inputs for prohibited clinical terminology or self-harm indicators before any generative processing.

SymbolicAgent: Extracts archetypes and symbolic nodes without making diagnostic assertions.

NarrativeAgent: Synthesizes symbolic data and emotional tone into structured, reflective outputs.

MCP Integration: Custom Model Context Protocol (MCP) servers act as connectors to cultural, folklore, and dream symbology databases, providing grounded, regional context.

Security & Privacy Standards
Security is the first layer of our architecture, not an add-on.

Zero Clinical Diagnosis: No component of the application generates responses that resemble psychiatric or medical diagnoses.

Pre-LLM Guardrails: All user input must pass through the Ethical Agent; if validation fails, the flow is interrupted immediately.

Data Privacy: Zero persistence or logging of Personally Identifiable Information (PII) extracted from user dreams.

TDD Approach: Development follows a test-driven approach, with security/evaluacion_local.py ensuring safety prompts function as intended during every deployment cycle.

Future Scalability
Onirium AI is built as a product-ready architecture with clear pathways for expansion:

Narrative Well-being: Evolving agents to act as "Non-Clinical Companions" for emotional vocabulary tracking.

Domain Adaptation: By swapping "context databases" via our Cultural MCP Servers, the engine can be ported to other narrative domains like education or professional writing coaching.

API-First Design: The architecture is built to serve as a backend service for diverse platforms, from web interfaces to community forums.

Quick Start & Testing
The project includes an isolated validation suite. Use the following to verify integrity:

Regression Testing: Run security/evaluacion_local.py to validate lexical blacklisting and short-circuit execution.

For a detailed demonstration of this workflow, visit our Kaggle Notebook.

## Live Demo & References
For a full demonstration of the execution flow, system logs, and the architecture in action, you can visit our official Notebook on Kaggle:

👉 [Onirium AI - Kaggle Notebook](https://www.kaggle.com/code/carlosenriquezerpa/onirium-artificial-intelligence-agent-orchestrat)
