# 📚 RAG & Knowledge Systems — Complete Catalog

> Every RAG framework, vector database, and knowledge management tool.

---

## 🏆 Top RAG Projects

| Project | Stars | Description | Language |
|---------|-------|-------------|----------|
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | 81K | Leading open-source RAG engine | Python |
| [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | 36K | Simple and fast RAG | Python |
| [microsoft/graphrag](https://github.com/microsoft/graphrag) | 33K | Graph-based RAG | Python |
| [NirDiamant/RAG_Techniques](https://github.com/NirDiamant/RAG_Techniques) | 28K | Advanced RAG techniques | Jupyter |
| [SciPhi-AI/R2R](https://github.com/SciPhi-AI/R2R) | 7.9K | Production-ready retrieval | Python |
| [weaviate/Verba](https://github.com/weaviate/Verba) | 7.7K | Weaviate RAG chatbot | Python |
| [Marker-Inc-Korea/AutoRAG](https://github.com/Marker-Inc-Korea/AutoRAG) | 4.8K | Auto-optimize RAG | Python |
| [truefoundry/cognita](https://github.com/truefoundry/cognita) | 4.4K | Modular RAG | Python |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | 50K | Document agent + RAG | Python |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | 138K | LLM framework + RAG | Python |

---

## 🗄️ Vector Databases

| Database | Stars | Type | License | Best For |
|----------|-------|------|---------|----------|
| [milvus-io/milvus](https://github.com/milvus-io/milvus) | 35K | Distributed | Apache 2.0 | Production scale |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | 23K | Rust-based | Apache 2.0 | Performance |
| [weaviate/weaviate](https://github.com/weaviate/weaviate) | 13K | Hybrid search | BSD-3 | Hybrid search |
| [chroma-core/chroma](https://github.com/chroma-core/chroma) | 19K | Embedded | Apache 2.0 | Development |
| [pgvector/pgvector](https://github.com/pgvector/pgvector) | 14K | PostgreSQL ext | PostgreSQL | Existing PG users |
| [lancedb/lancedb](https://github.com/lancedb/lancedb) | 6.5K | Embedded | Apache 2.0 | Serverless |
| [marqo-ai/marqo](https://github.com/marqo-ai/marqo) | 4.8K | Tensor search | Apache 2.0 | E-commerce |
| [vespa-engine/vespa](https://github.com/vespa-engine/vespa) | 6.2K | Big data | Apache 2.0 | Large scale |
| [pinecone-io/pinecone](https://github.com/pinecone-io/pinecone) | - | Managed | Proprietary | Serverless |
| [redis/redis](https://github.com/redis/redis) | 68K | In-memory | BSD-3 | Real-time |
| [opensearch-project/OpenSearch](https://github.com/opensearch-project/OpenSearch) | 10K | Search | Apache 2.0 | Full-text + vector |
| [Vald](https://github.com/vdaas/vald) | 1.7K | Distributed | Apache 2.0 | Cloud native |
| [tantivy-search/tantivy](https://github.com/tantivy-search/tantivy) | 12K | Rust search | MIT | Embedded |
| [facebooik/faiss](https://github.com/facebookresearch/faiss) | 32K | Similarity search | MIT | Research |
| [nmslib/hnswlib](https://github.com/nmslib/hnswlib) | 4.5K | HNSW | Apache 2.0 | Fast ANN |

---

## 🔍 RAG Techniques

### Basic Patterns
1. **Naive RAG** → Chunk → Embed → Retrieve → Generate
2. **Advanced RAG** → Query routing, reranking, hybrid search
3. **Modular RAG** → Flexible pipeline components
4. **Agentic RAG** → Agent decides when/how to retrieve

### Advanced Techniques (from RAG_Techniques repo)
- **Query Rewriting** — Improve retrieval with LLM-rewritten queries
- **HyDE** — Hypothetical Document Embeddings
- **Multi-Query** — Generate multiple queries for better coverage
- **Parent-Child Chunking** — Hierarchical document structure
- **Sentence Window** — Context around retrieved chunks
- **RAPTOR** — Recursive Abstractive Processing
- **Self-RAG** — Self-reflective retrieval
- **Corrective RAG (CRAG)** — Verify and correct retrieval
- **Graph RAG** — Knowledge graph + vector search
- **Adaptive RAG** — Dynamic retrieval strategy

---

## 📄 Document Processing

| Tool | Description | Stars |
|------|-------------|-------|
| [run-llama/llama_parse](https://github.com/run-llama/llama_parse) | Document parsing | - |
| [run-llama/liteparse](https://github.com/run-llama/liteparse) | Lightweight parsing | 59 |
| [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | OCR (78K stars) | 78K |
| [deepset-ai/haystack](https://github.com/deepset-ai/haystack) | NLP pipeline | - |
| [unstructured-io/unstructured](https://github.com/unstructured-io/unstructured) | Document processing | - |
| [Marker](https://github.com/datalab-to/marker) | PDF to Markdown | - |

---

## 🏗️ RAG Architecture Patterns

### Pattern 1: Basic RAG
```
Query → Embed → Vector Search → Top-K Chunks → Augment Prompt → LLM → Answer
```

### Pattern 2: Hybrid RAG
```
Query → [Vector Search + BM25] → Reranker → Top-K → Augment → LLM → Answer
```

### Pattern 3: Graph RAG
```
Query → Entity Extraction → Graph Traversal + Vector Search → Augment → LLM → Answer
```

### Pattern 4: Agentic RAG
```
Query → Agent → [Decide: Retrieve? Search? Calculate?] → Tools → LLM → Answer
```

### Pattern 5: Multi-Modal RAG
```
Query → [Text + Image + Table] → Multi-Modal Embedding → Search → Augment → LLM → Answer
```

---

*Last updated: 2026-05-25*
