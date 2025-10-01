# 🌬️ Anemoi: A Semi-Centralized Multi-Agent System Based on Agent-to-Agent Communication MCP Server

**Anemoi** is a **semi-centralized multi-agent system (MAS)** built on the **Agent-to-Agent (A2A) communication MCP server**.
Unlike traditional **context-engineering + centralized paradigms**, Anemoi enables **structured and direct inter-agent collaboration**, allowing agents to **debate, refine, and adapt** in real time.

<p align="center">
  <img src="Anemoi/images/Anemoi_semi.png" alt="Anemoi Concept" width="70%">
</p>

---

## ✨ Motivation

Recent advances in generalist MAS largely follow a **centralized planner + worker** paradigm, where:

* A **planner agent** coordinates multiple worker agents through unidirectional prompt passing.
* This design works with **strong LLMs**, but faces two critical limitations:

  1. **Over-reliance on large LLMs** → performance drops sharply in small-LLM settings.
  2. **Limited inter-agent communication** → collaboration is reduced to **prompt concatenation**, not genuine refinement.

**Anemoi** addresses these challenges by introducing **semi-centralized A2A collaboration** with **Multi-Agents Debate**, making agents behave more like a real-world team.

---

## 🚀 Key Features

* **Semi-Centralized Architecture**
  Reduces dependency on a single planner agent, enabling adaptive updates.

* **Multi-Agents Debate for Collaboration**
  All agents can **monitor progress, assess results, identify bottlenecks, and refine plans** in real time.

* **Collaboration-Driven Reliability**
  **Multi-Agents Debate** yields more **consistent and explainable outcomes** than stochastic worker behavior.


<p align="center">
  <img src="Anemoi/images/Anemoi_workflow.png" alt="Anemoi Workflow" width="85%">
</p>

---

## 📊 Benchmark Results (GAIA)

We evaluated Anemoi on the **General Artificial Intelligence Assistants (GAIA)** benchmark — a challenging suite of real-world, multi-step tasks (web search, file processing, coding).

| Setting              | Planner      | Workers                | Accuracy (pass@3) | Comparison vs. OWL |
| -------------------- | ------------ | ---------------------- | ----------------- | ------------------ |
| **Small-LLM (SOTA)** | GPT-4.1-mini | GPT-4.1-mini / o4-mini | **63.64%**        | +1.82%             |
| **Weaker Workers**   | GPT-4.1-mini | GPT-4o                 | **52.73%**        | +9.09%             |

📌 **Highlights:**

* Anemoi establishes a new **SOTA in the small-LLM regime**.
* Outperforms **Optimized Workforce Learning (OWL)** under identical settings.
* Case-level analysis:

  * **25 tasks solved by Anemoi but missed by OWL** → 48% enabled by **Multi-Agents Debate**.
  * OWL’s unique wins (86%) mainly reflect **stochastic worker behavior**.

---

## Reproduction

Set up environment variables:

```
echo '
export FIRECRAWL_API_KEY="your_firecrawl_api_key"
export GOOGLE_API_KEY="your_google_api_key"
export HF_HOME="your_hf_home_path"
export AZURE_KEY="your_azure_api_key"
export SEARCH_ENGINE_ID="your_search_engine_id"
export CHUNKR_API_KEY="your_chunkr_api_key"
' >> ~/.bashrc && source ~/.bashrc
```

Create environment:

```
cd Anemoi
/usr/bin/python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

We made some minor modifications to CAMEL 0.2.70 for our experiments:

```
rm -rf venv/lib/python3.12/site-packages/camel
cp -r utils/camel venv/lib/python3.12/site-packages/
```

Run the experiment:

```
cd ..
./gradlew run --console=plain
```




