# Chapter 4: Applying Embeddings to Retrieval Tasks

## Introduction to Task-Driven Embedding Selection

In Chapter 3, we explored the technical details of different embedding types. Now we'll shift focus to practical applications: how to choose and implement the right embedding approach for specific retrieval tasks. This chapter provides purpose-driven guides for common retrieval scenarios, complete with executable code and performance comparisons.

## Understanding Retrieval Task Categories

Different retrieval tasks have different requirements for accuracy, speed, interpretability, and resource usage. Let's map these requirements to optimal embedding strategies:

```mermaid
flowchart TD
    A[Retrieval Task] --> B{Primary Requirement}
    
    B --> C[Speed + Scale]
    B --> D[Accuracy]
    B --> E[Interpretability]
    B --> F[Resource Efficiency]
    
    C --> C1[Sparse Embeddings<br/>BM25, TF-IDF]
    C --> C2[Binary Embeddings<br/>Ultra-fast search]
    
    D --> D1[Dense Embeddings<br/>BERT, OpenAI]
    D --> D2[Multi-Vector<br/>ColBERT]
    
    E --> E1[Neural Sparse<br/>SPLADE]
    E --> E2[Traditional Sparse<br/>BM25 + analysis]
    
    F --> F1[Quantized<br/>8-bit, 4-bit]
    F --> F2[Variable-Dimension<br/>Matryoshka]
    
    C1 --> G[Document Search<br/>Legal, Academic]
    C2 --> H[Real-time Apps<br/>Mobile, Edge]
    D1 --> I[Semantic Search<br/>E-commerce, Q&A]
    D2 --> J[High-precision<br/>Research, Analysis]
    E1 --> K[Explainable AI<br/>Healthcare, Finance]
    E2 --> L[Traditional IR<br/>Libraries, Archives]
    F1 --> M[Large-scale<br/>Web search]
    F2 --> N[Adaptive Systems<br/>Multi-tier arch]
    
    style A fill:#f9f9f9,stroke:#333,stroke-width:3px,color:#000
    style B fill:#e1f5fe,stroke:#01579b,stroke-width:2px,color:#000
    style C fill:#ffebee,stroke:#c62828,stroke-width:2px,color:#000
    style D fill:#e8f5e8,stroke:#2e7d32,stroke-width:2px,color:#000
    style E fill:#fff3e0,stroke:#ef6c00,stroke-width:2px,color:#000
    style F fill:#f3e5f5,stroke:#6a1b9a,stroke-width:2px,color:#000
```

## Task 1: Keyword-Based Document Search

### Use Case Profile

**Goal**: Fast, exact-match retrieval for document collections where users search with specific terms.

**Examples**: Legal document search, academic paper retrieval, news article lookup.

**Requirements**:
- High precision for exact term matches
- Fast search across large collections
- Interpretable results (show why documents matched)
- Reliable handling of rare/technical terms

### Implementation with Sparse Embeddings

#### BM25-Based Document Search System

