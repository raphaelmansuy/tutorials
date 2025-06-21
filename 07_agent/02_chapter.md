# Chapter 2: ADK Foundations - Core Concepts

> *"Architecture is not just about building structures; it's about creating frameworks that enable endless possibilities."* - The ADK Design Philosophy

## Why This Chapter Matters: Building Your Mental Model

Imagine you're a master chef trying to cook with an unfamiliar kitchen. You might have the finest ingredients and the best recipes, but without understanding how the stove works, where the knives are kept, or how the oven heats, you'll struggle to create anything remarkable.

ADK is your new kitchen for building intelligent software. This chapter gives you the mental map you need to cook up agent systems that can transform your business. By the end, you'll think in "agent patterns" rather than traditional software architectures.

**The Promise:** After 20 minutes with this chapter, you'll understand ADK's core concepts well enough to architect your first multi-agent system and explain to your team why this approach is revolutionary.

---

## The ADK Universe: A Bird's Eye View

### The Three Pillars of ADK Architecture

Think of ADK like a modern city with three distinct districts, each serving a specific purpose but all connected by a sophisticated transportation system:

```mermaid
mindmap
  root((ADK Architecture))
    Agents
      LLM Agents
        Reasoning
        Language Understanding
        Dynamic Decision Making
      Workflow Agents
        Sequential Processing
        Parallel Execution
        Loop Orchestration
      Custom Agents
        Specialized Logic
        External Integrations
        Unique Behaviors
    Tools
      Function Tools
        Custom Business Logic
        API Integrations
        Data Processing
      Built-in Tools
        Google Search
        Code Execution
        File Processing
      Third-party Tools
        LangChain Integration
        CrewAI Tools
        OpenAPI Specs
    Runtime
      Sessions
        State Management
        User Context
        Conversation History
      Memory
        Long-term Storage
        Retrieval Systems
        Personalization
      Deployment
        Vertex AI Engine
        Cloud Run
        Local Development
```

**Pause and Reflect:** *Before diving deeper, think about a complex business process in your organization. Can you identify parts that require reasoning (LLM Agents), parts that follow predictable steps (Workflow Agents), and parts that need specialized logic (Custom Agents)?*

---

## Agent Types: The Heart of ADK

### 1. LLM Agents: The Intelligent Reasoners

LLM Agents are the "knowledge workers" of your agent ecosystem. They understand natural language, reason about complex problems, and make intelligent decisions.

**Real-World Analogy:** Think of them as your best consultants - they can analyze situations, provide insights, and adapt their approach based on context.

**When to Use LLM Agents:**

- **Complex decision-making** requiring interpretation
- **Natural language processing** and understanding
- **Dynamic problem-solving** where rules can't be predetermined
- **Creative tasks** like content generation or strategy development

**Example: Customer Service Intelligence**

```python
from google.adk.agents import Agent

customer_service_agent = Agent(
    name="customer_service_specialist",
    model="gemini-2.0-flash",
    instruction="""
    You are an expert customer service representative with 10 years of experience.
    
    Your approach:
    1. Listen actively to understand the customer's real concern
    2. Empathize with their situation
    3. Provide clear, actionable solutions
    4. Know when to escalate to human agents
    
    You have access to account information, order history, and policy documents.
    Always prioritize customer satisfaction while following company policies.
    """,
    tools=[
        get_account_info,
        check_order_status,
        process_refund,
        escalate_to_human
    ]
)
```

**The Magic Moment:** This agent doesn't just follow scripts - it understands context. A customer saying "I'm frustrated with this order" gets a different response than "I'd like to return this item," even though both might result in the same action.

### 2. Workflow Agents: The Process Orchestrators

Workflow Agents are the "project managers" of your system. They coordinate other agents, ensure processes follow the right sequence, and handle complex orchestration.

**The Three Workflow Patterns:**

#### Sequential Agents: Step-by-Step Processing

Perfect for processes that must happen in order, like onboarding or approval workflows.

```mermaid
flowchart TD
    A[Document Received] --> B[Validation Agent]
    B --> C{Valid?}
    C -->|Yes| D[Processing Agent]
    C -->|No| E[Rejection Agent]
    D --> F[Approval Agent]
    F --> G[Notification Agent]
    E --> H[Feedback Agent]
    
    style A fill:#e3f2fd
    style B fill:#f1f8e9
    style D fill:#e8f5e8
    style F fill:#fff3e0
    style G fill:#e0f2f1
    style E fill:#ffebee
    style H fill:#fce4ec
```

#### Parallel Agents: Concurrent Execution

When you need multiple tasks to happen simultaneously, like data gathering from multiple sources.

