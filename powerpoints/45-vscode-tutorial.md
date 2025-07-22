---
marp: true
theme: default
paginate: true
header: "VS Code Copilot Mastery - July 2025"
footer: "© Data Engineering Team"
style: |
  section {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }
  .lead {
    text-align: center;
    font-size: 1.5em;
  }
  .ask-mode {
    background: linear-gradient(135deg, #e3f2fd, #bbdefb);
  }
  .edit-mode {
    background: linear-gradient(135deg, #f3e5f5, #e1bee7);
  }
  .agent-mode {
    background: linear-gradient(135deg, #e8f5e8, #c8e6c9);
  }
  .tech-section {
    background: linear-gradient(135deg, #fff3e0, #ffcc02);
  }
  .code-highlight {
    background-color: #f8f8f8;
    border-left: 4px solid #2196f3;
    padding: 10px;
    margin: 10px 0;
  }
---

<!-- _class: lead -->

# 🚀 Mastering GitHub Copilot in VS Code 1.102

## for Python Data Engineering Teams

### July 2025 Edition

By  **Raphaël MANSUY**

**Transform your development workflow with AI-powered collaboration**

---

# 🎯 The Challenge We Face

![bg right:40%](https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800)

## Current Pain Points

- **Manual coding bottlenecks** slow down delivery
- **Inconsistent code quality** across team members
- **Knowledge silos** prevent effective collaboration
- **Complex ETL pipelines** require deep expertise
- **Documentation gaps** impact maintainability

---

# ✨ The Solution: Copilot as Your AI Partner

![bg left:40%](https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=800)

## AI-Powered Development

- **Collaborative AI assistant** integrated in VS Code
- **Three progressive modes** for different use cases
- **Context-aware suggestions** for data engineering
- **Team standardization** through custom instructions
- **External tool integration** via MCP

---

# 📚 What You'll Learn Today

## Learning Journey (45-60 minutes)

- **Understanding the three Copilot modes**
- **Hands-on demonstrations** with real data pipelines
  - Ask Mode: Safe exploration and learning
  - Edit Mode: Collaborative code improvement
  - Agent Mode: Autonomous task completion
- **Advanced features**: Custom instructions & MCP
- **Team implementation** strategies and best practices
- **Actionable roadmap** for immediate adoption

---

# ✅ Prerequisites Checklist

![bg right:30%](https://images.unsplash.com/photo-1611224923853-80b023f02d71?w=400)

## Essential Setup

- [x] **VS Code 1.102+** (June/July 2025 release)
- [x] **GitHub Copilot subscription** (Individual/Team/Enterprise)
- [x] **Python extension** with environment support
- [x] **GitHub account** with proper permissions
- [x] **Team policies** configured (if enterprise)

## Optional but Recommended

- [x] **Devcontainer** environment
- [x] **MCP servers** for database/cloud access

---

# 🧠 Available AI Models (July 2025)

| Model                 | Type     | Strengths & Use Cases                  |
| --------------------- | -------- | -------------------------------------- |
| **GPT-4.1**           | Standard | Fast, reliable, general coding and Q&A |
| **GPT-4o**            | Standard | Fastest, quick tasks and brainstorming |
| **Claude Sonnet 3.5** | Premium  | UI/CSS, code explanations              |
| **Claude Sonnet 3.7** | Premium  | Improved reasoning, code review        |
| **Claude Sonnet 4**   | Premium  | Deep analysis, complex workflows       |
| **Gemini 2.5 Pro**    | Premium  | Data analysis, Python, advanced ML     |
| **o4-mini**           | Premium  | Lightweight, fast syntax checks        |

---

<!-- _class: lead -->

# 🎛️ The Three-Mode Spectrum

## From Human Control → AI Autonomy

![bg](https://images.unsplash.com/photo-1518709268805-4e9042af2176?w=1200)

### 🤔 Ask Mode → ✏️ Edit Mode → 🤖 Agent Mode

---

# 🎯 Demo Environment Preview

![bg left:50%](https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=800)

## What We'll Build Together

- **Databricks notebook** with Delta Lake optimization
- **dbt models** with incremental materializations
- **Data quality tests** across both platforms
- **Automated documentation** and lineage
- **Team standardization** for modern data stack

_Get ready for real data engineering workflows!_

---

<!-- _class: ask-mode -->

# 🤔 Ask Mode: The Safe Learning Zone

![bg right:30%](https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400)

## Your AI Sandbox 🏖️

- **Zero file modifications** - completely safe
- **Learning and exploration** without risk
- **Brainstorming and ideation** support
- **Code review and analysis** capabilities
- **Context-aware Q&A** for your codebase

---

<!-- _class: ask-mode -->

# 🎯 When to Use Ask Mode

![bg right:40%](https://images.unsplash.com/photo-1434494878577-86c23bcb06b9?w=600)

## Four Key Scenarios

- **🆕 New to a project**: "What is this codebase structure?"
- **📚 Learning concepts**: "Explain async/await in Python pipelines"
- **💡 Brainstorming**: "Best approach for real-time notifications?"
- **🔍 Code review**: "Potential issues with this Pandas function?"

---

<!-- _class: ask-mode -->

# 🔴 Live Demo: Ask Mode in Action

<!-- Live Demo -->

![bg left:45%](https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=700)

## Demo Scenario

**Optimizing a dbt incremental model processing 10TB daily**

```sql
-- Current inefficient dbt model needing optimization
{{ config(materialized='table') }}

SELECT
    customer_id,
    DATE(transaction_timestamp) as transaction_date,
    SUM(amount) as daily_revenue,
    COUNT(*) as transaction_count
FROM {{ source('raw', 'transactions') }}
WHERE DATE(transaction_timestamp) = CURRENT_DATE()
GROUP BY customer_id, DATE(transaction_timestamp)
```

**Ask Copilot**: _"How can I convert this to an efficient incremental model that processes only new data and handles late-arriving records?"_

---

<!-- _class: ask-mode -->

# ⚡ Advanced Ask Mode Features

## Smart Apply Button ✨

- **Intelligent code insertion** across multiple files
- **Context-aware placement** without copy/paste
- **Maintains code structure** and formatting

## Context Management 🎯

- **Remove current file**: General questions without file context
- **Add screenshots**: UI mockups for implementation
- **Reference problems**: Use `#problems` for debugging

---

<!-- _class: ask-mode -->

# 🧠 Model Selection Strategy

![bg right:35%](https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=500)

## Decision Tree

- **GPT-4o**: Speed → Quick questions, brainstorming
- **Claude Sonnet 4**: Complexity → Architecture, refactoring
- **Gemini 2.5 Pro**: Data focus → ML, analytics, Python
- **o4-mini**: Simple tasks → Syntax checks, quick fixes

**Pro Tip**: Switch models based on task complexity!

---

<!-- _class: ask-mode -->

# 📊 Data Engineering Ask Examples

```text
"How can I optimize this Delta Lake merge operation for 1TB daily updates?"

"What's the best dbt incremental strategy for handling late-arriving facts?"

"@workspace Analyze our medallion architecture and suggest improvements"

"Help me troubleshoot this Databricks cluster auto-scaling configuration"

"Review our dbt data quality tests and suggest additional coverage"

"How can I implement proper SCD Type 2 in this dimension table?"

"What's the most cost-effective partition strategy for this time-series data?"
```

## Key Benefits

- **Learn best practices** from industry patterns
- **Optimize costs** with smarter data strategies
- **Debug faster** with expert troubleshooting
- **Scale efficiently** with proven architectures

---

<!-- _class: ask-mode -->

# 💡 Ask Mode Best Practices

![bg left:30%](https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=400)

## Maximize Your Learning

- ✅ **Start conversations fresh** with "New Chat"
- ✅ **Be specific**: "Generate BigQuery SQL" vs "Help with SQL"
- ✅ **Learn iteratively**: Follow up with examples and pitfalls
- ✅ **Copy in markdown**: Ask for formatted responses
- ✅ **Use context tools**: `@workspace`, `#file:`, drag-and-drop

---

<!-- _class: edit-mode -->

# ✏️ Edit Mode: Collaborative Jamming

![bg right:30%](https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?w=400)

## Your AI Pair Programmer 🎵

- **Direct file editing** with approval control
- **Iterative improvements** and refinements
- **Revolutionary two-stage saves** for safety
- **Line-by-line approval** system
- **Intelligent diff viewing** with context

---

<!-- _class: edit-mode -->

# 🎯 When to Use Edit Mode

![bg left:40%](https://images.unsplash.com/photo-1552664730-d307ca884978?w=600)

## Perfect Scenarios

- **🔧 Iterative improvements**: Enhancing functions or components
- **♻️ Focused refactoring**: Working on specific files
- **🎨 UI tweaks**: Styling and layout adjustments
- **⭐ Single-feature implementation**: Adding clear capabilities

**Transition from Ask**: When you're ready to make changes!

---

<!-- _class: edit-mode -->

# 🔴 Live Demo: Edit Mode Workflow

<!-- Live Demo -->

![bg right:45%](https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=700)

## Demo: Enhancing dbt Model

```sql
-- Before: Basic dbt model
{{ config(materialized='table') }}

SELECT
    customer_id,
    SUM(order_amount) as total_spent
FROM {{ ref('raw_orders') }}
GROUP BY customer_id

-- After: Enhanced with incremental processing
{{ config(
    materialized='incremental',
    unique_key='customer_id',
    on_schema_change='append_new_columns'
) }}

SELECT
    customer_id,
    SUM(order_amount) as total_spent,
    COUNT(*) as order_count,
    MAX(order_date) as last_order_date
FROM {{ ref('raw_orders') }}
{% if is_incremental() %}
    WHERE order_date > (SELECT MAX(last_order_date) FROM {{ this }})
{% endif %}
GROUP BY customer_id
```

---

<!-- _class: edit-mode -->

# 🚀 Revolutionary Two-Stage Saves

![bg left:35%](https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=500)

## Safety First! 🛡️

### Stage 1: **Save**

- Changes go to **memory**
- **Hot reload** active
- **Fully reversible**

### Stage 2: **Keep**

- **Commits permanently**
- Removes undo option
- **Final confirmation**

---

<!-- _class: edit-mode -->

# ✅ Line-by-Line Approval System

## Quality Control at Every Step

- **Green checkboxes** for individual line approval
- **Smart diff viewing** with context highlighting
- **Instant undo** before committing changes
- **Granular control** over what gets applied

## Benefits for Teams

- **Code review integration** built-in
- **Learning opportunities** from AI suggestions
- **Quality assurance** without manual overhead

---

<!-- _class: edit-mode -->

# 📊 Data Engineering Edit Examples

```text
"Convert this dbt table materialization to incremental with merge strategy"

"Add dbt test coverage for data quality: uniqueness, not_null, and freshness"

"Optimize this PySpark DataFrame operation to reduce shuffle and cache smartly"

"Refactor this Databricks notebook to follow medallion architecture patterns"

"Add comprehensive error handling with structured logging to this data pipeline"

"Convert these hard-coded SQL queries to parameterized dbt models"
```

## Real-World Improvements

- **Scale efficiently** from prototype to production workloads
- **Maintain quality** with automated testing and validation
- **Reduce costs** through performance optimization
- **Standardize patterns** across data engineering teams

---

<!-- _class: edit-mode -->

# 💡 Edit Mode Best Practices

![bg right:30%](https://images.unsplash.com/photo-1434494878577-86c23bcb06b9?w=400)

## Team Integration

- ✅ **Review diffs carefully** before keeping changes
- ✅ **Test changes immediately** with hot reload
- ✅ **Use version control** for backup safety
- ✅ **Communicate with team** about AI-assisted changes
- ✅ **Document decisions** for future reference

---

<!-- _class: edit-mode -->

# 🔄 Transition to Agent Mode

![bg left:40%](https://images.unsplash.com/photo-1518709268805-4e9042af2176?w=600)

## When Edit Isn't Enough

### Complexity Escalation Signs:

- **Multiple files** need coordination
- **External dependencies** required
- **Infrastructure changes** needed
- **Multi-step workflows** involved

**Ready for full AI autonomy?** 🚀

---

<!-- _class: agent-mode -->

# 🤖 Agent Mode: Full AI Autonomy

![bg right:30%](https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=400)

## Your AI DevOps Engineer 🛠️

- **Autonomous task execution** with human checkpoints
- **Multi-file coordination** and dependency management
- **External tool integration** via MCP
- **Infrastructure automation** capabilities
- **Self-healing workflows** with error recovery

---

<!-- _class: agent-mode -->

# 🎯 When to Use Agent Mode

![bg left:40%](https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=600)

## Complex Scenarios

- **🏗️ Complete feature implementation**: Full authentication systems
- **🔗 Cross-file changes**: Updates spanning multiple components
- **🏛️ Infrastructure setup**: Database schemas, API endpoints
- **🐛 Bug investigation**: Root cause analysis across codebase

---

<!-- _class: agent-mode -->

# ⚙️ Autonomous Actions Overview

## What Agent Can Do

- **📦 Install packages** (with approval)
- **📄 Create/modify/delete files**
- **💻 Run terminal commands**
- **🗃️ Execute database queries** (via MCP)
- **📖 Generate documentation**
- **🔧 Fix discovered issues**

## Self-Healing Behavior

- ✅ **Checks its own work**
- 💡 **Suggests improvements**
- 📏 **Follows best practices**

---

<!-- _class: agent-mode -->

# 🔴 Live Demo: Complete ETL Implementation

<!-- Live Demo -->

![bg right:45%](https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=700)

## End-to-End Scenario

**"Build complete dbt + Databricks data pipeline with testing and documentation"**

### Agent Will:

1. Create Databricks notebook for data ingestion
2. Build dbt models with proper materializations
3. Add data quality tests across both platforms
4. Generate comprehensive documentation
5. Set up automated workflow orchestration

---

<!-- _class: agent-mode -->

# 🔥 Advanced Agent Workflows

![bg left:35%](https://images.unsplash.com/photo-1518709268805-4e9042af2176?w=500)

## Database-Driven Development

```text
"Use Databricks Connect to analyze our Delta Lake schema,
then build comprehensive dbt models with proper lineage"
```

## Modern Data Stack Integration

```text
"Create end-to-end pipeline: Databricks ingestion → dbt transformations
→ automated testing and documentation with deployment to production"
```

---

<!-- _class: agent-mode -->

# 👤 Human-in-the-Loop Controls

## Safety Checkpoints 🛡️

- ✅ **Each MCP server call** requires approval
- 👀 **Review tool requests** before authorization
- ❌ **Reject sensitive** data source access
- 💰 **Monitor costs** for third-party services

## Visual Management

- **Green indicators** show running servers
- **Quick toggle** enable/disable via UI
- **Debug mode** for troubleshooting

---

<!-- _class: agent-mode -->

# 🚀 Beast Mode: Community Resources

![bg right:30%](https://images.unsplash.com/photo-1614680376593-902f74cf0d41?w=400)

## Advanced Techniques

**Burke Holland's Beast Mode Guide**
[Advanced Copilot Agent Workflow](https://gist.github.com/burkeholland/a232b706994aa2f4b2ddd3d97b11f9a7)

- Step-by-step agent instructions
- Community tips and tricks
- Troubleshooting guide
- Maximizing autonomy safely

---

<!-- _class: agent-mode -->

# 📊 Resource Monitoring

![bg left:40%](https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600)

## Performance Considerations

### Monitor Actively:

- **Memory usage** during Spark sessions
- **API call costs** for external services
- **Terminal process** resource consumption
- **Network bandwidth** for cloud operations

### Best Practices:

- 🐳 **Use dev containers** for isolation
- 🐣 **Start small** to build trust
- 🔒 **Review security** implications

---

<!-- _class: agent-mode -->

# 💡 Agent Mode Best Practices

## Team Implementation

- ✅ **Establish approval workflows** for autonomous actions
- ✅ **Set resource limits** and monitoring alerts
- ✅ **Train team members** on checkpoint decisions
- ✅ **Document agent outcomes** for learning
- ✅ **Regular security reviews** of generated code

## Risk Management

- 🔒 **Isolate development** environments
- 📊 **Track usage patterns** and costs
- 🚨 **Emergency stop procedures** in place

---

<!-- _class: tech-section -->

# ⚙️ Custom Instructions: Team Alignment

![bg right:30%](https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=400)

## Why Instructions Matter 🎯

- **Automatic code style** adherence
- **Team standard** enforcement
- **Context preservation** across sessions
- **Quality consistency** for all members
- **Onboarding acceleration** for new hires

---

<!-- _class: tech-section -->

# 🔄 One-Click Auto-Generation (VS Code 1.102+)

## Instant Setup Process

1. **💬 Open Copilot Chat** → gear icon → "Customize Chat"
2. **🔄 Click "Auto-update Instructions"** → scans workspace
3. **👀 Review generated markdown** → includes standards
4. **✨ Customize for team** → add specific requirements
5. **🔄 Re-run as needed** → keep instructions fresh

### Result: `.github/copilot-instructions.md`

---

<!-- _class: tech-section -->

# 📊 Before/After: Code Quality Impact

![bg left:40%](https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600)

## Without Instructions ❌

```python
def merge_data(df1, df2):
    return pd.merge(df1, df2, on='id')
```

## With Team Instructions ✅

```python
def merge_customer_data(
    customers_df: pd.DataFrame,
    orders_df: pd.DataFrame
) -> pd.DataFrame:
    """Merge customer and order datasets with validation."""
    # Validation and error handling included
```

---

<!-- _class: tech-section -->

# 📝 File-Type Specific Instructions

## Modular Approach for Large Teams

### Python Instructions (`.github/copilot-python.md`)

```markdown
---
applyTo: "**/*.py"
---

You are a senior data engineer specializing in Databricks and PySpark.

Code Standards:

- Use type hints for all functions and classes
- Include comprehensive docstrings with usage examples
- For Databricks: Always use spark.sql() or DataFrame API
- Prefer DataFrame operations over RDD transformations
- Use Delta Lake optimizations (Z-ORDER, VACUUM)
- Include proper error handling with structured logging
- Use dbutils for file system operations
- Follow medallion architecture patterns (bronze/silver/gold)

Performance Guidelines:

- Cache DataFrames when used multiple times
- Use broadcast joins for small dimension tables
- Implement incremental processing patterns
- Include partition strategy recommendations
```

### dbt Instructions (`.github/copilot-dbt.md`)

```markdown
---
applyTo: "**/*.sql"
---

You are a dbt expert following analytics engineering best practices.

Model Standards:

- Use incremental materializations for fact tables >1M rows
- Always include generic and custom data quality tests
- Document all models with business context descriptions
- Use semantic naming: dim* for dimensions, fct* for facts
- Follow staging → intermediate → marts layer pattern

Code Quality:

- Use CTEs for readability, avoid subqueries
- Include surrogate keys using dbt_utils.generate_surrogate_key
- Implement slowly changing dimensions (SCD) where needed
- Use dbt-expectations for advanced data quality testing
- Include freshness tests for critical source tables
```

---

<!-- _class: tech-section -->

# 🔌 Model Context Protocol (MCP)

![bg right:35%](https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=500)

## External Tool Integration 🛠️

- **Database connections** for live queries
- **Cloud service APIs** for infrastructure
- **GitHub integration** for project analysis
- **Filesystem access** for log analysis
- **Custom tools** via community servers

**Find servers at [fastmcp.me](https://fastmcp.me/)**

---

<!-- _class: tech-section -->

# 📊 Popular MCP Servers for Data Engineering

| Server Type       | Use Case                       | Installation                                     |
| ----------------- | ------------------------------ | ------------------------------------------------ |
| **🐙 GitHub**     | Project analysis, PR reviews   | `npx -y @modelcontextprotocol/server-github`     |
| **🔧 dbt Cloud**  | Model analysis, run monitoring | `dbt-cloud-mcp-server`                           |
| **📁 Filesystem** | Log analysis, data file access | `npx -y @modelcontextprotocol/server-filesystem` |
| **☁️ AWS S3**     | Cloud data operations          | `mcp-server-s3`                                  |

---

<!-- _class: tech-section -->

# 🔒 MCP Security & Best Practices

![bg left:30%](https://images.unsplash.com/photo-1563013544-824ae1b704d3?w=400)

## Security First 🛡️

- **Read-only connections** for databases
- **Environment isolation** dev vs production
- **Cost monitoring** for paid services
- **Access control** per team member
- **Audit logging** for compliance

## Implementation Strategy

- Start with **filesystem and GitHub**
- Add **database access** carefully
- **Monitor usage** patterns
- **Train team** on approval decisions

---

<!-- _class: tech-section -->

# 🔴 Live Demo: MCP Integration

<!-- Live Demo -->

![bg right:45%](https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=700)

## Scenario: Modern Data Stack Documentation

**"Use GitHub MCP to analyze our dbt project structure and Databricks notebooks, then generate comprehensive data pipeline documentation with lineage"**

### Agent Workflow:

1. Connect to GitHub MCP and Databricks APIs
2. Analyze dbt models and their dependencies
3. Review Databricks notebook workflows
4. Generate end-to-end pipeline documentation

---

<!-- _class: tech-section -->

# 💬 Custom Chat Modes

## Specialized AI Assistants 🤖

### Architecture Planning Mode

```yaml
name: "Architecture Planning"
tools: ["@workspace", "@codebase"]
focus: "System design and scalability"
```

### Data Engineering Review Mode

```yaml
name: "Data Review"
tools: ["@workspace", "mcp:postgres"]
focus: "Pipeline quality and performance"
```

**Location**: `.github/chatmodes/*.chatmode.md`

---

<!-- _class: tech-section -->

# 🌟 Community Resources

![bg right:30%](https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=400)

## awesome-copilot Repository

**[github.com/github/awesome-copilot](https://github.com/github/awesome-copilot)**

- **📄 Instruction templates** for different stacks
- **💡 Curated prompts** for common tasks
- **💬 Chat mode definitions** for workflows
- **🔄 Regular updates** with community contributions

### Team Workflow

1. Browse templates matching your stack
2. Copy and customize for your repo
3. Share updates with team
4. Iterate based on feedback

---

<!-- _class: lead -->

# 🐳 Team Implementation Strategy

![bg](https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=1200)

## From Individual to Enterprise Scale

---

# 🐳 Devcontainer: "Works on My Machine" Solution

![bg left:40%](https://images.unsplash.com/photo-1605810230434-7631ac76ec81?w=600)

## Team Consistency 🎯

### Benefits:

- **Same environment** for all developers
- **Pre-configured MCP** servers
- **Automatic extension** installation
- **Instant onboarding** for new hires

### Setup:

```json
{
  "name": "Data Engineering + MCP",
  "image": "mcr.microsoft.com/vscode/devcontainers/python:3.11",
  "extensions": ["GitHub.copilot-chat"],
  "postCreateCommand": "pip install -r requirements.txt"
}
```

---

# 🛠️ Step-by-Step Team Setup

## Configuration Workflow

1. **📁 Create `.devcontainer/devcontainer.json`**
2. **⚙️ Add team-specific MCP servers**
3. **📝 Include custom instructions**
4. **🔧 Configure workspace settings**
5. **🚀 Test with sample project**
6. **📚 Document for team**

## Result: **One-click environment** for entire team!

---

# 🧪 Testing & Quality Assurance

![bg right:35%](https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=500)

## AI-Generated Test Suites ✅

### Capabilities:

- **Unit tests** with edge cases
- **Integration tests** for APIs
- **Property-based testing** with Hypothesis
- **Performance benchmarks** for data operations
- **Security vulnerability** checks

### Example:

_"Generate comprehensive tests for this ETL function including error conditions and performance validation"_

---

# 🔴 Live Demo: Hands-On TDD Example

<!-- Live Demo -->

![bg left:45%](https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=700)

## Test-Driven Development with AI

### Workflow:

1. **Describe requirements** in natural language
2. **Generate test cases** with Copilot
3. **Implement function** to pass tests
4. **Refine and iterate** based on feedback
5. **Validate edge cases** and performance

**Live coding a data validation function!**

---

# 🔒 Performance & Security

![bg right:30%](https://images.unsplash.com/photo-1563013544-824ae1b704d3?w=400)

## AI-Powered Code Review

### Security Analysis:

- **Vulnerability detection** in data access
- **SQL injection** prevention
- **Credential management** review
- **Access control** validation

### Performance Optimization:

- **Memory usage** analysis for large datasets
- **Query optimization** suggestions
- **Parallel processing** recommendations
- **Resource monitoring** integration

---

# 🤝 Team Collaboration Features

## Standardized Workflows 🔄

### Shared Configuration:

- **Common MCP servers** across team
- **Unified coding standards** via instructions
- **Consistent chat modes** for different tasks
- **Version-controlled settings** in repo

### Benefits:

- **Faster onboarding** for new members
- **Consistent code quality** across projects
- **Knowledge sharing** through AI interactions
- **Reduced context switching** between tools

---

# 📈 Implementation Roadmap

## Progressive Adoption Strategy

### **Beginner (Week 1-2)** 🌱

- Set up VS Code 1.102+ and extensions
- Practice Ask mode with simple queries
- Try Edit mode for small improvements
- Generate basic custom instructions

### **Intermediate (Week 3-4)** 🚀

- Experiment with Agent mode workflows
- Set up GitHub and filesystem MCP
- Create team-specific chat modes
- Practice test generation and reviews

---

# 📈 Implementation Roadmap (continued)

![bg right:30%](https://images.unsplash.com/photo-1553028826-f4804a6dfd3b?w=400)

### **Advanced (Month 2+)** 🏆

- Implement database and cloud MCP
- Build comprehensive devcontainer setup
- Create extensive instruction templates
- Develop team training materials
- Establish governance and best practices

### **Enterprise (Ongoing)** 🏢

- Monitor usage and ROI metrics
- Expand to additional teams
- Integrate with existing workflows
- Continuous improvement processes

---

# ⚠️ Common Pitfalls to Avoid

![bg left:35%](https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=500)

## Learn from Others' Mistakes

- ❌ **Don't trust blindly** → Always review AI-generated code
- ❌ **Don't ignore context** → Provide sufficient background
- ❌ **Don't skip testing** → Validate all AI suggestions
- ❌ **Don't hardcode secrets** → Use environment variables
- ❌ **Don't ignore performance** → Monitor resource usage

### Pro Tip: **Start small, build trust gradually**

---

# 🆘 Support & Community

## Getting Help When You Need It 🤝

### Official Resources:

- **[VS Code GitHub Issues](https://github.com/microsoft/vscode/issues)** - Bug reports, features
- **[GitHub Copilot Support](https://support.github.com/copilot)** - Official channels
- **[VS Code Discord](https://discord.gg/0ZvbCAAha2g9c2Ej)** - Real-time community

### Community Learning:

- **[Stack Overflow](https://stackoverflow.com/questions/tagged/vscode+copilot)** - Q&A
- **[awesome-copilot](https://github.com/github/awesome-copilot)** - Templates and examples

---

<!-- _class: lead -->

# 🎯 Key Takeaways

![bg](https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=1200)

---

# 🌟 Top 5 Insights for Data Engineering Teams

## Transform Your Development Today

- **Progressive autonomy** → Start with Ask for dbt optimization, graduate to Agent for full pipelines
- **Team standardization** → Custom instructions eliminate inconsistency across Databricks notebooks
- **Safety first** → Human checkpoints maintain data quality and governance standards
- **Community leverage** → Use awesome-copilot for Databricks and dbt integrations
- **Continuous learning** → AI capabilities evolve rapidly with new data tools

### Remember: **Copilot is a collaborator, not a replacement for data engineering expertise** 🤝

---

# ✅ Data Engineering Implementation Checklist

![bg right:30%](https://images.unsplash.com/photo-1611224923853-80b023f02d71?w=400)

## Your 30-60-90 Day Plan

### **Immediate (This Week):**

- [ ] Update to VS Code 1.102+
- [ ] Set up GitHub Copilot subscription
- [ ] Generate dbt and Databricks custom instructions
- [ ] Practice Ask mode with existing pipelines

### **30 Days:**

- [ ] Implement Databricks and dbt MCP servers
- [ ] Create standardized devcontainer for data team
- [ ] Establish data quality coding standards
- [ ] Train 2-3 data engineers on new workflows

---

# ✅ Implementation Checklist (continued)

### **60 Days:**

- [ ] Deploy Agent mode for pipeline automation
- [ ] Integrate with dbt Cloud CI/CD
- [ ] Establish data governance policies
- [ ] Measure development velocity and quality gains

### **90 Days:**

- [ ] Full team adoption across all data projects
- [ ] Advanced MCP integrations with monitoring tools
- [ ] Copilot-generated documentation standards
- [ ] ROI analysis and optimization recommendations

### **90 Days:**

- [ ] Scale to entire team
- [ ] Advanced MCP integrations
- [ ] Community contribution
- [ ] ROI analysis and optimization

---

# 📚 Learning Paths & Resources

![bg left:40%](https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=600)

## Continue Your Journey

### **Documentation:**

- [VS Code Copilot Setup](https://code.visualstudio.com/docs/copilot/setup)
- [Custom Instructions Guide](https://code.visualstudio.com/docs/copilot/copilot-customization)
- [MCP Servers Documentation](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)

### **Community:**

- [Marp GitHub Discussions](https://github.com/marp-team/marp/discussions)
- [Burke Holland's Beast Mode](https://gist.github.com/burkeholland/a232b706994aa2f4b2ddd3d97b11f9a7)

---

# 🌍 Community Engagement

## Share Your Success 🎉

### **Contribute Back:**

- Share custom instructions on GitHub
- Create MCP servers for your domain
- Write blog posts about your experience
- Present at local meetups

### **Connect & Learn:**

- Join VS Code Discord community
- Participate in GitHub Discussions
- Follow @github and @code on Twitter
- Attend conferences and workshops

---

# ❓ Q&A Session

![bg right:40%](https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=600)

## Interactive Discussion 💬

### Common Questions:

- **Security concerns** with AI code generation
- **Integration challenges** with existing workflows
- **Cost management** for larger teams
- **Performance impact** on development speed
- **Troubleshooting** common issues

### **Let's solve problems together!**

---

<!-- _class: lead -->

# 🙏 Thank You!

## Ready to Transform Your Data Engineering Workflow?

![bg](https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=1200)

### **Start Your Copilot Journey Today**

---

# 📞 Resources & Contact

![bg left:30%](https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=400)

## Stay Connected

### **Essential Links:**

- 📖 **[Full Tutorial](https://github.com/tutorials/45-vs-code-agent-handson.md)**
- 🎯 **[awesome-copilot](https://github.com/github/awesome-copilot)**
- 🔧 **[VS Code Copilot Docs](https://code.visualstudio.com/docs/copilot)**
- 💬 **[Community Discord](https://discord.gg/0ZvbCAAha2g9c2Ej)**

### **Follow Updates:**

- 📰 **[VS Code Updates](https://code.visualstudio.com/updates)**
- 🤖 **[GitHub Copilot Blog](https://github.blog/category/copilot/)**

### **Happy Coding with AI! 🚀**