```python
import json
import math
import time
from collections import Counter, defaultdict
from typing import List, Dict, Tuple, Optional
import numpy as np

class DocumentSearchEngine:
    """Production-ready document search using BM25 with advanced features."""
    
    def __init__(self, k1: float = 1.2, b: float = 0.75):
        self.k1 = k1  # Term frequency saturation parameter
        self.b = b    # Length normalization parameter
        self.documents = []
        self.doc_metadata = []
        self.vocab = set()
        self.doc_freq = defaultdict(int)
        self.doc_tokens = []
        self.doc_lengths = []
        self.avg_doc_length = 0
        self.index_built = False
        
    def preprocess_text(self, text: str) -> List[str]:
        """Advanced text preprocessing for document search."""
        import re
        
        # Convert to lowercase and split
        text = text.lower()
        
        # Remove special characters but keep important punctuation
        text = re.sub(r'[^\w\s\-\.]', ' ', text)
        
        # Tokenize
        tokens = text.split()
        
        # Remove very short tokens and stop words
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
        tokens = [token for token in tokens if len(token) > 2 and token not in stop_words]
        
        return tokens
    
    def add_documents(self, documents: List[str], metadata: Optional[List[Dict]] = None):
        """Add documents to the search engine with optional metadata."""
        
        print(f"Adding {len(documents)} documents to index...")
        
        self.documents.extend(documents)
        
        # Add metadata (title, author, date, etc.)
        if metadata:
            self.doc_metadata.extend(metadata)
        else:
            self.doc_metadata.extend([{} for _ in documents])
        
        # Process new documents
        new_doc_tokens = []
        for doc in documents:
            tokens = self.preprocess_text(doc)
            new_doc_tokens.append(tokens)
            self.doc_lengths.append(len(tokens))
            
            # Update vocabulary and document frequency
            unique_tokens = set(tokens)
            for token in unique_tokens:
                self.vocab.add(token)
                self.doc_freq[token] += 1
        
        self.doc_tokens.extend(new_doc_tokens)
        self.avg_doc_length = sum(self.doc_lengths) / len(self.doc_lengths)
        self.index_built = True
        
        print(f"Index built: {len(self.documents)} documents, {len(self.vocab)} unique terms")
    
    def search(self, query: str, k: int = 10, min_score: float = 0.0) -> List[Tuple[int, float, str]]:
        """Search documents with BM25 scoring."""
        
        if not self.index_built:
            raise ValueError("No documents in index. Add documents first.")
        
        query_tokens = self.preprocess_text(query)
        scores = []
        
        for doc_idx, doc_tokens in enumerate(self.doc_tokens):
            score = self._calculate_bm25_score(query_tokens, doc_tokens, doc_idx)
            if score > min_score:
                scores.append((doc_idx, score))
        
        # Sort by score and return top-k with document text
        scores.sort(key=lambda x: x[1], reverse=True)
        results = []
        
        for doc_idx, score in scores[:k]:
            doc_text = self.documents[doc_idx]
            results.append((doc_idx, score, doc_text))
            
        return results
    
    def _calculate_bm25_score(self, query_tokens: List[str], doc_tokens: List[str], doc_idx: int) -> float:
        """Calculate BM25 score for a document."""
        
        doc_length = self.doc_lengths[doc_idx]
        term_freq = Counter(doc_tokens)
        score = 0.0
        
        for term in query_tokens:
            if term in self.vocab:
                tf = term_freq[term]
                df = self.doc_freq[term]
                
                # IDF calculation
                idf = math.log((len(self.documents) - df + 0.5) / (df + 0.5))
                
                # BM25 formula
                numerator = tf * (self.k1 + 1)
                denominator = tf + self.k1 * (1 - self.b + self.b * doc_length / self.avg_doc_length)
                
                score += idf * (numerator / denominator)
        
        return score
    
    def explain_search(self, query: str, doc_idx: int) -> Dict:
        """Explain why a document matched a query."""
        
        if doc_idx >= len(self.documents):
            raise ValueError(f"Document index {doc_idx} out of range")
        
        query_tokens = self.preprocess_text(query)
        doc_tokens = self.doc_tokens[doc_idx]
        doc_length = self.doc_lengths[doc_idx]
        term_freq = Counter(doc_tokens)
        
        explanation = {
            'query': query,
            'document_id': doc_idx,
            'document_length': doc_length,
            'avg_doc_length': self.avg_doc_length,
            'term_contributions': []
        }
        
        total_score = 0.0
        
        for term in query_tokens:
            if term in self.vocab:
                tf = term_freq[term]
                df = self.doc_freq[term]
                
                # Calculate components
                idf = math.log((len(self.documents) - df + 0.5) / (df + 0.5))
                numerator = tf * (self.k1 + 1)
                denominator = tf + self.k1 * (1 - self.b + self.b * doc_length / self.avg_doc_length)
                term_score = idf * (numerator / denominator)
                
                total_score += term_score
                
                explanation['term_contributions'].append({
                    'term': term,
                    'term_frequency': tf,
                    'document_frequency': df,
                    'idf': idf,
                    'bm25_component': term_score,
                    'in_document': tf > 0
                })
        
        explanation['total_score'] = total_score
        return explanation

# Example: Legal Document Search System
def create_legal_search_demo():
    """Demonstrate legal document search with BM25."""
    
    # Sample legal documents
    legal_documents = [
        "Patent application for machine learning algorithm in autonomous vehicle navigation systems. The invention relates to neural networks for real-time decision making in automotive environments.",
        "Contract agreement for software licensing between Technology Corp and Innovation Ltd. Terms include usage rights, liability limitations, and intellectual property provisions.",
        "Court ruling on data privacy violations in social media platforms. The court found that user consent was not properly obtained for personal data collection and processing.",
        "Employment contract containing non-disclosure agreement, competitive restrictions, and intellectual property assignment clauses for software engineers.",
        "Merger agreement between pharmaceutical companies regarding drug development collaboration and shared research facilities.",
        "Trademark dispute resolution involving brand name similarity in consumer electronics market. The plaintiff claims trademark infringement and unfair competition.",
        "Securities regulation compliance guidelines for financial technology startups handling customer investment portfolios and automated trading systems.",
        "Environmental impact assessment for renewable energy project including solar panel installation and battery storage systems."
    ]
    
    # Document metadata
    metadata = [
        {"type": "Patent", "date": "2024-01-15", "jurisdiction": "USPTO"},
        {"type": "Contract", "date": "2024-02-01", "parties": ["Tech Corp", "Innovation Ltd"]},
        {"type": "Court Ruling", "date": "2024-01-30", "court": "Federal District Court"},
        {"type": "Employment", "date": "2024-02-15", "category": "NDA"},
        {"type": "Merger", "date": "2024-01-20", "industry": "Pharmaceutical"},
        {"type": "Trademark", "date": "2024-02-10", "status": "Dispute"},
        {"type": "Regulation", "date": "2024-01-25", "authority": "SEC"},
        {"type": "Assessment", "date": "2024-02-05", "category": "Environmental"}
    ]
    
    # Create search engine
    search_engine = DocumentSearchEngine()
    search_engine.add_documents(legal_documents, metadata)
    
    # Test queries
    test_queries = [
        "machine learning patent autonomous vehicle",
        "software licensing contract intellectual property", 
        "data privacy user consent social media",
        "trademark dispute brand infringement",
        "financial technology compliance regulation"
    ]
    
    print("LEGAL DOCUMENT SEARCH RESULTS")
    print("=" * 50)
    
    for query in test_queries:
        print(f"\nQuery: '{query}'")
        print("-" * 40)
        
        # Perform search
        results = search_engine.search(query, k=3, min_score=0.5)
        
        for rank, (doc_idx, score, doc_text) in enumerate(results, 1):
            metadata_info = search_engine.doc_metadata[doc_idx]
            doc_type = metadata_info.get('type', 'Unknown')
            date = metadata_info.get('date', 'Unknown')
            
            print(f"{rank}. [{score:.3f}] ({doc_type}, {date})")
            print(f"   {doc_text[:100]}...")
            
        # Show explanation for top result
        if results:
            top_doc_idx = results[0][0]
            explanation = search_engine.explain_search(query, top_doc_idx)
            
            print(f"\nExplanation for top result:")
            for term_info in explanation['term_contributions'][:3]:
                term = term_info['term']
                tf = term_info['term_frequency']
                contribution = term_info['bm25_component']
                print(f"  '{term}': appears {tf} times, contributes {contribution:.3f} to score")

create_legal_search_demo()
```

