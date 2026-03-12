# RAG-Based Wine Recommendation System

This project demonstrates the implementation of a **Retrieval-Augmented Generation (RAG)** pipeline using a local LLM infrastructure. It compares standard LLM responses against responses augmented with domain-specific data retrieved from a vector database.

# Recall

from the trained model how much of correct data is retrived

# Precission

from the out put how much is correct percentage

## Technical Stack

* **Vector Database:** Qdrant (In-memory)
* **Orchestration:** Python (Pandas)
* **Embeddings & LLM:** OpenAI-compatible API (LM Studio)
* **Models used:** * `nomic-embed-text-v1.5` (Embeddings)
* `qwen2.5-coder-3b-instruct` / `ministral-3-3b` (Inference)



---

## Core Learning Objectives

### 1. Vectorization and Data Structuring

The workflow transforms a flat CSV dataset (`top_rated_wines.csv`) into high-dimensional vectors.

* **PointStruct:** Learning how to encapsulate unique IDs, vector arrays, and metadata (payload) for storage.
* **Cold Start:** Handling missing data using `fillna('')` to prevent encoding errors.

### 2. Semantic Search vs. Keyword Search

By utilizing `COSINE` distance within Qdrant, the system identifies wines based on the "intent" and "notes" rather than exact string matches. The query "Suggest me an amazing Malbec" retrieves results by comparing the vector of the user prompt against the vector of the wine descriptions.

### 3. The RAG Pattern

The code illustrates the three-step RAG architecture:

1. **Retrieval:** Querying Qdrant to find the top 3 most relevant wine records.
2. **Augmentation:** Injecting the retrieved records (`fullList`) into the LLM context.
3. **Generation:** Forcing the LLM to base its specialized recommendation on the provided dataset rather than general training data.

### 4. Local LLM Integration

The project demonstrates how to point the `OpenAI` Python client to a local server (`http://localhost:1234/v1`). This allows for:

* Data privacy (no external API calls for sensitive data).
* Cost-free experimentation with different model architectures.

---

## Implementation Workflow

### Data Ingestion

```python
# Encoding wine notes into vectors
vector=encoder.embeddings.create(
    input=doc["notes"],
    model="text-embedding-nomic-embed-text-v1.5"
).data[0].embedding

```

### Collection Configuration

The Qdrant collection is configured to match the specific output dimensions of the Nomic model (768 dimensions), ensuring mathematical compatibility during the search phase.

### Prompt Engineering

The system compares two methods:

* **Zero-Shot:** The LLM relies on internal knowledge.
* **RAG-Injected:** The assistant role is pre-loaded with retrieved wine data, ensuring the final suggestion exists within the local `top_rated_wines.csv` database.