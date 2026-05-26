# Claude Instructions — Library of Alexander

## What This Is

The Library of Alexander is the most comprehensive open-source AI/ML/coding knowledge base on the internet. It contains 2,800+ entries across 25 categories — every tool, model, API, framework, Chinese AI project, reverse-engineered architecture, and vibe-code audit from every country on Earth.

## How Every Agent Should Use This Library

### Before Starting Any Task

1. **Search the library first** — Check if tools/models/frameworks already exist in the relevant category
2. **Read reverse engineering files** — Check `23-reverse-engineering/` for architecture analysis of relevant tools
3. **Use the categorized structure** — Navigate to the numbered directory for the relevant category

### Category Guide

| Category | Directory | Use When |
|----------|-----------|----------|
| AI Models | `01-ai-models/` | Need to know which LLM/image/video model to use |
| Free APIs | `02-free-apis/` | Need free API access to AI services |
| Coding Tools | `03-coding-tools/` | Looking for AI coding assistants or IDEs |
| Image Generation | `04-image-generation/` | Need image generation models or tools |
| Video Generation | `05-video-generation/` | Need video generation or editing tools |
| Audio/Music | `06-audio-music/` | Need music generation or audio processing |
| Voice/TTS | `07-voice-tts/` | Need text-to-speech or voice cloning |
| AI Agents | `08-ai-agents/` | Building agents or multi-agent systems |
| RAG/Knowledge | `09-rag-knowledge/` | Need RAG systems or vector databases |
| Local LLMs | `10-local-llms/` | Running models locally on your hardware |
| Hardware | `11-hardware/` | Need GPU/NPU/edge device specs |
| Learning | `12-learning/` | Want to learn AI/ML concepts |
| Frameworks | `13-frameworks/` | Need ML/DL frameworks |
| DevOps/MLOps | `14-devops-mlops/` | Need deployment or serving tools |
| Robotics/Edge | `15-robotics-edge/` | Building robots or embedded AI |
| Research Papers | `16-research-papers/` | Need seminal AI papers |
| Datasets | `17-datasets/` | Need training data |
| Benchmarks | `18-benchmarks/` | Need model evaluation metrics |
| Communities | `19-communities/` | Looking for AI forums or groups |
| Mega Projects | `20-mega-projects/` | Large-scale open source AI projects |
| Chinese AI | `21-chinese-ai-ecosystem/` | Chinese AI tools and models |
| Vibe Code Audit | `22-vibe-code-audit/` | Projects that look good but are broken |
| Reverse Engineering | `23-reverse-engineering/` | Deep architecture analysis (167+ files) |
| ESP/Embedded | `24-esp-embedded-ai/` | AI on microcontrollers |
| Swarm Infrastructure | `25-swarm-infrastructure/` | Multi-node AI systems |

### When You Need to Add New Tools

1. Check if the tool already exists in the relevant category
2. If not, add it to the appropriate `README.md` in the numbered directory
3. Format: `| [owner/repo](URL) | Description | ⭐Stars | Language | Updated |`
4. If the tool is complex enough, create a reverse-engineering file in `23-reverse-engineering/`
5. Commit with message: `add: tool-name to category-XX`

### When You Need to Reverse Engineer a Tool

1. Clone the tool's repository
2. Analyze the architecture, data flow, and key design patterns
3. Create a file in `23-reverse-engineering/RE_owner_repo.md`
4. Include: architecture diagram, key components, data flow, lessons learned, and what we can reuse
5. Commit with message: `reverse-engineer: owner/repo architecture analysis`

### Key Principles

- **Dense, not verbose** — Pack maximum information into minimum space
- **Cross-reference** — Link related tools across categories
- **Verify** — Don't add tools you haven't checked exist and work
- **Update** — Tools change, stars change, update regularly
- **No fluff** — Every line must convey useful information

## This Library Is Open Source

Anyone can contribute. Fork, add tools, submit a PR. The goal is to make this the single source of truth for AI tools and knowledge.

## Maintained By

The House of Donn — a swarm of AI agents (Hermes, Jupiter, Nexus, Luna) working across a fleet of machines to discover, analyze, and catalog every AI tool on the internet.

## Content Policy

**STRICTLY NO PORN, NSFW, OR SEXUAL CONTENT.**

- This library is for professional AI/ML/coding tools only
- No adult content, pornographic tools, or sexually explicit descriptions
- No links to adult websites or services
- All tool descriptions must be appropriate for all audiences
- Violations will be removed immediately
- This rule is non-negotiable — keep it clean and professional

## Agent-Specific Instructions

Detailed instructions for 30+ AI agents are in `docs/agent-instructions/`:
- Claude, ChatGPT, Gemini, DeepSeek, Qwen, Copilot, Cursor, Codex
- OpenHands, AutoGPT, MetaGPT, CrewAI, LangChain, Ollama
- Dify, RAGFlow, FastGPT, Coze, Continue, Aider, Roo Code, Windsurf
- Perplexity, Grok, Mistral, Llama, Agent Zero, OpenClaw, Hermes

Each agent has specific guidance for how to use this library effectively.