```mermaid
flowchart TD
    A[Analysis Request] --> B[Parallel Coordinator]
    B --> C[Market Data Agent]
    B --> D[News Analysis Agent]
    B --> E[Social Media Agent]
    B --> F[Competitor Agent]
    
    C --> G[Report Synthesis Agent]
    D --> G
    E --> G
    F --> G
    
    G --> H[Final Report]
    
    style A fill:#e3f2fd
    style B fill:#f3e5f5
    style C fill:#e8f5e8
    style D fill:#fff3e0
    style E fill:#fce4ec
    style F fill:#e1f5fe
    style G fill:#e0f2f1
    style H fill:#f1f8e9
```

#### Loop Agents: Iterative Workflows

For processes that need to repeat until a condition is met, like quality assurance or optimization tasks.

**Real-World Example: Content Optimization Loop**

```python
from google.adk.agents import LoopAgent

content_optimizer = LoopAgent(
    name="content_optimization_loop",
    agents=[
        content_analyzer,      # Analyzes current performance
        improvement_generator, # Suggests improvements
        content_updater,      # Applies changes
        performance_checker   # Validates improvements
    ],
    max_iterations=5,
    break_condition="performance_score > 0.85"
)
```

### 3. Custom Agents: The Specialists

Custom Agents are your "expert contractors" - they handle specialized tasks that require unique logic or external integrations.

**When to Build Custom Agents:**

- **Legacy system integration** with complex protocols
- **Specialized business rules** that can't be expressed in natural language
- **High-performance requirements** needing optimized execution
- **Unique data processing** patterns

**Example: Financial Compliance Agent**

```python
from google.adk.agents import BaseAgent

class ComplianceAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="compliance_checker")
        self.regulations = load_regulatory_database()
        self.risk_models = load_risk_models()
    
    async def run(self, input_data):
        # Custom compliance logic
        risk_score = self.calculate_risk(input_data)
        violations = self.check_violations(input_data)
        
        if risk_score > 0.8 or violations:
            return self.generate_compliance_report(input_data, violations)
        
        return {"status": "compliant", "risk_score": risk_score}
```

---

## Tools: Extending Agent Capabilities

### The Tool Ecosystem

Think of tools as the "skills" your agents can learn. Just as a human employee might learn to use Salesforce, Excel, or Photoshop, your agents can learn to use various tools to accomplish their tasks.

#### Function Tools: Your Custom Business Logic

These are tools you create to handle your specific business needs.

**Simple Function Tool Example:**

```python
def calculate_shipping_cost(
    weight: float, 
    destination: str, 
    shipping_method: str
) -> dict:
    """Calculate shipping cost based on weight, destination, and method.
    
    Args:
        weight: Package weight in pounds
        destination: Destination zip code
        shipping_method: 'standard', 'express', or 'overnight'
    
    Returns:
        Dictionary with cost and estimated delivery time
    """
    base_rates = {
        'standard': 5.99,
        'express': 12.99,
        'overnight': 24.99
    }
    
    base_cost = base_rates.get(shipping_method, 5.99)
    weight_cost = weight * 0.5
    
    # Simplified zone calculation
    if destination.startswith(('1', '2', '3')):  # East Coast
        zone_multiplier = 1.0
    else:  # West Coast
        zone_multiplier = 1.2
    
    total_cost = (base_cost + weight_cost) * zone_multiplier
    
    delivery_days = {
        'standard': 5,
        'express': 2,
        'overnight': 1
    }
    
    return {
        'cost': round(total_cost, 2),
        'estimated_delivery_days': delivery_days[shipping_method],
        'currency': 'USD'
    }
```

#### Built-in Tools: Ready-to-Use Capabilities

ADK comes with powerful built-in tools that handle common tasks:

- **Google Search Tool**: Real-time web information
- **Code Execution Tool**: Run Python code safely
- **File Processing Tools**: Handle documents, images, and data files
- **RAG (Retrieval-Augmented Generation)**: Search and use knowledge bases

#### Third-Party Tools: Ecosystem Integration

One of ADK's superpowers is seamless integration with existing tool ecosystems:

- **LangChain Tools**: Access to 100+ pre-built integrations
- **CrewAI Tools**: Specialized agent tools and capabilities
- **OpenAPI Integration**: Automatically create tools from API specifications

---

## Sessions and State: Memory That Matters

### Understanding Sessions

Sessions are how ADK maintains context across interactions. Think of them as the "memory" that allows your agents to have coherent, ongoing conversations.

**Session Hierarchy:**

