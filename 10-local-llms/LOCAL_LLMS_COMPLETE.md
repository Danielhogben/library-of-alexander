# 🖥️ Local LLMs — Complete Guide

> Run AI models on your own hardware. Every tool, model format, and optimization technique.

---

## 🏆 Best Local LLM Runners

| Tool | Platform | UI | Best For | Ease |
|------|----------|-----|----------|------|
| [Ollama](https://ollama.com) | Mac/Linux/Windows | CLI + API | General purpose | ⭐⭐⭐⭐⭐ |
| [LM Studio](https://lmstudio.ai) | Mac/Linux/Windows | GUI | Beginners | ⭐⭐⭐⭐⭐ |
| [Jan](https://jan.ai) | Mac/Linux/Windows | GUI | Privacy-focused | ⭐⭐⭐⭐ |
| [GPT4All](https://gpt4all.io) | Mac/Linux/Windows | GUI | Offline chat | ⭐⭐⭐⭐ |
| [Faraday.dev](https://faraday.dev) | Mac | GUI | No-code local AI | ⭐⭐⭐⭐⭐ |
| [Text Generation WebUI](https://github.com/oobabooga/text-generation-webui) | Mac/Linux/Windows | Web UI | Power users | ⭐⭐⭐ |
| [KoboldCpp](https://github.com/LostRuins/koboldCpp) | Mac/Linux/Windows | Web UI | GGUF inference | ⭐⭐⭐ |
| [llama.cpp](https://github.com/ggerganov/llama.cpp) | All | CLI | Engine/backend | ⭐⭐ |
| [vLLM](https://github.com/vllm-project/vllm) | Linux | API | Production serving | ⭐⭐⭐ |
| [TGI](https://github.com/huggingface/text-generation-inference) | Linux | API | HuggingFace models | ⭐⭐⭐ |
| [MLX](https://github.com/ml-explore/mlx) | Apple Silicon | Framework | Apple developers | ⭐⭐⭐ |
| [llamafile](https://github.com/Mozilla-Ocho/llamafile) | All | CLI | Single-file LLM | ⭐⭐⭐⭐ |
| [Tabby](https://github.com/TabbyML/tabby) | All | API | Code completion | ⭐⭐⭐ |
| [Open WebUI](https://github.com/open-webui/open-webui) | All | Web UI | Ollama frontend | ⭐⭐⭐⭐ |
| [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) | All | Desktop | RAG + local LLM | ⭐⭐⭐⭐ |

---

## 📦 Model Formats

| Format | Size | Speed | Quality | Tools |
|--------|------|-------|---------|-------|
| GGUF | Medium | Fast | Good | llama.cpp, Ollama, LM Studio |
| EXL2 | Small | Fast | Very Good | ExLlamaV2 |
| GPTQ | Small | Fast | Good | AutoGPTQ, vLLM |
| AWQ | Small | Very Fast | Good | AutoAWQ, vLLM |
| BNB 4-bit | Small | Medium | Good | bitsandbytes |
| BNB 8-bit | Medium | Medium | Very Good | bitsandbytes |
| FP16 | Large | Slow | Best | PyTorch |
| FP8 | Medium | Fast | Very Good | vLLM, TGI |
| Q4_K_M | Small | Fast | Good | GGUF standard |
| Q5_K_M | Medium | Fast | Very Good | GGUF standard |
| Q8_0 | Medium | Fast | Excellent | GGUF standard |
| F16 | Large | Slow | Best | GGUF standard |

---

## 🏆 Best Models to Run Locally (by VRAM)

### 4GB VRAM (RTX 3050 / M1 8GB)
| Model | Params | Format | Quality |
|-------|--------|--------|---------|
| Qwen3-4B | 4B | Q4_K_M | Excellent |
| Gemma 4 4B | 4B | Q4_K_M | Very Good |
| Phi-4-mini | 3.8B | Q4_K_M | Very Good |
| MiniCPM-2B | 2B | Q4_K_M | Good |
| Qwen3-1.7B | 1.7B | Q4_K_M | Good |
| SmolLM2-1.7B | 1.7B | Q4_K_M | Decent |

### 8GB VRAM (M1/M2 16GB / RTX 3060)
| Model | Params | Format | Quality |
|-------|--------|--------|---------|
| Qwen3-8B | 8B | Q4_K_M | Excellent |
| Gemma 4 12B | 12B | Q4_K_M | Very Good |
| Phi-4 | 14B | Q4_K_M | Very Good |
| MiniCPM-8B | 8B | Q4_K_M | Very Good |
| Mistral Small 3.1 | ~14B | Q4_K_M | Very Good |
| DeepSeek-R1-8B | 8B | Q4_K_M | Excellent |

### 16GB VRAM (RTX 4060 Ti / M2 Pro)
| Model | Params | Format | Quality |
|-------|--------|--------|---------|
| Qwen3-14B | 14B | Q4_K_M | Excellent |
| Gemma 4 27B | 27B | Q4_K_M | Excellent |
| DeepSeek-R1-14B | 14B | Q4_K_M | Excellent |
| Llama 4 Scout | 17B | Q4_K_M | Excellent |
| Qwen3-32B | 32B | Q4_K_M | Outstanding |

### 24GB VRAM (RTX 3090/4090 / M2 Ultra)
| Model | Params | Format | Quality |
|-------|--------|--------|---------|
| Qwen3-72B | 72B | Q4_K_M | Outstanding |
| DeepSeek-R1-70B | 70B | Q4_K_M | Outstanding |
| Llama 4 Maverick | 400B MoE | Q4_K_M | Outstanding |
| Qwen3-Coder-480B | 480B MoE | Q4_K_M | Frontier |

### 48GB+ VRAM (A100 / Multi-GPU)
| Model | Params | Format | Quality |
|-------|--------|--------|---------|
| DeepSeek-V3 | 671B MoE | FP8 | Frontier |
| DeepSeek-R1 | 671B MoE | FP8 | Frontier |
| Qwen3-480B | 480B MoE | FP8 | Frontier |

---

## ⚡ Optimization Techniques

| Technique | Memory Reduction | Speed Impact | Quality Impact |
|-----------|-----------------|--------------|----------------|
| 4-bit quantization (Q4_K_M) | 75% | Faster | Minimal |
| 8-bit quantization (Q8_0) | 50% | Same | Negligible |
| Flash Attention 2 | 30% memory | 2x faster | None |
| Flash Attention 3 | 40% memory | 3x faster | None |
| PagedAttention (vLLM) | 50% memory | Faster | None |
| Speculative decoding | N/A | 2-3x faster | None |
| KV cache quantization | 50% KV memory | Slight | Minimal |
| CPU offloading | Unlimited | Slower | None |
| Model sharding | Distributed | Same | None |
| GGUF K-quants | 60-75% | Faster | Minimal |

---

## 🔧 Serving Infrastructure

| Tool | Use Case | Throughput | Ease |
|------|----------|------------|------|
| [vLLM](https://github.com/vllm-project/vllm) | Production serving | Very High | Medium |
| [TGI](https://github.com/huggingface/text-generation-inference) | HuggingFace serving | High | Medium |
| [SGLang](https://github.com/sgl-project/sglang) | Structured generation | Very High | Medium |
| [LMDeploy](https://github.com/InternLM/lmdeploy) | TurboMind inference | Very High | Medium |
| [llama.cpp](https://github.com/ggerganov/llama.cpp) | Edge/embedded | Medium | Easy |
| [Ollama](https://ollama.com) | Local development | Medium | Very Easy |
| [LiteLLM](https://github.com/BerriAI/litellm) | API gateway | High | Easy |
| [OpenRouter](https://openrouter.ai) | Cloud routing | High | Very Easy |

---

*Last updated: 2026-05-25*
