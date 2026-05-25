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