```mermaid
graph TD
    A[Application Level] --> B[User Level]
    B --> C[Session Level]
    C --> D[Conversation Level]
    
    A --> E[Global Configuration<br/>Shared Resources]
    B --> F[User Preferences<br/>Historical Data]
    C --> G[Conversation Context<br/>Current State]
    D --> H[Message History<br/>Immediate Context]
    
    style A fill:#e3f2fd
    style B fill:#f1f8e9
    style C fill:#e8f5e8
    style D fill:#fff3e0
    style E fill:#fce4ec
    style F fill:#e1f5fe
    style G fill:#e0f2f1
    style H fill:#f3e5f5
```

### State Management Patterns

**State Prefixes in ADK:**

- `app:*` - Application-wide data (shared across all users)
- `user:*` - User-specific data (across all sessions)
- `session:*` - Session-specific data (current conversation)
- `temp:*` - Temporary data (not persisted)

**Practical Example: E-commerce Assistant**

```python
def update_shopping_cart(item_id: str, quantity: int, tool_context: ToolContext):
    """Add or update item in user's shopping cart."""
    
    # Get user's cart from session state
    cart = tool_context.state.get('cart', {})
    
    # Update cart
    if quantity > 0:
        cart[item_id] = {
            'quantity': quantity,
            'added_at': datetime.now().isoformat()
        }
    else:
        cart.pop(item_id, None)  # Remove if quantity is 0
    
    # Save back to session state
    tool_context.state['cart'] = cart
    
    # Update user's cart history
    user_cart_history = tool_context.state.get('user:cart_history', [])
    user_cart_history.append({
        'action': 'update',
        'item_id': item_id,
        'quantity': quantity,
        'timestamp': datetime.now().isoformat()
    })
    tool_context.state['user:cart_history'] = user_cart_history
    
    return {
        'status': 'success',
        'cart_total_items': sum(item['quantity'] for item in cart.values()),
        'message': f'Cart updated with {quantity} of item {item_id}'
    }
```

---

## Deployment Architecture: From Development to Production

### The Deployment Spectrum

ADK supports multiple deployment strategies, from local development to enterprise-scale production:

```mermaid
graph TD
    A[Local Development] --> B[Development Web UI]
    A --> C[Local API Server]
    
    D[Cloud Deployment] --> E[Vertex AI Agent Engine]
    D --> F[Cloud Run]
    D --> G[Google Kubernetes Engine]
    
    E --> H[Fully Managed<br/>Auto-scaling<br/>Built-in Monitoring]
    F --> I[Container-based<br/>Serverless<br/>Pay-per-use]
    G --> J[Full Control<br/>Custom Configuration<br/>Enterprise Features]
    
    style A fill:#e3f2fd
    style D fill:#f1f8e9
    style E fill:#e8f5e8
    style F fill:#fff3e0
    style G fill:#fce4ec
    style H fill:#e0f2f1
    style I fill:#f3e5f5
    style J fill:#e1f5fe
```

### Choosing Your Deployment Strategy

**Local Development (`adk web`)**

Perfect for:

- Initial development and testing
- Rapid prototyping
- Learning and experimentation

**Vertex AI Agent Engine**

Ideal for:

- Production applications with variable load
- Teams wanting minimal infrastructure management
- Applications requiring tight Google Cloud integration

**Cloud Run**

Best for:

- Containerized applications
- Predictable scaling requirements
- Cost-conscious deployments

**Google Kubernetes Engine (GKE)**

Choose when you need:

- Maximum control over infrastructure
- Complex multi-service architectures
- Enterprise security and compliance requirements

---

## Common Patterns and Anti-Patterns

### ✅ Effective Agent Patterns

**1. Single Responsibility Agents**

```python
# Good: Focused, single-purpose agent
email_classifier = Agent(
    name="email_classifier",
    instruction="Classify emails as urgent, normal, or low priority based on content and sender."
)

# Avoid: Kitchen sink agent
# universal_agent = Agent(
#     name="do_everything_agent",
#     instruction="Handle emails, process orders, generate reports, and manage inventory."
# )
```

**2. Hierarchical Agent Organization**

```python
# Coordinator agent that delegates to specialists
customer_service_coordinator = Agent(
    name="service_coordinator",
    instruction="Route customer inquiries to appropriate specialist agents.",
    sub_agents=[
        billing_specialist,
        technical_support_specialist,
        product_specialist
    ]
)
```

**3. Graceful Degradation**

```python
def robust_data_fetcher(query: str, tool_context: ToolContext) -> dict:
    """Fetch data with multiple fallback strategies."""
    
    # Try primary data source
    try:
        return fetch_from_primary_api(query)
    except APIException:
        # Fallback to secondary source
        try:
            return fetch_from_cache(query)
        except CacheException:
            # Final fallback
            return {
                'status': 'partial',
                'message': 'Using basic information due to system issues',
                'data': get_basic_info(query)
            }
```

### ❌ Anti-Patterns to Avoid

**1. Chatbot Thinking**

