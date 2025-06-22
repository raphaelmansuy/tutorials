# ADK Constraint Resolution: Output Schema vs Tools

## Problem Identified

The original improved multi-agent pipeline was encountering this error:
```
❌ Error running improved pipeline: 1 validation error for LlmAgent
  Value error, Invalid config for agent contract_specialist: if output_schema is set, tools must be empty
```

## Root Cause

According to the official [ADK documentation](https://google.github.io/adk-docs/agents/llm-agents/#structuring-data-input_schema-output_schema-output_key):

> **Constraint**: Using `output_schema` enables controlled generation within the LLM but **disables the agent's ability to use tools or transfer control to other agents**. Your instructions must guide the LLM to produce JSON matching the schema directly.

## Solution Applied

### 1. **Removed Tools from Schema-Based Agents**
- All agents using `output_schema` (classification, extraction, and validation specialists) now have **NO tools**
- These agents rely purely on LLM instruction-based processing to generate structured JSON output

### 2. **Updated Agent Instructions**
- Changed instructions to emphasize "**IMPORTANT: You must respond with ONLY a JSON object**"
- Provided explicit JSON format examples in instructions
- Removed all references to tool-based state management in schema agents

### 3. **Maintained Hierarchical Coordination**
- The coordinator agent still uses tools for coordination (`get_shared_state`)
- Sub-agent relationships preserved through ADK's `sub_agents` parameter
- Agent-to-agent delegation works through ADK's built-in `transfer_to_agent` mechanism

## Results

✅ **Pipeline runs successfully** with proper ADK constraints
✅ **Hierarchical coordination pattern** maintained
✅ **Agent-to-agent delegation** working correctly
✅ **Structured output** generated from schema-based agents
✅ **ADK best practices** properly implemented

## Key Architecture Changes

### Before (Problematic):
```python
contract_specialist = LlmAgent(
    # ... other params
    tools=[save_extraction_to_state, get_shared_state],  # ❌ Not allowed with output_schema
    output_schema=ContractData,  # ❌ Conflicts with tools
)
```

### After (Correct):
```python
contract_specialist = LlmAgent(
    # ... other params
    output_schema=ContractData,  # ✅ Pure schema-based generation
    # No tools parameter - ADK constraint satisfied
    instruction="""IMPORTANT: Respond with ONLY JSON matching the schema..."""
)
```

## ADK Warnings Explained

The warnings seen during execution are **expected and normal**:
```
WARNING: output_schema cannot co-exist with agent transfer configurations. 
Setting disallow_transfer_to_parent=True, disallow_transfer_to_peers=True
```

ADK automatically adjusts transfer settings for `output_schema` agents, which is the correct behavior per the documentation.

## Lessons Learned

1. **Read ADK documentation carefully** - constraints are clearly documented
2. **Use `output_schema` for pure data extraction** agents
3. **Use `tools` for coordination** and workflow management agents  
4. **Don't mix `output_schema` with `tools`** - they serve different purposes
5. **Instructions become critical** when tools are not available

## Validation

The pipeline successfully demonstrates:
- ✅ Document classification with structured output
- ✅ Agent-to-agent delegation based on classification
- ✅ Structured data extraction using schema-based agents
- ✅ Proper ADK hierarchical coordination patterns
- ✅ Compliance with all ADK constraints

This resolution shows the importance of understanding framework constraints and designing architectures that work within those boundaries while still achieving the desired multi-agent coordination goals.
