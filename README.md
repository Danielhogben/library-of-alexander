# 🏛️ The Library of Alexander

> *"The universe is transformation; our life is what our thoughts make it."* — Marcus Aurelius

**The single most comprehensive, densely-organized collection of AI/ML/coding knowledge on the internet.**

This is not a link dump. This is a **curated, annotated, cross-referenced knowledge base** — every tool, model, API, framework, learning resource, hardware spec, agent, and reverse-engineered codebase, organized for maximum information density.

---

## 📊 What's Inside

| # | Directory | Contents | Entries |
|---|-----------|----------|---------|
| 01 | [`01-ai-models/`](01-ai-models/) | Every notable LLM, image, video, audio model | 500+ |
| 02 | [`02-free-apis/`](02-free-apis/) | Every free AI API, free tier, no-cost service | 100+ |
| 03 | [`03-coding-tools/`](03-coding-tools/) | AI coding assistants, agents, IDEs | 150+ |
| 04 | [`04-image-generation/`](04-image-generation/) | Image models, UIs, upscalers, editors | 200+ |
| 05 | [`05-video-generation/`](05-video-generation/) | Video models, lip sync, editing | 100+ |
| 06 | [`06-audio-music/`](06-audio-music/) | TTS, voice cloning, music generation | 150+ |
| 07 | [`07-voice-tts/`](07-voice-tts/) | Voice assistants, real-time voice, STT | 80+ |
| 08 | [`08-ai-agents/`](08-ai-agents/) | Agent frameworks, multi-agent, MCP | 100+ |
| 09 | [`09-rag-knowledge/`](09-rag-knowledge/) | RAG systems, vector DBs, knowledge bases | 80+ |
| 10 | [`10-local-llms/`](10-local-llms/) | Local inference, runners, quantization | 100+ |
| 11 | [`11-hardware/`](11-hardware/) | GPUs, NPUs, edge devices, ESP32+AI | 100+ |
| 12 | [`12-learning/`](12-learning/) | Courses, tutorials, papers, paths | 200+ |
| 13 | [`13-frameworks/`](13-frameworks/) | ML/DL frameworks, agent frameworks | 80+ |
| 14 | [`14-devops-mlops/`](14-devops-mlops/) | Deployment, serving, monitoring | 80+ |
| 15 | [`15-robotics-edge/`](15-robotics-edge/) | Robotics, embedded AI, TinyML | 60+ |
| 16 | [`16-research-papers/`](16-research-papers/) | Seminal papers, reading lists | 100+ |
| 17 | [`17-datasets/`](17-datasets/) | Training datasets, benchmarks | 80+ |
| 18 | [`18-benchmarks/`](18-benchmarks/) | Leaderboards, evaluation suites | 50+ |
| 19 | [`19-communities/`](19-communities/) | Forums, Discords, newsletters | 50+ |
| 20 | [`20-mega-projects/`](20-mega-projects/) | Large-scale open source AI projects | 50+ |
| 21 | [`21-chinese-ai-ecosystem/`](21-chinese-ai-ecosystem/) | Complete Chinese AI landscape | 300+ |
| 22 | [`22-vibe-code-audit/`](22-vibe-code-audit/) | Popular but broken projects + fixes | 100+ |
| 23 | [`23-reverse-engineering/`](23-reverse-engineering/) | Architecture deep-dives, code audits | 50+ |
| 24 | [`24-esp-embedded-ai/`](24-esp-embedded-ai/) | ESP32, microcontrollers + AI | 50+ |
| 25 | [`25-swarm-infrastructure/`](25-swarm-infrastructure/) | Multi-node AI, distributed inference | 30+ |

**Total: 2,800+ entries across 25 categories + global discovery**

---

## 🎯 How to Use This Library

### For Beginners
Start with [`12-learning/LEARNING_PATH.md`](12-learning/LEARNING_PATH.md) — a structured path from zero to building AI systems.

### For Developers
- Need a free API? → [`02-free-apis/`](02-free-apis/)
- Building an agent? → [`08-ai-agents/`](08-ai-agents/)
- Need a local model? → [`10-local-llms/`](10-local-llms/)
- Coding with AI? → [`03-coding-tools/`](03-coding-tools/)

### For Researchers
- Latest models? → [`01-ai-models/`](01-ai-models/)
- Benchmarks? → [`18-benchmarks/`](18-benchmarks/)
- Papers? → [`16-research-papers/`](16-research-papers/)
- Chinese research? → [`21-chinese-ai-ecosystem/`](21-chinese-ai-ecosystem/)

### For the Swarm
- ESP32 + AI projects? → [`24-esp-embedded-ai/`](24-esp-embedded-ai/)
- Multi-node setup? → [`25-swarm-infrastructure/`](25-swarm-infrastructure/)
- Hardware guide? → [`11-hardware/`](11-hardware/)

---

## 🔍 Key Sections

### 🇨🇳 Chinese AI Ecosystem (Section 21)
The most comprehensive English-language catalog of Chinese AI projects: DeepSeek, Qwen, GLM, Baichuan, Yi, InternLM, MiniCPM, Wan, CogVideoX, CosyVoice, F5-TTS, ChatTTS, Kolors, HunyuanVideo, and 300+ more.

### 🔬 Reverse Engineering (Section 23)
Architecture deep-dives into popular AI agent frameworks — how they actually work, their design patterns, and what we can learn from them.

### 🔧 Vibe Code Audit (Section 22)
Popular GitHub projects with many stars but poor code quality. We identify the issues and propose fixes. Learn from others' mistakes.

### 📡 ESP32 + Embedded AI (Section 24)
Everything about running AI on microcontrollers: ESP32, Sipeed, TinyML, ESP-DL, and more.

---

## 🤝 Contributing

This is a living document. PRs welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## 📜 License

MIT — use this knowledge freely.

---

*Built by the NexusAI Swarm. Updated continuously.*

## 🔍 Automated Discovery

This library is continuously updated by an automated discovery pipeline:

1. **GitHub Search** — 30+ search queries run every 4 hours
2. **Star Threshold** — Only tools with 50+ stars are added
3. **Deduplication** — Existing tools are skipped automatically
4. **Categorization** — Tools mapped to the correct category
5. **Reverse Engineering** — Complex tools get architecture deep-dives

The discovery pipeline runs via `scripts/discover_tools.sh` and is configured as a cron job.

### Adding Tools Manually

```bash
# Run discovery pipeline
./scripts/discover_tools.sh

# Check what was found
cat data/latest_discovery.json
```

### Contributing

1. Fork this repo
2. Add tools to the appropriate category README
3. Create reverse engineering files in `23-reverse-engineering/`
4. Submit a PR

**Format**: `| [name](url) | description | ⭐stars | language | updated |`

## 🌍 Global Discovery

This library catalogs AI tools from **every country on Earth** — translated to English.

- **11+ languages** searched: Chinese, Turkish, Spanish, Portuguese, Arabic, Japanese, French, Russian, Hindi, Vietnamese, Korean
- **10+ awesome lists** scraped: 7,766+ tools cataloged
- **285 GitHub repos** analyzed: 6.2M+ total stars
- **215 new tools** added from global discovery

The automated pipeline runs every 4 hours, searching GitHub in all languages and scraping all known awesome lists.

See [GLOBAL_DISCOVERY.md](GLOBAL_DISCOVERY.md) for full details.
