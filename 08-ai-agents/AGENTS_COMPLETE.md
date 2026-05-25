# 🤖 AI Agents — Complete Catalog

> Every agent framework, platform, and tool.reverse-engineered and documented.

---

## 🏆 The Agent Landscape (2026)

```
Agent Frameworks:
├── Single Agent
│   ├── OpenAI Agents SDK (minimal, handoffs)
│   ├── Google ADK (tool-centric, MCP)
│   ├── Agno (model-agnostic, fast)
│   └── DSPy (prompt optimization)
├── Multi-Agent
│   ├── CrewAI (role-based)
│   ├── AutoGen (conversational)
│   ├── LangGraph (graph-based)
│   ├── Mason (workflow)
│   └── msitarzewski/agency-agents (70+ personas)
├── Research Agents
│   ├── DeerFlow (ByteDance, deep research)
│   ├── OpenHands (full-stack coding)
│   ├── SWE-agent (bug fixing)
│   └── karpathy/autoresearch (ML research)
└── Memory-Enabled
    ├── Letta/MemGPT (persistent memory)
    ├── mem0ai/mem0 (universal memory)
    ├── claude-mem (session memory)
    └── MemPalace (local memory palace)
```

---

## 🥇 Top 50 AI Agent Projects (by GitHub Stars)

