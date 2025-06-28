# Chapter 2: Quick Start - Your First Embedding-based Search

## Get Results in 5 Minutes

Let's dive straight into building a working semantic search system. By the end of this chapter, you'll have a functioning search engine that understands meaning, not just keywords. We'll start with the simplest possible implementation and then explore what makes it work.

## Prerequisites Check

Before we begin, ensure you have:

- Python 3.8 or higher installed
- Basic familiarity with pip and virtual environments
- A text editor or IDE
- Terminal/command prompt access

## Step 1: Environment Setup

First, let's create a clean environment and install the necessary libraries:

```bash
# Create a virtual environment
python -m venv embedding_tutorial
source embedding_tutorial/bin/activate  # On Windows: embedding_tutorial\Scripts\activate

# Install required packages
pip install sentence-transformers faiss-cpu numpy
```

**Package Overview:**

- **sentence-transformers**: Provides easy access to state-of-the-art embedding models
- **faiss-cpu**: Facebook's similarity search library for efficient vector operations
- **numpy**: Essential for numerical operations on embeddings

## Step 2: Your First Semantic Search (5 Minutes)

Create a new file called `quick_search.py` and add the following code:

```python
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Step 1: Load a pre-trained embedding model
print("Loading embedding model...")
model = SentenceTransformer('all-MiniLM-L6-v2')
print(f"Model loaded. Embedding dimension: {model.get_sentence_embedding_dimension()}")

# Step 2: Create sample documents to search through
documents = [
    "I love programming in Python",
    "Machine learning is fascinating",
    "The weather is beautiful today",
    "Artificial intelligence will change the world",
    "I enjoy coding and building applications",
    "It's a sunny day outside",
    "Deep learning models are very powerful",
    "Software development is my passion",
    "The sky is clear and blue",
    "Neural networks can solve complex problems"
]

# Step 3: Convert documents to embeddings
print("Creating embeddings for documents...")
doc_embeddings = model.encode(documents)
print(f"Created {len(doc_embeddings)} embeddings, each with {doc_embeddings.shape[1]} dimensions")

# Step 4: Create FAISS index for fast similarity search
dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)  # L2 distance (Euclidean)
index.add(doc_embeddings.astype('float32'))
print(f"FAISS index created with {index.ntotal} vectors")

# Step 5: Perform search queries
queries = [
    "I want to learn about coding",
    "Tell me about the weather",
    "What is AI?"
]

print("\n" + "="*50)
print("SEMANTIC SEARCH RESULTS")
print("="*50)

for query in queries:
    print(f"\nQuery: '{query}'")
    print("-" * 40)
    
    # Convert query to embedding
    query_embedding = model.encode([query])
    
    # Search for similar documents
    k = 3  # Return top 3 results
    distances, indices = index.search(query_embedding.astype('float32'), k)
    
    # Display results
    for i, (distance, doc_idx) in enumerate(zip(distances[0], indices[0])):
        similarity_score = 1 / (1 + distance)  # Convert distance to similarity score
        print(f"  {i+1}. [{similarity_score:.3f}] {documents[doc_idx]}")
```

## Step 3: Run Your First Search

Execute the script:

```bash
python quick_search.py
```

You should see output similar to:

```
Loading embedding model...
Model loaded. Embedding dimension: 384
Creating embeddings for documents...
Created 10 embeddings, each with 384 dimensions
FAISS index created with 10 vectors

==================================================
SEMANTIC SEARCH RESULTS
==================================================

Query: 'I want to learn about coding'
----------------------------------------
  1. [0.847] I love programming in Python
  2. [0.823] I enjoy coding and building applications
  3. [0.801] Software development is my passion

Query: 'Tell me about the weather'
----------------------------------------
  1. [0.892] The weather is beautiful today
  2. [0.868] It's a sunny day outside
  3. [0.845] The sky is clear and blue

Query: 'What is AI?'
----------------------------------------
  1. [0.876] Artificial intelligence will change the world
  2. [0.854] Deep learning models are very powerful
  3. [0.832] Neural networks can solve complex problems
```

## Understanding What Just Happened

### The Magic of Semantic Understanding

Notice how the search understood concepts, not just keywords:

- **"learn about coding"** matched with **"programming"**, **"coding"**, and **"software development"**
- **"weather"** found **"sunny day"** and **"sky is clear"** even without the word "weather"
- **"What is AI?"** connected to **"artificial intelligence"**, **"deep learning"**, and **"neural networks"**

This is the power of embeddings – they capture semantic meaning in numerical form.

### System Architecture Overview