#### Performance Optimization for Large Collections

```python
from typing import Set
import pickle
import sqlite3

class OptimizedDocumentSearch:
    """Optimized document search for large collections."""
    
    def __init__(self, db_path: str = "search_index.db"):
        self.db_path = db_path
        self.init_database()
        
    def init_database(self):
        """Initialize SQLite database for persistent storage."""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create tables
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS documents (
                id INTEGER PRIMARY KEY,
                content TEXT,
                metadata TEXT,
                length INTEGER
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS term_frequencies (
                doc_id INTEGER,
                term TEXT,
                frequency INTEGER,
                FOREIGN KEY (doc_id) REFERENCES documents (id)
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS document_frequencies (
                term TEXT PRIMARY KEY,
                frequency INTEGER
            )
        ''')
        
        # Create indexes for fast lookup
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_term_freq ON term_frequencies (term)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_doc_term ON term_frequencies (doc_id, term)')
        
        conn.commit()
        conn.close()
    
    def build_index(self, documents: List[str], metadata: List[Dict] = None):
        """Build inverted index in database."""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Clear existing data
        cursor.execute('DELETE FROM documents')
        cursor.execute('DELETE FROM term_frequencies')
        cursor.execute('DELETE FROM document_frequencies')
        
        print(f"Building index for {len(documents)} documents...")
        
        # Process documents
        doc_freq = defaultdict(int)
        
        for doc_id, doc_content in enumerate(documents):
            # Preprocess and tokenize
            tokens = self.preprocess_text(doc_content)
            doc_length = len(tokens)
            
            # Store document
            metadata_json = json.dumps(metadata[doc_id] if metadata else {})
            cursor.execute(
                'INSERT INTO documents (id, content, metadata, length) VALUES (?, ?, ?, ?)',
                (doc_id, doc_content, metadata_json, doc_length)
            )
            
            # Count term frequencies
            term_freq = Counter(tokens)
            unique_terms = set(tokens)
            
            # Store term frequencies
            for term, freq in term_freq.items():
                cursor.execute(
                    'INSERT INTO term_frequencies (doc_id, term, frequency) VALUES (?, ?, ?)',
                    (doc_id, term, freq)
                )
            
            # Update document frequencies
            for term in unique_terms:
                doc_freq[term] += 1
            
            if (doc_id + 1) % 1000 == 0:
                print(f"Processed {doc_id + 1} documents...")
        
        # Store document frequencies
        for term, freq in doc_freq.items():
            cursor.execute(
                'INSERT INTO document_frequencies (term, frequency) VALUES (?, ?)',
                (term, freq)
            )
        
        conn.commit()
        conn.close()
        print("Index building complete!")
    
    def search(self, query: str, k: int = 10) -> List[Tuple[int, float, str]]:
        """Fast search using database index."""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        query_terms = self.preprocess_text(query)
        
        # Get document count
        cursor.execute('SELECT COUNT(*) FROM documents')
        total_docs = cursor.fetchone()[0]
        
        # Get average document length
        cursor.execute('SELECT AVG(length) FROM documents')
        avg_length = cursor.fetchone()[0]
        
        # Calculate scores for documents containing query terms
        doc_scores = defaultdict(float)
        
        for term in query_terms:
            # Get document frequency
            cursor.execute('SELECT frequency FROM document_frequencies WHERE term = ?', (term,))
            df_result = cursor.fetchone()
            if not df_result:
                continue
                
            df = df_result[0]
            idf = math.log((total_docs - df + 0.5) / (df + 0.5))
            
            # Get term frequencies for documents containing this term
            cursor.execute('''
                SELECT tf.doc_id, tf.frequency, d.length 
                FROM term_frequencies tf 
                JOIN documents d ON tf.doc_id = d.id 
                WHERE tf.term = ?
            ''', (term,))
            
            for doc_id, tf, doc_length in cursor.fetchall():
                # BM25 calculation
                k1, b = 1.2, 0.75
                numerator = tf * (k1 + 1)
                denominator = tf + k1 * (1 - b + b * doc_length / avg_length)
                score = idf * (numerator / denominator)
                doc_scores[doc_id] += score
        
        # Get top-k results
        top_docs = sorted(doc_scores.items(), key=lambda x: x[1], reverse=True)[:k]
        
        results = []
        for doc_id, score in top_docs:
            cursor.execute('SELECT content FROM documents WHERE id = ?', (doc_id,))
            content = cursor.fetchone()[0]
            results.append((doc_id, score, content))
        
        conn.close()
        return results
    
    def preprocess_text(self, text: str) -> List[str]:
        """Text preprocessing (same as DocumentSearchEngine)."""
        import re
        text = text.lower()
        text = re.sub(r'[^\w\s\-\.]', ' ', text)
        tokens = text.split()
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
        return [token for token in tokens if len(token) > 2 and token not in stop_words]

# Performance testing
def benchmark_document_search():
    """Benchmark document search performance."""
    
    # Generate test documents
    import random
    
    def generate_document(doc_id):
        topics = [
            "machine learning artificial intelligence neural networks",
            "software engineering development programming languages",
            "data science analytics statistics visualization",
            "cybersecurity privacy encryption protocols",
            "cloud computing distributed systems scalability",
            "mobile applications user interface design",
            "database management systems query optimization",
            "blockchain cryptocurrency distributed ledger"
        ]
        
        topic = random.choice(topics)
        return f"Document {doc_id}: {topic} " + " ".join(random.choices(topic.split(), k=50))
    
    # Test with different collection sizes
    collection_sizes = [1000, 5000, 10000]
    
    for size in collection_sizes:
        print(f"\nBenchmarking with {size} documents:")
        
        documents = [generate_document(i) for i in range(size)]
        
        # Test basic search engine
        basic_engine = DocumentSearchEngine()
        
        start_time = time.time()
        basic_engine.add_documents(documents)
        basic_index_time = time.time() - start_time
        
        # Test optimized search engine
        optimized_engine = OptimizedDocumentSearch(f"test_{size}.db")
        
        start_time = time.time()
        optimized_engine.build_index(documents)
        optimized_index_time = time.time() - start_time
        
        # Search performance
        test_query = "machine learning data science"
        
        start_time = time.time()
        basic_results = basic_engine.search(test_query, k=10)
        basic_search_time = time.time() - start_time
        
        start_time = time.time()
        optimized_results = optimized_engine.search(test_query, k=10)
        optimized_search_time = time.time() - start_time
        
        print(f"  Basic engine - Index: {basic_index_time:.3f}s, Search: {basic_search_time:.3f}s")
        print(f"  Optimized engine - Index: {optimized_index_time:.3f}s, Search: {optimized_search_time:.3f}s")
        print(f"  Speedup - Index: {basic_index_time/optimized_index_time:.1f}x, Search: {basic_search_time/optimized_search_time:.1f}x")

# benchmark_document_search()
```

