# Metacortex v0.1 - System Overview

This document describes the structural layout, component responsibilities, and processing flow of the `Metacortex v0.1` system. The system is designed as an experimental neural-symbolic architecture that interfaces with external LLMs (e.g., Mistral via Ollama) and applies Fourier-based structural decomposition to reason over axiomatic semantic dimensions.

---

## Project Structure

```
development/
├── metacortex/
│   ├── v0.1/
│   │   ├── core/              # Core processing logic
│   │   ├── api/               # FastAPI endpoints
│   │   ├── modules/           # Optional plugins or subcomponents
│   │   └── README.md          # This documentation
├── compass/
│   ├── v0.1/                  # Semantic decomposition logic (pre-superposition)
```

---

## Component Overview

### 1. `api/`

* **Purpose**: Acts as the external interface to receive queries.
* **Framework**: FastAPI
* **Responsibilities**:

  * Accept text input via POST.
  * Normalize request.
  * Forward to `core/metacortex_engine.py`.

### 2. `core/metacortex_engine.py`

* **Purpose**: Central controller for processing, transformation, and reasoning.
* **Responsibilities**:

  * Build symbolic and structural network.
  * Integrate Fourier-based vector processing.
  * Trigger `SuperpositionEngine`.

### 3. `core/superposition_response.py`

* **Purpose**: Analyze and process overlapping vector structures.
* **Responsibilities**:

  * Accept semantic vectors.
  * Apply interference logic (not mean-based).
  * Respect axis-defined weighting via axioms.
  * Forward to `token_engine`.

### 4. `core/token_engine.py`

* **Purpose**: Generate response text from interfered vector space.
* **Responsibilities**:

  * Synthesize meaningful output.
  * Log key semantic anchors.
  * Return final result.

---

## Processing Pipeline

```
User Input → FastAPI (api/routes.py)
            ↓
   Metacortex Engine (core/metacortex_engine.py)
            ↓
   Superposition Processing (core/superposition_response.py)
            ↓
   Token Generation (core/token_engine.py)
            ↓
         Response → Console / API Response
```

---

## Planned Extensions

* **Q-Transform Layer**: Quantization and decoherence of vector states.
* **Goal Anchoring**: Matching against long-term goal vector (COMPASS interface).
* **Semantic Mirror**: Add module to reflect human conceptual axis back into feedback loop.
* **Interactive Tuning**: Interface to adjust weightings per Axiom manually.

---

## External Components

* **Ollama**: Container-based Mistral interface for external LLM reasoning.
* **COMPASS**: Handles semantic decomposition and axiom grounding.
* **ArangoDB** *(temporarily disabled)*: Will store historical responses and vector resonance snapshots for learning.

---

> All components are subject to modular replacement or upgrade. This version (v0.1) serves as a minimal working scaffold for symbolic-structural reasoning pipelines.

---

**Author:** dwpplumb
**License:** Experimental, CC-BY 4.0 or similar