```mermaid
flowchart LR
    A[Input Documents] --> B[Sentence Transformer]
    B --> C[Document Embeddings]
    C --> D[FAISS Index]
    
    E[Query Text] --> F[Same Model]
    F --> G[Query Embedding]
    G --> H[Similarity Search]
    D --> H
    H --> I[Ranked Results]
    
    style A fill:#e1f5fe,stroke:#01579b,stroke-width:2px,color:#000
    style E fill:#e1f5fe,stroke:#01579b,stroke-width:2px,color:#000
    style B fill:#f3e5f5,stroke:#4a148c,stroke-width:2px,color:#000
    style F fill:#f3e5f5,stroke:#4a148c,stroke-width:2px,color:#000
    style D fill:#e8f5e8,stroke:#1b5e20,stroke-width:2px,color:#000
    style H fill:#e8f5e8,stroke:#1b5e20,stroke-width:2px,color:#000
    style I fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#000
```

### Key Components Explained

1. **Sentence Transformer Model**: Converts text into 384-dimensional vectors
2. **FAISS Index**: Efficiently stores and searches through vector embeddings
3. **Similarity Computation**: Finds vectors closest to the query vector
4. **Distance to Similarity**: Converts mathematical distance to intuitive similarity scores

## Experimenting with Different Models

Let's compare different embedding models to understand their characteristics:

```python
# models_comparison.py
from sentence_transformers import SentenceTransformer
import time

# Different models to compare
models_to_test = [
    'all-MiniLM-L6-v2',      # Small, fast model
    'all-mpnet-base-v2',     # Larger, more accurate model
    'paraphrase-MiniLM-L6-v2' # Specialized for paraphrase detection
]

test_text = "Machine learning is transforming the world"

print("Model Comparison:")
print("="*60)

for model_name in models_to_test:
    print(f"\nTesting: {model_name}")
    
    # Load model and measure time
    start_time = time.time()
    model = SentenceTransformer(model_name)
    load_time = time.time() - start_time
    
    # Get embedding and measure encoding time
    start_time = time.time()
    embedding = model.encode(test_text)
    encode_time = time.time() - start_time
    
    print(f"  Dimensions: {len(embedding)}")
    print(f"  Load time: {load_time:.2f} seconds")
    print(f"  Encode time: {encode_time:.4f} seconds")
    print(f"  Embedding (first 5 values): {embedding[:5]}")
```

## Building a More Realistic Example

Now let's create a more practical search system with a larger document corpus:

```python
# realistic_search.py
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import json
from typing import List, Tuple

class SemanticSearchEngine:
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        """Initialize the search engine with a specified model."""
        print(f"Loading model: {model_name}")
        self.model = SentenceTransformer(model_name)
        self.documents = []
        self.index = None
        self.embeddings = None
        
    def add_documents(self, documents: List[str]):
        """Add documents to the search corpus."""
        print(f"Adding {len(documents)} documents...")
        self.documents.extend(documents)
        
        # Create embeddings for all documents
        all_embeddings = self.model.encode(self.documents, show_progress_bar=True)
        
        # Create or update FAISS index
        if self.index is None:
            dimension = all_embeddings.shape[1]
            self.index = faiss.IndexFlatL2(dimension)
        
        self.index.add(all_embeddings.astype('float32'))
        self.embeddings = all_embeddings
        print(f"Index now contains {self.index.ntotal} documents")
        
    def search(self, query: str, k: int = 5) -> List[Tuple[str, float]]:
        """Search for documents similar to the query."""
        if self.index is None:
            raise ValueError("No documents added to search engine")
            
        # Encode the query
        query_embedding = self.model.encode([query])
        
        # Perform search
        distances, indices = self.index.search(query_embedding.astype('float32'), k)
        
        # Convert to results with similarity scores
        results = []
        for distance, idx in zip(distances[0], indices[0]):
            if idx < len(self.documents):  # Valid index
                similarity = 1 / (1 + distance)
                results.append((self.documents[idx], similarity))
                
        return results
    
    def save_index(self, filepath: str):
        """Save the search index to disk."""
        if self.index is not None:
            faiss.write_index(self.index, f"{filepath}.faiss")
            with open(f"{filepath}_docs.json", 'w') as f:
                json.dump(self.documents, f)
            print(f"Index saved to {filepath}")
    
    def load_index(self, filepath: str):
        """Load a previously saved search index."""
        self.index = faiss.read_index(f"{filepath}.faiss")
        with open(f"{filepath}_docs.json", 'r') as f:
            self.documents = json.load(f)
        print(f"Index loaded from {filepath}")

# Example usage with technology articles
tech_articles = [
    "Python is a versatile programming language used for web development, data science, and automation",
    "Machine learning algorithms can identify patterns in large datasets to make predictions",
    "Cloud computing provides scalable infrastructure for modern applications",
    "Artificial intelligence is revolutionizing healthcare with diagnostic tools and treatment recommendations",
    "Blockchain technology ensures secure and transparent transactions in digital currencies",
    "Mobile app development requires understanding of user experience and interface design",
    "Cybersecurity threats are evolving rapidly requiring advanced protection mechanisms",
    "Data visualization helps analysts communicate insights effectively to stakeholders",
    "Internet of Things devices are creating smart homes and connected cities",
    "Virtual reality technology is transforming entertainment and education experiences",
    "Quantum computing promises to solve complex problems that classical computers cannot handle",
    "DevOps practices streamline software development and deployment processes",
    "Microservices architecture enables scalable and maintainable software systems",
    "Edge computing brings processing power closer to data sources for reduced latency",
    "5G networks provide faster connectivity for mobile devices and IoT applications"
]

# Initialize and populate the search engine
search_engine = SemanticSearchEngine()
search_engine.add_documents(tech_articles)

# Interactive search demo
print("\n" + "="*60)
print("INTERACTIVE SEMANTIC SEARCH DEMO")
print("="*60)
print("Try queries like:")
print("  - 'How to build mobile apps?'")
print("  - 'What is AI used for?'")
print("  - 'Tell me about network technologies'")
print("  - Type 'quit' to exit")
print("-"*60)

while True:
    query = input("\nEnter your search query: ").strip()
    
    if query.lower() in ['quit', 'exit', 'q']:
        break
        
    if not query:
        continue
        
    try:
        results = search_engine.search(query, k=3)
        print(f"\nResults for: '{query}'")
        print("-" * 40)
        
        for i, (doc, score) in enumerate(results, 1):
            print(f"{i}. [{score:.3f}] {doc}")
            
    except Exception as e:
        print(f"Error: {e}")

print("\nThanks for trying the semantic search demo!")
```

