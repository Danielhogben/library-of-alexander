# 🔬 Reverse Engineering — Architecture Deep Dives

> How popular AI systems actually work. Design patterns, code analysis, and lessons learned.

---

## Agent Framework Architectures

### 1. LangChain Architecture

**Pattern:** Chain of Responsibility + Builder

```
Prompt → LLM → Parser → Chain → Agent → Tools → Output
```

**Key abstractions:**
- `Chain` — Sequential operations
- `Agent` — LLM + tools + reasoning loop
- `Tool` — Callable function with schema
- `Memory` — Conversation state
- `Retriever` — RAG document retrieval

**Strengths:**
- Massive ecosystem (1000+ integrations)
- Well-documented
- Huge community

**Weaknesses:**
- Overly complex abstractions
- Heavy dependencies
- Frequent breaking changes
- "LangChain syndrome" — over-engineering simple tasks

**Lessons:**
- Keep it simple — most agents don't need the full framework
- The agent loop is simple: think → act → observe → repeat
- Don't abstract what you don't need

---

### 2. CrewAI Architecture

**Pattern:** Role-Based Multi-Agent

```
Crew → [Agent(role, goal, backstory) → Task → Tool] → Output
```

**Key abstractions:**
- `Agent` — Role-based worker with LLM + tools
- `Task` — Unit of work with expected output
- `Crew` — Collection of agents + tasks
- `Process` — Sequential or hierarchical execution

**Strengths:**
- Intuitive role-based design
- Good for complex multi-step workflows
- Human-in-the-loop support

**Weaknesses:**
- Rigid structure
- Not suitable for dynamic workflows
- Limited tool ecosystem vs LangChain

**Lessons:**
- Role-based design is intuitive but inflexible
- Hierarchical task decomposition works well
- Process model (sequential vs hierarchical) matters

---

### 3. AutoGen Architecture

**Pattern:** Conversational Multi-Agent

```
UserProxy ↔ Assistant ↔ [Expert1, Expert2, ...] → Output
```

**Key abstractions:**
- `ConversableAgent` — Any entity that can send/receive messages
- `AssistantAgent` — LLM-powered agent
- `UserProxyAgent` — Human proxy
- `GroupChat` — Multi-agent conversation manager

**Strengths:**
- Flexible conversation patterns
- Strong academic foundation
- Good for research

**Weaknesses:**
- Complex configuration
- Message passing can be confusing
- Steep learning curve

**Lessons:**
- Message-passing is powerful but complex
- Group chat management is a hard problem
- Human-in-the-loop needs careful design

---

### 4. Google ADK Architecture

**Pattern:** Tool-Centric Agent

```
Agent(LLM, Tools, Instructions) → [Tool Call → Result] → Output
```

**Key abstractions:**
- `Agent` — LLM + tools + instructions
- `Tool` — Function with schema
- `Session` — Conversation state
- `Runner` — Execution engine

**Strengths:**
- Clean, minimal design
- Strong tool integration
- Good MCP support
- Production-ready

**Weaknesses:**
- Google-centric
- Smaller community
- Less flexible than AutoGen

**Lessons:**
- Simplicity wins — fewer abstractions = easier to understand
- Tool design is critical — good tools make good agents
- Session management is harder than it looks

---

### 5. OpenAI Agents SDK / Swarm

**Pattern:** Minimal Agent Loop

```
Agent(instructions, tools) → [handoff → Agent] → Output
```

**Key abstractions:**
- `Agent` — Instructions + tools + handoffs
- `Handoff` — Transfer to another agent
- `Runner` — Execute agent loop
- `Guardrail` — Input/output validation

**Strengths:**
- Extremely minimal
- Handoff pattern is elegant
- Guardrails for safety
- Easy to understand

**Weaknesses:**
- Very basic — you build everything else
- OpenAI-centric
- Limited ecosystem

**Lessons:**
- The agent loop is just: get input → call LLM → use tool → repeat
- Handoffs are the key pattern for multi-agent
- Guardrails are essential for production

---

### 6. DeerFlow (ByteDance) Architecture

** Pattern:** Sandbox + Sub-Agent Orchestration

```
Planner → [Sub-Agent in Sandbox] → Coordinator → Output
```

**Key abstractions:**
- `Planner` — Creates execution plan
- `Coordinator` — Manages sub-agents
- `Sub-Agent` — Specialized worker in sandbox
- `Sandbox` — Isolated execution environment

**Strengths:**
- Sandbox isolation for safety
- Sub-agent specialization
- Good for deep research

**Weaknesses:**
- Complex setup
- Sandbox overhead
- ByteDance-centric

**Lessons:**
- Sandboxing agents is important for safety
- Sub-agent decomposition is powerful
- Planning before execution improves quality

---

### 7. Letta (MemGPT) Architecture

** Pattern:** Persistent Memory Agent

```
Agent ↔ [Core Memory, Archival Memory, Recall Memory] → Output
```

**Key abstractions:**
- `Agent` — LLM with persistent memory
- `Memory Block` — Editable memory sections
- `Archival Memory` — Long-term storage
- `Recall Memory` — Searchable history

**Strengths:**
- Best-in-class memory management
- Persistent across sessions
- Human-like memory model

**Weaknesses:**
- Complex memory management
- Higher token usage
- Steeper learning curve

**Lessons:**
- Memory is the hardest problem in agents
- Three-tier memory (core/archival/recall) is a good model
- Memory editing (not just appending) is crucial

---

### 8. Agno Architecture

** Pattern:** Model-Agnostic Agent

```
Agent(model, tools, storage, knowledge) → Output
```

**Key abstractions:**
- `Agent` — Model-agnostic agent
- `Model` — Any LLM provider
- `Toolkit` — Grouped tools
- `Storage` — Persistent state
- `Knowledge` — RAG knowledge base

**Strengths:**
- True model agnosticism
- Clean separation of concerns
- Fast (written in Rust core)

**Weaknesses:**
- Newer, smaller community
- Less documentation
- Fewer integrations

**Lessons:**
- Model agnosticism is valuable — don't lock in
- Separation of concerns (model/tools/storage/knowledge) is clean
- Performance matters — Rust core is fast

---

## Common Design Patterns

### The Agent Loop
```
while not done:
    thought = llm.think(context, tools)
    if thought.is_tool_call:
        result = tool.execute(thought)
        context.add(result)
    else:
        return thought.answer
```

### The Handoff Pattern
```
agent_a → [handoff] → agent_b → [handoff] → agent_c → output
```

### The Sandbox Pattern
```
coordinator → [spawn sandbox] → agent → [collect result] → coordinator
```

### The Memory Pattern
```
input → [recall memory] → [core memory] → LLM → [update memory] → output
```

### The RAG Pattern
```
query → [embed] → [vector search] → [rerank] → [augment prompt] → LLM → output
```

---

## What We've Learned

1. **Simplicity wins.** The best frameworks have the fewest abstractions.
2. **Memory is hard.** Most agents fail because of poor memory management.
3. **Tools matter more than prompts.** Good tool design > clever prompting.
4. **Multi-agent is overhyped.** Single agent with good tools beats most multi-agent setups.
5. **Sandboxing is essential.** Never run untrusted code without isolation.
6. **Model agnosticism is valuable.** Today's best model is tomorrow's obsolete one.
7. **Guardrails are non-negotiable.** Production agents need input/output validation.
8. **Testing is hard but necessary.** Agent behavior is non-deterministic — test accordingly.

---

*Last updated: 2026-05-25*
