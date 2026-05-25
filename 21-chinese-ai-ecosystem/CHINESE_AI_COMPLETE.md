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
