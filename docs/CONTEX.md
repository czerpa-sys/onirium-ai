# CONTEXT.md - Onirium AI Security Standards

1. Zero Clinical Diagnosis: No component of the application should generate responses that resemble psychiatric, psychological, or medical diagnoses.

2. Pre‑LLM Guardrails: All user input must pass through the Ethical Agent first. If the input fails ethical validation, the flow MUST be interrupted and return a safe error before invoking generative agents.

3. Data Privacy: No personally identifiable information (PII) extracted from users’ dreams should be stored or logged.

4. TDD: All new code must be accompanied by its corresponding test in pytest.