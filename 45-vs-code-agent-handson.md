# Hands-On Tutorial: Mastering GitHub Copilot in VS Code 1.102 for Python Data Engineering Teams (July 2025 Edition)

Welcome to this hands-on, team-optimized guide for leveraging GitHub Copilot in Visual Studio Code (VS Code) 1.102 (June/July 2025). This tutorial is tailored for Python data engineering teams building ETL pipelines, processing data with Pandas/Spark, integrating SQL, and collaborating via GitHub. All steps reflect the latest open-source Copilot Chat, MCP support, and Python-specific enhancements.


## Prerequisites and Setup

1. **Update to VS Code 1.102**: Download from [code.visualstudio.com](https://code.visualstudio.com/updates/v1_102). Key Python features: improved Poetry activation, .venv handling, and bundled Python Environments extension.

2. **Install Extensions**:

   - [GitHub Copilot Chat (MIT, open source)](https://github.com/microsoft/vscode-copilot-chat)
   - [Python (includes Pylance, MCP tools)](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
   - [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
   - Sign in with GitHub (Enterprise for team policies/unlimited access)

3. **MCP Prerequisites**:

   - **Node.js 18+**: Required for npm-based MCP servers
   - **Python 3.8+**: For uvx-based servers (`pip install uvx`)
   - **Network Access**: Ensure firewall allows MCP server connections
   - **Tokens Ready**: GitHub PAT, API keys for third-party services

4. **Project Prep**:

   - Clone your team repo (e.g., Pandas ETL scripts)
   - Enable Git; use branches for agent experiments
   - Install data libraries via `requirements.txt` (pandas, pyspark, etc.)
   - Set workspace trust for terminals; configure GitHub policies to block sensitive data sharing
   - Monitor RAM for Spark sessions—agent mode can spike usage

5. **Team Configuration**:
   - **Shared MCP Setup**: Add `devcontainer.json` with pre-configured servers
   - **Role-Based Access**: Limit MCP servers by team role (junior devs vs. seniors)
   - **Cost Management**: Set usage policies for paid MCP services

## Section 1: Understanding Copilot Chat Modes

GitHub Copilot Chat offers three distinct modes, each with different levels of automation and control. Think of them as a "safety slider"—from full human control to AI autonomy.

### The Three-Mode Spectrum

| Mode      | Control Level         | Use Case                                  | File Changes                      |
| --------- | --------------------- | ----------------------------------------- | --------------------------------- |
| **Ask**   | Full human control    | Learning, brainstorming, safe exploration | None (manual copy/paste only)     |
| **Edit**  | Collaborative jamming | Iterative coding, specific improvements   | Direct file editing with approval |
| **Agent** | AI autonomy           | Multi-step tasks, full implementations    | Autonomous with human checkpoints |

## Section 1A: Ask Mode - The Safe Learning Zone

Ask mode is your "sandbox"—perfect for learning, brainstorming, and understanding codebases without any file modifications.

### When to Use Ask Mode

- **New to a project**: "What is this codebase structure?"
- **Learning concepts**: "Explain async/await in Python data pipelines"
- **Brainstorming**: "What's the best way to implement notifications?"
- **Code review**: "What are potential issues with this Pandas function?"

### Hands-On Steps

1. **Open Chat**: `Ctrl+Alt+I` (Windows/Linux) or `Cmd+Alt+I` (Mac)
2. **Stay in Ask Mode**: Default mode with maximum model selection
3. **Add Context**: Use `#file:`, drag files, or `@workspace` for broader context
4. **Interactive Learning**: Ask follow-up questions, request different formats

### Advanced Ask Mode Features

**Smart Apply**: Instead of copy/paste, use the "Apply in Editor" button for intelligent code insertion across multiple file locations.

**Context Management**:

- **Remove current file**: Click X to ask general questions without file context
- **Add screenshots**: Drag UI mockups for implementation guidance
- **Reference problems**: Use `#problems` to debug specific issues

**Model Selection Strategy**:

- **GPT-4o**: Fast responses, good for quick questions
- **Claude 3.5**: Superior for UI/CSS suggestions and complex explanations
- **Thinking models**: Deep analysis of complex problems
- **Mini models**: Simple syntax or quick lookups

### Data Engineering Ask Mode Examples

```text
"What are the performance implications of this Pandas groupby operation?"

"How would I implement error handling for this ETL pipeline?"

"@workspace What data validation patterns do we use across our pipelines?"

"Explain the memory usage differences between Pandas and Spark for this dataset size"
```

### Ask Mode Best Practices

- **Start conversations**: Use "New Chat" to reset context
- **Be specific**: "Generate SQL for BigQuery" vs "Help with SQL"
- **Learn iteratively**: Follow up with "show me an example" or "what are the pitfalls?"
- **Copy markdown**: Ask for "markdown format" to easily save responses

## Section 1B: Edit Mode - Collaborative Jamming

Edit mode moves you into active coding collaboration—Copilot edits files directly but you maintain approval control.

### When to Use Edit Mode

- **Iterative improvements**: Enhancing specific components or functions
- **Focused refactoring**: Working on particular files or features
- **UI tweaks**: Styling improvements, layout adjustments
- **Single-feature implementation**: Adding one clear capability

### Hands-On Steps (Edit Mode)

1. **Switch to Edit Mode**: Click "Edit" in chat interface
2. **Define scope**: Specify files or let Copilot search via `@codebase`
3. **Give clear instructions**: "Enhance button design" or "Add error handling"
4. **Review changes**: Use diff view to approve/reject modifications
5. **Save but don't keep**: Test changes before final commit

**Revolutionary Concept**: Edit mode introduces two-stage saves:

- **Save**: Changes go to memory, hot reload active, fully reversible
- **Keep**: Commits changes permanently, removes "undo" option

**Line-by-line approval**: Green checkboxes let you approve individual changes
**Smart diff viewing**: See exactly what changed with context
**Instant undo**: Revert all changes with one click before "keeping"

### Data Engineering Edit Examples

```text
"Add data validation to this ETL function using Pandas assertions"

"Optimize this SQL query for BigQuery performance"

"Refactor this Spark job to handle larger datasets"

"Add comprehensive error logging to this pipeline"
```

## Section 1C: Agent Mode - Full AI Autonomy

Agent mode gives Copilot maximum freedom to plan, execute, and iterate on complex multi-step tasks.

### When to Use Agent Mode

- **Complete feature implementation**: Full user authentication, complex workflows
- **Cross-file changes**: Updates spanning multiple components
- **Infrastructure setup**: Database schemas, API endpoints, configuration
- **Bug investigation**: Diagnosing and fixing issues across the codebase

**Autonomous actions**:

- Install npm packages (with approval)
- Create/modify/delete files
- Run terminal commands
- Make database queries (via MCP)
- Generate documentation
- Fix discovered issues

**Self-healing behavior**:

- Checks its own work
- Notices related improvements
- Follows coding best practices
- Iterates until completion

### Hands-On Workflow: Complete ETL Implementation

1. **Create GitHub Issue**: "Implement customer data ETL with validation"
2. **Agent Prompt**: "Work on issue #5 - build complete ETL pipeline with error handling"
3. **Tool Chain Execution**:
   - Analyzes existing codebase structure
   - **Human approval**: Install required packages
   - Creates data validation functions
   - Implements main ETL pipeline
   - **Human approval**: Run tests
   - Updates documentation
   - **Human approval**: Commit changes

### Advanced Agent Examples

**Database-driven development**:

```text
"Use the PostgreSQL MCP to analyze our sales schema, then implement a complete analytics pipeline with Pandas transformations and automated reporting"
```

**Infrastructure automation**:

```text
"Set up a complete CI/CD pipeline for our data processing jobs, including Docker configuration, GitHub Actions, and deployment scripts"
```

**Human checkpoints**: Agent stops for approval on:

- Terminal commands
- Package installations
- File deletions
- External API calls

**Best practices**:

- Use dev containers for isolation
- Start with smaller tasks to build trust
- Review generated code for security issues
- Monitor resource usage during execution

## Section 2: Custom Instructions

Enforce team Python standards (PEP8, docstrings) via repo files—auto-generated from codebase for data engineering consistency.

### Hands-On Steps (Custom Instructions)

1. **Generate File**: Run "Chat: Generate Instructions"—analyzes your ETL code for tailored `.github/copilot-instructions.md`.
2. **Apply**: Commit/push. Prompt: "Write a Pandas function to merge datasets." Verify adherence in "Used references."
3. **Team Refine**: Import shared modes from GitHub (e.g., data-eng templates).

### Actionable Tips

- **Data Eng Focus**: Include rules for error handling in pipelines, SQL best practices.
- **Team Sync**: Use glob patterns for conditional instructions (e.g., for notebooks).
- **Pitfalls**: If ignored, debug with Chat Debug View—logs prompts/tools.
- **Boost**: Reduces prompt verbosity; ideal for team onboarding.
- **Community Tip**: "Test iteratively; great for standardizing tests."

## Section 3: Model Context Protocol (MCP)

MCP extends agents with external tools and data sources—GA with full spec support (prompts, resources, sampling). Perfect for data engineering workflows requiring database access, cloud integrations, and automated documentation.

### Hands-On Steps (MCP)

1. **Enable MCP**: Open Command Palette (`Cmd+Shift+P`) → "Preferences: Open User Settings (JSON)"
2. **Configure Servers**: Add MCP block to `settings.json`:

```json
{
  "github.copilot.chat.experimental.mcp": true,
  "mcp": {
    "servers": {
      "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "env": {
          "GITHUB_PERSONAL_ACCESS_TOKEN": "your_token_here"
        }
      },
      "postgres": {
        "command": "uvx",
        "args": ["mcp-server-postgres", "--connection-string", "postgresql://user:pass@localhost/db"]
      },
      "filesystem": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/data"]
      }
    }
  }
}
```

3. **Verify Installation**: Command Palette → "MCP: List Servers" or click spanner icon in Copilot Chat

### Tips for MCP Server Setup

- **Data Source Security**: Always use read-only connections for databases.
- **Environment Isolation**: Use separate MCP servers for development and production.
- **Cost Monitoring**: Keep an eye on usage if using paid third-party MCP servers.

### Popular MCP Servers for Data Engineering

| Server Type | Use Case | Installation |
|-------------|----------|--------------|
| **GitHub** | Project analysis, issue tracking, PR reviews | `npx -y @modelcontextprotocol/server-github` |
| **PostgreSQL** | Direct DB queries, schema analysis | `uvx mcp-server-postgres` |
| **Filesystem** | Local data file access, log analysis | `npx -y @modelcontextprotocol/server-filesystem` |
| **Perplexity** | Research best practices, debugging help | Third-party API integration |
| **AWS S3** | Cloud data access, bucket operations | `mcp-server-s3` |

### Hands-On Workflow: Pipeline Documentation with MCP

**Scenario**: Generate comprehensive ETL pipeline documentation using GitHub issues and external research.

1. **Create GitHub Issue**: "Need documentation for customer_data_pipeline.py"
2. **Agent Prompt**: "Work on issue #5 using GitHub MCP to analyze our ETL codebase"
3. **Tool Chain Execution**:
   - Agent calls GitHub MCP → retrieves issue details
   - **Human approval required** → Click "Continue"
   - Agent calls Perplexity MCP → research ETL best practices
   - **Human approval required** → Click "Continue"
   - Agent generates documentation with context from both sources

**Expected Output**: Professional README with project overview, quick start guide, pipeline architecture, and troubleshooting sections.

### MCP Tool Chain Management

**Human-in-the-Loop Controls**:

- Each MCP server call requires explicit approval
- Review tool chain requests before authorizing
- Reject calls accessing sensitive data sources
- Monitor costs for third-party MCP services

**Visual Server Management**:

- **Status Check**: Green indicators show running servers
- **Quick Toggle**: Enable/disable servers via Copilot Chat UI
- **Debug Mode**: One-click debugging for server-side development

### Example Prompts for Advanced Integration

```text
"Use GitHub MCP to analyze recent issues and PRs, then create comprehensive documentation for our ETL pipelines including troubleshooting guide"
```

```text
"Use the codebase tool to find all Spark jobs, analyze performance patterns, then implement optimizations with before/after benchmarks"
```

```text
"Create a complete onboarding guide by analyzing our codebase structure, documenting setup steps, and generating example workflows for new data engineers"
```

### Example Prompts for Voice Input

```text
🎤 "Hey, the delete list button isn't working. Check if we're missing an API method or if there's an error. Also add a confirmation modal before deleting."

🎤 "Create a GitHub issue for adding light/dark mode toggle. Be specific about requirements and ask for clarification if needed."

🎤 "Look at the PostgreSQL schema and list all tables, then generate a Pandas ETL pipeline for the sales data."
```

## Section 3A: Devcontainer Setup for Copilot & MCP

A **devcontainer** lets you define a reproducible development environment for your team using VS Code. This ensures everyone gets the same Python, Node.js, Copilot, and MCP setup—removing "works on my machine" issues.

### Why Use Devcontainers?

- **Consistency:** All team members use the same tools, extensions, and settings.
- **Isolation:** Safely run agent workflows, install packages, and access data sources.
- **Automation:** Pre-install Copilot Chat, Python, and MCP servers for instant onboarding.

### Step-by-Step Devcontainer Setup

1. **Create a `.devcontainer` folder** in your project root.
2. **Add a `devcontainer.json` file** with recommended settings:

    ```json
    // filepath: .devcontainer/devcontainer.json
    {
      "name": "Data Engineering with MCP",
      "image": "mcr.microsoft.com/vscode/devcontainers/python:3.11",
      "features": {
        "ghcr.io/devcontainers/features/node:1": {"version": "18"}
      },
      "extensions": [
        "ms-python.python",
        "GitHub.copilot-chat"
      ],
      "settings": {
        "github.copilot.chat.experimental.mcp": true
      },
      "postCreateCommand": "pip install -r requirements.txt && npm install -g @modelcontextprotocol/server-github @modelcontextprotocol/server-filesystem"
    }
    ```

3. **Open your project in VS Code** and select "Reopen in Container" when prompted.
4. **Verify MCP servers**: Use `Cmd+Shift+P` → "MCP: List Servers" to check installed servers.
5. **Customize further**: Add environment variables, secrets, or additional extensions as needed.

### Devcontainer Best Practices

- Store secrets securely (never hard-code tokens in `devcontainer.json`).
- Use `postCreateCommand` for installing dependencies and MCP servers.
- Share `.devcontainer` in your repo for team onboarding.
- Combine with `.vscode/mcp.json` for workspace-specific MCP configuration.

---

## Quick Reference: Configuration Paths

| Aspect                     | Location Path / File                             | Description / Usage                       |
| -------------------------- | ------------------------------------------------ | ----------------------------------------- |
| VS Code Extensions         | Extensions View (`Ctrl+Shift+X`)                 | Install/Manage extensions                 |
| Copilot Chat Settings      | `settings.json` (User/Workspace)                 | General Copilot settings, model selection |
| MCP Servers (User)         | `mcp.json` (User Profile)                        | Global MCP server config (all workspaces) |
| MCP Servers (Workspace)    | `.vscode/mcp.json`                               | Project-specific MCP server config        |
| MCP Servers (Devcontainer) | `.devcontainer/devcontainer.json`                | Team-wide MCP config for containers       |
| Custom Instructions        | `.github/copilot-instructions.md`                | Team coding standards, auto-generated     |
| Custom Chat Modes          | `.github/chatmodes/*.chatmode.md`                | Custom chat mode definitions              |
| Python Extension Settings  | `settings.json`                                  | Python interpreter, linting, formatting   |
| Jupyter Extension Settings | `settings.json`                                  | Notebook, kernel, and Jupyter config      |
| Workspace Trust            | Workspace Settings / Command Palette             | Security for terminals, agent actions     |
| GitHub Policies            | GitHub Enterprise Admin / repo settings          | Data sharing, model access, org policies  |

---

## Pro Tips for Teams

- **Onboard Faster:** New team members just clone the repo and "Reopen in Container"—no manual setup.
- **Troubleshoot Easily:** Use MCP logs and VS Code output pane for debugging agent workflows.
- **Audit & Compliance:** Enable session logging and workspace trust for security.
- **Scale Safely:** Use devcontainer for experiments before rolling out changes to production.

---

**For more details:**  
- [VS Code Dev Containers Documentation](https://code.visualstudio.com/docs/devcontainers/containers)  
- [MCP Servers for Agent Mode Documentation](https://code.visualstudio.com/mcp)  
- [Python Data Science Handbook (Jupyter Notebooks)](https://github.com/jakevdp/PythonDataScienceHandbook)

Empower your team—Copilot as collaborator, not replacement!


## Configuration Location Reference

| Aspect                     | Location Path / File                             | Description / Usage                       |
| -------------------------- | ------------------------------------------------ | ----------------------------------------- |
| VS Code Extensions         | User/Workspace: Extensions View (`Ctrl+Shift+X`) | Install/Manage extensions                 |
| Copilot Chat Settings      | `settings.json` (User/Workspace)                 | General Copilot settings, model selection |
| MCP Servers (User)         | `mcp.json` (User Profile)                        | Global MCP server config (all workspaces) |
| MCP Servers (Workspace)    | `.vscode/mcp.json`                               | Project-specific MCP server config        |
| MCP Servers (Devcontainer) | `.devcontainer/devcontainer.json`                | Team-wide MCP config for containers       |
| Custom Instructions        | `.github/copilot-instructions.md`                | Team coding standards, auto-generated     |
| Custom Chat Modes          | `.github/chatmodes/*.chatmode.md`                | Custom chat mode definitions              |
| Python Extension Settings  | `settings.json`                                  | Python interpreter, linting, formatting   |
| Jupyter Extension Settings | `settings.json`                                  | Notebook, kernel, and Jupyter config      |
| Workspace Trust            | Workspace Settings / Command Palette             | Security for terminals, agent actions     |
| GitHub Policies            | GitHub Enterprise Admin / repo settings          | Data sharing, model access, org policies  |

Refer to these paths when configuring each aspect of Copilot, MCP, and extensions.

