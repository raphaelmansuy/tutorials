# Mermaid Diagram Guidelines for VS Code

## Overview
This document provides guidelines for creating and maintaining Mermaid diagrams in VS Code to ensure they render correctly and avoid common syntax issues.

## Common Issues and Solutions

### 1. Node Labels with Numbers and Periods
❌ **Avoid**: `A[1. Extract Data]`
✅ **Use**: `A[Extract Data]`

**Problem**: Mermaid interprets numbered lists (e.g., "1. ", "2. ") as markdown syntax, causing "Unsupported markdown: list" errors.

**Solution**: Remove the numbered list format from node labels. If you need to indicate sequence, use:
- Sequential naming: `Step1[Extract Data]`, `Step2[Clean Data]`
- Arrow flow to show sequence
- Descriptive labels without numbers

### 2. Parentheses in Labels
❌ **Avoid**: `Service[CDC Service<br/>(e.g., Debezium)]`
✅ **Use**: `Service[CDC Service<br/>Debezium]`

**Problem**: Parentheses `()` can conflict with Mermaid's node shape syntax.

**Solution**: 
- Remove parentheses from labels
- Use alternative text like "such as", "like", or simply list examples without parentheses
- Use line breaks `<br/>` to separate information

### 3. Subgraph Naming
❌ **Avoid**: `subgraph "Layer 1 (Medium Links)"`
✅ **Use**: `subgraph Layer1["Layer 1 - Medium Links"]`

**Problem**: Parentheses in subgraph titles can cause parsing issues.

**Solution**:
- Use ID-based subgraph naming with bracket notation for titles
- Replace parentheses with dashes or other separators

### 4. Special Characters in Text
❌ **Avoid**: Special characters that conflict with Mermaid syntax
✅ **Use**: Escape characters or alternative text

**Characters to be careful with**:
- `()` - Used for node shapes
- `{}` - Used for decision nodes
- `[]` - Used for rectangular nodes
- `--` - Used for connections
- `>>` - Used for special connections

## Best Practices

### 1. Validation Workflow
Always validate your Mermaid diagrams before committing:
1. Use the Mermaid validation tools in VS Code
2. Preview diagrams before finalizing
3. Test complex diagrams in smaller parts first

### 2. Node Naming Convention
- Use descriptive, clear labels
- Keep labels concise but informative
- Use consistent naming patterns within a diagram
- Avoid special characters that conflict with Mermaid syntax

### 3. Layout and Styling
- Use consistent styling across related diagrams
- Group related elements in subgraphs
- Use directional flow (`TD`, `LR`, etc.) appropriately
- Apply colors meaningfully to enhance understanding

### 4. Documentation
- Include comments in complex diagrams using `%% comment`
- Document the purpose and context of each diagram
- Maintain this guidelines document as new issues are discovered

## VS Code Extensions
Recommended extensions for working with Mermaid:
- **Mermaid Editor**: For syntax highlighting and preview
- **Markdown Preview Enhanced**: For viewing diagrams in markdown
- **Mermaid Markdown Syntax Highlighting**: For better syntax support

## Troubleshooting

### Common Error Messages
1. **"Unsupported markdown: list"**
   - Cause: Numbered list syntax in node labels
   - Fix: Remove "1. ", "2. " etc. from labels

2. **Parse error with node shapes**
   - Cause: Conflicting parentheses or brackets
   - Fix: Check for proper escaping or alternative text

3. **"Expecting..." syntax errors**
   - Cause: Malformed connections or node definitions
   - Fix: Verify all nodes are properly defined before use

### Debugging Steps
1. Start with a minimal version of the diagram
2. Add complexity incrementally
3. Validate each addition
4. Use browser developer tools to see detailed error messages
5. Check the official Mermaid documentation for syntax updates

## Resources
- [Official Mermaid Documentation](https://mermaid.js.org/)
- [Mermaid Live Editor](https://mermaid.live/) - For testing diagrams
- [VS Code Mermaid Extensions](https://marketplace.visualstudio.com/search?term=mermaid&target=VSCode)

---
*Last updated: June 28, 2025*
*Maintain this document as new Mermaid syntax issues are discovered in the workspace.*
