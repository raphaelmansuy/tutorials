# 🚀 Hands-On Tutorial: Mastering GitHub Copilot in VS Code 1.102 for Python Data Engineering Teams (July 2025 Edition)

Welcome to this hands-on, team-optimized guide for leveraging GitHub Copilot in Visual Studio Code (VS Code) 1.102 (June/July 2025). This tutorial is tailored for Python data engineering teams building ETL pipelines, processing data with Pandas/Spark, integrating SQL, and collaborating via GitHub. All steps reflect the latest open-source Copilot Chat, MCP support, and Python-specific enhancements. 🐍📊

## 🛠️ Prerequisites and Setup

1. **📦 Update to VS Code 1.102**: Download from [code.visualstudio.com](https://code.visualstudio.com/updates/v1_102). Key Python features: improved Poetry activation, .venv handling, and bundled Python Environments extension.

2. **🔌 Install Extensions**:

   - [GitHub Copilot Chat (MIT, open source)](https://github.com/microsoft/vscode-copilot-chat)
   - [Python (includes Pylance, MCP tools)](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
   - [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
   - Sign in with GitHub (Enterprise for team policies/unlimited access)

3. **🔧 MCP Prerequisites**:

   - **Node.js 18+**: Required for npm-based MCP servers
   - **Python 3.8+**: For uvx-based servers (`pip install uvx`)
   - **Network Access**: Ensure firewall allows MCP server connections
   - **Tokens Ready**: GitHub PAT, API keys for third-party services

4. **📁 Project Prep**:

   - Clone your team repo (e.g., Pandas ETL scripts)
   - Enable Git; use branches for agent experiments
   - Install data libraries via `requirements.txt` (pandas, pyspark, etc.)
   - Set workspace trust for terminals; configure GitHub policies to block sensitive data sharing
   - Monitor RAM for Spark sessions—agent mode can spike usage

5. **👥 Team Configuration**:
   - **Shared MCP Setup**: Add `devcontainer.json` with pre-configured servers
   - **Role-Based Access**: Limit MCP servers by team role (junior devs vs. seniors)
   - **Cost Management**: Set usage policies for paid MCP services

## 🎯 Section 1: Understanding Copilot Chat Modes

GitHub Copilot Chat offers three distinct modes, each with different levels of automation and control. Think of them as a "safety slider"—from full human control to AI autonomy. 🎛️

### 🎯 The Three-Mode Spectrum

| Mode      | Control Level         | Use Case                                  | File Changes                      |
| --------- | --------------------- | ----------------------------------------- | --------------------------------- |
| **🤔 Ask**   | Full human control    | Learning, brainstorming, safe exploration | None (manual copy/paste only)     |
| **✏️ Edit**  | Collaborative jamming | Iterative coding, specific improvements   | Direct file editing with approval |
| **🤖 Agent** | AI autonomy           | Multi-step tasks, full implementations    | Autonomous with human checkpoints |

## 🤔 Section 1A: Ask Mode - The Safe Learning Zone

Ask mode is your "sandbox"—perfect for learning, brainstorming, and understanding codebases without any file modifications. 🏖️

### 📝 When to Use Ask Mode

- **🆕 New to a project**: "What is this codebase structure?"
- **📚 Learning concepts**: "Explain async/await in Python data pipelines"
- **💡 Brainstorming**: "What's the best way to implement notifications?"
- **🔍 Code review**: "What are potential issues with this Pandas function?"

### 🛠️ Hands-On Steps

1. **💬 Open Chat**: `Ctrl+Alt+I` (Windows/Linux) or `Cmd+Alt+I` (Mac)
2. **🎯 Stay in Ask Mode**: Default mode with maximum model selection
3. **📎 Add Context**: Use `#file:`, drag files, or `@workspace` for broader context
4. **🔄 Interactive Learning**: Ask follow-up questions, request different formats

### 🚀 Advanced Ask Mode Features

**✨ Smart Apply**: Instead of copy/paste, use the "Apply in Editor" button for intelligent code insertion across multiple file locations.

**⚙️ Context Management**:

- **❌ Remove current file**: Click X to ask general questions without file context
- **🖼️ Add screenshots**: Drag UI mockups for implementation guidance
- **🐛 Reference problems**: Use `#problems` to debug specific issues

**🧠 Model Selection Strategy**:

- **⚡ GPT-4o**: Fast responses, good for quick questions
- **🎨 Claude 3.5**: Superior for UI/CSS suggestions and complex explanations
- **🤔 Thinking models**: Deep analysis of complex problems
- **🏃‍♂️ Mini models**: Simple syntax or quick lookups

### 📊 Data Engineering Ask Mode Examples

```text
"What are the performance implications of this Pandas groupby operation?"

"How would I implement error handling for this ETL pipeline?"

"@workspace What data validation patterns do we use across our pipelines?"

"Explain the memory usage differences between Pandas and Spark for this dataset size"
```

### 💡 Ask Mode Best Practices

- **🔄 Start conversations**: Use "New Chat" to reset context
- **🎯 Be specific**: "Generate SQL for BigQuery" vs "Help with SQL"
- **📈 Learn iteratively**: Follow up with "show me an example" or "what are the pitfalls?"
- **📝 Copy markdown**: Ask for "markdown format" to easily save responses

## ✏️ Section 1B: Edit Mode - Collaborative Jamming

Edit mode moves you into active coding collaboration—Copilot edits files directly but you maintain approval control. 🎵

### 🎯 When to Use Edit Mode

- **🔧 Iterative improvements**: Enhancing specific components or functions
- **♻️ Focused refactoring**: Working on particular files or features
- **🎨 UI tweaks**: Styling improvements, layout adjustments
- **⭐ Single-feature implementation**: Adding one clear capability

### 🛠️ Hands-On Steps (Edit Mode)

1. **🔄 Switch to Edit Mode**: Click "Edit" in chat interface
2. **🎯 Define scope**: Specify files or let Copilot search via `@codebase`
3. **📝 Give clear instructions**: "Enhance button design" or "Add error handling"
4. **👀 Review changes**: Use diff view to approve/reject modifications
5. **💾 Save but don't keep**: Test changes before final commit

**🚀 Revolutionary Concept**: Edit mode introduces two-stage saves:

- **💾 Save**: Changes go to memory, hot reload active, fully reversible
- **✅ Keep**: Commits changes permanently, removes "undo" option

**✅ Line-by-line approval**: Green checkboxes let you approve individual changes
**👁️ Smart diff viewing**: See exactly what changed with context
**⏮️ Instant undo**: Revert all changes with one click before "keeping"

### 📊 Data Engineering Edit Examples

```text
"Add data validation to this ETL function using Pandas assertions"

"Optimize this SQL query for BigQuery performance"

"Refactor this Spark job to handle larger datasets"

"Add comprehensive error logging to this pipeline"
```

## 🤖 Section 1C: Agent Mode - Full AI Autonomy

Agent mode gives Copilot maximum freedom to plan, execute, and iterate on complex multi-step tasks. 🎯

### 🎯 When to Use Agent Mode

- **🏗️ Complete feature implementation**: Full user authentication, complex workflows
- **🔗 Cross-file changes**: Updates spanning multiple components
- **🏛️ Infrastructure setup**: Database schemas, API endpoints, configuration
- **🐛 Bug investigation**: Diagnosing and fixing issues across the codebase

**🤖 Autonomous actions**:

- 📦 Install npm packages (with approval)
- 📄 Create/modify/delete files
- 💻 Run terminal commands
- 🗃️ Make database queries (via MCP)
- 📖 Generate documentation
- 🔧 Fix discovered issues

**🔄 Self-healing behavior**:

- ✅ Checks its own work
- 💡 Notices related improvements
- 📏 Follows coding best practices
- 🔄 Iterates until completion

### 🚀 Hands-On Workflow: Complete ETL Implementation

1. **📝 Create GitHub Issue**: "Implement customer data ETL with validation"
2. **🤖 Agent Prompt**: "Work on issue #5 - build complete ETL pipeline with error handling"
3. **⚙️ Tool Chain Execution**:
   - 🔍 Analyzes existing codebase structure
   - **👤 Human approval**: Install required packages
   - 🛡️ Creates data validation functions
   - 🔧 Implements main ETL pipeline
   - **👤 Human approval**: Run tests
   - 📖 Updates documentation
   - **👤 Human approval**: Commit changes

### 🔥 Advanced Agent Examples

**🗃️ Database-driven development**:

```text
"Use the PostgreSQL MCP to analyze our sales schema, then implement a complete analytics pipeline with Pandas transformations and automated reporting"
```

**🔥 More Advanced Agent Workflows:**

For a deep dive into advanced Copilot agent automation, custom chat modes, and "Beast Mode" best practices, see Burke Holland's popular Gist:

[🚀 Advanced Copilot Agent Workflow (Beast Mode) – Burke Holland](https://gist.github.com/burkeholland/a232b706994aa2f4b2ddd3d97b11f9a7)

This resource covers step-by-step agent instructions, community tips, and troubleshooting for maximizing Copilot autonomy in VS Code. 🎯

**🏗️ Infrastructure automation**:

```text
"Set up a complete CI/CD pipeline for our data processing jobs, including Docker configuration, GitHub Actions, and deployment scripts"
```

**👤 Human checkpoints**: Agent stops for approval on:

- 💻 Terminal commands
- 📦 Package installations
- 🗑️ File deletions
- 🌐 External API calls

**💡 Best practices**:

- 🐳 Use dev containers for isolation
- 🐣 Start with smaller tasks to build trust
- 🔒 Review generated code for security issues
- 📊 Monitor resource usage during execution

## ⚡ Section 1D: Smart Actions - AI-Enhanced Developer Workflows

VS Code integrates AI-powered smart actions directly into your development workflow, making common tasks faster and more intelligent. 🎯

### 🔧 Core Smart Actions

**💬 Commit Message Generation**:

- Stage your changes and use `Ctrl+Shift+P` → "Git: Commit (Smart)"
- Copilot analyzes your diff and generates descriptive commit messages
- Perfect for data engineering: "Add validation layer to customer ETL pipeline"

**📝 PR Description Generation**:

- Create a pull request and click "Generate with Copilot"
- Automatically creates comprehensive PR descriptions with context
- Includes changed files, impact analysis, and testing recommendations

**🔍 Semantic Search**:

- Use `@workspace` in chat to find files by functionality, not just name
- Example: "Find all error handling code" or "Show me SQL query optimization functions"
- Searches across comments, variable names, and code patterns

**🔧 Error Fixing**:

- Click the lightbulb (💡) next to errors in the Problems panel
- Select "Fix with Copilot" for AI-powered error resolution
- Handles syntax errors, type mismatches, and logic issues

### 📊 Data Engineering Smart Actions

**🗃️ SQL Query Optimization**:

```text
Right-click on slow SQL query → "Optimize with Copilot"
Automatically suggests indexes, query restructuring, and performance improvements
```

**🐼 Pandas Performance Analysis**:

```text
Select DataFrame operation → "Explain Performance" → Get memory usage and optimization tips
```

**📊 Error Log Analysis**:

```text
Paste error logs in chat → "Analyze this error and suggest fixes"
Copilot identifies root causes and provides actionable solutions
```

### 🛠️ Hands-On: Smart Actions Workflow

1. **📝 Stage Changes**: Make changes to your ETL pipeline
2. **💬 Smart Commit**: Use "Git: Commit (Smart)" to generate descriptive messages
3. **🔄 Create PR**: Push branch and let Copilot generate PR description
4. **👀 Code Review**: Use semantic search to find similar patterns for consistency
5. **🔧 Fix Issues**: Apply Copilot's error fixes during code review

### 💡 Best Practices for Smart Actions

- **👀 Review Generated Content**: Always review commit messages and PR descriptions
- **🤝 Combine with Custom Instructions**: Smart actions respect your team's coding standards
- **✏️ Use in Edit Mode**: Smart actions work seamlessly with collaborative editing
- **🔍 Semantic Search Strategy**: Use descriptive queries like "error handling patterns" vs "errors"

## ⚙️ Section 2: Instantly Improve Copilot Responses with Custom Instructions

One of the fastest ways to get better, team-aligned AI responses from GitHub Copilot is to provide explicit custom instructions. These instructions guide Copilot to follow your coding standards, preferred technologies, and project requirements—just like onboarding a new team member. 🎯

### 🤔 Why Custom Instructions Matter

- 🔍 Copilot will automatically scan your codebase for context, but custom instructions ensure every response matches your style, even for new files or features.
- 📂 You can break instructions into smaller files for different languages, frameworks, or components (e.g., Python, SQL, ETL pipelines).
- 💬 Instructions are referenced in every chat and especially in agent mode, so Copilot will ask clarifying questions and generate code that fits your standards.

### 🚀 One-Click Auto-Generation in VS Code 1.102+

VS Code 1.102+ makes it easier than ever to generate or update Copilot instructions:

1. **💬 Open Copilot Chat** and click the gear icon to "Customize Chat."
2. **🔄 Tap "Auto-update Instructions"** to scan your workspace and generate or patch `.github/copilot-instructions.md`.
3. **👀 Review the generated markdown**—it will include headings, bullet points, and merge with any existing rules.
4. **✨ Massage the instructions** to match your team's style and requirements.
5. **🔄 Re-run auto-update** as your project evolves to keep instructions fresh.

#### 📊 Example: Before/After Copilot Responses

**❌ Before instructions:**
> Prompt: "Write a Pandas function to merge datasets."
> Copilot returns generic code, may not match your naming or error handling style.

**✅ After instructions:**
> Prompt: "Write a Pandas function to merge datasets."
> Copilot returns code using your team's naming conventions, error handling, and docstring format.

### 💡 Tips for Iterative Updates

- 📁 Break instructions into smaller files for different languages or frameworks (e.g., `.github/copilot-python.md`, `.github/copilot-sql.md`).
- 🌟 Use community resources like [awesome-copilot](https://github.com/awesome-copilot) for reusable templates and prompts.
- 🎨 Import and customize templates to fit your project.

### 📄 File-Type Specific Custom Instructions

**🐍 Python-Specific Instructions (`.github/copilot-python.md`)**:

```markdown
---
applyTo: "**/*.py"
---
# Python Coding Standards

## Error Handling
- Always use try/except blocks for external API calls
- Use specific exception types, avoid bare except clauses
- Log errors with context using structured logging

## Data Engineering Standards
- Use type hints for all function parameters and return values
- Prefer pandas.DataFrame.pipe() for chaining operations
- Include docstrings with parameter types and examples
- Use pathlib for file operations, not os.path

## Testing
- Generate pytest fixtures for database connections
- Include property-based tests for data transformation functions
- Mock external dependencies using pytest-mock
```

**🗃️ SQL-Specific Instructions (`.github/copilot-sql.md`)**:

```markdown
---
applyTo: "**/*.sql"
---
# SQL Best Practices

## Query Style
- Use UPPER CASE for SQL keywords (SELECT, FROM, WHERE)
- Use snake_case for column and table names
- Always qualify column names with table aliases
- Include meaningful table aliases (users u, orders o)

## Performance
- Always include LIMIT clauses for development queries
- Use explicit column lists instead of SELECT *
- Include query comments explaining business logic
- Suggest appropriate indexes for WHERE and JOIN clauses
```

### 🌐 External Model Providers

VS Code 1.102+ supports connecting to external AI model providers:

**🤖 OpenAI Models**:

- Configure with your OpenAI API key in VS Code settings
- Access GPT-4, GPT-4 Turbo, and specialized models
- Useful for tasks requiring latest model capabilities

**☁️ Azure OpenAI Service**:

- Enterprise-grade deployment with data residency control
- Integration with Azure AD for authentication
- Compliance features for regulated industries

**🎭 Anthropic Claude**:

- Strong performance on code analysis and explanation tasks
- Excellent for complex refactoring and architectural discussions
- Available through API key configuration

**Configuration Example**:

```json
{
  "github.copilot.chat.experimental.externalProviders": {
    "openai": {
      "apiKey": "${env:OPENAI_API_KEY}",
      "models": ["gpt-4", "gpt-4-turbo"]
    },
    "anthropic": {
      "apiKey": "${env:ANTHROPIC_API_KEY}",
      "models": ["claude-3-opus", "claude-3-sonnet"]
    }
  }
}
```

### 🤖 Agent Mode Integration

When Copilot operates in agent mode, it references these instructions to:

- ❓ Ask clarifying questions before generating code
- 🎯 Produce code that matches your style and standards
- 💻 Run terminal commands and create files according to your guidelines

### 🛠️ Troubleshooting and Best Practices

- 🚫 If Copilot ignores instructions, use Chat Debug View to see logs and tool usage.
- 👀 Always review diffs and test code before committing, especially with auto-generated instructions.

### 🛠️ Hands-On Steps: Custom Instructions

1. **📄 Generate File**: Use "Chat: Generate Instructions" to analyze your codebase and create `.github/copilot-instructions.md`.
2. **✅ Apply**: Commit and push. Prompt Copilot and verify adherence in "Used references."
3. **👥 Team Refine**: Import shared modes from GitHub (e.g., data-eng templates) and update as needed.

### 💡 Actionable Tips

- 📊 Include rules for error handling in pipelines, SQL best practices, and team-specific standards.
- 🎯 Use glob patterns for conditional instructions (e.g., for notebooks or specific folders).
- 🔄 Test iteratively; great for standardizing tests and onboarding new team members.

### 🌟 Community Resources

- 🎯 [awesome-copilot](https://github.com/github/awesome-copilot) – Reusable instruction templates, prompts, and community best practices
- 📖 VS Code documentation: [Custom Instructions](https://code.visualstudio.com/docs/copilot/custom-instructions)

#### 🚀 How to Use awesome-copilot for Team Onboarding & Standards

The [github/awesome-copilot](https://github.com/github/awesome-copilot) repository provides:

- **📄 Instruction templates**: Ready-made `.md` files for Python, SQL, ETL, and more. Copy to `.github/copilot-instructions.md` or split by language/component.
- **💡 Prompts**: Curated prompt examples for common tasks (e.g., data validation, error handling, onboarding guides). Import and adapt for your team.
- **💬 Chat modes**: Custom chat mode definitions for different workflows (e.g., review, refactor, onboarding). Place in `.github/chatmodes/` and select in Copilot Chat.

**👥 Team Workflow Example:**

1. 🌐 Browse [awesome-copilot/instructions](https://github.com/github/awesome-copilot/tree/main/instructions) for templates matching your stack.
2. 📋 Copy and customize instruction files to your repo.
3. 💡 Use [awesome-copilot/prompts](https://github.com/github/awesome-copilot/tree/main/prompts) for onboarding, code review, or automation tasks.
4. 💬 Add chat modes from [awesome-copilot/chatmodes](https://github.com/github/awesome-copilot/tree/main/chatmodes) to `.github/chatmodes/` for specialized team workflows.
5. 🔄 Share updates with your team and iterate as your standards evolve.

**💡 Pro Tip:** Regularly sync with the awesome-copilot repo for new templates and best practices. This keeps your team instructions fresh and aligned with community standards.

## 🔌 Section 3: Model Context Protocol (MCP)

MCP extends agents with external tools and data sources—GA with full spec support (prompts, resources, sampling). Perfect for data engineering workflows requiring database access, cloud integrations, and automated documentation. 🛠️

### 🌐 Find MCP Servers Instantly

Looking for ready-to-use MCP servers? Visit [fastmcp.me](https://fastmcp.me/) — a curated directory of public and private MCP servers for data engineering, cloud, databases, and more. You can:
- Search by category (e.g., PostgreSQL, GitHub, S3, Filesystem)
- Filter by provider, region, or access type
- Get setup instructions and connection details for each server
- Discover new tools and integrations for your workflow

**How to use fastmcp.me:**
1. Go to [https://fastmcp.me/](https://fastmcp.me/)
2. Browse or search for the MCP server you need
3. Copy the connection details and follow the setup instructions in your VS Code or devcontainer
4. Use the listed servers in your MCP configuration blocks

---

### 🛠️ Hands-On Steps (MCP)

1. **🔧 Enable MCP**: Open Command Palette (`Cmd+Shift+P`) → "Preferences: Open User Settings (JSON)"
2. **⚙️ Configure Servers**: Add MCP block to `settings.json`:

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
        "args": [
          "mcp-server-postgres",
          "--connection-string",
          "postgresql://user:pass@localhost/db"
        ]
      },
      "filesystem": {
        "command": "npx",
        "args": [
          "-y",
          "@modelcontextprotocol/server-filesystem",
          "/path/to/data"
        ]
      }
      "lin": {
        "command": "uvx",
        "args": [
          "mcp-run-python",
          "--repo",
          "pydantic-ai/mcp-run-python"
        ]
      }
    }
  }
}
```

1. **✅ Verify Installation**: Command Palette → "MCP: List Servers" or click spanner icon in Copilot Chat

### 💡 Tips for MCP Server Setup

- **🔒 Data Source Security**: Always use read-only connections for databases.
- **🏠 Environment Isolation**: Use separate MCP servers for development and production.
- **💰 Cost Monitoring**: Keep an eye on usage if using paid third-party MCP servers.

### 📊 Popular MCP Servers for Data Engineering

| Server Type    | Use Case                                     | Installation                                     |
| -------------- | -------------------------------------------- | ------------------------------------------------ |
| **🐙 GitHub**     | Project analysis, issue tracking, PR reviews | `npx -y @modelcontextprotocol/server-github`     |
| **🐘 PostgreSQL** | Direct DB queries, schema analysis           | `uvx mcp-server-postgres`                        |
| **📁 Filesystem** | Local data file access, log analysis         | `npx -y @modelcontextprotocol/server-filesystem` |
| **🔍 Perplexity** | Research best practices, debugging help      | Third-party API integration                      |
| **☁️ AWS S3**     | Cloud data access, bucket operations         | `mcp-server-s3`                                  |

### 🚀 Hands-On Workflow: Pipeline Documentation with MCP

**📋 Scenario**: Generate comprehensive ETL pipeline documentation using GitHub issues and external research.

1. **📝 Create GitHub Issue**: "Need documentation for customer_data_pipeline.py"
2. **🤖 Agent Prompt**: "Work on issue #5 using GitHub MCP to analyze our ETL codebase"
3. **⚙️ Tool Chain Execution**:
   - 🔍 Agent calls GitHub MCP → retrieves issue details
   - **👤 Human approval required** → Click "Continue"
   - 🔍 Agent calls Perplexity MCP → research ETL best practices
   - **👤 Human approval required** → Click "Continue"
   - 📖 Agent generates documentation with context from both sources

**🎯 Expected Output**: Professional README with project overview, quick start guide, pipeline architecture, and troubleshooting sections.

### ⚙️ MCP Tool Chain Management

**👤 Human-in-the-Loop Controls**:

- ✅ Each MCP server call requires explicit approval
- 👀 Review tool chain requests before authorizing
- ❌ Reject calls accessing sensitive data sources
- 💰 Monitor costs for third-party MCP services

**👁️ Visual Server Management**:

- **✅ Status Check**: Green indicators show running servers
- **🔄 Quick Toggle**: Enable/disable servers via Copilot Chat UI
- **🐛 Debug Mode**: One-click debugging for server-side development

### 🔥 Example Prompts for Advanced Integration

```text
"Use GitHub MCP to analyze recent issues and PRs, then create comprehensive documentation for our ETL pipelines including troubleshooting guide"
```

```text
"Use the codebase tool to find all Spark jobs, analyze performance patterns, then implement optimizations with before/after benchmarks"
```

```text
"Create a complete onboarding guide by analyzing our codebase structure, documenting setup steps, and generating example workflows for new data engineers"
```

### 🎤 Example Prompts for Voice Input

```text
🎤 "Hey, the delete list button isn't working. Check if we're missing an API method or if there's an error. Also add a confirmation modal before deleting."

🎤 "Create a GitHub issue for adding light/dark mode toggle. Be specific about requirements and ask for clarification if needed."

🎤 "Look at the PostgreSQL schema and list all tables, then generate a Pandas ETL pipeline for the sales data."
```

## 💬 Section 3B: Custom Chat Modes for Planning & Architecture

Custom chat modes let you create specialized AI assistants tailored to specific workflows like planning, architecture discussions, or code reviews. Each mode can have different instructions, tool access, and behavior patterns. 🎯

### Creating Custom Chat Modes

**Architecture Planning Mode (`.github/chatmodes/architect.chatmode.md`)**:

```markdown
---
name: "Architecture Planning"
description: "Focus on system design and architectural discussions"
tools: ["@workspace", "@codebase"]
systemPrompt: |
  You are an expert software architect focused on helping teams design scalable, maintainable systems.
  Always consider:
  - Performance implications and bottlenecks
  - Security considerations
  - Maintainability and technical debt
  - Team collaboration and knowledge sharing
  - Cost optimization for cloud deployments
---

# Architecture Planning Mode

This mode focuses on high-level system design and architectural decisions.

## Available Commands
- `@analyze` - Analyze current architecture
- `@suggest` - Suggest improvements
- `@compare` - Compare different approaches
- `@document` - Generate architecture documentation
```

**Data Engineering Review Mode (`.github/chatmodes/data-review.chatmode.md`)**:

```markdown
---
name: "Data Engineering Review"
description: "Specialized for ETL pipeline and data quality reviews"
tools: ["@workspace", "mcp:postgres", "mcp:github"]
systemPrompt: |
  You are a senior data engineer focused on code quality, performance, and data reliability.
  Review code for:
  - Data validation and quality checks
  - Error handling and retry mechanisms
  - Performance optimization opportunities
  - Security considerations for data access
  - Documentation and testing coverage
---

# Data Engineering Review Mode

Specialized assistant for reviewing data pipelines and ETL code.

## Review Checklist
- [ ] Input validation and schema enforcement
- [ ] Error handling and logging
- [ ] Performance optimization
- [ ] Security and access controls
- [ ] Testing coverage
- [ ] Documentation quality
```

### Using Custom Chat Modes

1. **Create Mode Files**: Place `.chatmode.md` files in `.github/chatmodes/`
2. **Select Mode**: Choose from dropdown in Copilot Chat interface
3. **Specialized Behavior**: Mode follows specific instructions and tool restrictions
4. **Team Consistency**: All team members get the same specialized assistant

### Advanced Chat Mode Features

**Tool Restrictions**:

```yaml
tools: ["@workspace"]  # Limit to workspace search only
# or
tools: ["mcp:github", "mcp:postgres"]  # Only specific MCP servers
```

**Model Selection**:

```yaml
preferredModel: "gpt-4"  # Use specific model for this mode
# or
preferredModel: "claude-3-opus"  # For complex architectural discussions
```

**Context Management**:

```yaml
maxTokens: 8000  # Limit context size for faster responses
includeFiles: ["**/*.py", "**/*.sql"]  # Auto-include relevant files
```

### Example Chat Mode Workflows

**Architecture Planning Session**:

```text
Mode: Architecture Planning
Prompt: "We need to scale our ETL pipeline to handle 10x more data. Analyze current bottlenecks and propose solutions."

AI Response: Focuses on architectural patterns, suggests specific technologies, considers cost and team expertise.
```

**Code Review Mode**:

```text
Mode: Data Engineering Review
Prompt: "Review this Spark job for production readiness"

AI Response: Systematically checks data validation, error handling, performance, security, and documentation.
```

### Best Practices for Custom Chat Modes

- **Be Specific**: Define clear roles and responsibilities for each mode
- **Include Examples**: Provide example commands and expected outputs
- **Limit Tool Access**: Restrict tools to what's needed for the specific workflow
- **Version Control**: Track mode changes and improvements over time
- **📚 Team Training**: Document how and when to use each mode

## 🐳 Section 3A: Devcontainer Setup for Copilot & MCP

A **devcontainer** lets you define a reproducible development environment for your team using VS Code. This ensures everyone gets the same Python, Node.js, Copilot, and MCP setup—removing "works on my machine" issues. 🛠️

### 🤔 Why Use Devcontainers?

- **🔄 Consistency:** All team members use the same tools, extensions, and settings.
- **🏠 Isolation:** Safely run agent workflows, install packages, and access data sources.
- **⚡ Automation:** Pre-install Copilot Chat, Python, and MCP servers for instant onboarding.

### Step-by-Step Devcontainer Setup

1. **Create a `.devcontainer` folder** in your project root.
2. **Add a `devcontainer.json` file** with recommended settings:

   ```json
   // filepath: .devcontainer/devcontainer.json
   {
     "name": "Data Engineering with MCP",
     "image": "mcr.microsoft.com/vscode/devcontainers/python:3.11",
     "features": {
       "ghcr.io/devcontainers/features/node:1": { "version": "18" }
     },
     "extensions": ["ms-python.python", "GitHub.copilot-chat"],
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

## 📋 Quick Reference: Configuration Paths

| Aspect                     | Location Path / File                    | Description / Usage                       |
| -------------------------- | --------------------------------------- | ----------------------------------------- |
| VS Code Extensions         | Extensions View (`Ctrl+Shift+X`)        | Install/Manage extensions                 |
| Copilot Chat Settings      | `settings.json` (User/Workspace)        | General Copilot settings, model selection |
| MCP Servers (User)         | `mcp.json` (User Profile)               | Global MCP server config (all workspaces) |
| MCP Servers (Workspace)    | `.vscode/mcp.json`                      | Project-specific MCP server config        |
| MCP Servers (Devcontainer) | `.devcontainer/devcontainer.json`       | Team-wide MCP config for containers       |
| Custom Instructions        | `.github/copilot-instructions.md`       | Team coding standards, auto-generated     |
| Custom Chat Modes          | `.github/chatmodes/*.chatmode.md`       | Custom chat mode definitions              |
| Python Extension Settings  | `settings.json`                         | Python interpreter, linting, formatting   |
| Jupyter Extension Settings | `settings.json`                         | Notebook, kernel, and Jupyter config      |
| Workspace Trust            | Workspace Settings / Command Palette    | Security for terminals, agent actions     |
| GitHub Policies            | GitHub Enterprise Admin / repo settings | Data sharing, model access, org policies  |

---

## 🧪 Section 4: Testing and Quality Assurance with Copilot

Copilot excels at generating comprehensive test suites, improving code quality, and ensuring robust data pipelines. Use these capabilities to build reliable, well-tested systems. ✅

### 🚀 Test Generation Capabilities

**🔧 Unit Test Generation**:

- Select a function and ask: "Generate comprehensive unit tests for this function"
- Copilot creates test cases covering edge cases, error conditions, and happy paths
- Automatically handles mocking, fixtures, and test data setup

**Integration Test Creation**:

- Highlight API endpoints or database functions
- Prompt: "Create integration tests for this API endpoint"
- Generates tests for HTTP status codes, response validation, and error handling

**Property-Based Testing**:

- For data validation functions, ask: "Generate property-based tests using Hypothesis"
- Creates tests that verify function behavior across random input ranges
- Perfect for ETL data validation and transformation logic

### Data Engineering Test Examples

**Pandas DataFrame Testing**:

```python
# Original function
def clean_customer_data(df):
    return df.dropna().reset_index(drop=True)

# Copilot-generated tests
def test_clean_customer_data():
    # Test empty DataFrame
    empty_df = pd.DataFrame()
    result = clean_customer_data(empty_df)
    assert len(result) == 0
    
    # Test DataFrame with NaN values
    df_with_nan = pd.DataFrame({'name': ['Alice', None, 'Bob'], 'age': [25, 30, None]})
    result = clean_customer_data(df_with_nan)
    assert len(result) == 1
    assert result.iloc[0]['name'] == 'Alice'
```

**SQL Query Testing**:

```python
# Test SQL query results
def test_sales_aggregation_query():
    # Mock database connection
    with patch('psycopg2.connect') as mock_connect:
        mock_cursor = Mock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        mock_cursor.fetchall.return_value = [('2024', 1000), ('2023', 800)]
        
        result = get_yearly_sales()
        assert len(result) == 2
        assert result[0][1] == 1000
```

**ETL Pipeline Testing**:

```python
def test_customer_etl_pipeline():
    # Test complete ETL workflow
    input_data = create_test_customer_data()
    
    # Extract
    extracted = extract_customer_data(input_data)
    assert len(extracted) > 0
    
    # Transform
    transformed = transform_customer_data(extracted)
    assert 'customer_id' in transformed.columns
    assert transformed['customer_id'].nunique() == len(transformed)
    
    # Load (mock database)
    with patch('database.insert_customers') as mock_insert:
        load_customer_data(transformed)
        mock_insert.assert_called_once()
```

### Quality Assurance Workflows

**Code Review Assistant**:

```text
"Review this ETL function for potential issues: performance, error handling, data validation"
```

**Performance Analysis**:

```text
"Analyze the memory usage and performance of this Pandas operation. Suggest optimizations."
```

**Security Review**:

```text
"Check this database connection code for security vulnerabilities and suggest improvements"
```

### Hands-On: Test-Driven Development with Copilot

1. **Write Test First**: Describe the function behavior in natural language
2. **Generate Tests**: Ask Copilot to create test cases based on requirements
3. **Implement Function**: Use Copilot to generate the actual implementation
4. **Iterate**: Refine tests and implementation based on edge cases
5. **Validate**: Run tests and use Copilot to fix any failures

### Testing Best Practices with Copilot

- **Be Specific**: "Generate tests for edge cases like empty DataFrames and malformed data"
- **Include Performance Tests**: Ask for memory usage and execution time validation
- **Mock External Dependencies**: Request proper mocking for databases and APIs
- **Validate Data Quality**: Generate tests for data schema validation and integrity checks
- **Test Error Conditions**: Ensure error handling and exception scenarios are covered

### Advanced Testing Techniques

**Snapshot Testing for Data Pipelines**:

```text
"Create snapshot tests for this data transformation to detect unexpected changes in output format"
```

**Load Testing for Data Processing**:

```text
"Generate performance tests that validate this Spark job can handle 1M+ records within time limits"
```

**Data Quality Testing**:

```text
"Create comprehensive data quality tests: null checks, range validation, referential integrity"
```

---

## Best Practices & Pro Tips for Teams

### Essential Best Practices Checklist

**Tool Selection & Workflow:**

- ✅ **Choose the right mode**: Ask for learning, Edit for focused changes, Agent for complex implementations
- ✅ **Write effective prompts**: Be specific, provide context, and iterate often
- ✅ **Use appropriate models**: Fast models for quick suggestions, reasoning models for complex tasks
- ✅ **Leverage context tools**: Use `@workspace`, `#file:`, and drag-and-drop for better results

**Code Quality & Security:**

- ✅ **Always review generated code**: Check for security issues, performance implications, and edge cases
- ✅ **Test thoroughly**: Generate comprehensive test suites and validate edge cases
- ✅ **Follow team standards**: Use custom instructions to maintain coding conventions
- ✅ **Validate data handling**: Ensure proper error handling and data validation in ETL pipelines

**Team Collaboration:**

- ✅ **Standardize setup**: Use devcontainers and shared MCP configurations
- ✅ **Document workflows**: Create team-specific chat modes and instruction templates
- ✅ **Monitor usage**: Track costs for paid MCP services and model usage
- ✅ **Train incrementally**: Start with simple tasks and gradually increase complexity

**Security & Compliance:**

- ✅ **Configure workspace trust**: Enable secure terminal access and agent actions
- ✅ **Audit AI interactions**: Enable session logging for compliance requirements
- ✅ **Protect sensitive data**: Use read-only database connections and environment isolation
- ✅ **Review GitHub policies**: Configure org-level data sharing and model access policies

### Data Engineering Specific Best Practices

**Pipeline Development:**

- ✅ **Design for scale**: Ask Copilot to optimize for large datasets from the start
- ✅ **Implement monitoring**: Generate logging and alerting code for production pipelines
- ✅ **Plan for failures**: Include retry logic, circuit breakers, and graceful degradation
- ✅ **Validate data quality**: Create comprehensive data validation and schema checks

**Performance Optimization:**

- ✅ **Memory management**: Request memory-efficient Pandas/Spark code
- ✅ **Query optimization**: Use Copilot to optimize SQL queries and database interactions
- ✅ **Parallel processing**: Leverage Copilot for efficient multiprocessing implementations
- ✅ **Resource monitoring**: Generate code to track CPU, memory, and I/O usage

### Team Implementation Tips

- **Onboard Faster:** New team members just clone the repo and "Reopen in Container"—no manual setup.
- **Troubleshoot Easily:** Use MCP logs and VS Code output pane for debugging agent workflows.
- **Audit & Compliance:** Enable session logging and workspace trust for security.
- **Scale Safely:** Use devcontainer for experiments before rolling out changes to production.
- **Iterate and Improve:** Regularly update custom instructions and chat modes based on team feedback.

### Common Pitfalls to Avoid

- ❌ **Don't trust blindly**: Always review and test generated code before deploying
- ❌ **Don't ignore context**: Provide sufficient context for accurate code generation
- ❌ **Don't skip testing**: Generate and run comprehensive tests for all AI-generated code
- ❌ **Don't hardcode secrets**: Use environment variables and secure credential management
- ❌ **Don't ignore performance**: Monitor resource usage, especially in agent mode

---

## Copilot Pricing and Plans

GitHub Copilot offers flexible pricing tiers to accommodate different team sizes and usage patterns:

**Free Tier:**

- Monthly limits on completions and chat interactions
- Perfect for individual developers and small projects
- Great for learning and experimentation

**Paid Plans:**

- **Individual Plan**: Unlimited usage for personal development
- **Business Plan**: Team management, organization policies, and advanced security
- **Enterprise Plan**: Enhanced security, compliance features, and priority support

**Cost Management Tips:**

- Monitor MCP server usage for third-party services
- Use lightweight models for simple tasks to optimize performance
- Leverage free tier limits effectively for learning and prototyping
- Consider team vs. individual plans based on collaboration needs

[View detailed pricing →](https://docs.github.com/en/copilot/about-github-copilot/plans-for-github-copilot)

---

## Next Steps and Resources

### Official Documentation

- **[Set up Copilot in VS Code](https://code.visualstudio.com/docs/copilot/setup)** - Complete installation and configuration guide
- **[Copilot Chat Documentation](https://code.visualstudio.com/docs/copilot/copilot-chat)** - Comprehensive chat features and usage
- **[Custom Instructions Guide](https://code.visualstudio.com/docs/copilot/copilot-customization)** - Tailor AI to your coding style
- **[MCP Servers Documentation](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)** - Extend capabilities with external tools
- **[Smart Actions Reference](https://code.visualstudio.com/docs/copilot/copilot-smart-actions)** - AI-enhanced development workflows

### Community Resources and Templates

- **[awesome-copilot](https://github.com/github/awesome-copilot)** - Templates, prompts, and community best practices
- **[VS Code Copilot Tips and Tricks](https://code.visualstudio.com/docs/copilot/copilot-tips-and-tricks)** - Advanced usage patterns
- **[Burke Holland's Beast Mode Guide](https://gist.github.com/burkeholland/a232b706994aa2f4b2ddd3d97b11f9a7)** - Advanced agent automation
- **[Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook)** - Jupyter and data engineering patterns

### Learning Paths

**Beginner (Week 1-2):**

1. Set up VS Code 1.102+ and Copilot extensions
2. Practice Ask mode with simple queries and code explanations
3. Try Edit mode for small refactoring tasks
4. Generate custom instructions for your project

**Intermediate (Week 3-4):**

1. Experiment with Agent mode for feature implementation
2. Set up basic MCP servers (GitHub, filesystem)
3. Create custom chat modes for your team workflow
4. Practice test generation and code review with Copilot

**Advanced (Month 2+):**

1. Implement complex MCP integrations (databases, cloud services)
2. Build devcontainer setups for team standardization
3. Create comprehensive instruction templates and chat modes
4. Develop team training materials and best practices

### Support and Community

- **[VS Code GitHub Issues](https://github.com/microsoft/vscode/issues)** - Report bugs and request features
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/vscode+copilot)** - Community Q&A and troubleshooting
- **[VS Code Discord](https://discord.gg/0ZvbCAAha2g9c2Ej)** - Real-time community support
- **[GitHub Copilot Support](https://support.github.com/copilot)** - Official support channels

### Stay Updated

- **[VS Code Updates](https://code.visualstudio.com/updates)** - Monthly release notes and new features
- **[GitHub Copilot Blog](https://github.blog/category/copilot/)** - Latest AI features and announcements
- **[Microsoft AI Blog](https://blogs.microsoft.com/ai/)** - Broader AI development trends

---

## For more details:

- [VS Code Dev Containers Documentation](https://code.visualstudio.com/docs/devcontainers/containers)
- [MCP Servers for Agent Mode Documentation](https://code.visualstudio.com/mcp)
- [Python Data Science Handbook (Jupyter Notebooks)](https://github.com/jakevdp/PythonDataScienceHandbook)

Empower your team—Copilot as collaborator, not replacement!