## Performance Analysis

Let's measure and understand the performance characteristics:

```python
# performance_test.py
import time
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

def benchmark_embedding_performance():
    """Benchmark different aspects of embedding performance."""
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Test data of varying sizes
    test_sizes = [10, 100, 1000, 5000]
    sample_text = "This is a sample document for performance testing. " * 10
    
    print("Embedding Performance Benchmark")
    print("="*50)
    print(f"{'Documents':<12} {'Encode Time':<12} {'Per Doc (ms)':<12} {'Memory (MB)':<12}")
    print("-" * 50)
    
    for size in test_sizes:
        documents = [f"{sample_text} Document {i}" for i in range(size)]
        
        # Measure encoding time
        start_time = time.time()
        embeddings = model.encode(documents, show_progress_bar=False)
        encode_time = time.time() - start_time
        
        # Calculate metrics
        per_doc_ms = (encode_time / size) * 1000
        memory_mb = embeddings.nbytes / (1024 * 1024)
        
        print(f"{size:<12} {encode_time:<12.2f} {per_doc_ms:<12.2f} {memory_mb:<12.2f}")

def benchmark_search_performance():
    """Benchmark search performance with different index sizes."""
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Create test corpus
    corpus_sizes = [1000, 5000, 10000, 50000]
    sample_text = "Sample document for search performance testing"
    
    print("\nSearch Performance Benchmark")
    print("="*50)
    print(f"{'Corpus Size':<12} {'Index Time':<12} {'Search Time':<12} {'QPS':<12}")
    print("-" * 50)
    
    for size in corpus_sizes:
        documents = [f"{sample_text} {i}" for i in range(size)]
        
        # Create embeddings and index
        start_time = time.time()
        embeddings = model.encode(documents, show_progress_bar=False)
        index = faiss.IndexFlatL2(embeddings.shape[1])
        index.add(embeddings.astype('float32'))
        index_time = time.time() - start_time
        
        # Test search performance
        query_embedding = model.encode(["test query"])
        
        # Warm up
        for _ in range(10):
            index.search(query_embedding.astype('float32'), 5)
        
        # Measure search time
        num_queries = 100
        start_time = time.time()
        for _ in range(num_queries):
            index.search(query_embedding.astype('float32'), 5)
        search_time = time.time() - start_time
        
        avg_search_time = search_time / num_queries
        qps = 1 / avg_search_time
        
        print(f"{size:<12} {index_time:<12.2f} {avg_search_time:<12.4f} {qps:<12.0f}")

if __name__ == "__main__":
    benchmark_embedding_performance()
    benchmark_search_performance()
```

