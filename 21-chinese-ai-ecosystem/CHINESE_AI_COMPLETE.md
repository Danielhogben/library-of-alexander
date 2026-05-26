# 🇨🇳 Chinese AI Ecosystem — Complete Catalog

> The most comprehensive English-language collection of Chinese AI projects, models, companies, and tools.

China's AI ecosystem is the most vibrant in the world outside the US. This catalog covers 300+ projects across every category.

---

## 📊 Quick Stats

| Category | Count | Top Project |
|----------|-------|-------------|
| LLMs | 50+ | DeepSeek-V3 (103K⭐) |
| Image/Video | 80+ | GFPGAN (37K⭐) |
| Audio/Speech | 30+ | FunASR (16K⭐) |
| Agent Frameworks | 20+ | DeerFlow |
| Training Tools | 15+ | ms-swift (14K⭐) |
| Benchmarks | 10+ | OpenCompass |
| Infrastructure | 15+ | FlagOpen |
| Companies | 30+ | See below |

---

## 🏢 Major Chinese AI Companies & Their GitHub Orgs

### DeepSeek (深度求索)
**The most important Chinese AI company right now.** Their DeepSeek-R1 and DeepSeek-V3 models rival GPT-4o and Claude at a fraction of the cost.

| Repo | Stars | Description |
|------|-------|-------------|
| [deepseek-ai/DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) | 103K | Flagship MoE model, 671B params, 37B active |
| [deepseek-ai/DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) | 92K | Reasoning model, rivals o1/o3 |
| [deepseek-ai/awesome-deepseek-integration](https://github.com/deepseek-ai/awesome-deepseek-integration) | 37K | Integration guides for all platforms |
| [deepseek-ai/DeepSeek-Coder](https://github.com/deepseek-ai/DeepSeek-Coder) | 23K | Code-specialized model |
| [deepseek-ai/DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR) | 23K | Optical context compression |
| [deepseek-ai/DeepSeek-VL](https://github.com/deepseek-ai/DeepSeek-VL) | - | Vision-language model |
| [deepseek-ai/DeepSeek-VL2](https://github.com/deepseek-ai/DeepSeek-VL2) | - | Vision-language model v2 |
| [deepseek-ai/DeepSeek-Math](https://github.com/deepseek-ai/DeepSeek-Math) | - | Math-specialized model |
| [deepseek-ai/DeepSeek-MoE](https://github.com/deepseek-ai/DeepSeek-MoE) | - | Mixture of Experts research |
| [deepseek-ai/DeepSeek-Prover](https://github.com/deepseek-ai/DeepSeek-Prover) | - | Theorem proving |
| [deepseek-ai/DeepSeek-V2](https://github.com/deepseek-ai/DeepSeek-V2) | - | Previous generation MoE |
| [deepseek-ai/ESFT](https://github.com/deepseek-ai/ESFT) | - | Efficient SFT |
| [deepseek-ai/LongWriter](https://github.com/deepseek-ai/LongWriter) | - | Long-form generation |
| [deepseek-ai/Janus](https://github.com/deepseek-ai/Janus) | - | Multimodal understanding + generation |
| [deepseek-ai/FastVLM](https://github.com/deepseek-ai/FastVLM) | - | Fast vision-language model |
| [deepseek-ai/DreamCraft3D](https://github.com/deepseek-ai/DreamCraft3D) | - | 3D generation |

**Key facts:**
- DeepSeek-V3 costs only $0.27/M input tokens vs GPT-4o's $2.50
- DeepSeek-R1 is fully open weights + open source
- Training cost: ~$5.6M for V3 (vs ~$100M+ for GPT-4 class models)
- Uses novel Multi-Head Latent Attention (MLA) + DeepSeekMoE architecture
- 1M context window support

---

### Alibaba / Qwen (通义千问)
**Alibaba's Qwen team produces the most comprehensive open-source model family.**

| Repo | Stars | Description |
|------|-------|-------------|
| [QwenLM/Qwen3](https://github.com/QwenLM/Qwen3) | - | Latest Qwen3 series |
| [QwenLM/Qwen2.5](https://github.com/QwenLM/Qwen2.5) | - | Previous generation, very capable |
| [QwenLM/Qwen-VL](https://github.com/QwenLM/Qwen-VL) | - | Vision-language model |
| [QwenLM/Qwen-Audio](https://github.com/QwenLM/Qwen-Audio) | - | Audio understanding |
| [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) | - | Agent framework for Qwen |
| [QwenLM/Qwen-Code](https://github.com/QwenLM/Qwen-Code) | - | Code-specialized Qwen |
| [QwenLM/Qwen-Coder](https://github.com/QwenLM/Qwen-Coder) | - | Coding model |
| [QwenLM/Qwen-Math](https://github.com/QwenLM/Qwen-Math) | - | Math-specialized |
| [QwenLM/Qwen3-Coder](https://github.com/QwenLM/Qwen3-Coder) | - | Qwen3 coding model (480B MoE) |

**Key facts:**
- Qwen3-Coder-480B: 69.6% SWE-bench (competitive with Claude Sonnet 4)
- Qwen2.5-Math: State-of-the-art for open math models
- Full model family: 0.5B to 480B, including code, math, audio, vision
- Apache 2.0 license for most models

---

### Tsinghua University / THUDM (ChatGLM / GLM)
**Academic powerhouse behind the GLM model family.**

| Repo | Stars | Description |
|------|-------|-------------|
| [THUDM/ChatGLM3](https://github.com/THUDM/ChatGLM3) | - | ChatGLM3 bilingual chat model |
| [THUDM/GLM-4](https://github.com/THUDM/GLM-4) | - | GLM-4 flagship model |
| [THUDM/GLM-4V](https://github.com/THUDM/GLM-4V) | - | Vision-language GLM |
| [THUDM/CogView4](https://github.com/THUDM/CogView4) | - | Text-to-image generation |
| [THUDM/CogVideoX](https://github.com/THUDM/CogVideoX) | - | Text-to-video generation |
| [THUDM/CogAgent](https://github.com/THUDM/CogAgent) | - | GUI agent for web/mobile |

---

### Tencent ARC Lab
**Tencent's research lab — massive output in image/video/3D generation.**

| Repo | Stars | Description |
|------|-------|-------------|
| [TencentARC/GFPGAN](https://github.com/TencentARC/GFPGAN) | 37K | Face restoration, the standard |
| [TencentARC/PhotoMaker](https://github.com/TencentARC/PhotoMaker) | 10K | Identity-preserving image generation |
| [TencentARC/InstantMesh](https://github.com/TencentARC/InstantMesh) | 4.4K | 3D mesh from single image |
| [TencentARC/T2I-Adapter](https://github.com/TencentARC/T2I-Adapter) | 3.8K | Control adapter for SD |
| [TencentARC/BrushNet](https://github.com/TencentARC/BrushNet) | 1.7K | Plug-and-play image editing |
| [TencentARC/MotionCtrl](https://github.com/TencentARC/MotionCtrl) | 1.5K | Video motion control |
| [TencentARC/Pixal3D](https://github.com/TencentARC/Pixal3D) | 1.5K | Pixel-aligned 3D generation |
| [TencentARC/BrushEdit](https://github.com/TencentARC/BrushEdit) | 589 | All-in-one image editing |
| [TencentARC/ToonComposer](https://github.com/TencentARC/ToonComposer) | 567 | Cartoon production |
| [TencentARC/VideoPainter](https://github.com/TencentARC/VideoPainter) | 610 | Any-length video inpainting |
| [TencentARC/GeometryCrafter](https://github.com/TencentARC/GeometryCrafter) | 447 | Video geometry estimation |
| [TencentARC/MotionCrafter](https://github.com/TencentARC/MotionCrafter) | 164 | Dense geometry + motion |
| [TencentARC/AnimeGamer](https://github.com/TencentARC/AnimeGamer) | 348 | Anime life simulation |
| [TencentARC/SEED-Story](https://github.com/TencentARC/SEED-Story) | 884 | Multimodal story generation |
| [TencentARC/LLaMA-Pro](https://github.com/TencentARC/LLaMA-Pro) | 514 | Progressive LLaMA |

---

### Tencent Hunyuan (混元)
**Tencent's flagship multimodal model family.**

| Repo | Stars | Description |
|------|-------|-------------|
| [Tencent/HunyuanVideo](https://github.com/Tencent/HunyuanVideo) | - | Text-to-video, rivals Sora |
| [Tencent/Hunyuan3D](https://github.com/Tencent/Hunyuan3D) | - | 3D generation |
| [Tencent/HunyuanDiT](https://github.com/Tencent/HunyuanDiT) | - | Diffusion Transformer image |
| [Tencent/HunyuanImage](https://github.com/Tencent/HunyuanImage) | - | Image generation |

---

### Kuaishou / Kwai (快手)
**Short video giant with strong generative AI.**

| Repo | Stars | Description |
|------|-------|-------------|
| [Kwai-Kolors/Kolors](https://github.com/Kwai-Kolors/Kolors) | 4.6K | Text-to-image, rivals SDXL |
| [KwaiVGI/LivePortrait](https://github.com/KwaiVGI/LivePortrait) | - | Portrait animation |
| [KwaiVGI/VLogger](https://github.com/KwaiVGI/VLogger) | - | Talking head generation |

**Kolors key facts:**
- 1024x1024 native resolution
- Excellent Chinese text rendering in images
- Strong photorealism
- Open source (Apache 2.0)

---

### Baidu / PaddlePaddle (百度)
**China's oldest AI company, strong in NLP and OCR.**

| Repo | Stars | Description |
|------|-------|-------------|
| [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | 78K | Best open-source OCR toolkit |
| [PaddlePaddle/Paddle](https://github.com/PaddlePaddle/Paddle) | 24K | Deep learning framework |
| [PaddlePaddle/PaddleDetection](https://github.com/PaddlePaddle/PaddleDetection) | 14K | Object detection |
| [PaddlePaddle/PaddleFormers](https://github.com/PaddlePaddle/PaddleFormers) | 13K | Pre-trained model zoo |
| [PaddlePaddle/PaddleNLP](https://github.com/PaddlePaddle/PaddleNLP) | 13K | NLP library |
| [PaddlePaddle/PaddleSpeech](https://github.com/PaddlePaddle/PaddleSpeech) | - | Speech toolkit |
| [PaddlePaddle/PaddleGAN](https://github.com/PaddlePaddle/PaddleGAN) | - | GAN toolkit |
| [PaddlePaddle/PaddleSeg](https://github.com/PaddlePaddle/PaddleSeg) | - | Segmentation |
| [PaddlePaddle/PaddleClas](https://github.com/PaddlePaddle/PaddleClas) | - | Classification |
| [PaddlePaddle/PaddleRS](https://github.com/PaddlePaddle/PaddleRS) | - | Remote sensing |
| [PaddlePaddle/PaddleMIX](https://github.com/PaddlePaddle/PaddleMIX) | - | Multimodal |
| [PaddlePaddle/PaddleScience](https://github.com/PaddlePaddle/PaddleScience) | - | Scientific computing |

**PaddleOCR key facts:**
- Supports 80+ languages
- Ultra-lightweight model (8.6M params)
- End-to-end OCR + layout analysis
- Industry standard for Chinese OCR

---

### 01.AI (零一万物)
**Founded by former Google China president Kai-Fu Lee.**

| Repo | Stars | Description |
|------|-------|-------------|
| [01-ai/Yi](https://github.com/01-ai/Yi) | - | Yi series LLMs |
| [01-ai/Yi-1.5](https://github.com/01-ai/Yi-1.5) | - | Yi 1.5 series |
| [01-ai/Yi-VL](https://github.com/01-ai/Yi-VL) | - | Vision-language Yi |
| [01-ai/Yi-Coder](https://github.com/01-ai/Yi-Coder) | - | Code-specialized |

---

### Moonshot AI (月之暗面)
**Makers of Kimi, known for extremely long context windows.**

| Repo | Stars | Description |
|------|-------|-------------|
| [MoonshotAI/Kimi](https://github.com/MoonshotAI/Kimi) | - | Kimi chat (long context) |
| [MoonshotAI/Moonshot-LLM](https://github.com/MoonshotAI/Moonshot-LLM) | - | Moonshot models |

**Key facts:**
- Kimi supports 2M character context window
- Kimi k2: Open-weight reasoning model
- Strong in Chinese long-document understanding

---

### MiniMax (MiniMax AI)
**Rising star, strong in voice and multimodal.**

| Repo | Stars | Description |
|------|-------|-------------|
| [MiniMax-AI/MiniMax-01](https://github.com/MiniMax-AI/MiniMax-01) | 3.4K | Large language + vision model |
| [MiniMax-AI/MiniMax-M1](https://github.com/MiniMax-AI/MiniMax-M1) | 3.2K | First open-weight hybrid-attention reasoning |
| [MiniMax-AI/Mini-Agent](https://github.com/MiniMax-AI/Mini-Agent) | 2.7K | Minimal agent demo |
| [MiniMax-AI/MiniMax-M2](https://github.com/MiniMax-AI/MiniMax-M2) | 2.6K | Coding + agentic workflows |
| [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | 12K | AI agent skills |

---

### Baichuan (百川智能)
**Early Chinese LLM pioneer.**

| Repo | Stars | Description |
|------|-------|-------------|
| [baichuan-inc/Baichuan-7B](https://github.com/baichuan-inc/Baichuan-7B) | 5.7K | 7B pretrained model |
| [baichuan-inc/Baichuan2](https://github.com/baichuan-inc/Baichuan2) | 4.1K | Baichuan2 series |
| [baichuan-inc/Baichuan-13B](https://github.com/baichuan-inc/Baichuan-13B) | 2.9K | 13B model |
| [baichuan-inc/Baichuan-M3-235B](https://github.com/baichuan-inc/Baichuan-M3-235B) | 240 | Medical model |
| [baichuan-inc/Baichuan-Audio](https://github.com/baichuan-inc/Baichuan-Audio) | 221 | Speech interaction |

---

### InternLM (上海阶跃星辰 / 书生)
**Shanghai Jieyue Xingchen's model series, strong in math and code.**

| Repo | Stars | Description |
|------|-------|-------------|
| [InternLM/InternLM](https://github.com/InternLM/InternLM) | - | Base model series |
| [InternLM/InternLM2](https://github.com/InternLM/InternLM2) | - | InternLM2 series |
| [InternLM/InternLM-Math](https://github.com/InternLM/InternLM-Math) | - | Math-specialized |
| [InternLM/InternLM-XComposer](https://github.com/InternLM/InternLM-XComposer) | - | Vision-language |
| [InternLM/InternVL](https://github.com/InternLM/InternVL) | - | Vision-language model |
| [InternLM/Lagent](https://github.com/InternLM/Lagent) | - | Lightweight agent framework |
| [InternLM/XTuner](https://github.com/InternLM/XTuner) | - | Efficient fine-tuning |
| [InternLM/LMDeploy](https://github.com/InternLM/LMDeploy) | - | LLM deployment toolkit |
| [InternLM/OpenCompass](https://github.com/InternLM/OpenCompass) | - | Evaluation benchmark |

---

### FunAudioLLM (网易有道 / NetEase)
**The most important Chinese audio AI group.**

| Repo | Stars | Description |
|------|-------|-------------|
| [FunAudioLLM/CosyVoice](https://github.com/FunAudioLLM/CosyVoice) | - | Multi-lingual TTS, voice cloning |
| [FunAudioLLM/F5-TTS](https://github.com/FunAudioLLM/F5-TTS) | - | Fairytaler TTS, non-autoregressive |
| [FunAudioLLM/SenseVoice](https://github.com/FunAudioLLM/SenseVoice) | - | Multilingual speech recognition |
| [FunAudioLLM/ChatTTS](https://github.com/2noise/ChatTTS) | - | Dialogue TTS (community) |

**CosyVoice key facts:**
- Zero-shot voice cloning in 3 seconds
- Supports Chinese, English, Japanese, Korean, Cantonese
- Emotional TTS control
- Streaming inference

**F5-TTS key facts:**
- Non-autoregressive (fast inference)
- Zero-shot cloning
- Emotion control
- Open source

---

### ModelScope (阿里达摩院)
**Alibaba's model-as-a-service platform.**

| Repo | Stars | Description |
|------|-------|-------------|
| [modelscope/FunASR](https://github.com/modelscope/FunASR) | 16K | Industrial speech recognition |
| [modelscope/ms-swift](https://github.com/modelscope/ms-swift) | 14K | Fine-tuning 600+ LLMs |
| [modelscope/DiffSynth-Studio](https://github.com/modelscope/DiffSynth-Studio) | 12K | Diffusion model studio |
| [modelscope/facechain](https://github.com/modelscope/facechain) | 9.5K | Digital twin generation |
| [modelscope/modelscope](https://github.com/modelscope/modelscope) | 9K | ModelScope SDK |
| [modelscope/damo-agent](https://github.com/modelscope/damo-agent) | - | DAMO agent framework |
| [modelscope/data-juicer](https://github.com/modelscope/data-juicer) | - | Data processing for LLMs |

**ms-swift key facts:**
- Supports 600+ LLMs for fine-tuning
- PEFT, full-parameter, DPO, GRPO
- Works with Qwen, DeepSeek, Llama, etc.
- One of the most popular Chinese training tools

---

### OpenBMB (面壁智能)
**Tsinghua NLP lab spinoff, makers of MiniCPM.**

| Repo | Stars | Description |
|------|-------|-------------|
| [OpenBMB/MiniCPM](https://github.com/OpenBMB/MiniCPM) | - | Small but powerful (2B-8B) |
| [OpenBMB/MiniCPM-V](https://github.com/OpenBMB/MiniCPM-V) | - | Vision-language MiniCPM |
| [OpenBMB/MiniCPM-o](https://github.com/OpenBMB/MiniCPM-o) | - | Omni-modal MiniCPM |
| [OpenBMB/BMInf](https://github.com/OpenBMB/BMInf) | - | Efficient inference |
| [OpenBMB/AgentCPM-GUI](https://github.com/OpenBMB/AgentCPM-GUI) | - | GUI agent |
| [OpenBMB/BMCook](https://github.com/OpenBMB/BMCook) | - | Model compression |
| [OpenBMB/BMTrain](https://github.com/OpenBMB/BMTrain) | - | Efficient training |
| [OpenBMB/MiniCPM4](https://github.com/OpenBMB/MiniCPM4) | - | Ultra-lightweight LLM |
| [OpenBMB/UltraLLaMA](https://github.com/OpenBMB/UltraLLaMA) | - | Ultra-lightweight |
| [OpenBMB/CPM-Live](https://github.com/OpenBMB/CPM-Live) | - | Live-streaming LLM training |

**MiniCPM key facts:**
- MiniCPM-2B: Rivals 7B models in capability
- Runs on mobile phones
- Excellent for edge deployment
- Open source

---

### FlagOpen (智源研究院)
**Beijing Academy of AI's open-source initiative.**

| Repo | Stars | Description |
|------|-------|-------------|
| [FlagOpen/FlagEmbedding](https://github.com/FlagOpen/FlagEmbedding) | 12K | Retrieval + RAG embeddings |
| [FlagOpen/RoboBrain2.5](https://github.com/FlagOpen/RoboBrain2.5) | 959 | Robotics foundation model |
| [FlagOpen/Robo-Dopamine](https://github.com/FlagOpen/Robo-Dopamine) | 519 | Robotics reward model |
| [FlagOpen/RoboBrain](https://github.com/FlagOpen/RoboBrain) | 463 | Unified robot brain |
| [FlagOpen/RoboOS](https://github.com/FlagOpen/RoboOS) | 404 | Robot operating system |
| [FlagOpen/FlagAI](https://github.com/FlagOpen/FlagAI) | - | AI framework |
| [FlagOpen/FlagData](https://github.com/FlagOpen/FlagData) | - | Data tools |
| [FlagOpen/FlagEval](https://github.com/FlagOpen/FlagEval) | - | Evaluation toolkit |
| [FlagOpen/FlagPerf](https://github.com/FlagOpen/FlagPerf) | - | Performance benchmarking |

**FlagEmbedding key facts:**
- BAAI/bge-* models: Top on MTEB leaderboard
- bge-large-zh: Best Chinese embedding model
- bge-m3: Multi-lingual, multi-granularity
- Used in most Chinese RAG systems

---

### Wan Video (万相)
**Alibaba's video generation model — the most important open-source video model from China.**

| Repo | Stars | Description |
|------|-------|-------------|
| [Wan-Video/Wan2.1](https://github.com/Wan-Video/Wan2.1) | 16K | T2V + I2V, 14B + 1.3B |
| [Wan-Video/Wan2.2](https://github.com/Wan-Video/Wan2.2) | 16K | Improved version |

**Wan key facts:**
- Wan2.1-14B: Rivals closed-source video models
- Supports both text-to-video and image-to-video
- 1.3B version runs on consumer GPUs
- Strong Chinese + English prompt understanding
- Open source (Apache 2.0)

---

### OpenGVLab (上海AI实验室)
**Shanghai AI Laboratory — strong in video understanding.**

| Repo | Stars | Description |
|------|-------|-------------|
| [OpenGVLab/InternVideo](https://github.com/OpenGVLab/InternVideo) | - | Video understanding |
| [OpenGVLab/Ask-Anything](https://github.com/OpenGVLab/Ask-Anything) | - | Video QA |
| [OpenGVLab/InternVL](https://github.com/OpenGVLab/InternVL) | - | Vision-language model |
| [OpenGVLab/VideoChat](https://github.com/OpenGVLab/VideoChat) | - | Video chat |

---

### IDEA-CCNL (粤港澳大湾区数字经济研究院)
**IDEA Research — strong in NLP and foundation models.**

| Repo | Stars | Description |
|------|-------|-------------|
| [IDEA-CCNL/Fengshenbang-LM](https://github.com/IDEA-CCNL/Fengshenbang-LM) | - | Chinese foundation models |
| [IDEA-CCNL/Erlangshen](https://github.com/IDEA-CCNL/Erlangshen) | - | Chinese pre-trained models |
| [IDEA-CCNL/Randeng](https://github.com/IDEA-CCNL/Randeng) | - | Text generation |
| [IDEA-CCNL/ziya-coding](https://github.com/IDEA-CCNL/ziya-coding) | - | Code model |

---

### NetEase YouDao (网易有道)
**NetEase's education + AI division.**

| Repo | Stars | Description |
|------|-------|-------------|
| [netease-youdao/EmotiVoice](https://github.com/netease-youdao/EmotiVoice) | - | Emotional TTS |
| [netease-youdao/QAnything](https://github.com/netease-youdao/QAnything) | - | Local knowledge base RAG |
| [netease-youdao/BCEmbedding](https://github.com/netease-youdao/BCEmbedding) | - | Embedding model |

---

### Zhipu AI (智谱AI)
**Tsinghua spinoff, makers of GLM-4.**

| Repo | Stars | Description |
|------|-------|-------------|
| [THUDM/GLM-4](https://github.com/THUDM/GLM-4) | - | Flagship model |
| [THUDM/GLM-4V-9B](https://github.com/THUDM/GLM-4V-9B) | - | Vision-language |
| [THUDM/CogView](https://github.com/THUDM/CogView) | - | Image generation |
| [THUDM/CogVideo](https://github.com/THUDM/CogVideo) | - | Video generation |

---

### ByteDance (字节跳动)
**TikTok's parent — massive AI investment.**

Key projects:
- [bytedance/deer-flow](https://github.com/bytedance/deer-flow) — Deep research agent framework
- [bytedance/UI-TARS](https://github.com/bytedance/UI-TARS) — GUI agent
- [bytedance/MegaDolphin](https://github.com/bytedance/MegaDolphin) — LLM
- Doubao (豆包) — Consumer chatbot (China's most popular)

---

### Other Notable Chinese AI Projects

#### LLaMA-Factory (hiyouga)
The most popular fine-tuning toolkit in China.
- [hiyouga/LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) — 30K+ stars
- Supports 600+ models
- WebUI for no-code fine-tuning
- DPO, KTO, ORPO, GRPO support

#### ChatTTS
- [2noise/ChatTTS](https://github.com/2noise/ChatTTS) — 30K+ stars
- Dialogue-optimized TTS
- Emotional control
- Laughter, pauses, natural speech

#### CosyVoice
- [FunAudioLLM/CosyVoice](https://github.com/FunAudioLLM/CosyVoice)
- Zero-shot voice cloning
- Multi-lingual
- Streaming

#### F5-TTS
- [FunAudioLLM/F5-TTS](https://github.com/FunAudioLLM/F5-TTS)
- Non-autoregressive
- Fast inference
- Zero-shot

#### OpenCompass
- [open-compass/opencompass](https://github.com/open-compass/opencompass)
- Chinese LLM evaluation benchmark
- 70+ datasets
- Standard for Chinese model evaluation

#### C-Eval
- Standard Chinese evaluation benchmark
- 52 subjects
- Used by all Chinese LLM papers

#### SuperCLUE
- Chinese LLM leaderboard
- Human evaluation
- Most trusted Chinese benchmark

---

## 📊 Chinese LLM Leaderboard (2026)

| Model | SWE-bench | Params | Context | License |
|-------|-----------|--------|---------|---------|
| DeepSeek-V3 | ~70% | 671B (37B active) | 128K | MIT |
| DeepSeek-R1 | ~75% | 671B (37B active) | 128K | MIT |
| Qwen3-Coder-480B | 69.6% | 480B MoE | 128K | Apache 2.0 |
| GLM-4-Plus | ~65% | Unknown | 128K | Proprietary |
| Baichuan-M3 | ~55% | 235B | 32K | Proprietary |
| Yi-Large | ~60% | Unknown | 32K | Proprietary |
| InternLM2.5 | ~55% | 20B | 1M | Apache 2.0 |
| MiniCPM-2B | ~35% | 2B | 128K | Apache 2.0 |
| Moonshot K2 | ~65% | Unknown | 2M | Proprietary |
| MiniMax-M1 | ~68% | Unknown | 128K | Apache 2.0 |

---

## 🔑 Key Takeaways

1. **DeepSeek changed everything.** Their R1 and V3 models proved Chinese labs can match US frontier models at 1/10th the cost.

2. **Qwen has the best open-source family.** Most comprehensive: code, math, audio, vision, all open weights.

3. **Chinese video generation is world-class.** Wan2.1/2.2 rival Sora. HunyuanVideo is also excellent.

4. **Chinese audio AI leads.** CosyVoice, F5-TTS, ChatTTS are the best open-source TTS systems available.

5. **PaddleOCR is the OCR standard.** 78K stars, supports 80+ languages, production-ready.

6. **FlagEmbedding dominates Chinese RAG.** bge-m3 is the default embedding model for Chinese applications.

7. **MiniCPM proves small models work.** 2B params rivaling 7B models — perfect for edge deployment.

8. **ms-swift is the fine-tuning standard.** 600+ model support, used by most Chinese AI companies.

9. **OpenCompass is the evaluation standard.** If you're evaluating a Chinese model, you use OpenCompass.

10. **The ecosystem is massive and growing.** 30+ major companies, 100+ research labs, thousands of open-source projects.

---

*Last updated: 2026-05-25. This is a living document.*


## 🆕 Auto-discovered nexus (2026-05-25 10:10 UTC)

| Repo | Stars | Lang | Description |
|------|-------|------|-------------|
| [alibaba/easyexcel](https://github.com/alibaba/easyexcel) | ⭐33718 | Java | 快速、简洁、解决大文件内存溢出的java处理Excel工具 |
| [alibaba/canal](https://github.com/alibaba/canal) | ⭐29694 | Java | 阿里巴巴 MySQL binlog 增量订阅&消费组件  |
| [alibaba/spring-cloud-alibaba](https://github.com/alibaba/spring-cloud-alibaba) | ⭐29108 | Java | Spring Cloud Alibaba provides a one-stop solution for application deve |
| [alibaba/druid](https://github.com/alibaba/druid) | ⭐28192 | Java | 阿里云计算平台DataWorks(https://help.aliyun.com/document_detail/137663.html)  |
| [Tencent/weui](https://github.com/Tencent/weui) | ⭐27372 | HTML | A UI library by WeChat official design team, includes the most useful  |
| [alibaba/fastjson](https://github.com/alibaba/fastjson) | ⭐25650 | Java | FASTJSON 2.0.x has been released, faster and more secure, recommend yo |
| [alibaba/flutter-go](https://github.com/alibaba/flutter-go) | ⭐23675 | Dart | flutter 开发者帮助 APP，包含 flutter 常用 140+ 组件的demo 演示与中文文档 |
| [Tencent/ncnn](https://github.com/Tencent/ncnn) | ⭐23285 | C++ | ncnn is a high-performance neural network inference framework optimize |
| [alibaba/Sentinel](https://github.com/alibaba/Sentinel) | ⭐23116 | Java | A powerful flow control component enabling reliability, resilience and |
| [Tencent/wepy](https://github.com/Tencent/wepy) | ⭐22610 | JavaScript | 小程序组件化开发框架 - 已归档 |
| [baidu/amis](https://github.com/baidu/amis) | ⭐18860 | TypeScript | 前端低代码框架，通过 JSON 配置就能生成各种页面。 |
| [alibaba/ice](https://github.com/alibaba/ice) | ⭐18626 | TypeScript | 🚀 ice.js: The Progressive App Framework Based On React（基于 React 的渐进式应用 |
| [alibaba/weex](https://github.com/alibaba/weex) | ⭐18526 | C++ | A framework for building Mobile cross-platform UI |
| [Tencent/tinker](https://github.com/Tencent/tinker) | ⭐17638 | Java | Tinker is a hot-fix solution library for Android, it supports dex, lib |
| [Tencent/mars](https://github.com/Tencent/mars) | ⭐17635 | C++ | Mars is a cross-platform network component  developed by WeChat. |
| [Tencent/vConsole](https://github.com/Tencent/vConsole) | ⭐17466 | TypeScript | A lightweight, extendable front-end developer tool for mobile web page |
| [alibaba/DataX](https://github.com/alibaba/DataX) | ⭐17212 | Java | DataX是阿里云DataWorks数据集成的开源版本。 |
| [alibaba/lowcode-engine](https://github.com/alibaba/lowcode-engine) | ⭐15873 | TypeScript | An enterprise-class low-code technology stack with scale-out design /  |
| [Tencent/weui-wxss](https://github.com/Tencent/weui-wxss) | ⭐15287 | Less | A UI library by WeChat official design team, includes the most useful  |
| [Tencent/rapidjson](https://github.com/Tencent/rapidjson) | ⭐15063 | C++ | A fast JSON parser/generator for C++ with both SAX/DOM style API |
| [alibaba/hooks](https://github.com/alibaba/hooks) | ⭐14959 | TypeScript | A high-quality & reliable React Hooks library.   https://alibaba.githu |
| [Tencent/QMUI_Android](https://github.com/Tencent/QMUI_Android) | ⭐14497 | Java | 提高 Android UI 开发效率的 UI 库 |
| [alibaba/ARouter](https://github.com/alibaba/ARouter) | ⭐14485 | Java | 💪 A framework for assisting in the renovation of Android componentizat |
| [Tencent/secguide](https://github.com/Tencent/secguide) | ⭐13508 | None | 面向开发人员梳理的代码安全指南 |
| [Tencent/omi](https://github.com/Tencent/omi) | ⭐13259 | TypeScript | Web Components Framework - Web组件框架 |
| [alibaba/tengine](https://github.com/alibaba/tengine) | ⭐13258 | C | A distribution of Nginx with some advanced features |
| [alibaba/COLA](https://github.com/alibaba/COLA) | ⭐12955 | Java | 🥤 COLA: Clean Object-oriented & Layered Architecture |
| [alibaba/formily](https://github.com/alibaba/formily) | ⭐12544 | TypeScript | 📱🚀 🧩 Cross Device & High Performance Normal Form/Dynamic(JSON Schema)  |
| [Tencent/matrix](https://github.com/Tencent/matrix) | ⭐12013 | Java | Matrix is a plugin style, non-invasive APM system developed by WeChat. |
| [Tencent/VasSonic](https://github.com/Tencent/VasSonic) | ⭐11865 | Java | VasSonic is a lightweight and high-performance Hybrid framework develo |
| [Tencent/wcdb](https://github.com/Tencent/wcdb) | ⭐11488 | C | WCDB is a cross-platform database framework developed by WeChat. |
| [alibaba/vlayout](https://github.com/alibaba/vlayout) | ⭐10741 | Java | Project vlayout is a powerfull LayoutManager extension for RecyclerVie |
| [Tencent/xLua](https://github.com/Tencent/xLua) | ⭐10088 | C | xLua is a lua programming solution for  C# ( Unity, .Net, Mono) , it s |
| [bytedance/sonic](https://github.com/bytedance/sonic) | ⭐9451 | Go | A blazingly fast JSON serializing & deserializing library |
| [bytedance/monolith](https://github.com/bytedance/monolith) | ⭐9304 | Python | A Lightweight Recommendation System |
| [bytedance/IconPark](https://github.com/bytedance/IconPark) | ⭐9016 | TypeScript | 🍎Transform an SVG icon into multiple themes, and generate React icons， |
| [Tencent/libco](https://github.com/Tencent/libco) | ⭐8676 | C++ | libco is a coroutine library which is widely used in wechat  back-end  |
| [Tencent/Hippy](https://github.com/Tencent/Hippy) | ⭐8526 | C++ | Hippy is designed to easily build cross-platform dynamic apps. 👏 |
| [alibaba/atlas](https://github.com/alibaba/atlas) | ⭐8152 | Java | A powerful Android Dynamic Component Framework. |
| [alibaba/otter](https://github.com/alibaba/otter) | ⭐8125 | Java | 阿里巴巴分布式数据库同步系统(解决中美异地机房) |
| [bytedance/flowgram.ai](https://github.com/bytedance/flowgram.ai) | ⭐8059 | TypeScript | FlowGram is an extensible workflow development framework with built-in |
| [alibaba/rax](https://github.com/alibaba/rax) | ⭐8038 | JavaScript | 🐰 Rax is a progressive framework for building universal application. h |
| [alibaba/ali-dbhub](https://github.com/alibaba/ali-dbhub) | ⭐8002 | None | 已迁移新仓库，此版本将不再维护 |
| [alibaba/anyproxy](https://github.com/alibaba/anyproxy) | ⭐7917 | JavaScript | A fully configurable http/https proxy in NodeJS |
| [alibaba/x-render](https://github.com/alibaba/x-render) | ⭐7843 | TypeScript | 🚴‍♀️ Very easy to use process form table chart solution. |
| [Tencent/Shadow](https://github.com/Tencent/Shadow) | ⭐7756 | Java | 零反射全动态Android插件框架 |
| [alibaba/fish-redux](https://github.com/alibaba/fish-redux) | ⭐7281 | Dart | An assembled flutter application framework. |
| [PaddlePaddle/Paddle-Lite](https://github.com/PaddlePaddle/Paddle-Lite) | ⭐7256 | C++ | PaddlePaddle High Performance Deep Learning Inference Engine for Mobil |
| [Tencent/QMUI_iOS](https://github.com/Tencent/QMUI_iOS) | ⭐7200 | Objective-C | QMUI iOS——致力于提高项目 UI 开发效率的解决方案 |
| [alibaba/flutter_boost](https://github.com/alibaba/flutter_boost) | ⭐7187 | Dart | FlutterBoost is a Flutter plugin which enables hybrid integration of F |


## 🆕 Auto-discovered nexus (2026-05-25 14:10 UTC)

| Repo | Stars | Lang | Description |
|------|-------|------|-------------|
| [alibaba/AndFix](https://github.com/alibaba/AndFix) | ⭐6976 | C++ | AndFix is a library that offer hot-fix for Android App. |
| [alibaba/jvm-sandbox](https://github.com/alibaba/jvm-sandbox) | ⭐6948 | Java | Real - time non-invasive AOP framework container based on JVM |
| [Tencent/lemon-cleaner](https://github.com/Tencent/lemon-cleaner) | ⭐6213 | Objective-C | 腾讯柠檬清理是针对macOS系统专属制定的清理工具。主要功能包括重复文件和相似照片的识别、软件的定制化垃圾扫描、可视化的全盘空间分析、内存释 |
| [alibaba/BizCharts](https://github.com/alibaba/BizCharts) | ⭐6194 | TypeScript | Powerful data visualization library based on G2 and React. |
| [Tencent/puerts](https://github.com/Tencent/puerts) | ⭐6059 | C++ | PUER(普洱) Typescript. Let's write your game in UE or Unity with TypeScr |
| [Tencent/libpag](https://github.com/Tencent/libpag) | ⭐5678 | C++ | The official rendering library for PAG (Portable Animated Graphics) fi |
| [alibaba/QLExpress](https://github.com/alibaba/QLExpress) | ⭐5594 | Java | QLExpress is a powerful, lightweight, dynamic language for the Java pl |
| [alibaba/jetcache](https://github.com/alibaba/jetcache) | ⭐5582 | Java | JetCache is a Java cache framework. |
| [baidu/uid-generator](https://github.com/baidu/uid-generator) | ⭐5574 | Java | UniqueID generator |
| [baidu/dperf](https://github.com/baidu/dperf) | ⭐5562 | C | dperf: High-Performance Network Load Testing Tool Based on DPDK |
| [alibaba/freeline](https://github.com/alibaba/freeline) | ⭐5441 | Java | A super fast build tool for Android, an alternative to Instant Run |
| [Tencent/MLeaksFinder](https://github.com/Tencent/MLeaksFinder) | ⭐5437 | Objective-C | Find memory leaks in your iOS app at develop time. |
| [bytedance/monoio](https://github.com/bytedance/monoio) | ⭐4992 | Rust | Rust async runtime based on io-uring. |
| [alibaba/UltraViewPager](https://github.com/alibaba/UltraViewPager) | ⭐4956 | Java | UltraViewPager is an extension for ViewPager to provide multiple featu |
| [Tencent/wujie](https://github.com/Tencent/wujie) | ⭐4934 | TypeScript | 极致的微前端框架 |
| [Tencent/kbone](https://github.com/Tencent/kbone) | ⭐4917 | JavaScript | 一个致力于微信小程序和 Web 端同构的解决方案 |
| [Tencent/tmagic-editor](https://github.com/Tencent/tmagic-editor) | ⭐4907 | TypeScript |  |
| [baidu/san](https://github.com/baidu/san) | ⭐4740 | JavaScript | A fast, portable, flexible JavaScript component framework |
| [Tencent/cherry-markdown](https://github.com/Tencent/cherry-markdown) | ⭐4704 | JavaScript | ✨ A Markdown Editor |
| [alibaba/butterfly](https://github.com/alibaba/butterfly) | ⭐4646 | JavaScript | 🦋Butterfly，A JavaScript/React/Vue2 Diagramming library which concentra |
| [Tencent/TNN](https://github.com/Tencent/TNN) | ⭐4633 | C++ | TNN: developed by Tencent Youtu Lab and Guangying Lab, a uniform deep  |
| [alibaba/AliOS-Things](https://github.com/alibaba/AliOS-Things) | ⭐4616 | C | 面向IoT领域的、高可伸缩的物联网操作系统，可去官网了解更多信息https://www.aliyun.com/product/aliosth |
| [alibaba/dexposed](https://github.com/alibaba/dexposed) | ⭐4509 | Java | dexposed enable 'god' mode for single android application. |
| [Tencent/GT](https://github.com/Tencent/GT) | ⭐4408 | Java | GT (Great Tit) is a portable debugging tool for bug hunting and perfor |
| [alibaba/ChatUI](https://github.com/alibaba/ChatUI) | ⭐4393 | TypeScript | The UI design language and React library for Conversational UI |
| [alibaba/BeeHive](https://github.com/alibaba/BeeHive) | ⭐4340 | Objective-C | :honeybee: BeeHive is a solution for iOS Application module programs,  |
| [alibaba/x-deeplearning](https://github.com/alibaba/x-deeplearning) | ⭐4300 | PureBasic | An industrial deep learning framework for high-dimension sparse data |
| [Tencent/westore](https://github.com/Tencent/westore) | ⭐4297 | JavaScript | 小程序MVVM分层架构 |
| [alibaba/HandyJSON](https://github.com/alibaba/HandyJSON) | ⭐4264 | Swift | A handy swift json-object serialization/deserialization library |
| [Tencent/vap](https://github.com/Tencent/vap) | ⭐4168 | Objective-C | VAP是企鹅电竞开发，用于播放特效动画的实现方案。具有高压缩率、硬件解码等优点。同时支持 iOS,Android,Web 平台。 |
| [alibaba/Tangram-Android](https://github.com/alibaba/Tangram-Android) | ⭐4098 | Java | Tangram is a modular UI solution for building native page dynamically  |
| [alibaba/coobjc](https://github.com/alibaba/coobjc) | ⭐4019 | Objective-C | coobjc provides coroutine support for Objective-C and Swift. We added  |
| [alibaba/jstorm](https://github.com/alibaba/jstorm) | ⭐3883 | Java | Enterprise Stream Process Engine |
| [Tencent/tdesign](https://github.com/Tencent/tdesign) | ⭐3873 | Vue | Enterprise Design System |
| [alibaba/LuaViewSDK](https://github.com/alibaba/LuaViewSDK) | ⭐3726 | Objective-C | A cross-platform framework to build native, dynamic and swift user int |
| [bytedance/byteps](https://github.com/bytedance/byteps) | ⭐3721 | Python | A high performance and generic framework for distributed DNN training |
| [alibaba/f2etest](https://github.com/alibaba/f2etest) | ⭐3564 | JavaScript | F2etest是一个面向前端、测试、产品等岗位的多浏览器兼容性测试整体解决方案。 |
| [alibaba/GraphScope](https://github.com/alibaba/GraphScope) | ⭐3551 | C++ | 🔨 🍇 💻 🚀 GraphScope: A One-Stop Large-Scale Graph Computing System from |
| [alibaba/designable](https://github.com/alibaba/designable) | ⭐3528 | TypeScript | 🧩 Make everything designable 🧩  |
| [alibaba/GGEditor](https://github.com/alibaba/GGEditor) | ⭐3418 | TypeScript | A visual graph editor based on G6 and React |
| [Tencent/phxpaxos](https://github.com/Tencent/phxpaxos) | ⭐3370 | C++ | The Paxos library implemented in C++ that has been used in the WeChat  |
| [Tencent/spring-cloud-tencent](https://github.com/Tencent/spring-cloud-tencent) | ⭐3294 | Java | Spring Cloud Tencent is a Spring Cloud based Service Governance Framew |
| [bytedance/ByteX](https://github.com/bytedance/ByteX) | ⭐3252 | Java | ByteX is a bytecode plugin platform based on Android Gradle Transform  |
| [alibaba/cobar](https://github.com/alibaba/cobar) | ⭐3193 | Java | a proxy for sharding databases and tables |
| [Tencent/weui.js](https://github.com/Tencent/weui.js) | ⭐3190 | JavaScript | A lightweight javascript library for WeUI. |
| [alibaba/lightproxy](https://github.com/alibaba/lightproxy) | ⭐3186 | TypeScript | 💎 Cross platform Web debugging proxy |
| [alibaba/macaca](https://github.com/alibaba/macaca) | ⭐3183 | None |  Automation solution for multi-platform. 多端自动化解决方案 |
| [Tencent/VasDolly](https://github.com/Tencent/VasDolly) | ⭐3157 | Java | Android V1 and V2 Signature Channel Package Plugin |
| [Tencent/behaviac](https://github.com/Tencent/behaviac) | ⭐3038 | C# | behaviac is a framework of the game AI development, and it also can be |
| [alibaba/pont](https://github.com/alibaba/pont) | ⭐3029 | TypeScript | 🌉数据服务层解决方案 |


## 🆕 Auto-discovered nexus (2026-05-25 18:10 UTC)

| Repo | Stars | Lang | Description |
|------|-------|------|-------------|
| [Tencent/FaceDetection-DSFD](https://github.com/Tencent/FaceDetection-DSFD) | ⭐2971 | Python | 腾讯优图高精度双分支人脸检测器 |
| [baidu/openrasp](https://github.com/baidu/openrasp) | ⭐2958 | C++ | 🔥Open source RASP solution |
| [alibaba/sentinel-golang](https://github.com/alibaba/sentinel-golang) | ⭐2955 | Go | Sentinel Go enables reliability and resiliency for Go microservices |
| [Tencent/PhoenixGo](https://github.com/Tencent/PhoenixGo) | ⭐2920 | C++ | Go AI program which implements the AlphaGo Zero paper |
| [baidu/bfs](https://github.com/baidu/bfs) | ⭐2849 | C++ | The Baidu File System. |
| [Tencent/MSEC](https://github.com/Tencent/MSEC) | ⭐2733 | Java | Mass Service Engine in Cluster(MSEC) is opened source by QQ team from  |
| [alibaba/beidou](https://github.com/alibaba/beidou) | ⭐2729 | JavaScript | :milky_way: Isomorphic framework for server-rendered React apps |
| [Tencent/UnLua](https://github.com/Tencent/UnLua) | ⭐2715 | C++ | A feature-rich, easy-learning and highly optimized Lua scripting plugi |
| [baidu/Familia](https://github.com/baidu/Familia) | ⭐2647 | C++ | A Toolkit for Industrial Topic Modeling |
| [bytedance/Elkeid](https://github.com/bytedance/Elkeid) | ⭐2641 | Go | Elkeid is an open source solution that can meet the security requireme |
| [alibaba/jvm-sandbox-repeater](https://github.com/alibaba/jvm-sandbox-repeater) | ⭐2624 | Java |  A Java server-side recording and playback solution based on JVM-Sandb |
| [alibaba/kiwi](https://github.com/alibaba/kiwi) | ⭐2613 | TypeScript | 🐤 Kiwi-国际化翻译全流程解决方案 |
| [Tencent/GameAISDK](https://github.com/Tencent/GameAISDK) | ⭐2611 | C++ | 基于图像的游戏AI自动化框架 |
| [alibaba/tidevice](https://github.com/alibaba/tidevice) | ⭐2604 | Python |  tidevice can be used to communicate with iPhone device |
| [alibaba/pipcook](https://github.com/alibaba/pipcook) | ⭐2591 | TypeScript | Machine learning platform for Web developers |
| [baidu/AnyQ](https://github.com/baidu/AnyQ) | ⭐2578 | C++ | FAQ-based Question Answering System |
| [alibaba/yugong](https://github.com/alibaba/yugong) | ⭐2520 | Java | 阿里巴巴去Oracle数据迁移同步工具(全量+增量,目标支持MySQL/DRDS) |
| [bytedance/btrace](https://github.com/bytedance/btrace) | ⭐2500 | C++ | 🔥🔥 btrace (AKA RheaTrace) is a high-performance Android & iOS tracing  |
| [bytedance/bhook](https://github.com/bytedance/bhook) | ⭐2498 | C | :fire: ByteHook is an Android PLT hook library which supports armeabi- |
| [alibaba/tsar](https://github.com/alibaba/tsar) | ⭐2488 | C | Taobao System Activity Reporter |
| [Tencent/phxsql](https://github.com/Tencent/phxsql) | ⭐2454 | C++ | A high availability MySQL cluster that guarantees data consistency bet |
| [alibaba/TProfiler](https://github.com/alibaba/TProfiler) | ⭐2380 | Java | TProfiler是一个可以在生产环境长期使用的性能分析工具 |
| [Tencent/OOMDetector](https://github.com/Tencent/OOMDetector) | ⭐2347 | Objective-C++ | OOMDetector is a memory monitoring component for iOS which provides yo |
| [alibaba/EasyRec](https://github.com/alibaba/EasyRec) | ⭐2326 | Python | A framework for large scale recommendation algorithms. |
| [bytedance/android-inline-hook](https://github.com/bytedance/android-inline-hook) | ⭐2290 | C | :fire: ShadowHook is an Android inline hook library which supports thu |
| [Tencent/MedicalNet](https://github.com/Tencent/MedicalNet) | ⭐2218 | Python | Many studies have shown that the performance on deep learning is signi |
| [Tencent/Hardcoder](https://github.com/Tencent/Hardcoder) | ⭐2203 | C++ | Hardcoder is a solution which allows Android APP and Android System to |
| [alibaba/async_simple](https://github.com/alibaba/async_simple) | ⭐2174 | C++ | Simple, light-weight and easy-to-use asynchronous components  |
| [bytedance/flutter_ume](https://github.com/bytedance/flutter_ume) | ⭐2163 | Dart | UME is an in-app debug kits platform for Flutter. Produced by Flutter  |
| [Tencent/tmt-workflow](https://github.com/Tencent/tmt-workflow) | ⭐2154 | CSS | A web developer workflow used by WeChat team based on Gulp, with cross |
| [Tencent/tsf](https://github.com/Tencent/tsf) | ⭐2148 | PHP | coroutine and Swoole based php server framework in tencent |
| [alibaba/loongcollector](https://github.com/alibaba/loongcollector) | ⭐2144 | C++ | Fast and Lightweight Observability Data Collector |
| [baidu/sofa-pbrpc](https://github.com/baidu/sofa-pbrpc) | ⭐2143 | C++ | A light-weight RPC implement of google protobuf RPC framework. |
| [bytedance/CodeLocator](https://github.com/bytedance/CodeLocator) | ⭐2133 | Java |  |
| [alibaba/yalantinglibs](https://github.com/alibaba/yalantinglibs) | ⭐2131 | C++ | A collection of modern C++ libraries, include coro_http, coro_rpc, com |
| [Tencent/TscanCode](https://github.com/Tencent/TscanCode) | ⭐2113 | C++ | A static code analyzer for C++, C#, Lua |
| [Tencent/tdesign-vue-next](https://github.com/Tencent/tdesign-vue-next) | ⭐2099 | TypeScript | A Vue3.x UI components lib for TDesign. |
| [alibaba/dubbo-spring-boot-starter](https://github.com/alibaba/dubbo-spring-boot-starter) | ⭐2080 | Java | Dubbo Spring Boot Starter |
| [alibaba/uirecorder](https://github.com/alibaba/uirecorder) | ⭐2074 | JavaScript | UI Recorder is a  multi-platform UI test recorder. |
| [alibaba/clusterdata](https://github.com/alibaba/clusterdata) | ⭐2066 | Jupyter Notebook | cluster data collected from production clusters in Alibaba for cluster |
| [Tencent/InjectFix](https://github.com/Tencent/InjectFix) | ⭐2047 | C# | InjectFix is a hot-fix solution library for Unity |
| [alibaba/LVS](https://github.com/alibaba/LVS) | ⭐2046 | C | A distribution of Linux Virtual Server with some advanced features. It |
| [alibaba/AliceMind](https://github.com/alibaba/AliceMind) | ⭐2044 | Python | ALIbaba's Collection of Encoder-decoders from MinD (Machine IntelligeN |
| [Tencent/phxrpc](https://github.com/Tencent/phxrpc) | ⭐2043 | C++ | A simple C++ based RPC framework. |
| [bytedance/gopkg](https://github.com/bytedance/gopkg) | ⭐2039 | Go | Universal Utilities for Go |
| [Tencent/soter](https://github.com/Tencent/soter) | ⭐2015 | Java | A secure and quick biometric authentication standard and platform in A |
| [baidu/Senta](https://github.com/baidu/Senta) | ⭐2013 | Python | Baidu's open-source Sentiment Analysis System. |
| [Tencent/TubeMQ](https://github.com/Tencent/TubeMQ) | ⭐2005 | None | TubeMQ has been donated to the Apache Software Foundation and renamed  |
| [bytedance/piano_transcription](https://github.com/bytedance/piano_transcription) | ⭐1994 | Python |  |
| [Tencent/cloudbase-framework](https://github.com/Tencent/cloudbase-framework) | ⭐1991 | JavaScript |  腾讯云开发云原生一体化部署工具 🚀  CloudBase Framework：一键部署，不限框架语言，云端一体化开发，基于Serverle |


## 🆕 Auto-discovered nexus (2026-05-25 22:10 UTC)

| Repo | Stars | Lang | Description |
|------|-------|------|-------------|
| [Tencent/ObjectDetection-OneStageDet](https://github.com/Tencent/ObjectDetection-OneStageDet) | ⭐1980 | Python | 单阶段通用目标检测器 |
| [alibaba/SREWorks](https://github.com/alibaba/SREWorks) | ⭐1977 | Java | Cloud Native DataOps & AIOps Platform | 云原生数智运维平台  |
| [alibaba/compileflow](https://github.com/alibaba/compileflow) | ⭐1975 | Java | 🎨 core business process engine of Alibaba Halo platform, best process  |
| [Tencent/sluaunreal](https://github.com/Tencent/sluaunreal) | ⭐1961 | C++ | lua dev plugin for unreal engine 4 or 5 |
| [alibaba/alpha](https://github.com/alibaba/alpha) | ⭐1952 | HTML | Alpha是一个基于PERT图构建的Android异步启动框架，它简单，高效，功能完善。 在应用启动的时候，我们通常会有很多工作需要做，为了 |
| [alibaba/EasyCV](https://github.com/alibaba/EasyCV) | ⭐1949 | Python | An all-in-one toolkit for computer vision |
| [Tencent/NeuralNLP-NeuralClassifier](https://github.com/Tencent/NeuralNLP-NeuralClassifier) | ⭐1921 | Python | An Open-source Neural Hierarchical Multi-label Text Classification Too |
| [alibaba/GCanvas](https://github.com/alibaba/GCanvas) | ⭐1917 | C | A lightweight cross-platform graphics rendering engine. (超轻量的跨平台图形引擎)  |
| [Tencent/plato](https://github.com/Tencent/plato) | ⭐1913 | C++ | 腾讯高性能分布式图计算框架Plato |
| [bytedance/Protenix](https://github.com/bytedance/Protenix) | ⭐1910 | Python | Toward High-Accuracy Open-Source Biomolecular Structure Prediction. |
| [Tencent/phxqueue](https://github.com/Tencent/phxqueue) | ⭐1898 | C++ | A high-availability, high-throughput and highly reliable distributed q |
| [alibaba/xquic](https://github.com/alibaba/xquic) | ⭐1891 | C | XQUIC Library released by Alibaba is a cross-platform implementation o |
| [bytedance/GiantMIDI-Piano](https://github.com/bytedance/GiantMIDI-Piano) | ⭐1883 | Python |  |
| [alibaba/lowcode-demo](https://github.com/alibaba/lowcode-demo) | ⭐1866 | TypeScript | An enterprise-class low-code technology stack with scale-out design /  |
| [alibaba/Tangram-iOS](https://github.com/alibaba/Tangram-iOS) | ⭐1858 | Objective-C | Tangram is a modular UI solution for building native page dynamically, |
| [alibaba/testable-mock](https://github.com/alibaba/testable-mock) | ⭐1842 | Java | 换种思路写Mock，让单元测试更简单 |
| [alibaba/havenask](https://github.com/alibaba/havenask) | ⭐1829 | C++ | Havenask is a large-scale distributed information search system widely |
| [Tencent/CodeAnalysis](https://github.com/Tencent/CodeAnalysis) | ⭐1828 | Python | Static Code Analysis - 静态代码分析 |
| [alibaba/wax](https://github.com/alibaba/wax) | ⭐1825 | Objective-C | Wax is a framework that lets you write native iPhone apps in Lua. |
| [alibaba/MongoShake](https://github.com/alibaba/MongoShake) | ⭐1812 | Go | MongoShake is a universal data replication platform based on MongoDB's |
| [Tencent/TSW](https://github.com/Tencent/TSW) | ⭐1803 | TypeScript | Tencent Server Web |
| [Tencent/Metis](https://github.com/Tencent/Metis) | ⭐1759 | Python | Metis is a learnware platform in the field of AIOps.  |
| [bytedance/appshark](https://github.com/bytedance/appshark) | ⭐1736 | Kotlin | Appshark is a static taint analysis platform to scan vulnerabilities i |
| [bytedance/go-tagexpr](https://github.com/bytedance/go-tagexpr) | ⭐1732 | Go | An interesting go struct tag expression syntax for field validation, e |
| [Tencent/QMUI_Web](https://github.com/Tencent/QMUI_Web) | ⭐1713 | JavaScript | An efficient front-end framework for developers building UI on the web |
| [Tencent/Biny](https://github.com/Tencent/Biny) | ⭐1682 | PHP | Biny is a tiny, high-performance PHP framework for web applications |
| [bytedance/bitsail](https://github.com/bytedance/bitsail) | ⭐1680 | Java | BitSail is a distributed high-performance data integration engine whic |
| [alibaba/kt-connect](https://github.com/alibaba/kt-connect) | ⭐1662 | Go | A toolkit for Integrating with your kubernetes dev environment more ef |
| [Tencent/tdesign-miniprogram](https://github.com/Tencent/tdesign-miniprogram) | ⭐1659 | Vue | Wechat MiniProgram and Uniapp UI components lib for TDesign |
| [alibaba/mdrill](https://github.com/alibaba/mdrill) | ⭐1548 | Java | for千亿数据即席分析 |
| [alibaba/FederatedScope](https://github.com/alibaba/FederatedScope) | ⭐1530 | Python | An easy-to-use federated learning platform |
| [Tencent/TFace](https://github.com/Tencent/TFace) | ⭐1509 | Python | A trusty face analysis research platform developed by Tencent Youtu La |
| [Tencent/nohost](https://github.com/Tencent/nohost) | ⭐1478 | JavaScript | 基于 Whistle 实现的多账号多环境远程配置及抓包调试平台 |
| [alibaba/Virtualview-Android](https://github.com/alibaba/Virtualview-Android) | ⭐1454 | Java | A light way to build UI in custom XML. |
| [Tencent/TBase](https://github.com/Tencent/TBase) | ⭐1437 | C | TBase is an enterprise-level distributed HTAP database. Through a sing |
| [alibaba/tb_tddl](https://github.com/alibaba/tb_tddl) | ⭐1430 | None |  |
| [Tencent/TencentOS-kernel](https://github.com/Tencent/TencentOS-kernel) | ⭐1417 | None | 腾讯针对云的场景研发的服务器操作系统 |
| [Tencent/tquic](https://github.com/Tencent/tquic) | ⭐1414 | Rust | A high-performance, lightweight, and cross-platform QUIC library |
| [bytedance/AabResGuard](https://github.com/bytedance/AabResGuard) | ⭐1395 | Java | The tool of obfuscated aab resources.(Android app bundle资源混淆工具) |
| [Tencent/flare](https://github.com/Tencent/flare) | ⭐1393 | C++ |  Flare是广泛投产于腾讯广告后台的现代化C++开发框架，包含了基础库、RPC、各种客户端等。主要特点为易用性强、长尾延迟低。  |
| [Tencent/WeDemo](https://github.com/Tencent/WeDemo) | ⭐1387 | Objective-C | WeDemo为微信团队开源项目，用于帮助微信开发者完成微信登录、微信分享等功能的接入和开发。开发者可参考源代码完成开发，也可以直接将代码应用 |
| [Tencent/feflow](https://github.com/Tencent/feflow) | ⭐1380 | TypeScript | 🚀 A command line tool aims to improve front-end engineer workflow and  |
| [Tencent/GAutomator](https://github.com/Tencent/GAutomator) | ⭐1373 | Objective-C |  Automation for mobile games |
| [alibaba/Logics-Parsing](https://github.com/alibaba/Logics-Parsing) | ⭐1372 | Python |  |
| [Tencent/LuaPanda](https://github.com/Tencent/LuaPanda) | ⭐1370 | Lua | lua debug and code tools for VS Code |
| [alibaba/react-intl-universal](https://github.com/alibaba/react-intl-universal) | ⭐1354 | JavaScript | Internationalize React apps. Not only for Component but also for Vanil |
| [alibaba/graph-learn](https://github.com/alibaba/graph-learn) | ⭐1341 | C++ | An Industrial Graph Neural Network Framework |
| [alibaba/web-editor](https://github.com/alibaba/web-editor) | ⭐1327 | JavaScript | please use https://uiauto.dev instead |
| [baidu/bfe-book](https://github.com/baidu/bfe-book) | ⭐1296 | None | In-depth Understanding of BFE《深入理解BFE》（Book for BFE, a CNCF open sourc |
| [alibaba/GaiaX](https://github.com/alibaba/GaiaX) | ⭐1287 | C | 动态模板引擎是一套轻量化、跨平台、高性能的纯原生移动端卡片渲染动态化解决方案 |


## 🆕 Auto-discovered nexus (2026-05-26 02:09 UTC)

| Repo | Stars | Lang | Description |
|------|-------|------|-------------|
| [alibaba/bindingx](https://github.com/alibaba/bindingx) | ⭐1270 | JavaScript | :rocket: Bind actions to effects. |
| [alibaba/tfs](https://github.com/alibaba/tfs) | ⭐1245 | C++ | TFS (Taobao File System) is a distributed file system similar to GFS. |
| [alibaba/IOC-golang](https://github.com/alibaba/IOC-golang) | ⭐1233 | Go | 一款服务于 Go 开发者的依赖注入框架，方便搭建任何 Go 应用。 A Golang depenedency injection frame |
| [baidu/BaikalDB](https://github.com/baidu/BaikalDB) | ⭐1233 | C++ | BaikalDB, A Distributed HTAP Database. |
| [Tencent/FeatherCNN](https://github.com/Tencent/FeatherCNN) | ⭐1228 | C++ | FeatherCNN is a high performance inference engine for convolutional ne |
| [bytedance/USO](https://github.com/bytedance/USO) | ⭐1222 | Python | [CVPR 2026] 🔥🔥 Official Repo of USO: Unified Style and Subject-Driven  |
| [bytedance/BoostMultiDex](https://github.com/bytedance/BoostMultiDex) | ⭐1201 | Java | BoostMultiDex is a solution for quickly loading multiple dex files on  |
| [alibaba/PhotonLibOS](https://github.com/alibaba/PhotonLibOS) | ⭐1197 | C++ | Probably the fastest coroutine lib in the world! |
| [bytedance/Fastbot_Android](https://github.com/bytedance/Fastbot_Android) | ⭐1186 | C++ | Fastbot(2.0) is a model-based testing tool for modeling GUI transition |
| [bytedance/memory-leak-detector](https://github.com/bytedance/memory-leak-detector) | ⭐1184 | C |  |
| [baidu/DuReader](https://github.com/baidu/DuReader) | ⭐1177 | Python | Baseline Systems of DuReader Dataset |
| [bytedance/1d-tokenizer](https://github.com/bytedance/1d-tokenizer) | ⭐1153 | Jupyter Notebook | This repo contains the code for 1D tokenizer and generator |
| [Tencent/tdesign-flutter](https://github.com/Tencent/tdesign-flutter) | ⭐1141 | Dart | A Flutter UI components lib for TDesign. |
| [baidu/bigflow](https://github.com/baidu/bigflow) | ⭐1133 | C++ | Baidu Bigflow is an interface that allows for writing distributed comp |
| [alibaba/dawn](https://github.com/alibaba/dawn) | ⭐1132 | JavaScript | :sunrise: Dawn is a lightweight task management and build tool for fro |
| [Tencent/hel](https://github.com/Tencent/hel) | ⭐1114 | JavaScript | A module federation SDK for browser and node, it is unrelated to tool  |
| [PaddlePaddle/Paddle.js](https://github.com/PaddlePaddle/Paddle.js) | ⭐1094 | JavaScript | Paddle.js is a web project for Baidu PaddlePaddle, which is an open so |
| [alibaba/G3D](https://github.com/alibaba/G3D) | ⭐1077 | TypeScript | A pure 3D render engine compatible with webgl, running both in browser |
| [alibaba/taokeeper](https://github.com/alibaba/taokeeper) | ⭐1043 | Java | ZooKeeper-Monitor, a monitor for zookeeper in java. Download https://g |
| [bytedance/godlp](https://github.com/bytedance/godlp) | ⭐1037 | Go | sensitive information protection toolkit |
| [Tencent/tdesign-vue](https://github.com/Tencent/tdesign-vue) | ⭐1015 | TypeScript | A Vue.js UI components lib for TDesign. |
| [TencentARC/SEED-Voken](https://github.com/TencentARC/SEED-Voken) | ⭐1009 | Python | SEED-Voken: A Series of Powerful Visual Tokenizers |
| [bytedance/SandboxFusion](https://github.com/bytedance/SandboxFusion) | ⭐1009 | Python |  |
| [baidu/DDParser](https://github.com/baidu/DDParser) | ⭐1000 | Python | 百度开源的依存句法分析系统 |
| [Tencent/TencentKona-8](https://github.com/Tencent/TencentKona-8) | ⭐998 | Java | Tencent Kona is a no-cost, production-ready distribution of the Open J |
| [alibaba/ali-react-table](https://github.com/alibaba/ali-react-table) | ⭐979 | TypeScript | Performent, flexible and modern React table component. |
| [baidu/starlight](https://github.com/baidu/starlight) | ⭐979 | Java | Java implementation for Baidu RPC, multi-protocol & high performance R |
| [alibaba/alist](https://github.com/alibaba/alist) | ⭐975 | TypeScript | Alibaba Group Unified List Solution. |
| [Tencent/RapidView](https://github.com/Tencent/RapidView) | ⭐972 | Java | RapidView is an android ui and lightapp development framework |
| [bytedance/sonic-cpp](https://github.com/bytedance/sonic-cpp) | ⭐972 | C++ | A fast JSON serializing & deserializing library, accelerated by SIMD. |
| [Tencent/tdesign-vue-next-starter](https://github.com/Tencent/tdesign-vue-next-starter) | ⭐970 | Vue | A starter-kit for TDesign Vue Next UI components |
| [alibaba/java-dns-cache-manipulator](https://github.com/alibaba/java-dns-cache-manipulator) | ⭐967 | Java | 🌏 A tiny 0-dependency thread-safe Java™ lib for setting/viewing dns pr |
| [baidu/CUP](https://github.com/baidu/CUP) | ⭐949 | Python | CUP, common useful python-lib.  (Currently, Most popular python lib in |
| [Tencent/tdesign-react](https://github.com/Tencent/tdesign-react) | ⭐945 | TypeScript | A React UI components lib for TDesign. |
| [Tencent/FAutoTest](https://github.com/Tencent/FAutoTest) | ⭐939 | Python | A UI automated testing framework for H5 and applets |
| [alibaba/funcraft](https://github.com/alibaba/funcraft) | ⭐935 | JavaScript | (have) Fun with Serverless(API Gateway & Function Compute) |
| [alibaba/ApsaraCache](https://github.com/alibaba/ApsaraCache) | ⭐930 | C | archived | ApsaraCache is a Redis branch originated from Alibaba Group |
| [alibaba/BladeDISC](https://github.com/alibaba/BladeDISC) | ⭐926 | C++ | BladeDISC is an end-to-end DynamIc Shape Compiler project for machine  |
| [Tencent/mxflutter](https://github.com/Tencent/mxflutter) | ⭐911 | Dart | 使用 TypeScript/JavaScript 来开发 Flutter 应用的框架。 |
| [bytedance/fedlearner](https://github.com/bytedance/fedlearner) | ⭐903 | Python | A multi-party collaborative machine learning framework |
| [bytedance/mockey](https://github.com/bytedance/mockey) | ⭐900 | Go | A simple and easy-to-use Go mocking library derived from ByteDance's i |
| [alibaba/SmartEngine](https://github.com/alibaba/SmartEngine) | ⭐897 | Java | SmartEngine is a lightweight business orchestration engine. |
| [Tencent/Face2FaceTranslator](https://github.com/Tencent/Face2FaceTranslator) | ⭐896 | JavaScript | 面对面翻译小程序是微信团队针对面对面沟通的场景开发的流式语音翻译小程序，通过微信同声传译插件提供了语音识别，文本翻译等功能。 |
| [alibaba/TinyNeuralNetwork](https://github.com/alibaba/TinyNeuralNetwork) | ⭐878 | Python | TinyNeuralNetwork is an efficient and easy-to-use deep learning model  |
| [Tencent/Pebble](https://github.com/Tencent/Pebble) | ⭐874 | C++ | Pebble分布式开发框架 |
| [bytedance/g3](https://github.com/bytedance/g3) | ⭐873 | Rust | Enterprise-oriented Generic Proxy Solutions |
| [alibaba/nginx-http-concat](https://github.com/alibaba/nginx-http-concat) | ⭐866 | C | A Nginx module for concatenating files in a given context: CSS and JS  |
| [Tencent/Real-SR](https://github.com/Tencent/Real-SR) | ⭐824 | Python | Real-World Super-Resolution via Kernel Estimation and Noise Injection |
| [alibaba/youku-sdk-tool-woodpecker](https://github.com/alibaba/youku-sdk-tool-woodpecker) | ⭐822 | Objective-C | In-app-debug tool for iOS |
| [Tencent/tdesign-miniprogram-starter-retail](https://github.com/Tencent/tdesign-miniprogram-starter-retail) | ⭐818 | JavaScript | TDesign - 微信小程序 - 零售行业模板 |