```python
# Anti-pattern: Treating agents like chatbots
bad_agent = Agent(
    instruction="Answer user questions"  # Too generic
)

# Better: Specific, actionable instructions
good_agent = Agent(
    instruction="""
    You are a technical support specialist for cloud infrastructure.
    
    When users report issues:
    1. Gather specific error messages and timestamps
    2. Check system status using diagnostic tools
    3. Provide step-by-step troubleshooting guidance
    4. Escalate to human engineers for complex issues
    """
)
```

**2. Synchronous Blocking**

```python
# Anti-pattern: Blocking operations
def slow_operation(data):
    time.sleep(30)  # Blocks entire system
    return process_data(data)

# Better: Asynchronous processing
async def efficient_operation(data, tool_context: ToolContext):
    # Start background task
    task_id = start_background_processing(data)
    
    # Store task reference
    tool_context.state['processing_task'] = task_id
    
    return {
        'status': 'processing',
        'task_id': task_id,
        'message': 'Processing started. Check back in a few minutes.'
    }
```

**3. State Pollution**

```python
# Anti-pattern: Storing everything in state
tool_context.state['temporary_calculation'] = complex_data
tool_context.state['debug_info'] = debug_data
tool_context.state['api_response_cache'] = response_data

# Better: Use appropriate state prefixes
tool_context.state['temp:calculation'] = complex_data  # Won't persist
tool_context.state['user:preferences'] = user_prefs   # User-specific
tool_context.state['session:context'] = session_data  # Session-specific
```

---

## Your Mental Model Checklist

Before moving to the next chapter, ensure you can answer these questions:

**Agent Types:**

- When would you use an LLM Agent vs. a Workflow Agent?
- What are the three types of Workflow Agents and their use cases?
- When should you build a Custom Agent?

**Tools:**

- How do Function Tools differ from Built-in Tools?
- What information should you include in a tool's docstring?
- How do you handle tool errors gracefully?

**Sessions and State:**

- What's the difference between session-level and user-level state?
- When would you use temporary state vs. persistent state?
- How do you maintain context across multiple agent interactions?

**Architecture:**

- How do you decide between different deployment options?
- What are the key patterns for agent organization?
- How do you avoid common anti-patterns?

---

## Hands-On Challenge: Design Your First Agent System

**Scenario:** You work for a mid-sized software company that needs to automate their customer onboarding process. Currently, it takes 5 days and involves 3 different departments.

**Your Challenge:** Design an agent system that can:

1. **Validate** new customer information
2. **Create** accounts in multiple systems
3. **Generate** personalized welcome materials
4. **Schedule** kickoff calls
5. **Monitor** progress and handle exceptions

**Design Questions:**

1. What types of agents would you use for each step?
2. What tools would each agent need?
3. How would you handle state management?
4. What would your escalation strategy be?
5. How would you deploy this system?

Spend 15 minutes sketching out your approach. We'll implement this system in later chapters!

---

## Pro Tips: Foundation Best Practices

**💡 Start with the Data Model**

Before building agents, map out your state structure. What data needs to persist? What's temporary? What's user-specific vs. global?

**💡 Design for Observability**

ADK provides excellent debugging tools. Use them! Name your agents and tools descriptively, and include meaningful logging.

**💡 Think in Workflows**

Even simple tasks often have multiple steps. Consider whether a single LLM Agent or a Workflow Agent with multiple steps would be more maintainable.

**💡 Plan for Failure**

Every external API call, every LLM interaction, every tool execution can fail. Build graceful degradation into your agent design from day one.

---

## Chapter Wrap-Up: Your Foundation is Set

You now have the mental model necessary to think in "agent patterns." You understand the three types of agents, how tools extend capabilities, and how sessions maintain context across interactions.

In the next chapter, we'll put this knowledge into practice by building your first complete agent system. You'll see how these concepts work together to create something truly powerful.

**Key Takeaways:**

- **LLM Agents** for intelligence and reasoning
- **Workflow Agents** for process orchestration  
- **Custom Agents** for specialized requirements
- **Tools** extend agent capabilities
- **Sessions** maintain context and state
- **Deployment** options scale from local to enterprise

**Remember:** The best agent architectures are simple, focused, and composable. Start small, think big, and build systems that can grow with your needs.

---

*Next Chapter Preview: "Your First Agent: Quick Wins" - Where we'll build a complete weather and news assistant that demonstrates all these concepts working together.*

**Quick Self-Check:**

1. What are the three types of agents in ADK?
2. What's the difference between session state and user state?
3. When would you use a Parallel Agent vs. a Sequential Agent?

*(Answers: 1. LLM Agents, Workflow Agents, Custom Agents 2. Session state is conversation-specific, user state persists across all sessions 3. Parallel for concurrent tasks, Sequential for ordered processes)*