| Rank | Project | Stars | Description | Language |
|------|---------|-------|-------------|----------|
| 1 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 111K | 100+ AI Agent & RAG apps | Python |
| 2 | [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | 104K | Gemini CLI agent | TypeScript |
| 3 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | 95K | Browser automation for agents | Python |
| 4 | [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | 83K | Autonomous ML research agent | Python |
| 5 | [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | 81K | RAG engine | Python |
| 6 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 78K | Persistent context for agents | TypeScript |
| 7 | [lobehub/lobehub](https://github.com/lobehub/lobehub) | 77K | Agent orchestration platform | TypeScript |
| 8 | [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | 75K | AI-driven development | Python |
| 9 | [hiyouga/LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) | 72K | Fine-tuning 600+ LLMs | Python |
| 10 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | 69K | Long-horizon SuperAgent | Python |
| 11 | [FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 68K | Multi-agent software company | Python |
| 12 | [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | 65K | 12 lessons on agents | Jupyter |
| 13 | [mem0ai/mem0](https://github.com/mem0ai/mem0) | 57K | Universal memory layer | Python |
| 14 | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | 54K | Agent orchestration for Claude | TypeScript |
| 15 | [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise) | 53K | Visual AI agent builder | TypeScript |
| 16 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | 52K | Role-based multi-agent | Python |
| 17 | [run-llama/llama_index](https://github.com/run-llama/llama_index) | 50K | Document agent + OCR | Python |
| 18 | [microsoft/autogen](https://github.com/microsoft/autogen) | 58K | Agentic AI framework | Python |
| 19 | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | 137K | Agent engineering platform | Python |
| 20 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 124K | Web scraping for AI agents | TypeScript |
| 21 | [langflow-ai/langflow](https://github.com/langflow-ai/langflow) | 149K | Visual AI builder | Python |
| 22 | [langgenius/dify](https://github.com/langgenius/dify) | 142K | Agentic workflow platform | TypeScript |
| 23 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 166K | Nous Research agent | Python |
| 24 | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | 105K | 70+ agent personas | Shell |
| 25 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | 138K | System prompts collection | - |
| 26 | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | 59K | Best agent harness | TypeScript |
| 27 | [earendil-works/pi](https://github.com/earendil-works/pi) | 54K | AI agent toolkit | TypeScript |
| 28 | [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | 74K | Prompt engineering guide | MDX |
| 29 | [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | 68K | Financial data + AI agents | Python |
| 30 | [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | 55K | Claude Code best practices | HTML |

---

## 🏗️ Agent Framework Deep Dives

### 1. LangChain (137K ⭐)
**Pattern:** Chain of Responsibility + Builder
**Architecture:** Prompt → LLM → Parser → Chain → Agent → Tools → Output
**Key abstractions:** Chain, Agent, Tool, Memory, Retriever
**Strengths:** Massive ecosystem, 1000+ integrations
**Weaknesses:** Overly complex, heavy deps, breaking changes
**Verdict:** 🟡 Use for prototyping, not production

### 2. LlamaIndex (50K ⭐)
**Pattern:** Document-centric RAG
**Architecture:** Documents → Index → Query Engine → Response
**Key abstractions:** Index, Query Engine, Agent, Tool
**Strengths:** Best RAG framework, great document processing
**Weaknesses:** Can be slow, complex configuration
**Verdict:** 🟢 Best for RAG-heavy applications

### 3. CrewAI (52K ⭐)
**Pattern:** Role-Based Multi-Agent
**Architecture:** Crew → [Agent(role, goal) → Task] → Output
**Key abstractions:** Agent, Task, Crew, Process
**Strengths:** Intuitive role design, good for complex workflows
**Weaknesses:** Rigid structure, limited tool ecosystem
**Verdict:** 🟢 Good for structured multi-agent workflows

### 4. AutoGen (58K ⭐)
**Pattern:** Conversational Multi-Agent
**Architecture:** UserProxy ↔ Assistant ↔ [Experts] → Output
**Key abstractions:** ConversableAgent, GroupChat, AssistantAgent
**Strengths:** Flexible conversations, strong academic foundation
**Weaknesses:** Complex config, steep learning curve
**Verdict:** 🟡 Good for research, complex for production

### 5. Google ADK
**Pattern:** Tool-Centric Agent
**Architecture:** Agent(LLM, Tools, Instructions) → [Tool Call → Result] → Output
**Key abstractions:** Agent, Tool, Session, Runner
**Strengths:** Clean design, strong MCP support, production-ready
**Weaknesses:** Google-centric, smaller community
**Verdict:** 🟢 Best for Google ecosystem integration

### 6. DeerFlow (69K ⭐) — ByteDance
**Pattern:** Sandbox + Sub-Agent Orchestration
**Architecture:** Planner → [Sub-Agent in Sandbox] → Coordinator → Output
**Key abstractions:** Planner, Coordinator, Sub-Agent, Sandbox
**Strengths:** Sandbox isolation, sub-agent specialization
**Weaknesses:** Complex setup, ByteDance-centric
**Verdict:** 🟢 Best for deep research tasks

### 7. LangFlow (149K ⭐)
**Pattern:** Visual Flow Builder
**Architecture:** Visual graph → Python code → Agent execution
**Key abstractions:** Flow, Component, Edge
**Strengths:** Visual builder, huge component library
**Weaknesses:** Can generate messy code, vendor lock-in
**Verdict:** 🟢 Best for rapid prototyping

### 8. Dify (142K ⭐)
**Pattern:** Production Agent Platform
**Architecture:** Workflow → Agents → Tools → APIs
**Key abstractions:** App, Workflow, Agent, Dataset
**Strengths:** Production-ready, great UI, RAG built-in
**Weaknesses:** Can be expensive at scale
**Verdict:** 🟢 Best for production agent apps

### 9. Flowise (53K ⭐)
**Pattern:** Open-source LangFlow alternative
**Architecture:** Visual flow → LangChain code → Execution
**Key abstractions:** Flow, Node, Connection
**Strengths:** Open source, self-hostable
**Weaknesses:** Smaller ecosystem than LangFlow
**Verdict:** 🟢 Best open-source visual agent builder

### 10. MetaGPT (68K ⭐)
**Pattern:** AI Software Company
**Architecture:** Product Manager → Architect → Engineer → Tester → Output
**Key abstractions:** Role, Action, Message, Environment
**Strengths:** Full software development lifecycle
**Weaknesses:** Can be slow, expensive token usage
**Verdict:** 🟡 Interesting for automated development

---

## 🧠 Memory Systems

| Project | Stars | Type | Description |
|---------|-------|------|-------------|
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | 57K | Universal memory | Memory layer for any agent |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 78K | Session memory | Persistent context across sessions |
| [letta-ai/letta](https://github.com/letta-ai/letta) | - | Persistent agent | Agents with long-term memory |
| [MemPalace](https://github.com/MemPalace/MemPalace) | - | Local memory | Hierarchical memory palace |
| [OpenBMB/ClawXMemory](https://github.com/OpenBMB/ClawXMemory) | 33 | Plugin | Multi-level memory for OpenClaw |

---

## 🌐 Browser & Web Agents

| Project | Stars | Description |
|---------|-------|-------------|
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | 95K | Browser automation for AI agents |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 124K | Web scraping for AI agents |
| [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | 75K | Full-stack coding agent |
| [ScaleCUA](https://github.com/OpenGVLab/ScaleCUA) | 1.1K | Computer use agent |

---

## 🔧 MCP (Model Context Protocol) Servers

| Server | Description | Stars |
|--------|-------------|-------|
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Official MCP servers | - |
| [OpenBMB/MiniMax-Coding-Plan-MCP](https://github.com/MiniMax-AI/MiniMax-Coding-Plan-MCP) | Coding plan MCP | 83 |
| [baichuan-inc/baichuan-mcp-servers](https://github.com/baichuan-inc/baichuan-mcp-servers) | Baichuan MCP servers | 9 |

---

## 📊 Agent Benchmarks

| Benchmark | What It Tests | Top Model |
|-----------|--------------|-----------|
| SWE-bench Verified | Real GitHub issues | Claude Opus 4.5 (80.9%) |
| WebArena | Web navigation | - |
| OSWorld | OS manipulation | - |
| AgentBench | Agent capabilities | - |
| GAIA | General AI assistants | - |
| WildClawBench | Real-world agent tasks | - |

---

*Last updated: 2026-05-25*