### When to Use Keyword-Based Search

**Optimal Scenarios:**

- **Legal and compliance documents**: Exact term matching is crucial
- **Technical documentation**: Users search for specific API names, error codes
- **Academic papers**: Researchers look for specific methodologies or terms
- **News and journalism**: Users search for names, places, events

**Performance Characteristics:**

- **Precision**: Excellent for exact matches
- **Speed**: Very fast (sub-millisecond for indexed collections)
- **Scalability**: Handles millions of documents efficiently
- **Interpretability**: Clear explanation of why documents matched

## Task 2: Semantic Search for E-commerce

### Use Case Profile

**Goal**: Help customers find products using natural language descriptions, even when they don't know exact product names.

**Examples**: "comfortable running shoes for long distances", "laptop for video editing under $1500".

**Requirements**:
- Understand semantic meaning and intent
- Handle synonyms and related concepts
- Rank by relevance to user needs
- Support multilingual queries

### Implementation with Dense Embeddings

```python
from sentence_transformers import SentenceTransformer, util
import pandas as pd
import numpy as np
import faiss
from typing import List, Dict, Tuple
import json

class EcommerceSemanticSearch:
    """Semantic search system for e-commerce products."""
    
    def __init__(self, model_name: str = 'all-mpnet-base-v2'):
        self.model = SentenceTransformer(model_name)
        self.products = []
        self.product_embeddings = None
        self.index = None
        self.embedding_dim = self.model.get_sentence_embedding_dimension()
        
        print(f"Initialized semantic search with model: {model_name}")
        print(f"Embedding dimension: {self.embedding_dim}")
    
    def create_product_description(self, product: Dict) -> str:
        """Create rich product description for embedding."""
        
        # Combine multiple product fields for better semantics
        description_parts = []
        
        if 'name' in product:
            description_parts.append(product['name'])
        
        if 'category' in product:
            description_parts.append(f"Category: {product['category']}")
        
        if 'brand' in product:
            description_parts.append(f"Brand: {product['brand']}")
        
        if 'description' in product:
            description_parts.append(product['description'])
        
        if 'features' in product:
            if isinstance(product['features'], list):
                description_parts.append("Features: " + ", ".join(product['features']))
            else:
                description_parts.append(f"Features: {product['features']}")
        
        if 'tags' in product:
            if isinstance(product['tags'], list):
                description_parts.append("Tags: " + ", ".join(product['tags']))
            else:
                description_parts.append(f"Tags: {product['tags']}")
        
        # Include price information semantically
        if 'price' in product:
            price = product['price']
            if price < 50:
                description_parts.append("affordable budget-friendly inexpensive")
            elif price < 200:
                description_parts.append("moderately priced good value")
            elif price < 500:
                description_parts.append("premium quality higher-end")
            else:
                description_parts.append("luxury high-end expensive premium")
        
        return ". ".join(description_parts)
    
    def add_products(self, products: List[Dict]):
        """Add products to the search index."""
        
        print(f"Adding {len(products)} products to semantic index...")
        
        self.products.extend(products)
        
        # Create enriched descriptions
        descriptions = []
        for product in products:
            description = self.create_product_description(product)
            descriptions.append(description)
        
        # Generate embeddings
        new_embeddings = self.model.encode(
            descriptions, 
            show_progress_bar=True,
            convert_to_numpy=True
        )
        
        # Update embeddings
        if self.product_embeddings is None:
            self.product_embeddings = new_embeddings
        else:
            self.product_embeddings = np.vstack([self.product_embeddings, new_embeddings])
        
        # Build FAISS index
        self.build_faiss_index()
        
        print(f"Index built with {len(self.products)} products")
    
    def build_faiss_index(self):
        """Build FAISS index for fast similarity search."""
        
        if self.product_embeddings is None:
            return
        
        # Create FAISS index
        self.index = faiss.IndexFlatIP(self.embedding_dim)  # Inner product for cosine similarity
        
        # Normalize embeddings for cosine similarity
        faiss.normalize_L2(self.product_embeddings)
        
        # Add to index
        self.index.add(self.product_embeddings.astype('float32'))
    
    def search(self, query: str, k: int = 10, filters: Dict = None) -> List[Tuple[Dict, float]]:
        """Search products with semantic understanding."""
        
        if self.index is None:
            raise ValueError("No products in index. Add products first.")
        
        # Encode query
        query_embedding = self.model.encode([query], convert_to_numpy=True)
        faiss.normalize_L2(query_embedding)
        
        # Search
        scores, indices = self.index.search(query_embedding.astype('float32'), k)
        
        results = []
        for score, idx in zip(scores[0], indices[0]):
            if idx < len(self.products):
                product = self.products[idx]
                
                # Apply filters if specified
                if filters and not self.apply_filters(product, filters):
                    continue
                
                results.append((product, float(score)))
        
        return results
    
    def apply_filters(self, product: Dict, filters: Dict) -> bool:
        """Apply filtering criteria to products."""
        
        for filter_key, filter_value in filters.items():
            if filter_key == 'price_range':
                min_price, max_price = filter_value
                if 'price' in product:
                    if not (min_price <= product['price'] <= max_price):
                        return False
            
            elif filter_key == 'category':
                if 'category' in product:
                    if product['category'].lower() != filter_value.lower():
                        return False
            
            elif filter_key == 'brand':
                if 'brand' in product:
                    if product['brand'].lower() != filter_value.lower():
                        return False
            
            elif filter_key == 'rating_min':
                if 'rating' in product:
                    if product['rating'] < filter_value:
                        return False
        
        return True
    
    def get_recommendations(self, product_id: str, k: int = 5) -> List[Tuple[Dict, float]]:
        """Get product recommendations based on similarity."""
        
        # Find the product
        target_product = None
        target_idx = None
        
        for idx, product in enumerate(self.products):
            if product.get('id') == product_id:
                target_product = product
                target_idx = idx
                break
        
        if target_product is None:
            raise ValueError(f"Product with ID {product_id} not found")
        
        # Get embedding for target product
        target_embedding = self.product_embeddings[target_idx:target_idx+1]
        
        # Search for similar products
        scores, indices = self.index.search(target_embedding.astype('float32'), k + 1)  # +1 to exclude self
        
        recommendations = []
        for score, idx in zip(scores[0], indices[0]):
            if idx != target_idx and idx < len(self.products):  # Exclude the target product itself
                similar_product = self.products[idx]
                recommendations.append((similar_product, float(score)))
        
        return recommendations[:k]

# Create sample e-commerce data
def create_sample_products():
    """Create sample product data for demonstration."""
    
    products = [
        {
            "id": "shoe_001",
            "name": "UltraRun Pro Running Shoes",
            "category": "Athletic Footwear",
            "brand": "SportMax",
            "price": 129.99,
            "rating": 4.5,
            "description": "Lightweight running shoes with advanced cushioning technology for long-distance running",
            "features": ["Breathable mesh upper", "Memory foam insole", "Shock absorption", "Lightweight design"],
            "tags": ["running", "athletic", "comfort", "durable", "sports"]
        },
        {
            "id": "laptop_001", 
            "name": "ProEdit 15 Creative Workstation",
            "category": "Computers",
            "brand": "TechCorp",
            "price": 1299.99,
            "rating": 4.7,
            "description": "Powerful laptop designed for video editing and creative professionals",
            "features": ["Intel i7 processor", "32GB RAM", "1TB SSD", "4K display", "Dedicated graphics"],
            "tags": ["video editing", "creative", "professional", "powerful", "laptop"]
        },
        {
            "id": "headphones_001",
            "name": "SoundWave Noise-Canceling Headphones",
            "category": "Audio",
            "brand": "AudioTech",
            "price": 199.99,
            "rating": 4.3,
            "description": "Premium wireless headphones with active noise cancellation",
            "features": ["Active noise cancellation", "30-hour battery", "Wireless Bluetooth", "Premium sound"],
            "tags": ["wireless", "noise-canceling", "premium", "music", "travel"]
        },
        {
            "id": "watch_001",
            "name": "FitTracker Pro Smartwatch",
            "category": "Wearables",
            "brand": "HealthTech",
            "price": 299.99,
            "rating": 4.2,
            "description": "Advanced fitness tracking smartwatch with health monitoring",
            "features": ["Heart rate monitor", "GPS tracking", "Sleep analysis", "Water resistant"],
            "tags": ["fitness", "health", "tracking", "smartwatch", "sport"]
        },
        {
            "id": "shoe_002",
            "name": "Comfort Walk Casual Sneakers",
            "category": "Casual Footwear", 
            "brand": "ComfortBrand",
            "price": 79.99,
            "rating": 4.1,
            "description": "Everyday comfortable sneakers perfect for walking and casual wear",
            "features": ["Memory foam sole", "Breathable fabric", "Casual design", "All-day comfort"],
            "tags": ["casual", "comfortable", "walking", "everyday", "sneakers"]
        },
        {
            "id": "laptop_002",
            "name": "BudgetBook Essential Laptop",
            "category": "Computers",
            "brand": "ValueTech",
            "price": 449.99,
            "rating": 3.8,
            "description": "Affordable laptop for basic computing needs and students",
            "features": ["Intel i3 processor", "8GB RAM", "256GB SSD", "14-inch display"],
            "tags": ["budget", "affordable", "student", "basic", "portable"]
        }
    ]
    
    return products

# Demonstration
def ecommerce_search_demo():
    """Demonstrate e-commerce semantic search capabilities."""
    
    # Create search engine
    search_engine = EcommerceSemanticSearch()
    
    # Add sample products
    products = create_sample_products()
    search_engine.add_products(products)
    
    # Test semantic search queries
    test_queries = [
        "comfortable shoes for long runs",
        "powerful computer for video editing under 1500",
        "wireless headphones for travel",
        "budget laptop for college student",
        "fitness watch with heart rate monitoring"
    ]
    
    print("\nE-COMMERCE SEMANTIC SEARCH RESULTS")
    print("=" * 50)
    
    for query in test_queries:
        print(f"\nQuery: '{query}'")
        print("-" * 40)
        
        results = search_engine.search(query, k=3)
        
        for rank, (product, score) in enumerate(results, 1):
            print(f"{rank}. [{score:.3f}] {product['name']}")
            print(f"   {product['brand']} | ${product['price']} | ⭐{product['rating']}")
            print(f"   {product['description'][:80]}...")
    
    # Test product recommendations
    print(f"\n\nRECOMMENDATIONS")
    print("=" * 50)
    
    target_product_id = "shoe_001"
    target_product = next(p for p in products if p['id'] == target_product_id)
    
    print(f"Based on: {target_product['name']}")
    print("-" * 40)
    
    recommendations = search_engine.get_recommendations(target_product_id, k=3)
    
    for rank, (product, score) in enumerate(recommendations, 1):
        print(f"{rank}. [{score:.3f}] {product['name']}")
        print(f"   {product['brand']} | ${product['price']}")
    
    # Test with filters
    print(f"\n\nFILTERED SEARCH")
    print("=" * 50)
    
    query = "laptop computer"
    filters = {'price_range': (400, 800), 'category': 'Computers'}
    
    print(f"Query: '{query}'")
    print(f"Filters: Price $400-$800, Category: Computers")
    print("-" * 40)
    
    filtered_results = search_engine.search(query, k=5, filters=filters)
    
    for rank, (product, score) in enumerate(filtered_results, 1):
        print(f"{rank}. [{score:.3f}] {product['name']}")
        print(f"   ${product['price']} | {product['category']}")

ecommerce_search_demo()
```

