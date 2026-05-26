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


## 🆕 Auto-discovered nexus (2026-05-25 10:10 UTC)

| Repo | Stars | Lang | Description |
|------|-------|------|-------------|
| [openai/codex](https://github.com/openai/codex) | ⭐85456 | Rust | Lightweight coding agent that runs in your terminal |
| [alibaba/arthas](https://github.com/alibaba/arthas) | ⭐37328 | Java | Alibaba Java Diagnostic Tool Arthas/Alibaba Java诊断利器Arthas |
| [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | ⭐35189 | TypeScript | The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI  |
| [alibaba/nacos](https://github.com/alibaba/nacos) | ⭐32964 | Java | an easy-to-use dynamic service discovery, configuration and service ma |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) | ⭐27500 | Python | 🤗 smolagents: a barebones library for agents that think in code. |
| [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) | ⭐23292 | Python | The batteries-included agent harness. |
| [openai/swarm](https://github.com/openai/swarm) | ⭐21526 | Python | Educational framework exploring ergonomic, lightweight multi-agent orc |
| [alibaba/page-agent](https://github.com/alibaba/page-agent) | ⭐18076 | TypeScript | JavaScript in-page GUI agent. Control web interfaces with natural lang |
| [langchain-ai/langchainjs](https://github.com/langchain-ai/langchainjs) | ⭐17719 | TypeScript | The agent engineering platform |
| [alibaba/OpenSandbox](https://github.com/alibaba/OpenSandbox) | ⭐10805 | Python | Secure, Fast, and Extensible Sandbox runtime for AI agents. |
| [bytedance/UI-TARS](https://github.com/bytedance/UI-TARS) | ⭐10730 | Python | Pioneering Automated GUI Interaction with Native Agents |
| [huggingface/skills](https://github.com/huggingface/skills) | ⭐10570 | Python | Give your agents the power of the Hugging Face ecosystem |
| [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) | ⭐9728 | Java | Agentic AI Framework for Java Developers |
| [google-deepmind/lab](https://github.com/google-deepmind/lab) | ⭐7358 | C | A customisable 3D platform for agent-based AI research |
| [openai/openai-realtime-agents](https://github.com/openai/openai-realtime-agents) | ⭐6876 | TypeScript | This is a simple demonstration of more advanced, agentic patterns buil |
| [openai/openai-cs-agents-demo](https://github.com/openai/openai-cs-agents-demo) | ⭐6378 | Python | Demo of a customer service use case implemented with the OpenAI Agents |
| [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell) | ⭐6230 | Rust | OpenShell is the safe, private runtime for autonomous AI agents. |
| [crewAIInc/crewAI-examples](https://github.com/crewAIInc/crewAI-examples) | ⭐5976 | Jupyter Notebook | A collection of examples that show how to use CrewAI framework to auto |
| [google-deepmind/open_spiel](https://github.com/google-deepmind/open_spiel) | ⭐5237 | C++ | OpenSpiel is a collection of environments and algorithms for research  |
| [modelscope/ms-agent](https://github.com/modelscope/ms-agent) | ⭐4279 | Python | MS-Agent: a lightweight framework to empower agentic execution of comp |
| [google-deepmind/acme](https://github.com/google-deepmind/acme) | ⭐3986 | Python | A library of reinforcement learning components and agents |
| [openai/openai-agents-js](https://github.com/openai/openai-agents-js) | ⭐3114 | TypeScript | A lightweight, powerful framework for multi-agent workflows and voice  |
| [openai/multiagent-particle-envs](https://github.com/openai/multiagent-particle-envs) | ⭐2764 | Python | Code for a multi-agent particle environment used in the paper "Multi-A |
| [langchain-ai/social-media-agent](https://github.com/langchain-ai/social-media-agent) | ⭐2584 | TypeScript | 📲 An agent for sourcing, curating, and scheduling social media posts w |
| [NVIDIA/NeMo-Agent-Toolkit](https://github.com/NVIDIA/NeMo-Agent-Toolkit) | ⭐2325 | Python | The NVIDIA NeMo Agent toolkit is an open-source library for efficientl |
| [stepfun-ai/gelab-zero](https://github.com/stepfun-ai/gelab-zero) | ⭐2172 | Python | STEP-GUI: The top GUI agent solution in the galaxy.  Developed by the  |
| [stepfun-ai/Step-3.5-Flash](https://github.com/stepfun-ai/Step-3.5-Flash) | ⭐2046 | C++ | Fast, Sharp & Reliable Agentic Intelligence |
| [openai/maddpg](https://github.com/openai/maddpg) | ⭐1974 | Python | Code for the MADDPG algorithm from the paper "Multi-Agent Actor-Critic |
| [langchain-ai/open-agent-platform](https://github.com/langchain-ai/open-agent-platform) | ⭐1860 | TypeScript | An open-source, no-code agent building platform. |
| [openai/multi-agent-emergence-environments](https://github.com/openai/multi-agent-emergence-environments) | ⭐1800 | Python | Environment generation code for the paper "Emergent Tool Use From Mult |
| [langchain-ai/agents-from-scratch](https://github.com/langchain-ai/agents-from-scratch) | ⭐1780 | Jupyter Notebook | Build an email assistant with human-in-the-loop and memory |
| [openai/openai-cua-sample-app](https://github.com/openai/openai-cua-sample-app) | ⭐1725 | TypeScript | Learn how to use CUA (our Computer Using Agent) via the API on multipl |
| [openai/neural-mmo](https://github.com/openai/neural-mmo) | ⭐1651 | Python | Code for the paper "Neural MMO: A Massively Multiagent Game Environmen |
| [langchain-ai/streamlit-agent](https://github.com/langchain-ai/streamlit-agent) | ⭐1634 | Python | Reference implementations of several LangChain agents as Streamlit app |
| [langchain-ai/deep-agents-ui](https://github.com/langchain-ai/deep-agents-ui) | ⭐1620 | TypeScript | Custom UI for Deep Agents |
| [openai/mle-bench](https://github.com/openai/mle-bench) | ⭐1539 | Python | MLE-bench is a benchmark for measuring how well AI agents perform at m |
| [google-deepmind/concordia](https://github.com/google-deepmind/concordia) | ⭐1439 | Python | A library for generative social simulation |
| [crewAIInc/crewAI-tools](https://github.com/crewAIInc/crewAI-tools) | ⭐1430 | Python | Extend the capabilities of your CrewAI agents with Tools |
| [OpenBMB/AgentCPM-GUI](https://github.com/OpenBMB/AgentCPM-GUI) | ⭐1369 | Python | AgentCPM-GUI: An on-device GUI agent for operating Android apps, enhan |
| [langchain-ai/deepagentsjs](https://github.com/langchain-ai/deepagentsjs) | ⭐1256 | TypeScript | The batteries included agent harness. |
| [MiniMax-AI/OpenRoom](https://github.com/MiniMax-AI/OpenRoom) | ⭐1192 | TypeScript | A browser-based desktop where AI Agent operates every app through natu |
| [OpenGVLab/ScaleCUA](https://github.com/OpenGVLab/ScaleCUA) | ⭐1114 | Python | [ICLR 2026 Oral] ScaleCUA is the open-sourced computer use agents that |
| [openai/universe-starter-agent](https://github.com/openai/universe-starter-agent) | ⭐1102 | Python | A starter agent that can solve a number of universe environments. |
| [google-deepmind/scalable_agent](https://github.com/google-deepmind/scalable_agent) | ⭐1026 | Python | A TensorFlow implementation of Scalable Distributed Deep-RL with Impor |
| [langchain-ai/agent-inbox](https://github.com/langchain-ai/agent-inbox) | ⭐994 | TypeScript | 📥 An inbox UX for interacting with human-in-the-loop agents. |
| [huggingface/meshgen](https://github.com/huggingface/meshgen) | ⭐878 | Python | Use AI Agents directly in Blender. |
| [alibaba/loongsuite-go-agent](https://github.com/alibaba/loongsuite-go-agent) | ⭐857 | Go | OpenTelemetry Compile-Time Instrumentation for Golang |
| [openai/openai-chatkit-starter-app](https://github.com/openai/openai-chatkit-starter-app) | ⭐851 | Python | Starter app to build with OpenAI ChatKit + Agent Builder |
| [openai/multiagent-competition](https://github.com/openai/multiagent-competition) | ⭐836 | Python |  Code for the paper "Emergent Complexity via Multi-agent Competition" |
| [google-deepmind/meltingpot](https://github.com/google-deepmind/meltingpot) | ⭐836 | Python | A suite of test scenarios for multi-agent reinforcement learning. |


## 🆕 Auto-discovered nexus (2026-05-25 14:10 UTC)

| Repo | Stars | Lang | Description |
|------|-------|------|-------------|
| [openai/openai-testing-agent-demo](https://github.com/openai/openai-testing-agent-demo) | ⭐764 | TypeScript | Demo of a UI testing agent using the OpenAI CUA model and the Response |
| [langchain-ai/react-agent](https://github.com/langchain-ai/react-agent) | ⭐745 | Python | LangGraph template for a simple ReAct agent |
| [langchain-ai/deep-agents-from-scratch](https://github.com/langchain-ai/deep-agents-from-scratch) | ⭐693 | Jupyter Notebook |  |
| [huggingface/upskill](https://github.com/huggingface/upskill) | ⭐650 | Python | Generate and evaluate agent skills for code agents like Claude Code, O |
| [langchain-ai/agentevals](https://github.com/langchain-ai/agentevals) | ⭐601 | Python | Readymade evaluators for agent trajectories |
| [langchain-ai/agent-protocol](https://github.com/langchain-ai/agent-protocol) | ⭐593 | Python |  |
| [alibaba/one-java-agent](https://github.com/alibaba/one-java-agent) | ⭐578 | Java |  |
| [NVIDIA/skills](https://github.com/NVIDIA/skills) | ⭐548 | Python | AI agent skills published by NVIDIA |
| [langchain-ai/langgraph-bigtool](https://github.com/langchain-ai/langgraph-bigtool) | ⭐539 | Python | Build LangGraph agents with large numbers of tools |
| [google-deepmind/dqn_zoo](https://github.com/google-deepmind/dqn_zoo) | ⭐501 | Python | DQN Zoo is a collection of reference implementations of reinforcement  |
| [crewAIInc/awesome-crewai](https://github.com/crewAIInc/awesome-crewai) | ⭐495 | None | A curated list of open-source projects built by the CrewAI community.  |
| [langchain-ai/deepagents-quickstarts](https://github.com/langchain-ai/deepagents-quickstarts) | ⭐469 | Jupyter Notebook | REPO MOVED |
| [openai/safety-starter-agents](https://github.com/openai/safety-starter-agents) | ⭐463 | Python | Basic constrained RL agents used in experiments for the "Benchmarking  |
| [langchain-ai/memory-agent](https://github.com/langchain-ai/memory-agent) | ⭐441 | Python |  |
| [google-deepmind/lab2d](https://github.com/google-deepmind/lab2d) | ⭐440 | C++ | A customisable 2D platform for agent-based AI research |
| [langchain-ai/react-voice-agent](https://github.com/langchain-ai/react-voice-agent) | ⭐431 | HTML |  |
| [InternLM/WildClawBench](https://github.com/InternLM/WildClawBench) | ⭐406 | Python | An in-the-wild benchmark for AI agents in the OpenClaw Environment. |
| [langchain-ai/langgraphjs-gen-ui-examples](https://github.com/langchain-ai/langgraphjs-gen-ui-examples) | ⭐399 | TypeScript | A collection of generative UI agents written with LangGraph.js |
| [Tencent/TPAT](https://github.com/Tencent/TPAT) | ⭐368 | Python | TensorRT Plugin Autogen Tool |
| [bytedance/agentkit-samples](https://github.com/bytedance/agentkit-samples) | ⭐340 | Python | Awesome samples for Volcengine AgentKit Platform with VeADK. |
| [google-deepmind/science-skills](https://github.com/google-deepmind/science-skills) | ⭐336 | Python | GDM Science Skills to speed up agentic scientific workflows with bette |
| [THUDM/DeepDive](https://github.com/THUDM/DeepDive) | ⭐319 | Python | DeepDive: Advancing Deep Search Agents with Knowledge Graphs and Multi |
| [modelscope/motionagent](https://github.com/modelscope/motionagent) | ⭐311 | Python | MotionAgent is your AI assistent to convert ideas into motion pictures |
| [langchain-ai/rag-research-agent-template](https://github.com/langchain-ai/rag-research-agent-template) | ⭐306 | Python |  |
| [OpenBMB/AppCopilot](https://github.com/OpenBMB/AppCopilot) | ⭐296 | Python | A General, Accurate, Long-Horizon, and Efficient Mobile Agent driven b |
| [THUDM/AgentRL](https://github.com/THUDM/AgentRL) | ⭐290 | Python | Scaling Agentic Reinforcement Learning with a Multi-Turn, Multi-Task F |
| [openai/openai-voice-agent-sdk-sample](https://github.com/openai/openai-voice-agent-sdk-sample) | ⭐254 | TypeScript | Sample application to add voice capabilities to the Agents SDK |
| [langchain-ai/data-enrichment](https://github.com/langchain-ai/data-enrichment) | ⭐231 | Jupyter Notebook | LangGraph Studio template for creating an agent that does web research |
| [modelscope/ultron](https://github.com/modelscope/ultron) | ⭐219 | Python | Ultron: Collective Intelligence System — Shared Memories, Skills, and  |
| [langchain-ai/langgraph-cua-py](https://github.com/langchain-ai/langgraph-cua-py) | ⭐207 | Python | An implementation of a computer use agent (CUA) using LangGraph |
| [NVIDIA/metropolis-nim-workflows](https://github.com/NVIDIA/metropolis-nim-workflows) | ⭐198 | Jupyter Notebook | Collection of reference workflows for building intelligent agents with |
| [alibaba/anolisa](https://github.com/alibaba/anolisa) | ⭐195 | TypeScript | ANOLISA - Agentic Nexus Operating Layer & Interface System Architectur |
| [intel/gprofiler-performance-studio](https://github.com/intel/gprofiler-performance-studio) | ⭐193 | JavaScript | The local version of the backend and UI for the gProfiler agent, featu |
| [openai/openai-support-agent-demo](https://github.com/openai/openai-support-agent-demo) | ⭐187 | TypeScript | Demo of a customer support agent interface using NextJS and the OpenAI |
| [huggingface/jat](https://github.com/huggingface/jat) | ⭐187 | Python | General multi-task deep RL Agent |
| [langchain-ai/create-agent-chat-app](https://github.com/langchain-ai/create-agent-chat-app) | ⭐180 | TypeScript | The quickest way to get started building a LangGraph app |
| [NVIDIA/workbench-example-agentic-rag](https://github.com/NVIDIA/workbench-example-agentic-rag) | ⭐164 | Jupyter Notebook | An NVIDIA AI Workbench example project for an Agentic Retrieval Augmen |
| [alibaba/nginx-http-user-agent](https://github.com/alibaba/nginx-http-user-agent) | ⭐163 | C | A nginx module to match browsers and crawlers |
| [langchain-ai/retrieval-agent-template](https://github.com/langchain-ai/retrieval-agent-template) | ⭐162 | Python |  |
| [Tencent/tat-agent](https://github.com/Tencent/tat-agent) | ⭐157 | Rust | TAT agent is an agent written in Rust, which run in CVM, Lighthouse or |
| [huggingface/screensuite](https://github.com/huggingface/screensuite) | ⭐143 | Python | ScreenSuite - The most comprehensive benchmarking suite for GUI Agents |
| [langchain-ai/openshell-deepagent](https://github.com/langchain-ai/openshell-deepagent) | ⭐140 | Python | A general-purpose coding agent that runs inside an NVIDIA OpenShell sa |
| [NVIDIA/OpenShell-Community](https://github.com/NVIDIA/OpenShell-Community) | ⭐136 | Dockerfile | OpenShell is the safe, private runtime for autonomous AI agents. |
| [alibaba/iot_remote_access](https://github.com/alibaba/iot_remote_access) | ⭐135 | C | 阿里云IoT远程运维套装之远程访问设备侧源码 |
| [01-ai/langcrew](https://github.com/01-ai/langcrew) | ⭐114 | Python | A high-level multi-agent development framework built on LangGraph, com |
| [google-deepmind/dm_env_rpc](https://github.com/google-deepmind/dm_env_rpc) | ⭐109 | Python | A networking protocol for agent-environment communication |
| [langchain-ai/react-agent-js](https://github.com/langchain-ai/react-agent-js) | ⭐106 | TypeScript |  |
| [Tencent/SelfEvolvingAgent](https://github.com/Tencent/SelfEvolvingAgent) | ⭐100 | Python | Research works from Tencent AI Lab regarding self-evolving agents |
| [alibaba/loongsuite-python-agent](https://github.com/alibaba/loongsuite-python-agent) | ⭐100 | Python |  |
| [NVIDIA/NeMo-Agent-Toolkit-UI](https://github.com/NVIDIA/NeMo-Agent-Toolkit-UI) | ⭐99 | TypeScript | The NVIDIA NeMo Agent Toolkit UI streamlines interacting with NeMo Age |


## 🆕 Auto-discovered nexus (2026-05-25 18:10 UTC)

| Repo | Stars | Lang | Description |
|------|-------|------|-------------|
| [openai/ml-agents](https://github.com/openai/ml-agents) | ⭐88 | Python | Unity Machine Learning Agents Toolkit |
| [baidu/cosui](https://github.com/baidu/cosui) | ⭐81 | TypeScript | A frontend UI solution for the AI era. Includes UI protocols, renderin |
| [alibaba/UI-Ins](https://github.com/alibaba/UI-Ins) | ⭐74 | Python | Official implementation of UI-Ins: Enhancing GUI Grounding with Multi- |
| [alibaba/loongsuite-java-agent](https://github.com/alibaba/loongsuite-java-agent) | ⭐73 | Java | Based on OpenTelemetry Java Instrumentation, open source parts of Alib |
| [Tencent/WebAggregator](https://github.com/Tencent/WebAggregator) | ⭐68 | Python | [ACL 2026 Main Conference] WebAggregator |
| [langchain-ai/oap-langgraph-tools-agent](https://github.com/langchain-ai/oap-langgraph-tools-agent) | ⭐67 | Python |  |
| [THUDM/SWE-Dev](https://github.com/THUDM/SWE-Dev) | ⭐60 | Python | [ACL25' Findings] SWE-Dev is an SWE agent with a scalable test case co |
| [langchain-ai/langsmith-cli](https://github.com/langchain-ai/langsmith-cli) | ⭐59 | Go | A coding agent-first CLI for interacting with LangSmith. |
| [crewAIInc/crewAI-quickstarts](https://github.com/crewAIInc/crewAI-quickstarts) | ⭐59 | Jupyter Notebook | A comprehensive collection of CrewAI quickstarts and feature demos des |
| [NVIDIA/voice-agent-examples](https://github.com/NVIDIA/voice-agent-examples) | ⭐55 | Python | Pipecat framework based orchestrator for building real-time, voice-ena |
| [MiniMax-AI/minimax_search](https://github.com/MiniMax-AI/minimax_search) | ⭐54 | Python | MiniMax Search is an MCP (Model Context Protocol) server that provides |
| [modelscope/ms-enclave](https://github.com/modelscope/ms-enclave) | ⭐52 | Python | A modular and stable agent sandbox runtime environment. |
| [alibaba/open-agent-auth](https://github.com/alibaba/open-agent-auth) | ⭐52 | Java | An enterprise framework implementing the Agent Operation Authorization |
| [crewAIInc/enterprise-mcp-server](https://github.com/crewAIInc/enterprise-mcp-server) | ⭐51 | Python | MCP Server for kicking off and getting status of your crew deployments |
| [huggingface/ml-agents](https://github.com/huggingface/ml-agents) | ⭐49 | C# | Unity Machine Learning Agents Toolkit |
| [langchain-ai/memory-agent-js](https://github.com/langchain-ai/memory-agent-js) | ⭐49 | TypeScript |  |
| [NVIDIA/Quantum-Calibration-Agent-Blueprint](https://github.com/NVIDIA/Quantum-Calibration-Agent-Blueprint) | ⭐49 | TypeScript | This is a reference agent blueprint for AI-powered quantum device cali |
| [langchain-ai/agent-inbox-langgraph-example](https://github.com/langchain-ai/agent-inbox-langgraph-example) | ⭐42 | Python | An example repository for getting started with the Agent Inbox and Lan |
| [bytedance/GUI-ReWalk](https://github.com/bytedance/GUI-ReWalk) | ⭐41 | Python | The official code for "GUI-ReWalk: Massive Data Generation for GUI Age |
| [langchain-ai/rag-research-agent-template-js](https://github.com/langchain-ai/rag-research-agent-template-js) | ⭐39 | TypeScript |  |
| [NVIDIA/NeMo-Relay](https://github.com/NVIDIA/NeMo-Relay) | ⭐38 | Rust | Multi-language agent runtime for execution scope management, lifecycle |
| [THUDM/SceneGenAgent](https://github.com/THUDM/SceneGenAgent) | ⭐37 | Python | [ACL 2025 Main] SceneGenAgent: Precise Industrial Scene Generation wit |
| [baidu/ipipe-agent](https://github.com/baidu/ipipe-agent) | ⭐37 | Java |  |
| [langchain-ai/langgraphjs-api](https://github.com/langchain-ai/langgraphjs-api) | ⭐37 | TypeScript | LangGraph.js CLI and in-memory server implementation |
| [huggingface/context-course](https://github.com/huggingface/context-course) | ⭐34 | Python | A course on context engineering with code agents. |
| [langchain-ai/agents-from-scratch-ts](https://github.com/langchain-ai/agents-from-scratch-ts) | ⭐34 | Jupyter Notebook | LangGraph Typescript Agents Notebooks: email, human in the loop, memor |
| [huggingface/physics-intern](https://github.com/huggingface/physics-intern) | ⭐33 | Python | An agentic framework for solving scientific research problems |
| [langchain-ai/langsmith-agent-lifecycle-workshop](https://github.com/langchain-ai/langsmith-agent-lifecycle-workshop) | ⭐33 | Jupyter Notebook | Workshop series teaching the AI Engineering Lifecycle using LangChain, |
| [openai/signup-forms](https://github.com/openai/signup-forms) | ⭐32 | CSS | Code for the paper "World of Bits: An Open-Domain Platform for Web-Bas |
| [langchain-ai/retrieval-agent-template-js](https://github.com/langchain-ai/retrieval-agent-template-js) | ⭐32 | TypeScript |  |
| [langchain-ai/ambient-agent-101](https://github.com/langchain-ai/ambient-agent-101) | ⭐30 | Jupyter Notebook | Learn about the fundamentals of LangGraph through building an ambient  |
| [NVIDIA/NeMo-Agent-Toolkit-Examples](https://github.com/NVIDIA/NeMo-Agent-Toolkit-Examples) | ⭐29 | Python | Community examples utilizing NVIDIA NeMo Agent Toolkit. |
| [NVIDIA/fleet-intelligence-agent](https://github.com/NVIDIA/fleet-intelligence-agent) | ⭐27 | Go | NVIDIA Fleet Intelligence Agent - Host agent for GPU telemetry collect |
| [crewAIInc/skills](https://github.com/crewAIInc/skills) | ⭐25 | None |  |
| [crewAIInc/companies-powered-by-crewai](https://github.com/crewAIInc/companies-powered-by-crewai) | ⭐25 | None | A showcase of companies and platforms leveraging CrewAI to power their |
| [intel/fffc](https://github.com/intel/fffc) | ⭐24 | Python | Easy-to-use tool which autogenerates a type-aware fuzzer from a debugg |
| [NVIDIA/Nemotron-CORTEXA](https://github.com/NVIDIA/Nemotron-CORTEXA) | ⭐23 | Python | Nemotron-CORTEXA is an open-source software engineering agent that fix |
| [01-ai/open-agentkit](https://github.com/01-ai/open-agentkit) | ⭐22 | None | Open-source alternative to OpenAI AgentKit — build, manage, and deploy |
| [langchain-ai/agent-inbox-langgraphjs-example](https://github.com/langchain-ai/agent-inbox-langgraphjs-example) | ⭐22 | JavaScript | An example repository for getting started with the Agent Inbox and Lan |
| [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) | ⭐22 | Python | Security scanner for AI agent skills. Detect vulnerabilities, maliciou |
| [OpenBMB/XAgent-doc](https://github.com/OpenBMB/XAgent-doc) | ⭐21 | None | Document for XAgent. |
| [alibaba/tron-one-agent](https://github.com/alibaba/tron-one-agent) | ⭐21 | Java |  |
| [crewAIInc/marketplace-crew-template](https://github.com/crewAIInc/marketplace-crew-template) | ⭐21 | Python |  |
| [langchain-ai/fullstack-chat-client](https://github.com/langchain-ai/fullstack-chat-client) | ⭐20 | TypeScript | 🦜💬 Web app for interacting with any LangGraph agent (PY & TS) via a ch |
| [google-deepmind/agent_debugger](https://github.com/google-deepmind/agent_debugger) | ⭐20 | Python | Causal Analysis of Agent Behavior for AI Safety |
| [crewAIInc/template_deep_research](https://github.com/crewAIInc/template_deep_research) | ⭐19 | Python |  |
| [Tencent/teamai-cli](https://github.com/Tencent/teamai-cli) | ⭐18 | TypeScript | The team harness for AI agents |
| [alibaba/skill-up](https://github.com/alibaba/skill-up) | ⭐18 | Go | A CLI evaluation framework to make your Agent Skill Up. |
| [alibaba/loongsuite-js-plugins](https://github.com/alibaba/loongsuite-js-plugins) | ⭐18 | TypeScript | OpenTelemetry instrumentation plugins for JavaScript-based AI coding a |
| [alibaba/obz-cli](https://github.com/alibaba/obz-cli) | ⭐16 | Rust | Multi-backend observability CLI for metrics, logs, and traces — unifie |


## 🆕 Auto-discovered nexus (2026-05-25 22:10 UTC)

| Repo | Stars | Lang | Description |
|------|-------|------|-------------|
| [huggingface/ml-agents-patch](https://github.com/huggingface/ml-agents-patch) | ⭐16 | C# | The Unity Machine Learning Agents Toolkit (ML-Agents) is an open-sourc |
| [huggingface/Huggy](https://github.com/huggingface/Huggy) | ⭐15 | None | Huggy is a Unity ML-Agents environment showcasing a dog mastering stic |
| [langchain-ai/async-deep-agents](https://github.com/langchain-ai/async-deep-agents) | ⭐15 | Python |  |
| [langchain-ai/agent-evals](https://github.com/langchain-ai/agent-evals) | ⭐15 | Python | Evals for agents |
| [langchain-ai/text-to-sql-agent](https://github.com/langchain-ai/text-to-sql-agent) | ⭐12 | Jupyter Notebook |  |
| [alibaba/BettaFish](https://github.com/alibaba/BettaFish) | ⭐11 | None | 微舆：人人可用的多Agent舆情分析助手，打破信息茧房，还原舆情原貌，预测未来走向，辅助决策！从0实现，不依赖任何框架。(Fork for  |
| [langchain-ai/react-agent-tool-server](https://github.com/langchain-ai/react-agent-tool-server) | ⭐11 | Python |  |
| [InternLM/EMemBench](https://github.com/InternLM/EMemBench) | ⭐10 | Python | Official Repository of EMemBench: Interactive Benchmarking of Episodic |
| [huggingface/hugex](https://github.com/huggingface/hugex) | ⭐10 | TypeScript | Coding agent user interface |
| [langchain-ai/deep-agent-template](https://github.com/langchain-ai/deep-agent-template) | ⭐10 | Python |  |
| [langchain-ai/cisco-agents-workshop](https://github.com/langchain-ai/cisco-agents-workshop) | ⭐10 | Jupyter Notebook |  |
| [openai/chef-logdna_agent](https://github.com/openai/chef-logdna_agent) | ⭐9 | Ruby | Installs the LogDNA host agent. Currently only supports apt systems. |
| [langchain-ai/mcp-agent](https://github.com/langchain-ai/mcp-agent) | ⭐9 | Python |  |
| [crewAIInc/marketplace-flow-template](https://github.com/crewAIInc/marketplace-flow-template) | ⭐9 | Python |  |
| [THUDM/BattleAgentBench](https://github.com/THUDM/BattleAgentBench) | ⭐8 | Python |  |
| [OpenBMB/RaD-Agent](https://github.com/OpenBMB/RaD-Agent) | ⭐8 | Python | The official implementation of the Rational Decision-Making Agent with |
| [Tencent/tencent-edgeone-agent-plugins](https://github.com/Tencent/tencent-edgeone-agent-plugins) | ⭐8 | None |  |
| [huggingface/rl-baselines3-zoo-update](https://github.com/huggingface/rl-baselines3-zoo-update) | ⭐7 | Python | A training framework for Stable Baselines3 reinforcement learning agen |
| [langchain-ai/deepagents-sandbox-demo](https://github.com/langchain-ai/deepagents-sandbox-demo) | ⭐7 | Python |  |
| [langchain-ai/memory-agent-functional-api](https://github.com/langchain-ai/memory-agent-functional-api) | ⭐7 | None |  |
| [google-deepmind/tabula_rasa_agents](https://github.com/google-deepmind/tabula_rasa_agents) | ⭐7 | Jupyter Notebook |  |
| [Tencent/POINTS-Seeker](https://github.com/Tencent/POINTS-Seeker) | ⭐6 | None | POINTS-Seeker: Towards Training a Multimodal Agentic Search Model from |
| [huggingface/Unity-MLAgents-LoadFromHub-Assets](https://github.com/huggingface/Unity-MLAgents-LoadFromHub-Assets) | ⭐6 | None | Unity scripts and UI for easily loading models from the Hugging Face H |
| [langchain-ai/lca-reliable-agents](https://github.com/langchain-ai/lca-reliable-agents) | ⭐6 | Python |  |
| [crewAIInc/crewai-enterprise-trigger-examples](https://github.com/crewAIInc/crewai-enterprise-trigger-examples) | ⭐6 | Python |  |
| [crewAIInc/template_conversational_example](https://github.com/crewAIInc/template_conversational_example) | ⭐6 | HTML | Demo example of a crew with a conversational interface |
| [crewAIInc/hackaton-demos](https://github.com/crewAIInc/hackaton-demos) | ⭐6 | Jupyter Notebook |  |
| [Tencent/APEX-SQL-Project](https://github.com/Tencent/APEX-SQL-Project) | ⭐5 | Python | APEX-SQL is an agentic Text-to-SQL framework that shifts the paradigm  |
| [alibaba/harbor](https://github.com/alibaba/harbor) | ⭐5 | Python | Harbor is a framework for running agent evaluations and creating and u |
| [huggingface/is-transformers-agentic-enough](https://github.com/huggingface/is-transformers-agentic-enough) | ⭐5 | Python |  |
| [huggingface/tau2-bench](https://github.com/huggingface/tau2-bench) | ⭐5 | Python | τ²-Bench: Evaluating Conversational Agents in a Dual-Control Environme |
| [crewAIInc/template_pull_request_review](https://github.com/crewAIInc/template_pull_request_review) | ⭐5 | Python |  |
| [huggingface/ML-Agents-Training-Executables](https://github.com/huggingface/ML-Agents-Training-Executables) | ⭐4 | None | This repo contains the Unity ML-Agents environments' executables for W |
| [crewAIInc/nvidia-nemotron-demo](https://github.com/crewAIInc/nvidia-nemotron-demo) | ⭐4 | Jupyter Notebook |  |
| [crewAIInc/nvidia-demo](https://github.com/crewAIInc/nvidia-demo) | ⭐4 | Jupyter Notebook |  |
| [huggingface/hf-agentfinder](https://github.com/huggingface/hf-agentfinder) | ⭐3 | Python | Agent Finder Client/Server  |
| [huggingface/pr-search-cli](https://github.com/huggingface/pr-search-cli) | ⭐3 | Python | CLI for accessing PR Similarity Search for Agent PR management |
| [huggingface/Snowball-Target](https://github.com/huggingface/Snowball-Target) | ⭐3 | None | Snowball Target is a Unity ML-Agents environment where you need to tra |
| [langchain-ai/deep-agent-template-js](https://github.com/langchain-ai/deep-agent-template-js) | ⭐3 | TypeScript |  |
| [langchain-ai/stateful-deepagents](https://github.com/langchain-ai/stateful-deepagents) | ⭐3 | Jupyter Notebook | stateful deepagents demo |
| [crewAIInc/course-generator](https://github.com/crewAIInc/course-generator) | ⭐3 | Python | A production-ready example of CrewAI's Flow + Crew hybrid pattern for  |
| [crewAIInc/crewai_training_step_by_step](https://github.com/crewAIInc/crewai_training_step_by_step) | ⭐3 | Python |  |
| [crewAIInc/qdrant_rag_chat_app](https://github.com/crewAIInc/qdrant_rag_chat_app) | ⭐3 | Python | Frontend for CrewAI Rag Application |
| [NVIDIA/air_agent](https://github.com/NVIDIA/air_agent) | ⭐3 | Python | A Python agent for receiving instructions from the NVIDIA Air platform |
| [intel/fdk-debug-agent](https://github.com/intel/fdk-debug-agent) | ⭐3 | C++ |  |
| [huggingface/WebShop](https://github.com/huggingface/WebShop) | ⭐2 | Python | [NeurIPS 2022] 🛒WebShop: Towards Scalable Real-World Web Interaction w |
| [huggingface/rl-baselines3-zoo](https://github.com/huggingface/rl-baselines3-zoo) | ⭐2 | Python | A training framework for Stable Baselines3 reinforcement learning agen |
| [Stability-AI/strands-tools](https://github.com/Stability-AI/strands-tools) | ⭐2 | Python | A set of tools that gives agents powerful capabilities. |
| [langchain-ai/fleet-deepagent-export](https://github.com/langchain-ai/fleet-deepagent-export) | ⭐2 | Python | Self-contained code export for LangSmith Fleet deep agents (AB-2171) |
| [langchain-ai/async-subagents-template](https://github.com/langchain-ai/async-subagents-template) | ⭐2 | Python |  |


## 🆕 Auto-discovered nexus (2026-05-26 02:09 UTC)

| Repo | Stars | Lang | Description |
|------|-------|------|-------------|
| [langchain-ai/sql-support-bot-starter](https://github.com/langchain-ai/sql-support-bot-starter) | ⭐2 | Python | Simple starter code for building a customer support agent with LangSmi |
| [langchain-ai/voice-agents-tracing](https://github.com/langchain-ai/voice-agents-tracing) | ⭐2 | Python |  |
| [crewAIInc/agent-control](https://github.com/crewAIInc/agent-control) | ⭐2 | None |  |
| [crewAIInc/crew-action-2026-03](https://github.com/crewAIInc/crew-action-2026-03) | ⭐2 | TypeScript |  |
| [crewAIInc/crewai-omniauth-okta](https://github.com/crewAIInc/crewai-omniauth-okta) | ⭐2 | Ruby | OAuth2 strategy for Okta with updated code that allows using the defau |
| [crewAIInc/crewai-community-tools](https://github.com/crewAIInc/crewai-community-tools) | ⭐2 | None |  |
| [crewAIInc/sidekiq](https://github.com/crewAIInc/sidekiq) | ⭐2 | None | Sidekiq worker on Render |
| [modelscope/modelscope-skills](https://github.com/modelscope/modelscope-skills) | ⭐1 | None | Equip your agents with skills to interact with ModelScope |
| [alibaba/OSWorld](https://github.com/alibaba/OSWorld) | ⭐1 | None | [NeurIPS 2024] OSWorld: Benchmarking Multimodal Agents for Open-Ended  |
| [huggingface/meta-agents-research-environments](https://github.com/huggingface/meta-agents-research-environments) | ⭐1 | Python | Meta Agents Research Environments is a comprehensive platform designed |
| [huggingface/AgentLite](https://github.com/huggingface/AgentLite) | ⭐1 | None |  |
| [Stability-AI/strands-sdk-python](https://github.com/Stability-AI/strands-sdk-python) | ⭐1 | Python | A model-driven approach to building AI agents in just a few lines of c |
| [langchain-ai/simple-agent-template](https://github.com/langchain-ai/simple-agent-template) | ⭐1 | Python |  |
| [crewAIInc/template_research_agent](https://github.com/crewAIInc/template_research_agent) | ⭐1 | None |  |
| [crewAIInc/template_job_fit_assessment](https://github.com/crewAIInc/template_job_fit_assessment) | ⭐1 | Python | Job Fit Assessment demo app |
| [crewAIInc/template_support_ticket_front](https://github.com/crewAIInc/template_support_ticket_front) | ⭐1 | CSS |  |
| [crewAIInc/template_frontend_crewai_flows_streamlit_ui](https://github.com/crewAIInc/template_frontend_crewai_flows_streamlit_ui) | ⭐1 | Python |  |
| [crewAIInc/Corsair_SnowflakeProject](https://github.com/crewAIInc/Corsair_SnowflakeProject) | ⭐1 | Python |  |
| [crewAIInc/Madison-Reed-MVP](https://github.com/crewAIInc/Madison-Reed-MVP) | ⭐1 | Python |  |
| [intel/sagent-helm](https://github.com/intel/sagent-helm) | ⭐1 | None | sagest helm chart for certification |
| [01-ai/open-agentkit-builder](https://github.com/01-ai/open-agentkit-builder) | ⭐0 | TypeScript | open-agentkit-builder |
| [Stability-AI/strands-docs](https://github.com/Stability-AI/strands-docs) | ⭐0 | None | Documentation for the Strands Agents SDK. A model-driven approach to b |
