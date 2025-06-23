# ADK Data Extraction Examples - Restructured

This directory contains educational examples comparing different Google ADK agent coordination patterns for document processing. Each example has been restructured to follow ADK best practices with proper separation of concerns.

## Quick Start with ADK Commands

All examples are designed to work with ADK commands. To run any example:

### Setup
1. Navigate to the examples directory
2. Copy the example's `.env.example` to `.env` and add your API key
3. Run with ADK commands

### Running Examples

#### Web UI (Recommended for testing)
```bash
cd /path/to/examples
adk web
```
Then select your desired example from the dropdown.

#### Command Line
```bash
cd /path/to/examples
adk run basic_contact_extraction "Your input text here"
adk run sequential_contract_pipeline "Contract text here"
adk run hierarchical_document_pipeline "Document text here"
adk run legal_document_analysis "Legal document text here"
```

### Available Examples
- `basic_contact_extraction` - Simple contact extraction
- `sequential_contract_pipeline` - Sequential contract processing
- `hierarchical_document_pipeline` - Hierarchical document processing
- `legal_document_analysis` - Legal document analysis

## Directory Structure

```
examples/
├── basic_contact_extraction/          # ✅ Single-Agent Pattern (Beginner)
│   ├── agent.py                      # Main entry point
│   ├── agents/                       # Agent definitions
│   ├── schemas/                      # Data models
│   └── README.md                     # Example documentation
├── sequential_contract_pipeline/      # ✅ Sequential Pattern (Intermediate)
│   ├── agent.py                      # Sequential coordinator
│   ├── sub_agents/                   # Sequential processing agents
│   ├── schemas/                      # Contract data models
│   ├── data/                         # Sample contract data
│   └── README.md                     # Sequential pattern docs
├── hierarchical_document_pipeline/    # ✅ Hierarchical Pattern (Advanced)
│   ├── agent.py                      # Main coordinator agent
│   ├── sub_agents/                   # Specialized sub-agents
│   ├── tools/                        # Coordination tools
│   ├── schemas/                      # Document schemas
│   └── README.md                     # Hierarchical pattern docs
├── legal_document_analysis/           # ✅ Specialized Analysis (Intermediate)
│   ├── agent.py                      # Legal analysis coordinator
│   ├── agents/                       # Specialized legal agents
│   ├── schemas/                      # Legal document schemas
│   └── README.md                     # Legal analysis docs
└── README.md                         # This file
```

## ADK Patterns Demonstrated

### 🎯 1. Single-Agent Pattern (`basic_contact_extraction/`)
**Best For:** Simple, focused extraction tasks

- **Pattern**: Single `LlmAgent` with output schema
- **Complexity**: Beginner
- **Use Case**: Contact information extraction
- **Key Features**: 
  - Single-purpose agent
  - Structured output with Pydantic schema
  - Simple session management

### 🔄 2. Sequential Pattern (`sequential_contract_pipeline/`)
**Best For:** Fixed workflow processes

- **Pattern**: `SequentialAgent` with ordered sub-agents
- **Complexity**: Intermediate
- **Use Case**: Contract processing pipeline
- **Key Features**:
  - Deterministic execution order
  - Conversation flow communication
  - Extract → Validate → Report workflow

### 🏗️ 3. Hierarchical Pattern (`hierarchical_document_pipeline/`)
**Best For:** Complex coordination with intelligent routing

- **Pattern**: Parent `LlmAgent` with specialized sub-agents
- **Complexity**: Advanced
- **Use Case**: Multi-document type processing
- **Key Features**:
  - Intelligent document classification
  - Dynamic routing to specialists
  - Shared session state coordination
  - Tool-based coordination

### ⚖️ 4. Specialized Analysis (`legal_document_analysis/`)
**Best For:** Domain-specific analysis

- **Pattern**: Specialized `LlmAgent` for legal documents
- **Complexity**: Intermediate
- **Use Case**: Legal document analysis
- **Key Features**:
  - Domain-specific schemas
  - Specialized instructions
  - Financial term extraction

