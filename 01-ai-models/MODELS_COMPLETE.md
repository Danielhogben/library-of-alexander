# 🤖 AI Models — Complete Catalog

> Every notable AI model across all modalities. Organized by category.

---

## 📊 Model Landscape 2026

```
Frontier Models (Closed):
├── GPT-5.1 / GPT-5.1-Codex-Max (OpenAI) — Best overall + coding
├── Claude Opus 4.5 / Sonnet 4.5 (Anthropic) — Best reasoning + safety
├── Gemini 3 Pro / Gemini 3 Flash (Google) — Best multimodal
├── Grok 4 (xAI) — Best real-time knowledge
└── Doubao / Kimi k2 (China) — Best Chinese capability

Open-Weight Frontier:
├── DeepSeek-V3 / R1 (671B MoE) — Best open reasoning
├── Qwen3-Coder-480B — Best open coding
├── Llama 4 Maverick / Scout — Best open general
├── GLM-4-Plus — Best Chinese open
└── MiniMax-M1 — Best open reasoning (hybrid attention)

Small Models (<10B):
├── Gemma 4 (1B-27B) — Google's efficient family
├── Phi-4 (14B) — Microsoft's reasoning model
├── Qwen3 (0.5B-72B) — Alibaba's full family
├── MiniCPM (2B-8B) — Best edge model
└── Mistral Small 3.1 — Best European model
```

---

## 🧠 Large Language Models (LLMs)

### Frontier Closed Models

| Model | Provider | SWE-bench | Context | Strengths |
|-------|----------|-----------|---------|-----------|
| GPT-5.1-Codex-Max | OpenAI | 77.9% | 128K | Best coding |
| GPT-5 | OpenAI | 74.9% | 128K | General purpose |
| GPT-5 mini | OpenAI | 71.0% | 128K | Fast + cheap |
| Claude Opus 4.5 | Anthropic | 80.9% | 200K | Best reasoning |
| Claude Sonnet 4.5 | Anthropic | 77.2% | 200K | Best balance |
| Claude Haiku 4.5 | Anthropic | ~70% | 200K | Fast + cheap |
| Gemini 3 Pro | Google | 76.2% | 1M | Best multimodal |
| Gemini 3 Flash | Google | ~65% | 1M | Fast multimodal |
| Grok 4 | xAI | ~70% | 128K | Real-time data |
| o3 | OpenAI | ~72% | 200K | Deep reasoning |
| o4-mini | OpenAI | ~68% | 200K | Fast reasoning |

### Open-Weight Frontier Models

| Model | Params | SWE-bench | Context | License | Provider |
|-------|--------|-----------|---------|---------|----------|
| DeepSeek-V3 | 671B (37B active) | ~70% | 128K | MIT | DeepSeek |
| DeepSeek-R1 | 671B (37B active) | ~75% | 128K | MIT | DeepSeek |
| DeepSeek-V4-Flash | 284B MoE | ~65% | 128K | MIT | DeepSeek |
| Qwen3-Coder-480B | 480B MoE | 69.6% | 128K | Apache 2.0 | Alibaba |
| Qwen3-72B | 72B | ~60% | 128K | Apache 2.0 | Alibaba |
| Llama 4 Maverick | 400B MoE | ~65% | 10M | Llama 4 | Meta |
| Llama 4 Scout | 17B MoE | ~55% | 10M | Llama 4 | Meta |
| GLM-4-Plus | Unknown | ~65% | 128K | Proprietary | Zhipu AI |
| MiniMax-M1 | Unknown | ~68% | 128K | Apache 2.0 | MiniMax |
| Yi-Large | Unknown | ~60% | 32K | Apache 2.0 | 01.AI |
| Baichuan-M3-235B | 235B | ~55% | 32K | Proprietary | Baichuan |
| InternLM2.5-20B | 20B | ~55% | 1M | Apache 2.0 | InternLM |
| Moonshot K2 | Unknown | ~65% | 2M | Proprietary | Moonshot |

### Small Open Models (<10B)

| Model | Params | Strengths | License | Provider |
|-------|--------|-----------|---------|----------|
| Gemma 4 27B | 27B | Best mid-size | Gemma | Google |
| Gemma 4 12B | 12B | Efficient | Gemma | Google |
| Gemma 4 4B | 4B | Edge capable | Gemma | Google |
| Gemma 4 1B | 1B | Tiny | Gemma | Google |
| Phi-4 | 14B | Reasoning | MIT | Microsoft |
| Phi-4-mini | 3.8B | Efficient | MIT | Microsoft |
| Qwen3-8B | 8B | Best 8B | Apache 2.0 | Alibaba |
| Qwen3-4B | 4B | Efficient | Apache 2.0 | Alibaba |
| Qwen3-1.7B | 1.7B | Tiny | Apache 2.0 | Alibaba |
| Qwen3-0.5B | 0.5B | Micro | Apache 2.0 | Alibaba |
| MiniCPM-8B | 8B | Best edge | Apache 2.0 | OpenBMB |
| MiniCPM-2B | 2B | Mobile | Apache 2.0 | OpenBMB |
| Mistral Small 3.1 | ~14B | European | Apache 2.0 | Mistral |
| Ministral 3B | 3B | Tiny | Proprietary | Mistral |
| SmolLM2 | 1.7B | Ultra-tiny | Apache 2.0 | HuggingFace |
| OLMo 2 7B | 7B | Fully open | Apache 2.0 | AI2 |

---

## 🖼️ Image Generation Models

### Text-to-Image

| Model | Type | Resolution | License | Provider |
|-------|------|------------|---------|----------|
| Flux.1 Dev | Diffusion | 1024px | Apache 2.0 | Black Forest Labs |
| Flux.1 Pro | Diffusion | 2048px | Proprietary | Black Forest Labs |
| Flux.1 Schnell | Diffusion | 1024px | Apache 2.0 | Black Forest Labs |
| Flux Kontext | Diffusion | 1024px | Proprietary | Black Forest Labs |
| Stable Diffusion 3.5 | Diffusion | 1024px | Open | Stability AI |
| Stable Diffusion XL | Diffusion | 1024px | Open | Stability AI |
| Stable Diffusion 1.5 | Diffusion | 512px | Open | Stability AI |
| Kolors | Diffusion | 1024px | Apache 2.0 | Kuaishou |
| CogView4 | Diffusion | 1024px | Apache 2.0 | Tsinghua |
| HunyuanDiT | Diffusion | 1024px | Apache 2.0 | Tencent |
| SD3.5 Large | Diffusion | 1024px | Open | Stability AI |
| Playground v2.5 | Diffusion | 1024px | Open | Playground |
| Ideogram 3.0 | Diffusion | 1024px | Proprietary | Ideogram |
| DALL-E 3 | Diffusion | 1024px | Proprietary | OpenAI |
| Midjourney v6.1 | Diffusion | 2048px | Proprietary | Midjourney |
| PixArt-α | DiT | 1024px | Open | Tencent |
| PixArt-Σ | DiT | 2048px | Open | Tencent |
| Kandinsky 3.1 | Diffusion | 1024px | Open | Sber |
| Lumina-T2X | DiT | 1024px | Open | FlagAI |
| AuraFlow | Flow | 1024px | Open | Fal |
| SDXL Turbo | Distillation | 1024px | Open | Stability AI |
| SDXL Lightning | Distillation | 1024px | Open | ByteDance |

### Image Editing

