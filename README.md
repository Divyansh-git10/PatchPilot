# PatchPilot 🚀

PatchPilot is an agentic AI framework designed to assist with solving issues in open-source Go repositories.

The system analyzes GitHub issues, understands repository structure, retrieves relevant code context, generates engineering plans, proposes code patches, validates changes using real Go tests, and creates professional pull request summaries.

This project was built as part of an Agentic AI take-home assignment focused on repository-aware autonomous software engineering workflows.

---

# ✨ Features

* GitHub issue understanding using LLM reasoning
* Repository-aware code analysis
* Relevant Go file identification
* Lightweight semantic code retrieval
* Engineering planning agent
* Repository-aware code patch generation
* Real Go repository validation (`go test ./...`)
* Automated pull request summary generation
* Modular multi-agent architecture

---

# 🧩 Tech Stack

* Python
* OpenRouter API
* DeepSeek LLM
* GitPython
* Go Toolchain
* Requests
* BeautifulSoup


# 🧠 System Architecture

```
GitHub Issue
      ↓
Issue Analyzer Agent
      ↓
Repository Mapper Agent
      ↓
Semantic Retrieval Layer
      ↓
Planner Agent
      ↓
Code Generation Agent
      ↓
Validation Agent
      ↓
PR Writer Agent
```

---

# 🤖 Agents

## 1. Issue Analyzer

Understands GitHub issues and extracts:

* problem summary
* affected modules
* testing considerations
* suggested fix directions

---

## 2. Repository Mapper

Scans Go repositories and identifies:

* relevant source files
* test files
* contextually important modules

---

## 3. Semantic Retrieval Layer

Performs lightweight semantic-style retrieval across repository code to surface relevant files for the issue context.

---

## 4. Planner Agent

Creates an engineering plan including:

* root cause analysis
* files to modify
* functions likely to change
* testing strategy
* risk assessment

---

## 5. Code Generation Agent

Generates focused Go patch suggestions using:

* repository context
* engineering plans
* retrieved code structure

---

## 6. Validation Agent

Runs:

```bash
go test ./...
```

against the repository to validate generated changes.

---

## 7. PR Writer Agent

Automatically generates:

* PR title
* PR description
* testing summary
* implementation notes

---

# 📂 Project Structure

```text
PatchPilot/
│
├── agents/
│   ├── issue_analyzer.py
│   ├── repo_mapper.py
│   ├── planner.py
│   ├── coder.py
│   ├── validator.py
│   └── pr_writer.py
│
├── tools/
│   ├── embedding_tool.py
│   ├── github_tool.py
│   ├── git_tool.py
│   ├── search_tool.py
│   └── test_runner.py
│
├── repositories/
│   └── cobra/
│
├── outputs/
│
├── memory/
│
├── prompts/
│
├── main.py
├── requirements.txt
└── README.md
```

# 📦 Supported Repositories

Currently tested with:

* spf13/cobra

The framework architecture is extensible and can support additional Go repositories with minimal changes.


---

# ⚙️ Setup Instructions

## 1. Clone Repository

```bash
git clone <your_repo_url>
cd PatchPilot
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure API Key

Create a `.env` file:

```env
OPENAI_API_KEY=your_openrouter_api_key
```

---

## 5. Install Go

PatchPilot uses real Go validation.

Verify installation:

```bash
go version
```

---

## 6. Clone Supported Repository

Example:

```bash
cd repositories
git clone https://github.com/spf13/cobra.git
cd ..
```

---

# ▶️ Running PatchPilot

```bash
python main.py
```

Example issue:

```text
https://github.com/spf13/cobra/issues/2259
```

---

# ✅ Example Workflow

PatchPilot performs:

1. GitHub issue analysis
2. Repository scanning
3. Relevant code retrieval
4. Engineering planning
5. Patch generation
6. Go test validation
7. PR summary generation

---

# 🧪 Validation

PatchPilot executes real Go repository tests:

```bash
go test ./...
```

Validation results are surfaced transparently, including:

* successful builds
* compilation failures
* test failures
* environment limitations

---

# 🛠️ Design Decisions

## Lightweight Retrieval

A lightweight semantic-style retrieval approach was used to keep the framework fast, portable, and easy to run locally.

## Modular Agent Architecture

Each capability is separated into independent agents to improve extensibility and maintainability.

## Safe Patch Generation

The framework generates focused patch suggestions instead of blindly modifying repositories.

---

# 🚀 Future Improvements

* Transformer-based vector embeddings
* Automatic Git diff generation
* Repository graph understanding
* Multi-file coordinated patching
* Autonomous fix validation loops
* Dockerized execution environment
* Benchmarking against accepted PRs

---

# 📌 Notes

PatchPilot is intentionally designed as a focused and understandable framework rather than a fully autonomous production software engineering agent.

The goal is to demonstrate:

* repository reasoning
* agent orchestration
* retrieval-augmented engineering workflows
* safe code generation pipelines

---

# 📄 License

MIT License
