# Chapter 7: Tools to Grab—Your Shortcut Arsenal

No need to reinvent the wheel. Here's your toolkit:

---

## Navigation

- [← Previous: Examples That Stick](06_examples.md)
- [Next: Pitfalls to Dodge →](08_pitfalls.md)
- [🏠 Back to Main](README.md)

---

## 7.1 Essential Tools

- **Contextual AI**: Platform for building context-aware AI applications. Check their documentation for current RAG and integration features ([contextual.ai](https://contextual.ai)).
- **LangChain**: Open-source framework for chaining LLMs and context sources ([langchain.com](https://langchain.com)).
- **Elicit**: AI research assistant for literature review and data extraction ([elicit.com](https://elicit.com)).

### Tool Deep-Dive

- **Contextual AI**: Provides tools for context management and retrieval. Features may change; consult their docs for details.
- **LangChain**: Enables chaining of context sources and LLMs for advanced workflows.
- **Elicit**: Focuses on research and evidence gathering from academic sources.

## 7.2 MCP-Native Tools

**The New Standard**: Model Context Protocol tools are transforming how we build context systems.

- **MCP Servers**: Pre-built servers for common data sources (databases, APIs, file systems, cloud storage)
- **MCP Client Libraries**: Integration libraries for Python, TypeScript, and other languages
- **MCP Inspector**: Tool for debugging and monitoring MCP connections and resource access
- **Community Ecosystem**: Growing collection of specialized MCP servers for different domains

### Getting Started with MCP

1. **Install MCP SDK**: `pip install mcp-sdk` or `npm install @modelcontextprotocol/sdk`
2. **Choose MCP Servers**: Browse available servers for your data sources
3. **Configure Authentication**: Set up secure connections using MCP's built-in auth
4. **Integrate with Your AI**: Use MCP client to access context resources

**Pro Tip**: Start with community MCP servers—they're battle-tested and save weeks of development time.

## 7.3 Vector Databases

Essential for storing and retrieving context embeddings:

- **Pinecone**: Managed vector database with excellent performance
- **Weaviate**: Open-source with GraphQL API
- **Qdrant**: High-performance vector search engine
- **FAISS**: Facebook's similarity search library
- **Chroma**: Simple, open-source embedding database

## 7.4 Embedding Models

Transform text into searchable vectors:

- **OpenAI Ada-002**: General-purpose, high-quality embeddings
- **Sentence Transformers**: Open-source, domain-specific models
- **Cohere Embed**: Multilingual embedding service
- **Azure OpenAI**: Enterprise-grade with security features

## 7.5 Development Frameworks

Build context systems faster:

- **LlamaIndex**: Data framework for LLM applications
- **Haystack**: End-to-end NLP framework with RAG support
- **DSPy**: Programming framework for AI systems
- **Semantic Kernel**: Microsoft's AI orchestration framework

## 7.6 Monitoring and Analytics

Track your context system performance:

- **LangSmith**: LangChain's monitoring platform
- **Weights & Biases**: ML experiment tracking
- **Arize AI**: ML observability platform
- **WhyLabs**: Data and ML monitoring

## 7.7 Quick Start Combinations

### For Beginners

- **LangChain** + **OpenAI Embeddings** + **Chroma** = Simple RAG system
- **LlamaIndex** + **Pinecone** = Production-ready context retrieval

### For Enterprise

- **MCP** + **Azure OpenAI** + **Weaviate** = Secure, scalable context system
- **Semantic Kernel** + **Qdrant** + **LangSmith** = Enterprise monitoring

### For Researchers

- **DSPy** + **Sentence Transformers** + **FAISS** = Experimental context systems
- **Haystack** + **Cohere** + **W&B** = Research pipeline with tracking

---

## Tool Selection Guide

| Need | Recommended Tools | Why |
|------|------------------|-----|
| Quick prototype | LangChain + OpenAI + Chroma | Fast setup, good documentation |
| Production system | MCP + Pinecone + LangSmith | Scalable, monitored, secure |
| Research project | DSPy + FAISS + W&B | Flexible, experimental, trackable |
| Enterprise deployment | Semantic Kernel + Azure + Weaviate | Security, compliance, support |

---

## Getting Help

- **Documentation**: Most tools have excellent getting-started guides
- **Communities**: Join Discord/Slack channels for real-time help
- **Examples**: GitHub repositories with working implementations
- **Tutorials**: YouTube and blog tutorials for visual learners

---

## Next Steps

Got your tools picked out? Chapter 8 shows you the common pitfalls to avoid when building your context system.