| Model | Type | License | Provider |
|-------|------|---------|----------|
| Flux Kontext | Instruct | Proprietary | BFL |
| SD WebUI Inpaint | Inpaint | Open | AUTOMATIC1111 |
| ControlNet | Control | Open | lllyasviel |
| IP-Adapter | Style transfer | Open | TencentARC |
| T2I-Adapter | Control | Open | TencentARC |
| PhotoMaker | Identity | Open | TencentARC |
| InstantID | Identity | Open | InstantX |
| IP-Adapter FaceID | Face | Open | H95155609 |
| BrushNet | Plug-and-play | Open | TencentARC |
| PowerPaint | Inpaint | Open | TencentARC |

### Image Enhancement

| Model | Type | License | Provider |
|-------|------|---------|----------|
| Real-ESRGAN | Upscale | Open | TencentARC |
| GFPGAN | Face restore | Open | TencentARC |
| CodeFormer | Face restore | Open | TencentARC |
| StableSR | Super-res | Open | Tsinghua |
| SwinIR | Super-res | Open | ETH Zurich |
| Upscayl | Upscale (app) | Open | upscayl |
| Topaz Photo AI | Upscale (app) | Proprietary | Topaz |

---

## 🎬 Video Generation Models

| Model | Type | Resolution | Length | License | Provider |
|-------|------|------------|--------|---------|----------|
| Wan2.1-14B | Diffusion | 720p | 81 frames | Apache 2.0 | Alibaba |
| Wan2.2 | Diffusion | 720p | 81 frames | Apache 2.0 | Alibaba |
| HunyuanVideo | Diffusion | 720p | 129 frames | Apache 2.0 | Tencent |
| CogVideoX-5B | Diffusion | 480p | 49 frames | Apache 2.0 | Tsinghua |
| LTX-Video | DiT | 720p | 256 frames | Apache 2.0 | Lightricks |
| Mochi | Diffusion | 480p | 163 frames | Apache 2.0 | Genmo |
| Stable Video Diffusion | Diffusion | 576p | 25 frames | Open | Stability AI |
| VideoCrafter | Diffusion | 512p | 16 frames | Open | Tencent |
| AnimateDiff | Motion | 512p | Variable | Open | Community |
| Sora | Diffusion | 1080p | 60s | Proprietary | OpenAI |
| Kling 2.0 | Diffusion | 1080p | 10s | Proprietary | Kuaishou |
| Veo 3 | Diffusion | 1080p | 60s | Proprietary | Google |
| Pika 2.5 | Diffusion | 720p | 3s | Proprietary | Pika |
| Runway Gen-4 | Diffusion | 1080p | 10s | Proprietary | Runway |
| Dream Machine | Diffusion | 720p | 5s | Proprietary | Luma |
| WanGP | Diffusion | 720p | Variable | Open | deepbeepmeep |

---

## 🎵 Audio/Music Generation Models

### Text-to-Speech

| Model | Type | Languages | License | Provider |
|-------|------|-----------|---------|----------|
| CosyVoice | TTS | 5+ | Apache 2.0 | FunAudio/NetEase |
| F5-TTS | TTS | EN/ZH | MIT | FunAudio/NetEase |
| ChatTTS | TTS | EN/ZH | AGPL | Community |
| StyleTTS 2 | TTS | EN | MIT | Aaron (York) |
| XTTS v2 | TTS | 16 | Cohere | Cohere |
| Bark | TTS | 13 | MIT | Suno |
| VALL-E X | TTS | EN/ZH | MIT | Microsoft |
| EmotiVoice | TTS | ZH/EN | Apache 2.0 | NetEase |
| E2-TTS | TTS | EN | MIT | Fairseq |
| Piper | TTS | 30+ | MIT | rhasspy |
| Coqui TTS | TTS | 30+ | Apache 2.0 | Coqui |
| Kokoro | TTS | EN | Apache 2.0 | hexgrad |
| ChatTTS | TTS | EN/ZH | AGPL | 2noise |
| OpenVoice | TTS | EN/ZH | MIT | MyShell |
| GPT-SoVITS | TTS | EN/ZH | MIT | RVC-Boss |

### Voice Cloning

| Model | Samples Needed | Quality | License | Provider |
|-------|---------------|---------|---------|----------|
| CosyVoice | 3s | Excellent | Apache 2.0 | FunAudio |
| F5-TTS | 5s | Excellent | MIT | FunAudio |
| OpenVoice v2 | 1s | Very Good | MIT | MyShell |
| GPT-SoVITS | 10s | Excellent | MIT | RVC-Boss |
| RVC v2 | 1min | Good | MIT | RVC-Boss |
| XTTS v2 | 6s | Good | Cohere | Cohere |
| MockingBird | 5s | Fair | MIT | babysor |
| Real-Time Voice Cloning | 5s | Fair | MIT | CorentinJ |
| VALL-E X | 3s | Good | MIT | Microsoft |

### Music Generation

| Model | Type | Length | License | Provider |
|-------|------|--------|---------|----------|
| MusicGen | Autoregressive | 30s | CC-BY-NC | Meta |
| AudioCraft | Autoregressive | 30s | CC-BY-NC | Meta |
| Stable Audio Open | Diffusion | 47s | Open | Stability AI |
| Stable Audio 2.0 | Diffusion | 197s | Proprietary | Stability AI |
| Riffusion | Diffusion | 10s | MIT | Community |
| Suno v4.5 | Unknown | 4min | Proprietary | Suno |
| Udio | Unknown | 4min | Proprietary | Udio |
| Mureka | Unknown | 4min | Proprietary |昆仑万维 |

### Speech Recognition

| Model | Languages | License | Provider |
|-------|-----------|---------|----------|
| Whisper Large v3 | 99 | MIT | OpenAI |
| Whisper Turbo | 99 | MIT | OpenAI |
| SenseVoice | 50+ | Apache 2.0 | FunAudio |
| FunASR | 50+ | Apache 2.0 | ModelScope |
| Silero VAD | 100+ | MIT | Silero |
| WeNet | ZH/EN | Apache 2.0 | WeNet |
| Vosk | 20+ | Apache 2.0 | Alphacep |
| DeepSpeech | EN | Mozilla | Mozilla |
| WhisperX | 99 | MIT | m-bain |
| faster-whisper | 99 | MIT | SYSTRAN |

---

## 👁️ Vision Models

| Model | Type | License | Provider |
|-------|------|---------|----------|
| GPT-4o Vision | Multimodal | Proprietary | OpenAI |
| Gemini 3 Pro Vision | Multimodal | Proprietary | Google |
| Claude 3.5 Sonnet | Multimodal | Proprietary | Anthropic |
| LLaVA-1.5 | VLM | Apache 2.0 | UW |
| LLaVA-NeXT | VLM | Apache 2.0 | UW |
| InternVL2 | VLM | MIT | OpenGVLab |
| Qwen-VL | VLM | Apache 2.0 | Alibaba |
| DeepSeek-VL2 | VLM | MIT | DeepSeek |
| MiniCPM-V | VLM | Apache 2.0 | OpenBMB |
| Molmo | VLM | Apache 2.0 | AI2 |
| Idefics3 | VLM | Apache 2.0 | HuggingFace |
| PaliGemma | VLM | Gemma | Google |
| Florence-2 | VLM | MIT | Microsoft |
| SAM 2 | Segmentation | Apache 2.0 | Meta |
| DINOv2 | Embedding | CC-BY-NC | Meta |
| GroundingDINO | Detection | Apache 2.0 | IDEA |

---

## 🔢 Embedding Models

