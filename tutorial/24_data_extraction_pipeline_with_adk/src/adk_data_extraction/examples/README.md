# Sequential vs Hierarchical Document Processing Pipelines

This directory contains educational examples comparing two different Google ADK agent coordination patterns for document processing:

## Files Overview

### 1. `smart_document_extraction_pipeline.py`
**Hierarchical Coordination Pattern**
- Main coordinator agent with specialized sub-agents
- Dynamic routing based on document classification
- Complex coordination logic with conditional branching
- Supports multiple document types (contracts, invoices, reports)

### 2. `sequential_contract_pipeline.py` 
**Sequential Agent Pattern**
- Fixed execution order: Classify → Extract → Validate → Report
- Deterministic workflow with no branching
- State-based communication using `output_key`
- Focused on contract processing only

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