### Advanced Semantic Search Features

#### Multi-Modal Search with Image and Text

```python
from PIL import Image
import torch
from transformers import CLIPProcessor, CLIPModel

class MultiModalEcommerceSearch:
    """Multi-modal search combining text and images."""
    
    def __init__(self):
        # Load CLIP model for multi-modal embeddings
        self.clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
        self.clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.clip_model.to(self.device)
        
        print("Loaded CLIP model for multi-modal search")
    
    def encode_text(self, text: str) -> np.ndarray:
        """Encode text using CLIP."""
        inputs = self.clip_processor(text=[text], return_tensors="pt").to(self.device)
        
        with torch.no_grad():
            text_features = self.clip_model.get_text_features(**inputs)
            text_features = text_features / text_features.norm(dim=-1, keepdim=True)
        
        return text_features.cpu().numpy()
    
    def encode_image(self, image_path: str) -> np.ndarray:
        """Encode image using CLIP."""
        image = Image.open(image_path)
        inputs = self.clip_processor(images=image, return_tensors="pt").to(self.device)
        
        with torch.no_grad():
            image_features = self.clip_model.get_image_features(**inputs)
            image_features = image_features / image_features.norm(dim=-1, keepdim=True)
        
        return image_features.cpu().numpy()
    
    def search_by_image(self, image_path: str, products: List[Dict], k: int = 5):
        """Search products using an image query."""
        
        # Encode query image
        query_embedding = self.encode_image(image_path)
        
        # Encode product images or descriptions
        product_embeddings = []
        for product in products:
            if 'image_path' in product:
                product_embedding = self.encode_image(product['image_path'])
            else:
                # Fall back to text description
                description = product.get('description', product.get('name', ''))
                product_embedding = self.encode_text(description)
            
            product_embeddings.append(product_embedding)
        
        product_embeddings = np.vstack(product_embeddings)
        
        # Compute similarities
        similarities = np.dot(query_embedding, product_embeddings.T).flatten()
        
        # Get top-k results
        top_indices = np.argsort(similarities)[::-1][:k]
        
        results = []
        for idx in top_indices:
            if similarities[idx] > 0.1:  # Minimum similarity threshold
                results.append((products[idx], similarities[idx]))
        
        return results

# Example usage would require actual product images
# multi_modal_search = MultiModalEcommerceSearch()
# results = multi_modal_search.search_by_image("query_image.jpg", products)
```