| Model | Dim | MTEB Rank | License | Provider |
|-------|-----|-----------|---------|----------|
| text-embedding-3-large | 3072 | Top 3 | Proprietary | OpenAI |
| bge-m3 | 1024 | Top 5 | MIT | BAAI |
| bge-large-zh | 1024 | Top CN | MIT | BAAI |
| bge-large-en | 1024 | Top EN | MIT | BAAI |
| jina-embeddings-v3 | 1024 | Top 10 | CC-BY | Jina AI |
| nomic-embed-v1.5 | 768 | Top 15 | Apache 2.0 | Nomic |
| gte-large | 1024 | Top 20 | MIT | Alibaba |
| e5-mistral-7b | 4096 | Top 10 | MIT | Microsoft |
| Cohere Embed v3 | 1024 | Top 5 | Proprietary | Cohere |
| Jina Embeddings v3 | 1024 | Top 10 | CC-BY | Jina AI |
| SFR-Embedding-Mistral | 4096 | Top 15 | Apache 2.0 | Salesforce |
| GritLM-7B | 4096 | Top 20 | MIT | Contextual AI |

---

*Last updated: 2026-05-25*


## 🆕 Auto-discovered nexus (2026-05-25 10:10 UTC)

| Repo | Stars | Lang | Description |
|------|-------|------|-------------|
| [huggingface/transformers](https://github.com/huggingface/transformers) | ⭐160943 | Python | 🤗 Transformers: the model-definition framework for state-of-the-art ma |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | ⭐137587 | Python | The agent engineering platform. |
| [deepseek-ai/DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) | ⭐103608 | Python |  |
| [deepseek-ai/DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) | ⭐92019 | None |  |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | ⭐80943 | Python | A high-throughput and memory-efficient inference and serving engine fo |
| [openai/openai-cookbook](https://github.com/openai/openai-cookbook) | ⭐73759 | Jupyter Notebook | Examples and guides for using the OpenAI API |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | ⭐69489 | Python | An open-source long-horizon SuperAgent harness that researches, codes, |
| [meta-llama/llama](https://github.com/meta-llama/llama) | ⭐59436 | Python | Inference code for Llama models |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | ⭐52143 | Python | Framework for orchestrating role-playing, autonomous AI agents. By fos |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | ⭐49645 | Python | LlamaIndex is the leading document agent and OCR platform |
| [deepseek-ai/awesome-deepseek-integration](https://github.com/deepseek-ai/awesome-deepseek-integration) | ⭐37578 | None | Integrate the DeepSeek API into popular software |
| [huggingface/diffusers](https://github.com/huggingface/diffusers) | ⭐33696 | Python | 🤗 Diffusers: State-of-the-art diffusion models for image, video, and a |
| [OpenBMB/ChatDev](https://github.com/OpenBMB/ChatDev) | ⭐33185 | Python | ChatDev 2.0: Dev All through LLM-powered Multi-Agent Collaboration |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | ⭐32885 | Python | Build resilient agents. |
| [meta-llama/llama3](https://github.com/meta-llama/llama3) | ⭐29286 | Python | The official Meta Llama 3 GitHub site |
| [huggingface/agents-course](https://github.com/huggingface/agents-course) | ⭐28859 | MDX | This repository contains the Hugging Face Agents Course.  |
| [QwenLM/Qwen3](https://github.com/QwenLM/Qwen3) | ⭐27257 | Python | Qwen3 is the large language model series developed by Qwen team, Aliba |
| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | ⭐26629 | Python | A lightweight, powerful framework for multi-agent workflows |
| [huggingface/open-r1](https://github.com/huggingface/open-r1) | ⭐26020 | Python | Fully open reproduction of DeepSeek-R1 |
| [OpenBMB/MiniCPM-V](https://github.com/OpenBMB/MiniCPM-V) | ⭐25247 | Python | A Pocket-Sized MLLM for Ultra-Efficient Image and Video Understanding  |
| [openai/gpt-2](https://github.com/openai/gpt-2) | ⭐24877 | Python | Code for the paper "Language Models are Unsupervised Multitask Learner |
| [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) | ⭐24650 | TypeScript | An open-source AI agent that lives in your terminal. |
| [deepseek-ai/DeepSeek-Coder](https://github.com/deepseek-ai/DeepSeek-Coder) | ⭐23466 | Python | DeepSeek Coder: Let the Code Write Itself |
| [deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR) | ⭐23166 | Python | Contexts Optical Compression |
| [huggingface/datasets](https://github.com/huggingface/datasets) | ⭐21534 | Python | 🤗 The largest hub of ready-to-use datasets for AI models with fast, ea |
| [FunAudioLLM/CosyVoice](https://github.com/FunAudioLLM/CosyVoice) | ⭐21233 | Python | Multi-lingual large voice generation model, providing inference, train |
| [openai/chatgpt-retrieval-plugin](https://github.com/openai/chatgpt-retrieval-plugin) | ⭐21205 | Python | The ChatGPT Retrieval Plugin lets you easily find personal or work doc |
| [QwenLM/Qwen](https://github.com/QwenLM/Qwen) | ⭐21185 | Python | The official repo of Qwen (通义千问) chat & pretrained large language mode |
| [huggingface/peft](https://github.com/huggingface/peft) | ⭐21181 | Python | 🤗 PEFT: State-of-the-art Parameter-Efficient Fine-Tuning. |
| [openai/gpt-oss](https://github.com/openai/gpt-oss) | ⭐20118 | Python | gpt-oss-120b and gpt-oss-20b are two open-weight language models by Op |
| [QwenLM/Qwen3-VL](https://github.com/QwenLM/Qwen3-VL) | ⭐19235 | Jupyter Notebook | Qwen3-VL is the multimodal large language model series developed by Qw |
| [openai/evals](https://github.com/openai/evals) | ⭐18527 | Python | Evals is a framework for evaluating LLMs and LLM systems, and an open- |
| [huggingface/trl](https://github.com/huggingface/trl) | ⭐18461 | Python | Train transformer language models with reinforcement learning. |
| [meta-llama/llama-cookbook](https://github.com/meta-llama/llama-cookbook) | ⭐18332 | Jupyter Notebook | Welcome to the Llama Cookbook! This is your go to guide for Building w |
| [deepseek-ai/Janus](https://github.com/deepseek-ai/Janus) | ⭐17731 | Python | Janus-Series: Unified Multimodal Understanding and Generation Models |
| [QwenLM/Qwen3-Coder](https://github.com/QwenLM/Qwen3-Coder) | ⭐16557 | Python | Qwen3-Coder is the code version of Qwen3, the large language model ser |
| [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | ⭐16394 | Python | Agent framework and applications built upon Qwen>=3.0, featuring Funct |
| [meta-llama/codellama](https://github.com/meta-llama/codellama) | ⭐16321 | Python | Inference code for CodeLlama models |
| [modelscope/FunASR](https://github.com/modelscope/FunASR) | ⭐16263 | Python | Industrial-grade speech recognition toolkit: 170x realtime, 50+ langua |
| [openai/gpt-3](https://github.com/openai/gpt-3) | ⭐15740 | None | GPT-3: Language Models are Few-Shot Learners |
| [Stability-AI/StableLM](https://github.com/Stability-AI/StableLM) | ⭐15698 | Jupyter Notebook | StableLM: Stability AI Language Models |
| [Tencent/WeKnora](https://github.com/Tencent/WeKnora) | ⭐15502 | Go | Open-source LLM knowledge platform: turn raw documents into a queryabl |
| [alibaba/MNN](https://github.com/alibaba/MNN) | ⭐15248 | C++ | MNN: A blazing-fast, lightweight inference engine battle-tested by Ali |
| [modelscope/ms-swift](https://github.com/modelscope/ms-swift) | ⭐14254 | Python | Use PEFT or Full-parameter to CPT/SFT/DPO/GRPO 600+ LLMs (Qwen3.6, Dee |
| [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) | ⭐13717 | Python | TensorRT LLM provides users with an easy-to-use Python API to define L |
| [PaddlePaddle/PaddleFormers](https://github.com/PaddlePaddle/PaddleFormers) | ⭐12987 | Python | PaddleFormers is an easy-to-use library of pre-trained large language  |
| [PaddlePaddle/PaddleNLP](https://github.com/PaddlePaddle/PaddleNLP) | ⭐12947 | Python | Easy-to-use and powerful LLM and SLM library with awesome model zoo. |
| [deepseek-ai/FlashMLA](https://github.com/deepseek-ai/FlashMLA) | ⭐12661 | C++ | FlashMLA: Efficient Multi-head Latent Attention Kernels |
| [FlagOpen/FlagEmbedding](https://github.com/FlagOpen/FlagEmbedding) | ⭐11720 | Python | Retrieval and Retrieval-augmented LLMs |
| [bytedance/trae-agent](https://github.com/bytedance/trae-agent) | ⭐11585 | Python | Trae Agent is an LLM-based agent for general purpose software engineer |


## 🆕 Auto-discovered nexus (2026-05-25 14:10 UTC)

| Repo | Stars | Lang | Description |
|------|-------|------|-------------|
| [QwenLM/Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | ⭐11544 | Python | Qwen3-TTS is an open-source series of TTS models developed by the Qwen |
| [huggingface/text-generation-inference](https://github.com/huggingface/text-generation-inference) | ⭐10856 | Python | Large Language Model Text Generation Inference |
| [mistralai/mistral-inference](https://github.com/mistralai/mistral-inference) | ⭐10808 | Jupyter Notebook | Official inference library for Mistral models |
| [MoonshotAI/Kimi-K2](https://github.com/MoonshotAI/Kimi-K2) | ⭐10803 | None | Kimi K2 is the large language model series developed by Moonshot AI te |
| [huggingface/tokenizers](https://github.com/huggingface/tokenizers) | ⭐10766 | Rust | 💥 Fast State-of-the-Art Tokenizers optimized for Research and Producti |
| [huggingface/chat-ui](https://github.com/huggingface/chat-ui) | ⭐10727 | TypeScript | The open source codebase powering HuggingChat |
| [OpenGVLab/InternVL](https://github.com/OpenGVLab/InternVL) | ⭐10040 | Python | [CVPR 2024 Oral] InternVL Family: A Pioneering Open-Source Alternative |
| [deepseek-ai/3FS](https://github.com/deepseek-ai/3FS) | ⭐9924 | C++ |  A high-performance distributed file system designed to address the ch |
| [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | ⭐9846 | Python | An Open-Source Asynchronous Coding Agent |
| [alibaba/zvec](https://github.com/alibaba/zvec) | ⭐9691 | C++ | A lightweight, lightning-fast, in-process vector database |
| [deepseek-ai/DeepEP](https://github.com/deepseek-ai/DeepEP) | ⭐9664 | Cuda | DeepEP: an efficient expert-parallel communication library |
| [OpenBMB/MiniCPM](https://github.com/OpenBMB/MiniCPM) | ⭐8943 | Jupyter Notebook | MiniCPM5-1B: A SOTA 1B on-device LLM, small yet powerful. |
| [intel/ipex-llm](https://github.com/intel/ipex-llm) | ⭐8811 | Python | Accelerate local LLM inference and finetuning (LLaMA, Mistral, ChatGLM |
| [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | ⭐8733 | Python | Kimi Code CLI is your next CLI agent. |
| [OpenBMB/XAgent](https://github.com/OpenBMB/XAgent) | ⭐8532 | Python | An Autonomous LLM Agent for Complex Task Solving |
| [FunAudioLLM/SenseVoice](https://github.com/FunAudioLLM/SenseVoice) | ⭐8218 | Python | Multilingual Voice Understanding Model |
| [deepseek-ai/open-infra-index](https://github.com/deepseek-ai/open-infra-index) | ⭐7998 | None | Production-tested AI infrastructure tools for efficient AGI developmen |
| [QwenLM/Qwen-Image](https://github.com/QwenLM/Qwen-Image) | ⭐7927 | Python | Qwen-Image is a powerful image generation foundation model capable of  |
| [NVIDIA/garak](https://github.com/NVIDIA/garak) | ⭐7902 | Python | the LLM vulnerability scanner |
| [InternLM/lmdeploy](https://github.com/InternLM/lmdeploy) | ⭐7871 | Python | LMDeploy is a toolkit for compressing, deploying, and serving LLMs. |
| [01-ai/Yi](https://github.com/01-ai/Yi) | ⭐7821 | Jupyter Notebook | A series of large language models trained from scratch by developers @ |
| [PaddlePaddle/ERNIE](https://github.com/PaddlePaddle/ERNIE) | ⭐7717 | Python | The official repository for ERNIE 4.5 and ERNIEKit – its industrial-gr |
| [meta-llama/llama-models](https://github.com/meta-llama/llama-models) | ⭐7613 | Python | Utilities intended for use with Llama models. |
| [deepseek-ai/DeepGEMM](https://github.com/deepseek-ai/DeepGEMM) | ⭐7293 | Cuda | DeepGEMM: clean and efficient FP8 GEMM kernels with fine-grained scali |
| [InternLM/InternLM](https://github.com/InternLM/InternLM) | ⭐7210 | Python | Official release of InternLM series (InternLM, InternLM2, InternLM2.5, |
| [deepseek-ai/DeepSeek-LLM](https://github.com/deepseek-ai/DeepSeek-LLM) | ⭐6946 | Makefile | DeepSeek LLM: Let there be answers |
| [InternLM/MindSearch](https://github.com/InternLM/MindSearch) | ⭐6861 | JavaScript | 🔍 An LLM-based Multi-agent Framework of Web Search Engine (like Perple |
| [deepseek-ai/DeepSeek-Coder-V2](https://github.com/deepseek-ai/DeepSeek-Coder-V2) | ⭐6780 | None | DeepSeek-Coder-V2: Breaking the Barrier of Closed-Source Models in Cod |
| [langchain-ai/opengpts](https://github.com/langchain-ai/opengpts) | ⭐6743 | Rich Text Format |  |
| [QwenLM/Qwen-VL](https://github.com/QwenLM/Qwen-VL) | ⭐6655 | Python | The official repo of Qwen-VL (通义千问-VL) chat & pretrained large vision  |
| [run-llama/rags](https://github.com/run-llama/rags) | ⭐6535 | Python | Build ChatGPT over your data, all with natural language |
| [NVIDIA/FasterTransformer](https://github.com/NVIDIA/FasterTransformer) | ⭐6414 | C++ | Transformer related optimization, including BERT, GPT |
| [OpenGVLab/LLaMA-Adapter](https://github.com/OpenGVLab/LLaMA-Adapter) | ⭐5921 | Python | [ICLR 2024] Fine-tuning LLaMA to follow Instructions within 1 Hour and |
| [THUDM/slime](https://github.com/THUDM/slime) | ⭐5773 | Python | slime is an LLM post-training framework for RL Scaling. |
| [baichuan-inc/Baichuan-7B](https://github.com/baichuan-inc/Baichuan-7B) | ⭐5658 | Python | A large-scale 7B pretraining language model developed by BaiChuan-Inc. |
| [OpenBMB/ToolBench](https://github.com/OpenBMB/ToolBench) | ⭐5652 | Python | [ICLR'24 spotlight] An open platform for training, serving, and evalua |
| [modelscope/FunClip](https://github.com/modelscope/FunClip) | ⭐5637 | Python | Open-source, accurate and easy-to-use video speech recognition & clipp |
| [huggingface/alignment-handbook](https://github.com/huggingface/alignment-handbook) | ⭐5605 | Python | Robust recipes to align language models with human and AI preferences |
| [OpenBMB/UltraRAG](https://github.com/OpenBMB/UltraRAG) | ⭐5557 | Python | A Low-Code MCP Framework for Building Complex and Innovative RAG Pipel |
| [langchain-ai/open-canvas](https://github.com/langchain-ai/open-canvas) | ⭐5454 | TypeScript | 📃 A better UX for chat, writing content, and coding with LLMs. |
| [deepseek-ai/DeepSeek-VL2](https://github.com/deepseek-ai/DeepSeek-VL2) | ⭐5286 | Python | DeepSeek-VL2: Mixture-of-Experts Vision-Language Models for Advanced M |
| [google-deepmind/gemma](https://github.com/google-deepmind/gemma) | ⭐5264 | Python | Gemma open-weight LLM library, from Google DeepMind |
| [run-llama/liteparse](https://github.com/run-llama/liteparse) | ⭐5217 | Rust | A fast, helpful, and open-source document parser |
| [InternLM/xtuner](https://github.com/InternLM/xtuner) | ⭐5136 | Python | A Next-Generation Training Engine Built for Ultra-Large MoE Models |
| [OpenBMB/AgentVerse](https://github.com/OpenBMB/AgentVerse) | ⭐5040 | JavaScript | 🤖 AgentVerse 🪐 is designed to facilitate the deployment of multiple LL |
| [deepseek-ai/DeepSeek-V2](https://github.com/deepseek-ai/DeepSeek-V2) | ⭐5007 | None | DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts La |
| [deepseek-ai/smallpond](https://github.com/deepseek-ai/smallpond) | ⭐4958 | Python | A lightweight data processing framework built on DuckDB and 3FS. |
| [OpenGVLab/DragGAN](https://github.com/OpenGVLab/DragGAN) | ⭐4951 | Python | Unofficial Implementation of DragGAN - "Drag Your GAN: Interactive Poi |
| [vllm-project/vllm-omni](https://github.com/vllm-project/vllm-omni) | ⭐4883 | Python | A framework for efficient model inference with omni-modality models |
| [vllm-project/aibrix](https://github.com/vllm-project/aibrix) | ⭐4828 | Go | Cost-efficient and pluggable Infrastructure components for GenAI infer |


## 🆕 Auto-discovered nexus (2026-05-25 18:10 UTC)

| Repo | Stars | Lang | Description |
|------|-------|------|-------------|
| [huggingface/text-embeddings-inference](https://github.com/huggingface/text-embeddings-inference) | ⭐4820 | Rust | A blazing fast inference solution for text embeddings models |
| [MoonshotAI/Kimi-Audio](https://github.com/MoonshotAI/Kimi-Audio) | ⭐4641 | Python | Kimi-Audio, an open-source audio foundation model excelling in audio u |
| [deepseek-ai/Engram](https://github.com/deepseek-ai/Engram) | ⭐4422 | Python | Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Lar |
| [openai/harmony](https://github.com/openai/harmony) | ⭐4383 | Rust | Renderer for the harmony response format to be used with gpt-oss |
| [mistralai/mistral-vibe](https://github.com/mistralai/mistral-vibe) | ⭐4283 | Python | Minimal CLI coding agent by Mistral |
| [run-llama/llama_cloud_services](https://github.com/run-llama/llama_cloud_services) | ⭐4254 | TypeScript | Knowledge Agents and Management in the Cloud |
| [openai/plugins-quickstart](https://github.com/openai/plugins-quickstart) | ⭐4237 | Python | Get a ChatGPT plugin up and running in under 5 minutes! |
| [vllm-project/semantic-router](https://github.com/vllm-project/semantic-router) | ⭐4214 | Go | System Level Intelligent Router for Mixture-of-Models at Cloud, Data C |
| [meta-llama/PurpleLlama](https://github.com/meta-llama/PurpleLlama) | ⭐4192 | Python | Set of tools to assess and improve LLM security. |
| [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | ⭐4135 | TypeScript | TencentDB Agent Memory delivers fully local long-term memory for AI Ag |
| [deepseek-ai/DeepSeek-VL](https://github.com/deepseek-ai/DeepSeek-VL) | ⭐4112 | Python | DeepSeek-VL: Towards Real-World Vision-Language Understanding |
| [baichuan-inc/Baichuan2](https://github.com/baichuan-inc/Baichuan2) | ⭐4102 | Python | A series of large language models developed by Baichuan Intelligent Te |
| [NVIDIA/GenerativeAIExamples](https://github.com/NVIDIA/GenerativeAIExamples) | ⭐4029 | Jupyter Notebook | Generative AI reference workflows optimized for accelerated infrastruc |
| [QwenLM/Qwen2.5-Omni](https://github.com/QwenLM/Qwen2.5-Omni) | ⭐4013 | Jupyter Notebook | Qwen2.5-Omni is an end-to-end multimodal model by Qwen team at Alibaba |
| [huggingface/smollm](https://github.com/huggingface/smollm) | ⭐3788 | Python | Everything about the SmolLM and SmolVLM family of models  |
| [QwenLM/Qwen3-Omni](https://github.com/QwenLM/Qwen3-Omni) | ⭐3781 | Jupyter Notebook | Qwen3-omni is a natively end-to-end, omni-modal LLM developed by the Q |
| [Tencent/AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard) | ⭐3772 | Python | A full-stack AI Red Teaming platform securing AI ecosystems via OpenCl |
| [PaddlePaddle/FastDeploy](https://github.com/PaddlePaddle/FastDeploy) | ⭐3686 | Python | High-performance Inference and Deployment Toolkit for LLMs and VLMs ba |
| [THUDM/GLM](https://github.com/THUDM/GLM) | ⭐3501 | Python | GLM (General Language Model) |
| [run-llama/llama-hub](https://github.com/run-llama/llama-hub) | ⭐3475 | Jupyter Notebook | A library of data loaders for LLMs made by the community -- to be used |
| [MoonshotAI/Kimi-k1.5](https://github.com/MoonshotAI/Kimi-k1.5) | ⭐3472 | None |  |
| [THUDM/AgentBench](https://github.com/THUDM/AgentBench) | ⭐3451 | Python | A Comprehensive Benchmark to Evaluate LLMs as Agents (ICLR'24) |
| [QwenLM/Qwen3.6](https://github.com/QwenLM/Qwen3.6) | ⭐3431 | None | Qwen3.6 is the large language model series developed by Qwen team, Ali |
| [MiniMax-AI/MiniMax-01](https://github.com/MiniMax-AI/MiniMax-01) | ⭐3419 | Python | The official repo of MiniMax-Text-01 and MiniMax-VL-01, large-language |
| [OpenGVLab/Ask-Anything](https://github.com/OpenGVLab/Ask-Anything) | ⭐3339 | Python | [CVPR2024 Highlight][VideoChatGPT] ChatGPT with video understanding! A |
| [bytedance/lightseq](https://github.com/bytedance/lightseq) | ⭐3301 | C++ | LightSeq: A High Performance Library for Sequence Processing and Gener |
| [deepseek-ai/DeepSeek-Math](https://github.com/deepseek-ai/DeepSeek-Math) | ⭐3295 | Python | DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Lan |
| [vllm-project/llm-compressor](https://github.com/vllm-project/llm-compressor) | ⭐3284 | Python | Transformers-compatible library for applying various compression algor |
| [openai/human-eval](https://github.com/openai/human-eval) | ⭐3239 | Python | Code for the paper "Evaluating Large Language Models Trained on Code" |
| [OpenGVLab/InternGPT](https://github.com/OpenGVLab/InternGPT) | ⭐3203 | Python | InternGPT (iGPT) is an open source demo platform where you can easily  |
| [alibaba/ROLL](https://github.com/alibaba/ROLL) | ⭐3173 | Python | An Efficient and User-Friendly Scaling Library for Reinforcement Learn |
| [MiniMax-AI/MiniMax-M1](https://github.com/MiniMax-AI/MiniMax-M1) | ⭐3153 | Python | MiniMax-M1, the world's first open-weight, large-scale hybrid-attentio |
| [mistralai/mistral-finetune](https://github.com/mistralai/mistral-finetune) | ⭐3091 | Python |  |
| [run-llama/LlamaIndexTS](https://github.com/run-llama/LlamaIndexTS) | ⭐3080 | TypeScript | Data framework for your LLM applications. Focus on server side solutio |
| [deepseek-ai/DreamCraft3D](https://github.com/deepseek-ai/DreamCraft3D) | ⭐3007 | Python | [ICLR 2024] Official implementation of DreamCraft3D: Hierarchical 3D G |
| [deepseek-ai/DualPipe](https://github.com/deepseek-ai/DualPipe) | ⭐2954 | Python | A bidirectional pipeline parallelism algorithm for computation-communi |
| [langchain-ai/langgraphjs](https://github.com/langchain-ai/langgraphjs) | ⭐2952 | TypeScript | Framework to build resilient language agents as graphs. |
| [baichuan-inc/Baichuan-13B](https://github.com/baichuan-inc/Baichuan-13B) | ⭐2931 | Python | A 13B large language model developed by Baichuan Intelligent Technolog |
| [InternLM/InternLM-XComposer](https://github.com/InternLM/InternLM-XComposer) | ⭐2927 | Python | InternLM-XComposer2.5-OmniLive: A Comprehensive Multimodal System for  |
| [deepseek-ai/DeepSeek-OCR-2](https://github.com/deepseek-ai/DeepSeek-OCR-2) | ⭐2877 | Python | Visual Causal Flow |
| [langchain-ai/agent-chat-ui](https://github.com/langchain-ai/agent-chat-ui) | ⭐2869 | TypeScript | 🦜💬 Web app for interacting with any LangGraph agent (PY & TS) via a ch |
| [modelscope/evalscope](https://github.com/modelscope/evalscope) | ⭐2844 | Python | A streamlined and customizable framework for efficient large model (LL |
| [OpenBMB/BMTools](https://github.com/OpenBMB/BMTools) | ⭐2775 | Python | Tool Learning for Big Models, Open-Source Solutions of ChatGPT-Plugins |
| [QwenLM/Qwen3-ASR](https://github.com/QwenLM/Qwen3-ASR) | ⭐2749 | Python | Qwen3-ASR is an open-source series of ASR models developed by the Qwen |
| [huggingface/nanotron](https://github.com/huggingface/nanotron) | ⭐2699 | Python | Minimalistic large language model 3D-parallelism training |
| [MiniMax-AI/Mini-Agent](https://github.com/MiniMax-AI/Mini-Agent) | ⭐2655 | Python | A minimal yet professional single agent demo project that showcases th |
| [intel/neural-compressor](https://github.com/intel/neural-compressor) | ⭐2644 | Python | SOTA low-bit LLM quantization (INT8/FP8/MXFP8/INT4/MXFP4/NVFP4) & spar |
| [run-llama/sec-insights](https://github.com/run-llama/sec-insights) | ⭐2598 | TypeScript | A real world full-stack application using LlamaIndex |
| [MiniMax-AI/MiniMax-M2](https://github.com/MiniMax-AI/MiniMax-M2) | ⭐2594 | None | MiniMax-M2, a model built for Max coding & agentic workflows. |
| [InternLM/HuixiangDou](https://github.com/InternLM/HuixiangDou) | ⭐2490 | Python | HuixiangDou: Overcoming Group Chat Scenarios with LLM-based Technical  |


## 🆕 Auto-discovered nexus (2026-05-25 22:10 UTC)

| Repo | Stars | Lang | Description |
|------|-------|------|-------------|
| [huggingface/lighteval](https://github.com/huggingface/lighteval) | ⭐2428 | Python | Lighteval is your all-in-one toolkit for evaluating LLMs across multip |
| [vllm-project/production-stack](https://github.com/vllm-project/production-stack) | ⭐2353 | Python | vLLM’s reference system for K8S-native cluster-wide deployment with co |
| [langchain-ai/langserve](https://github.com/langchain-ai/langserve) | ⭐2330 | JavaScript | LangServe 🦜️🏓 |
| [deepseek-ai/awesome-deepseek-agent](https://github.com/deepseek-ai/awesome-deepseek-agent) | ⭐2328 | None |  |
| [InternLM/lagent](https://github.com/InternLM/lagent) | ⭐2254 | Python | A lightweight framework for building LLM-based agents |
| [mistralai/cookbook](https://github.com/mistralai/cookbook) | ⭐2251 | Jupyter Notebook |  |
| [intel/intel-extension-for-transformers](https://github.com/intel/intel-extension-for-transformers) | ⭐2177 | Python | ⚡ Build your chatbot within minutes on your favorite device; offer SOT |
| [openai/prm800k](https://github.com/openai/prm800k) | ⭐2133 | Python | 800,000 step-level correctness labels on LLM solutions to MATH problem |
| [vllm-project/vllm-ascend](https://github.com/vllm-project/vllm-ascend) | ⭐2129 | C++ | Community maintained hardware plugin for vLLM on Ascend |
| [MoonshotAI/MoBA](https://github.com/MoonshotAI/MoBA) | ⭐2120 | Python | MoBA: Mixture of Block Attention for Long-Context LLMs |
| [huggingface/evaluation-guidebook](https://github.com/huggingface/evaluation-guidebook) | ⭐2111 | Jupyter Notebook | Sharing both practical insights and theoretical knowledge about LLM ev |
| [openai/image-gpt](https://github.com/openai/image-gpt) | ⭐2089 | Python |  |
| [QwenLM/Qwen2-Audio](https://github.com/QwenLM/Qwen2-Audio) | ⭐2071 | Python | The official repo of Qwen2-Audio chat & pretrained large audio languag |
| [run-llama/llama_deploy](https://github.com/run-llama/llama_deploy) | ⭐2069 | Python | Deploy your agentic worfklows to production |
| [openai/gpt-2-output-dataset](https://github.com/openai/gpt-2-output-dataset) | ⭐2031 | Python | Dataset of GPT-2 outputs for research in detection, biases, and more |
| [MoonshotAI/Kimi-K2.5](https://github.com/MoonshotAI/Kimi-K2.5) | ⭐1991 | None | Moonshot's most powerful model |
| [InternLM/Tutorial](https://github.com/InternLM/Tutorial) | ⭐1956 | Python | LLM&VLM Tutorial |
| [deepseek-ai/DeepSeek-MoE](https://github.com/deepseek-ai/DeepSeek-MoE) | ⭐1933 | Python | DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Expe |
| [QwenLM/Qwen3-Embedding](https://github.com/QwenLM/Qwen3-Embedding) | ⭐1931 | Python |  |
| [QwenLM/Qwen-Audio](https://github.com/QwenLM/Qwen-Audio) | ⭐1896 | Python | The official repo of Qwen-Audio (通义千问-Audio) chat & pretrained large a |
| [QwenLM/Qwen-Image-Layered](https://github.com/QwenLM/Qwen-Image-Layered) | ⭐1890 | Python | Qwen-Image-Layered: Layered Decomposition for Inherent Editablity |
| [run-llama/notebookllama](https://github.com/run-llama/notebookllama) | ⭐1890 | Python | A fully open-source, LlamaCloud-backed alternative to NotebookLM |
| [openai/gpt-5-coding-examples](https://github.com/openai/gpt-5-coding-examples) | ⭐1884 | HTML | GPT-5 coding examples |
| [THUDM/LongWriter](https://github.com/THUDM/LongWriter) | ⭐1859 | Python | [ICLR 2025] LongWriter: Unleashing 10,000+ Word Generation from Long C |
| [openai/gpt-discord-bot](https://github.com/openai/gpt-discord-bot) | ⭐1834 | Python | Example Discord bot written in Python that uses the completions API to |
| [run-llama/semtools](https://github.com/run-llama/semtools) | ⭐1796 | Rust | Semantic search and document parsing tools for the command line |
| [huggingface/transfer-learning-conv-ai](https://github.com/huggingface/transfer-learning-conv-ai) | ⭐1759 | Python | 🦄 State-of-the-Art Conversational AI with Transfer Learning |
| [huggingface/swift-coreml-transformers](https://github.com/huggingface/swift-coreml-transformers) | ⭐1683 | Swift | Swift Core ML 3 implementations of GPT-2, DistilGPT-2, BERT, and Disti |
| [huggingface/aisheets](https://github.com/huggingface/aisheets) | ⭐1635 | TypeScript | Build, enrich, and transform datasets using AI models with no code |
| [THUDM/WebGLM](https://github.com/THUDM/WebGLM) | ⭐1604 | Python | WebGLM: An Efficient Web-enhanced Question Answering System (KDD 2023) |
| [bytedance/Sa2VA](https://github.com/bytedance/Sa2VA) | ⭐1603 | Python | Official Repo For Pixel-LLM Codebase: Sa2VA (Arxiv-25), SAMTok (CVPR-2 |
| [deepseek-ai/DeepSeek-V3.2-Exp](https://github.com/deepseek-ai/DeepSeek-V3.2-Exp) | ⭐1591 | Python |  |
| [meta-llama/synthetic-data-kit](https://github.com/meta-llama/synthetic-data-kit) | ⭐1591 | Python | Tool for generating high quality Synthetic datasets |
| [deepseek-ai/DeepSeek-Math-V2](https://github.com/deepseek-ai/DeepSeek-Math-V2) | ⭐1588 | Python |  |
| [alibaba/Pai-Megatron-Patch](https://github.com/alibaba/Pai-Megatron-Patch) | ⭐1576 | Python | The official repo of Pai-Megatron-Patch for LLM & VLM large scale trai |
| [bytedance/pasa](https://github.com/bytedance/pasa) | ⭐1571 | Python | PaSa -- an advanced paper search agent powered by large language model |
| [deepseek-ai/TileKernels](https://github.com/deepseek-ai/TileKernels) | ⭐1556 | Python | A kernel library written in tilelang |
| [Tencent/TurboTransformers](https://github.com/Tencent/TurboTransformers) | ⭐1548 | C++ | a fast and user-friendly runtime for transformer inference (Bert, Albe |
| [huggingface/pytorch-openai-transformer-lm](https://github.com/huggingface/pytorch-openai-transformer-lm) | ⭐1522 | Python | 🐥A PyTorch implementation of OpenAI's finetuned transformer language m |
| [run-llama/llama-lab](https://github.com/run-llama/llama-lab) | ⭐1514 | Python |  |
| [langchain-ai/langgraph-swarm-py](https://github.com/langchain-ai/langgraph-swarm-py) | ⭐1496 | Python | For your multi-agent needs |
| [THUDM/AgentTuning](https://github.com/THUDM/AgentTuning) | ⭐1488 | Python | AgentTuning: Enabling Generalized Agent Abilities for LLMs |
| [run-llama/create-llama](https://github.com/run-llama/create-llama) | ⭐1484 | Python | The easiest way to get started with LlamaIndex |
| [MoonshotAI/Moonlight](https://github.com/MoonshotAI/Moonlight) | ⭐1482 | None | Muon is Scalable for LLM Training |
| [modelscope/AgentEvolver](https://github.com/modelscope/AgentEvolver) | ⭐1442 | Python | AgentEvolver: Towards Efficient Self-Evolving Agent System |
| [stepfun-ai/Step-Audio2](https://github.com/stepfun-ai/Step-Audio2) | ⭐1442 | Python | Step-Audio 2 is an end-to-end multi-modal large language model designe |
| [bytedance/SALMONN](https://github.com/bytedance/SALMONN) | ⭐1439 | None | SALMONN family: A suite of advanced multi-modal LLMs |
| [openai/SWELancer-Benchmark](https://github.com/openai/SWELancer-Benchmark) | ⭐1439 | None | This repo contains the dataset and code for the paper "SWE-Lancer: Can |
| [intel/auto-round](https://github.com/intel/auto-round) | ⭐1411 | Python | A SOTA quantization algorithm for high-accuracy low-bit LLM inference, |
| [MoonshotAI/Kimi-Linear](https://github.com/MoonshotAI/Kimi-Linear) | ⭐1394 | None |  |


## 🆕 Auto-discovered nexus (2026-05-26 02:09 UTC)

| Repo | Stars | Lang | Description |
|------|-------|------|-------------|
| [openai/lm-human-preferences](https://github.com/openai/lm-human-preferences) | ⭐1393 | Python | Code for the paper Fine-Tuning Language Models from Human Preferences |
| [deepseek-ai/EPLB](https://github.com/deepseek-ai/EPLB) | ⭐1379 | Python | Expert Parallelism Load Balancer |
| [FunAudioLLM/ThinkSound](https://github.com/FunAudioLLM/ThinkSound) | ⭐1354 | Python | [NeurIPS 2025] PyTorch implementation of [ThinkSound], a unified frame |
| [FunAudioLLM/FunMusic](https://github.com/FunAudioLLM/FunMusic) | ⭐1350 | Python | A fundamental toolkit designed for music, song, and audio generation |
| [huggingface/llm-vscode](https://github.com/huggingface/llm-vscode) | ⭐1316 | TypeScript | LLM powered development for VSCode |
| [deepseek-ai/DeepSeek-Prover-V2](https://github.com/deepseek-ai/DeepSeek-Prover-V2) | ⭐1267 | None |  |
| [QwenLM/Qwen3-VL-Embedding](https://github.com/QwenLM/Qwen3-VL-Embedding) | ⭐1253 | Python |  |
| [Tencent/AngelSlim](https://github.com/Tencent/AngelSlim) | ⭐1243 | Python | Model compression toolkit engineered for enhanced usability, comprehen |
| [MoonshotAI/Kimi-Dev](https://github.com/MoonshotAI/Kimi-Dev) | ⭐1220 | Python | open-source coding LLM for software engineering tasks |
| [vllm-project/vllm-metal](https://github.com/vllm-project/vllm-metal) | ⭐1198 | Python | Community maintained hardware plugin for vLLM on Apple Silicon |
| [langchain-ai/langchain-extract](https://github.com/langchain-ai/langchain-extract) | ⭐1196 | Rich Text Format | 🦜⛏️ Did you say you like data? |
| [MoonshotAI/Kimi-VL](https://github.com/MoonshotAI/Kimi-VL) | ⭐1193 | None | Kimi-VL: Mixture-of-Experts Vision-Language Model for Multimodal Reaso |
| [THUDM/LongBench](https://github.com/THUDM/LongBench) | ⭐1178 | Python | LongBench v2 and LongBench (ACL 25'&24') |
| [FunAudioLLM/Fun-ASR](https://github.com/FunAudioLLM/Fun-ASR) | ⭐1172 | Python | End-to-end speech recognition large model: 31 languages, dialects, acc |
| [vllm-project/guidellm](https://github.com/vllm-project/guidellm) | ⭐1166 | Python | Evaluate and Enhance Your LLM Deployments for Real-World Inference Nee |
| [huggingface/llm.nvim](https://github.com/huggingface/llm.nvim) | ⭐1163 | Lua | LLM powered development for Neovim |
| [deepseek-ai/profile-data](https://github.com/deepseek-ai/profile-data) | ⭐1157 | None | Analyze computation-communication overlap in V3/R1. |
| [OpenGVLab/VisionLLM](https://github.com/OpenGVLab/VisionLLM) | ⭐1148 | Python | VisionLLM Series |
| [alibaba/rtp-llm](https://github.com/alibaba/rtp-llm) | ⭐1130 | Cuda | RTP-LLM: Alibaba's high-performance LLM inference engine for diverse a |
| [NVIDIA/audio-flamingo](https://github.com/NVIDIA/audio-flamingo) | ⭐1130 | None | PyTorch implementation of Audio Flamingo: Series of Advanced Audio Und |
| [NVIDIA/kvpress](https://github.com/NVIDIA/kvpress) | ⭐1091 | Python | LLM KV cache compression made easy |
| [Tencent/TencentPretrain](https://github.com/Tencent/TencentPretrain) | ⭐1087 | Python | Tencent Pre-training framework in PyTorch & Pre-trained Model Zoo  |
| [google-deepmind/dramatron](https://github.com/google-deepmind/dramatron) | ⭐1085 | Jupyter Notebook | Dramatron uses large language models to generate coherent scripts and  |
| [QwenLM/Qwen2.5-Math](https://github.com/QwenLM/Qwen2.5-Math) | ⭐1079 | Python | A series of math-specific large language models of our Qwen2 series. |
| [NVIDIA/sentiment-discovery](https://github.com/NVIDIA/sentiment-discovery) | ⭐1071 | Python | Unsupervised Language Modeling at scale for robust sentiment classific |
| [langchain-ai/openevals](https://github.com/langchain-ai/openevals) | ⭐1062 | Python | Readymade evaluators for your LLM apps |
| [langchain-ai/mcpdoc](https://github.com/langchain-ai/mcpdoc) | ⭐990 | Python | Expose llms-txt to IDEs for development |
| [run-llama/chat-llamaindex](https://github.com/run-llama/chat-llamaindex) | ⭐983 | TypeScript |  |
| [OpenBMB/RepoAgent](https://github.com/OpenBMB/RepoAgent) | ⭐968 | Python | An LLM-powered repository agent designed to assist developers and team |
| [QwenLM/Qwen3-ASR-Toolkit](https://github.com/QwenLM/Qwen3-ASR-Toolkit) | ⭐964 | Python | Official Python toolkit for the Qwen3-ASR API. Parallel high‑throughpu |
| [MoonshotAI/checkpoint-engine](https://github.com/MoonshotAI/checkpoint-engine) | ⭐956 | Python | Checkpoint-engine is a simple middleware to update model weights in LL |
| [FunAudioLLM/Fun-Audio-Chat](https://github.com/FunAudioLLM/Fun-Audio-Chat) | ⭐947 | Python | Fun-Audio-Chat is a Large Audio Language Model built for natural, low- |
| [THUDM/P-tuning](https://github.com/THUDM/P-tuning) | ⭐939 | Python | A novel method to tune language models. Codes and datasets for paper ` |
| [THUDM/AutoWebGLM](https://github.com/THUDM/AutoWebGLM) | ⭐932 | Python | An LLM-based Web Navigating Agent (KDD'24) |
| [stepfun-ai/Step-Audio-EditX](https://github.com/stepfun-ai/Step-Audio-EditX) | ⭐921 | Python | A powerful 3B-parameter, LLM-based Reinforcement Learning audio edit m |
| [OpenGVLab/OmniQuant](https://github.com/OpenGVLab/OmniQuant) | ⭐898 | Python | [ICLR2024 spotlight] OmniQuant is a simple and powerful quantization t |
| [mistralai/mistral-common](https://github.com/mistralai/mistral-common) | ⭐895 | Python | Official inference library for pre-processing of Mistral models |
| [TencentARC/SEED-Story](https://github.com/TencentARC/SEED-Story) | ⭐884 | Python | SEED-Story: Multimodal Long Story Generation with Large Language Model |
| [huggingface/llm-ls](https://github.com/huggingface/llm-ls) | ⭐872 | Rust | LSP server leveraging LLMs for code completion (and more?) |
| [mistralai/megablocks-public](https://github.com/mistralai/megablocks-public) | ⭐868 | None |  |
| [OpenBMB/ProAgent](https://github.com/OpenBMB/ProAgent) | ⭐864 | Python | An LLM-based Agent for the New Automation Paradigm - Agentic Process A |
| [Tencent/hpc-ops](https://github.com/Tencent/hpc-ops) | ⭐857 | C++ | High Performance LLM Inference Operator Library |
| [OpenBMB/IoA](https://github.com/OpenBMB/IoA) | ⭐821 | Python | An open-source framework for collaborative AI agents, enabling diverse |
| [meta-llama/prompt-ops](https://github.com/meta-llama/prompt-ops) | ⭐814 | Python | An open-source tool for LLM prompt optimization. |
| [vllm-project/recipes](https://github.com/vllm-project/recipes) | ⭐808 | JavaScript | Common recipes to run vLLM |
| [Tencent/AICGSecEval](https://github.com/Tencent/AICGSecEval) | ⭐796 | Python | A.S.E (AICGSecEval) is a repository-level AI-generated code security e |
| [OpenBMB/AgentCPM](https://github.com/OpenBMB/AgentCPM) | ⭐795 | Python | An End-to-End Infrastructure for Training and Evaluating Various LLM A |
| [deepseek-ai/awesome-deepseek-coder](https://github.com/deepseek-ai/awesome-deepseek-coder) | ⭐785 | None | A curated list of open-source projects related to DeepSeek Coder |
| [Tencent/PatrickStar](https://github.com/Tencent/PatrickStar) | ⭐775 | Python | PatrickStar enables Larger, Faster, Greener Pretrained Models for NLP  |
| [google-deepmind/opro](https://github.com/google-deepmind/opro) | ⭐746 | Python | official code for "Large Language Models as Optimizers" |