## Understanding the Results

### What Makes This Work?

1. **Pre-trained Models**: The `all-MiniLM-L6-v2` model was trained on millions of text pairs to understand semantic similarity

2. **Vector Space Mathematics**: Similar concepts cluster together in the 384-dimensional space

3. **Efficient Search**: FAISS uses optimized algorithms for fast nearest neighbor search

4. **Distance Metrics**: L2 (Euclidean) distance provides a meaningful similarity measure

### Performance Characteristics

From our benchmarks, you'll typically see:

- **Encoding speed**: ~1-10ms per document for small models
- **Search speed**: Sub-millisecond for thousands of documents
- **Memory usage**: ~1.5KB per document (384 dimensions × 4 bytes)
- **Accuracy**: 60-70% similarity to human judgments

## Common Patterns and Variations

### Pattern 1: Batch Processing

For large document collections, process in batches:

```python
def encode_documents_in_batches(model, documents, batch_size=32):
    """Encode documents in batches for memory efficiency."""
    all_embeddings = []
    
    for i in range(0, len(documents), batch_size):
        batch = documents[i:i + batch_size]
        batch_embeddings = model.encode(batch)
        all_embeddings.extend(batch_embeddings)
        
        if i % (batch_size * 10) == 0:
            print(f"Processed {i + len(batch)}/{len(documents)} documents")
    
    return np.array(all_embeddings)
```

### Pattern 2: Similarity Thresholding

Filter results by minimum similarity:

```python
def search_with_threshold(search_engine, query, min_similarity=0.7, k=10):
    """Search with minimum similarity threshold."""
    results = search_engine.search(query, k=k)
    return [(doc, score) for doc, score in results if score >= min_similarity]
```

### Pattern 3: Hybrid Search

Combine keyword and semantic search:

```python
def hybrid_search(search_engine, query, documents, k=5):
    """Combine semantic and keyword-based search."""
    # Semantic search results
    semantic_results = search_engine.search(query, k=k*2)
    
    # Simple keyword search
    query_terms = query.lower().split()
    keyword_results = []
    
    for i, doc in enumerate(documents):
        score = sum(1 for term in query_terms if term in doc.lower())
        if score > 0:
            keyword_results.append((doc, score / len(query_terms)))
    
    # Combine and re-rank (simplified approach)
    combined_scores = {}
    
    for doc, score in semantic_results:
        combined_scores[doc] = score * 0.7  # Weight semantic search
    
    for doc, score in keyword_results:
        if doc in combined_scores:
            combined_scores[doc] += score * 0.3  # Add keyword score
        else:
            combined_scores[doc] = score * 0.3
    
    # Sort by combined score
    sorted_results = sorted(combined_scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_results[:k]
```

## Next Steps and Exploration

### Immediate Experiments You Can Try

1. **Different Models**: Try `all-mpnet-base-v2` for better accuracy
2. **Multilingual Search**: Use `paraphrase-multilingual-MiniLM-L12-v2`
3. **Domain-Specific**: Test with scientific text using `allenai-specter`
4. **Larger Corpus**: Load real datasets from your domain

### Understanding Limitations

This quick start demonstrates the basics, but production systems need:

- **Index persistence**: Save/load indexes to avoid recomputation
- **Incremental updates**: Add new documents without rebuilding
- **Distributed search**: Handle millions of documents across servers
- **Query optimization**: Handle complex queries and filters
- **Evaluation metrics**: Measure search quality systematically

## Chapter Summary

In just 5 minutes, you've built a working semantic search system that:

- **Understands meaning** beyond keyword matching
- **Processes natural language queries** effectively  
- **Scales** to thousands of documents
- **Provides similarity scores** for ranking results

The key insights from this quick start:

1. **Embeddings bridge human and machine understanding** by converting text to numerical vectors
2. **Pre-trained models work immediately** without domain-specific training
3. **Vector similarity search is fast and effective** for most applications
4. **The technology is mature and accessible** through simple APIs

### What's Next

This foundation prepares you for the deeper exploration in Chapter 3, where we'll:

- Understand the mathematical foundations of embeddings
- Compare all six embedding types in detail
- Learn when to choose each approach
- Implement more sophisticated search patterns

The quick start showed you **what's possible**. Chapter 3 will show you **how it works** and **when to use what**.

---

**Ready to go deeper?** Continue to [Chapter 3: Deep Dive into Embedding Types](03_embedding_types.md) to understand the theory and implementation details behind each embedding approach.