### Performance Characteristics

**Advantages of Dense Embeddings for E-commerce:**

- **Semantic understanding**: Finds products even with different terminology
- **Intent recognition**: Understands user needs beyond exact matches
- **Multilingual support**: Single model works across languages
- **Recommendation quality**: Excellent for "similar products" features

**Performance Metrics:**

- **Relevance**: 70-85% user satisfaction in A/B tests
- **Search speed**: ~10ms for 100K products
- **Memory usage**: ~1.5KB per product (384-dim embeddings)
- **Coverage**: Handles 95%+ of natural language queries

## Chapter Summary

This chapter demonstrated how to apply different embedding types to specific retrieval tasks:

### Task-Embedding Mapping

1. **Keyword-based Document Search** → **Sparse Embeddings (BM25)**
   - Optimal for exact term matching
   - Excellent interpretability
   - Fast performance on large collections

2. **Semantic E-commerce Search** → **Dense Embeddings (Sentence Transformers)**
   - Superior understanding of user intent
   - Handles synonyms and related concepts
   - Enables sophisticated recommendation systems

### Key Implementation Patterns

**For Production Systems:**

- **Database indexing** for sparse embeddings (inverted indexes)
- **FAISS integration** for dense embeddings (vector search)
- **Hybrid approaches** combining multiple embedding types
- **Filtering and faceting** for refined search experiences