## Comparison Analysis

### Sequential Agent Pattern

**✅ Benefits:**
- **Deterministic execution**: Fixed order guarantees predictable behavior
- **Simple state management**: Data flows linearly through `output_key` pattern
- **Easy debugging**: Clear execution path with no complex routing
- **Consistent performance**: Predictable resource usage patterns
- **Straightforward architecture**: No coordination complexity

**❌ Limitations:**
- **No adaptability**: Cannot skip steps based on document characteristics
- **Resource inefficiency**: All agents execute regardless of document complexity
- **Limited flexibility**: No conditional processing or dynamic routing
- **Single document focus**: Designed for one document type only

### Hierarchical Coordination Pattern

**✅ Benefits:**
- **Intelligent routing**: Dynamic agent selection based on document type
- **Efficiency**: Specialized agents for optimal processing
- **Scalability**: Easy to add new document types and specialists
- **Flexibility**: Conditional processing based on classification
- **Production-ready**: Complex coordination for enterprise scenarios

**❌ Limitations:**
- **Complex architecture**: Requires coordination logic and tools
- **Harder debugging**: Multiple execution paths to trace
- **State management**: Requires shared state tools and session handling
- **Development complexity**: More intricate agent relationships

## When to Use Each Pattern

### Use Sequential Agents When:
- You have a **fixed, predictable workflow**
- **All processing steps are always required**
- You need **deterministic execution** for compliance/audit
- **Simple state management** is sufficient
- Processing **single document types** with consistent requirements
- **Educational/learning scenarios** to understand basic patterns

### Use Hierarchical Coordination When:
- You need **dynamic routing** based on document characteristics
- Processing **multiple document types** requiring different specialists
- **Conditional processing** to optimize efficiency
- **Complex coordination** with specialized agents
- **Production environments** requiring scalability and flexibility
- **Enterprise scenarios** with varying processing requirements

## Code Structure Comparison

### Sequential Pattern Structure:
```python
# Simple linear flow
SequentialAgent(
    sub_agents=[
        classifier_agent,    # Step 1: Always runs
        extractor_agent,     # Step 2: Always runs  
        validator_agent,     # Step 3: Always runs
        reporter_agent       # Step 4: Always runs
    ]
)
```

### Hierarchical Pattern Structure:
```python
# Complex coordination with routing
LlmAgent(  # Coordinator
    sub_agents=[
        classifier_agent,           # Classification
        contract_specialist,        # Conditional: contracts only
        invoice_specialist,         # Conditional: invoices only
        general_specialist,         # Conditional: other documents
        validation_specialist       # Validation
    ],
    tools=[get_shared_state],      # Coordination tools
    # Complex routing logic in instructions
)
```

## Educational Value

This comparison demonstrates fundamental trade-offs in agent architecture design:

1. **Simplicity vs Flexibility**: Sequential patterns are simpler but less adaptable
2. **Determinism vs Intelligence**: Fixed flows are predictable but may be inefficient
3. **Development Speed vs Production Readiness**: Simple patterns are faster to implement
4. **Resource Usage vs Optimization**: All-steps-execute vs intelligent routing

## Running the Examples

Both examples can be run independently to see the different patterns in action:

```bash
# Run sequential pattern
python sequential_contract_pipeline.py

# Run hierarchical pattern  
python smart_document_extraction_pipeline.py
```

Make sure you have your Google API key configured:
```bash
export GOOGLE_API_KEY="your-api-key-here"
```

## Key Learning Points

1. **Sequential Agents** are perfect for **educational purposes** and **fixed workflows**
2. **Hierarchical Coordination** is suited for **production systems** requiring **flexibility**
3. **State management** differs significantly between patterns
4. **Error handling** and **debugging** complexity varies between approaches
5. **Performance characteristics** depend on document processing requirements

Both patterns have their place in the ADK ecosystem, and understanding their trade-offs helps in choosing the right approach for specific use cases.