### Performance Considerations

```mermaid
graph TD
    A[Retrieval Task] --> B{Collection Size}
    
    B --> C[Small < 10K]
    B --> D[Medium 10K-1M] 
    B --> E[Large > 1M]
    
    C --> C1[In-memory search<br/>Any embedding type]
    D --> D1[FAISS indexes<br/>Dense embeddings]
    D --> D2[Database indexes<br/>Sparse embeddings]
    E --> E1[Distributed search<br/>Quantized embeddings]
    E --> E2[Tiered architecture<br/>Variable-dimension]
    
    style A fill:#f9f9f9,stroke:#333,stroke-width:3px,color:#000
    style B fill:#e1f5fe,stroke:#01579b,stroke-width:2px,color:#000
    style C fill:#e8f5e8,stroke:#2e7d32,stroke-width:2px,color:#000
    style D fill:#fff3e0,stroke:#ef6c00,stroke-width:2px,color:#000
    style E fill:#ffebee,stroke:#c62828,stroke-width:2px,color:#000
```

### What's Next

In the following chapters, we'll explore:

- **Chapter 5**: Complete implementation guides for production systems
- **Chapter 6**: Real-world case studies and industry applications  
- **Chapter 7**: Advanced topics including the remaining embedding types

The foundation established in this chapter - understanding how to match tasks with appropriate embedding types - is crucial for building effective retrieval systems.

---

**Continue to [Chapter 5: Practical Implementation Guide](05_practical_implementation.md)** to learn how to deploy these approaches in production environments.
