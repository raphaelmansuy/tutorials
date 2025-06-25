# Vertex AI & Agent Engine Observability: A Practical Guide

This tutorial provides a comprehensive, step-by-step guide to implementing robust observability for your Vertex AI Generative AI and Agent Engine applications. You'll learn how to monitor, trace, and log your AI systems to ensure reliability, optimize performance, and control costs.

## 🎯 What You'll Build

By following this guide, you will create a complete observability solution for your Vertex AI applications, featuring:

- **Live Log Streaming:** Real-time logs from your Gemini API calls and Agent Engine deployments, sent directly to Google Cloud Logging.
- **Token Usage Tracking:** Detailed monitoring of token consumption with cost estimates, provided in structured JSON logs.
- **Request Tracing:** End-to-end tracing to identify performance bottlenecks and understand request flows.
- **Custom Dashboards:** Ready-to-use dashboards in the Google Cloud Console to visualize key metrics.
- **Agent Engine Built-in Observability:** Leverage Agent Engine's automatic integration with Google Cloud's operations suite.

## 🚀 Key Outcomes

Upon completing this tutorial, you will be able to:

- **Debug AI Issues Faster:** Use correlated logs and traces to resolve problems in seconds, not hours.
- **Prevent Costly Surprises:** Proactively monitor token usage and set up alerts to avoid unexpected expenses.
- **Ensure Compliance:** Implement comprehensive audit logging to meet security and compliance requirements.
- **Optimize Performance:** Leverage detailed latency and throughput metrics to enhance application performance.
- **Scale with Confidence:** Deploy production-grade monitoring and alerting to support your applications as they grow.

## 📖 Tutorial Structure

This tutorial is divided into two main paths, allowing you to choose the level of depth that best suits your needs:

- **⚡ Quick Wins Path (5 Minutes):** Get immediate, valuable insights into your applications with minimal setup.
- **🏢 Production Path (2-4 Hours):** Implement an enterprise-ready observability solution with advanced security, custom metrics, and automated alerting.

---

## ✅ Prerequisites

Before you begin, ensure you have the following set up:

### Required Tools and Accounts

- [ ] **Google Cloud Project:** You need a Google Cloud project with billing enabled.
- [ ] **Python:** Python 3.11 or higher must be installed on your local machine (Python 3.9+ is supported, but 3.11+ is recommended for optimal performance).
- [ ] **Google Cloud CLI:** The `gcloud` command-line tool should be installed and configured.
- [ ] **Permissions:** You need "Editor" or "Owner" permissions for the project, or a custom role with the necessary permissions.

### Required IAM Permissions

For the **Quick Wins Path**, you will need the following IAM roles:

- `roles/monitoring.viewer`: Allows you to view monitoring dashboards.
- `roles/cloudtrace.user`: Allows you to view trace data.

For the **Production Path**, you will also need these roles:

- `roles/monitoring.admin`: Allows you to configure custom metrics and alerts.
- `roles/cloudtrace.admin`: Allows you to configure trace settings.
- `roles/logging.admin`: Allows you to configure log-based metrics.
- `roles/iam.serviceAccountAdmin`: Allows you to manage service accounts.

### Cost Considerations

While many services used in this tutorial have a generous free tier, be aware of potential costs as you scale:

- **Vertex AI:** Pricing is based on token usage. See the [official pricing page](https://cloud.google.com/vertex-ai/pricing) for details.
- **Cloud Run:** You are charged for CPU and memory consumed by your container instances.
- **Cloud Logging/Monitoring/Tracing:** These services have free monthly allotments. Costs are incurred for data ingested or stored beyond the free tier.

> **💡 Recommendation:** Always set up budget alerts in your Google Cloud project to avoid unexpected charges.

### Dependency Installation

Install the required Python libraries by running the following command:

```bash
pip install google-genai>=1.21.0 \
            google-cloud-aiplatform>=1.71.0 \
            google-cloud-monitoring>=2.15.1 \
            google-cloud-trace>=1.13.0 \
            google-cloud-logging>=3.8.0 \
            opentelemetry-api>=1.20.0 \
            opentelemetry-sdk>=1.20.0 \
            opentelemetry-exporter-otlp>=1.20.0 \
            opentelemetry-instrumentation-flask>=0.41b0 \
            flask>=3.0.0 \
            gunicorn>=22.0.0 \
            langchain>=0.1.0 \
            langchain-google-vertexai>=2.0.0
```

> **📝 Important:** The Google Gen AI SDK (`google-genai`) replaces the deprecated `vertexai.generative_models` module. The Vertex AI generative models are deprecated as of June 2025 and will be removed in June 2026. For agents, we use the Vertex AI Agent Engine (formerly Reasoning Engine) which provides a managed runtime for deploying agents built with LangChain, LangGraph, and other frameworks.

### Verify Your Setup

Run the following commands to ensure your environment is correctly configured:

```bash
gcloud auth list
gcloud config get-value project
python --version
```

> **⚠️ Important:** If you do not have the required permissions, please work with your GCP administrator to have them granted. Alternatively, you can use a dedicated project for this tutorial where you have full access.

---

## 🧪 Quick Environment Test (2 minutes)

Before diving into the full tutorial, let's verify your environment is ready with a simple test.

### Step 1: Test Your Google Cloud Setup

Create a file named `test_setup.py` and run it to ensure your local environment can authenticate and connect to Google Cloud observability services.

```python
# test_setup.py
import google.cloud.logging
import google.cloud.monitoring_v3
import google.cloud.trace_v1
import sys

def test_gcp_setup():
    """Verify that GCP clients can be initialized."""
    try:
        google.cloud.logging.Client()
        print("✅ Cloud Logging client created successfully")
        google.cloud.monitoring_v3.MetricServiceClient()
        print("✅ Cloud Monitoring client created successfully")
        google.cloud.trace_v1.TraceServiceClient()
        print("✅ Cloud Trace client created successfully")
        print("\n🎉 Your environment is ready for the tutorial!")
        return True
    except Exception as e:
        print(f"❌ GCP setup test failed: {e}")
        return False

if __name__ == "__main__":
    success = test_gcp_setup()
    sys.exit(0 if success else 1)
```

```bash
python test_setup.py
```

### Step 2: Test Vertex AI Access

Next, create a file named `test_vertex_ai.py` to confirm you can access the Vertex AI Gemini API using the new Google Gen AI SDK.

```python
# test_vertex_ai.py
from google import genai
import sys

def test_vertex_ai():
    """Verify access to the Vertex AI Gemini API using Google Gen AI SDK."""
    try:
        # Create client for Vertex AI
        client = genai.Client(
            vertexai=True,
            project='your-project-id',  # Replace with your project ID
            location='us-central1'
        )
        print("✅ Google Gen AI client for Vertex AI created successfully")

        # Test Gemini API call
        response = client.models.generate_content(
            model='gemini-2.0-flash-001',
            contents='Hello!'
        )
        print("✅ Gemini API call successful")
        print(f"✅ Response received: {response.text[:40]}...")
        print(f"✅ Token usage: {response.usage_metadata.total_token_count} tokens")
        print("\n🎉 Vertex AI access is working!")
        return True
    except Exception as e:
        print(f"❌ Vertex AI test failed: {e}")
        return False

if __name__ == "__main__":
    success = test_vertex_ai()
    sys.exit(0 if success else 1)
```

```bash
python test_vertex_ai.py
```

### Expected Output

If everything is configured correctly, you should see output similar to this:

```text
✅ Cloud Logging client created successfully
✅ Cloud Monitoring client created successfully
✅ Cloud Trace client created successfully

🎉 Your environment is ready for the tutorial!

✅ Google Gen AI client for Vertex AI created successfully
✅ Gemini API call successful
✅ Response received: Hello! I am a large language model, trained by Google....
✅ Token usage: 12 tokens

🎉 Vertex AI access is working!
```

### ⚠️ If You See Errors

- **Authentication Issues:** If you see authentication errors, run `gcloud auth application-default login`.
- **Permission Issues:** Ensure your account has the required IAM roles listed in the prerequisites.
- **API Not Enabled:** If you see errors about APIs being disabled, run `gcloud services enable aiplatform.googleapis.com monitoring.googleapis.com logging.googleapis.com cloudtrace.googleapis.com`.

---

## 🧠 Understanding Observability: Metrics, Logs, and Traces

Before we dive in, let's briefly cover the three pillars of observability and how they apply to AI applications.

### The Three Pillars of Observability

```mermaid
flowchart TB
    subgraph "🔍 Observability Pillars"
        METRICS[📊 Metrics<br/>Numbers over time]
        LOGS[📋 Logs<br/>Event records]
        TRACES[🔗 Traces<br/>Request flows]
    end

    subgraph "🤖 AI Agent Example"
        REQUEST[User Query:<br/>What are your hours?]
        AGENT[ADK Agent Processing]
        TOOLS[Tool Execution]
        LLM[LLM Generation]
        RESPONSE[Agent Response]
    end

    subgraph "📈 What Each Pillar Shows"
        M_DATA[• Request count: 1,250/hour<br/>• Latency P95: 850ms<br/>• Token usage: 2,500<br/>• Error rate: 2.1%]
        L_DATA[• Query started: ID req_123<br/>• Tool get_hours executed<br/>• LLM response: 145 tokens<br/>• Query completed successfully]
        T_DATA[• Request span: 850ms<br/>• Tool span: 200ms<br/>• LLM span: 600ms<br/>• Response span: 50ms]
    end

    REQUEST --> AGENT
    AGENT --> TOOLS
    TOOLS --> LLM
    LLM --> RESPONSE

    AGENT -.->|Count, Rate, Duration| METRICS
    TOOLS -.->|Events, Errors, Details| LOGS
    REQUEST -.->|End-to-end Flow| TRACES

    METRICS --> M_DATA
    LOGS --> L_DATA
    TRACES --> T_DATA

    REQUEST --> LOGS
    RESPONSE --> LOGS


    style METRICS fill:#e6f4ea,stroke:#5bb974
    style LOGS fill:#e8f0fe,stroke:#4285f4
    style TRACES fill:#fef7e0,stroke:#fbbc04
    style M_DATA fill:#e6f4ea,stroke:#5bb974
    style L_DATA fill:#e8f0fe,stroke:#4285f4
    style T_DATA fill:#fef7e0,stroke:#fbbc04
```

### Direct LLM Generation Call Observability

For direct Vertex AI Gemini API calls, here's how the three pillars work together in practice:

```mermaid
flowchart LR
    subgraph "🚀 Direct LLM Call Flow"
        USER[User Request]
        API[Gemini API Call]
        MODEL[Gemini Model]
        RESP[Response]
    end

    subgraph "📊 Metrics Captured"
        M1[Request Rate:<br/>15 calls/min]
        M2[Latency P95:<br/>1.2 seconds]
        M3[Token Usage:<br/>2,847 tokens]
        M4[Cost Per Request:<br/>$0.0021]
    end

    subgraph "📋 Logs Generated"
        L0["User identified:<br/>user_id=abc123"]
        L1["Request started:<br/>model=gemini-2.5-flash<br/>prompt_length=156"]
        L2["Generation completed:<br/>tokens=2847<br/>duration=1180ms"]
        L3["Safety check passed:<br/>no_blocked_content"]
        L4["Response delivered:<br/>status=success"]
    end

    subgraph "🔗 Trace Spans"
        T1[Total Request: 1.18s]
        T2[API Authentication: 45ms]
        T3[Model Processing: 980ms]
        T4[Response Assembly: 155ms]
    end

    USER --> API
    API --> MODEL
    MODEL --> RESP

    API -.->|Count & Rate| M1
    API -.->|Duration| M2
    MODEL -.->|Token Count| M3
    RESP -.->|Cost Calc| M4

    USER -.->|User Info| L0
    API -.->|Start Event| L1
    MODEL -.->|Completion| L2
    MODEL -.->|Safety Info| L3
    RESP -.->|Final Status| L4

    USER -.->|Request Span| T1
    API -.->|Auth Span| T2
    MODEL -.->|Processing Span| T3
    RESP -.->|Response Span| T4

    style USER fill:#e3f2fd,stroke:#1976d2
    style API fill:#fff2cc,stroke:#d6b656
    style MODEL fill:#f8cecc,stroke:#b85450
    style RESP fill:#e8f5e8,stroke:#4caf50

    style M1 fill:#e6f4ea,stroke:#5bb974
    style M2 fill:#e6f4ea,stroke:#5bb974
    style M3 fill:#e6f4ea,stroke:#5bb974
    style M4 fill:#e6f4ea,stroke:#5bb974

    style L0 fill:#e8f0fe,stroke:#4285f4
    style L1 fill:#e8f0fe,stroke:#4285f4
    style L2 fill:#e8f0fe,stroke:#4285f4
    style L3 fill:#e8f0fe,stroke:#4285f4
    style L4 fill:#e8f0fe,stroke:#4285f4

    style T1 fill:#fef7e0,stroke:#fbbc04
    style T2 fill:#fef7e0,stroke:#fbbc04
    style T3 fill:#fef7e0,stroke:#fbbc04
    style T4 fill:#fef7e0,stroke:#fbbc04
```

---

## ⚡ Quick Wins Path (5 Minutes)

Get immediate observability for your AI applications with minimal setup. This section covers both direct Vertex AI Gemini API usage and ADK agents.

> **🎯 Success Criteria:** By the end of this section, you'll have logs, traces, and metrics working for your Generative AI applications in under 5 minutes.

### Option A: Direct Vertex AI Gemini Applications

#### 1. Instant Logging (30 seconds) ⚡

Add just three lines to your existing Gemini code to get started:

```python
# Add these 3 lines at the top of your script
import google.cloud.logging
client = google.cloud.logging.Client()
client.setup_logging()

# Your existing Gemini code works unchanged with the new Google Gen AI SDK
from google import genai
import logging

logger = logging.getLogger(__name__)

def generate_content(prompt: str):
    try:
        # Create client for Vertex AI using the new Google Gen AI SDK
        client = genai.Client(
            vertexai=True,
            project='your-project-id',  # Replace with your project ID
            location='us-central1'
        )

        response = client.models.generate_content(
            model='gemini-2.0-flash-001',
            contents=prompt
        )

        # This log will automatically appear in Cloud Logging
        logger.info(f"Generated response with {response.usage_metadata.total_token_count} tokens")
        return response.text

    except Exception as e:
        logger.error(f"Generation failed: {e}")
        raise

# Test it
result = generate_content("Write a short poem about observability")
print(result)
```

#### ✅ Checkpoint 1: Verify Basic Logging

1. **Run the code** and make a few requests.
2. **Go to the [Logs Explorer](https://console.cloud.google.com/logs/query)** in the Google Cloud Console.
3. Look for your logs under the "Global" resource type.
4. Filter by severity using the query `severity>=INFO`.

You should see log entries similar to this:

```text
2025-06-25 10:30:15  INFO  Generated response with 156 tokens
```

**🚨 Not seeing logs?**

- Check that your project ID is correct: `gcloud config get-value project`
- Verify that authentication is working: `gcloud auth list`
- Ensure the Cloud Logging API is enabled: `gcloud services list --enabled | grep logging`

#### 2. Structured Logging with Token Tracking (2 minutes) 📊

Enhance your logging with structured JSON payloads to track token usage and other metadata:

```python
import google.cloud.logging
import json
import time
from google import genai

# Setup Cloud Logging
client = google.cloud.logging.Client()
client.setup_logging()

import logging
logger = logging.getLogger(__name__)

def monitored_generate_content(prompt: str, model: str = "gemini-2.0-flash-001"):
    """Generate content with comprehensive logging using Google Gen AI SDK."""
    request_id = f"req_{int(time.time() * 1000)}"
    start_time = time.time()

    # Log the request start, including the prompt
    logger.info("Gemini request started", extra={
        "json_fields": {
            "request_id": request_id,
            "event_type": "request_start",
            "prompt": prompt,
            "model": model
        }
    })

    try:
        # Create client for Vertex AI using the new Google Gen AI SDK
        client = genai.Client(
            vertexai=True,
            project='your-project-id',  # Replace with your project ID
            location='us-central1'
        )

        response = client.models.generate_content(
            model=model,
            contents=prompt
        )

        duration_ms = (time.time() - start_time) * 1000
        usage = response.usage_metadata
        completion = response.text

        # Log successful completion with structured data
        logger.info("Gemini request completed", extra={
            "json_fields": {
                "request_id": request_id,
                "event_type": "request_success",
                "model": model,
                "prompt": prompt,
                "completion": completion,
                "total_tokens": usage.total_token_count,
                "prompt_tokens": usage.prompt_token_count,
                "completion_tokens": usage.candidates_token_count,
                "latency_ms": duration_ms,
                "success": True
            }
        })

        return {
            "text": completion,
            "request_id": request_id,
            "usage": {
                "total_tokens": usage.total_token_count
            }
        }

    except Exception as e:
        duration_ms = (time.time() - start_time) * 1000

        logger.error("Gemini request failed", extra={
            "json_fields": {
                "request_id": request_id,
                "event_type": "request_error",
                "model": model,
                "prompt": prompt,
                "error": str(e),
                "latency_ms": duration_ms,
                "success": False
            }
        })
        raise

# Test with structured logging
result = monitored_generate_content("Explain machine learning in simple terms")
print(f"Generated {result['usage']['total_tokens']} tokens")
```

#### ✅ Checkpoint 2: View Structured Logs

1. Go to the **[Logs Explorer](https://console.cloud.google.com/logs/query)**.
2. Switch to the "Advanced filter" mode.
3. Use the filter `jsonPayload.event_type="request_success"`.
4. Click on a log entry to see the structured JSON payload with token counts and other metadata.

#### 3. Add Tracing (3 minutes) 🔍

Add OpenTelemetry tracing to track request flows and identify performance bottlenecks:

```bash
# Install OpenTelemetry dependencies if you haven't already
pip install opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp opentelemetry-instrumentation-flask
```

```python
import google.cloud.logging
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor

# --- Observability Setup ---
# 1. Standard Logging Setup
logging_client = google.cloud.logging.Client()
logging_client.setup_logging()

# 2. OpenTelemetry Setup
trace.set_tracer_provider(TracerProvider())
span_processor = BatchSpanProcessor(OTLPSpanExporter())
trace.get_tracer_provider().add_span_processor(span_processor)
tracer = trace.get_tracer(__name__)
# --- End Observability Setup ---

from google import genai
from flask import Flask, request, jsonify
import logging
import os
import time

logger = logging.getLogger(__name__)

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)

def traced_generate_content(prompt: str, model: str = "gemini-2.0-flash-001"):
    """Generate content with tracing and logging using Google Gen AI SDK."""
    with tracer.start_as_current_span("gemini_generation") as span:
        span.set_attribute("model", model)
        span.set_attribute("prompt", prompt)
        span.set_attribute("prompt_length", len(prompt))

        request_id = f"req_{int(time.time() * 1000)}"
        start_time = time.time()

        try:
            # Create client for Vertex AI using the new Google Gen AI SDK
            client = genai.Client(
                vertexai=True,
                project='your-project-id',  # Replace with your project ID
                location='us-central1'
            )

            response = client.models.generate_content(
                model=model,
                contents=prompt
            )

            duration_ms = (time.time() - start_time) * 1000
            usage = response.usage_metadata
            completion = response.text

            # Add span attributes, including the response
            span.set_attribute("response_text", response.text)
            span.set_attribute("total_tokens", usage.total_token_count)
            span.set_attribute("duration_ms", duration_ms)
            span.set_attribute("success", True)

            # Log with trace correlation, including prompt and response
            logger.info("Traced Gemini request completed", extra={
                "json_fields": {
                    "request_id": request_id,
                    "prompt": prompt,
                    "response_text": response.text,
                    "total_tokens": usage.total_token_count,
                    "duration_ms": duration_ms,
                    "trace_id": format(span.get_span_context().trace_id, '032x')
                }
            })

            return response.text

        except Exception as e:
            span.set_attribute("error", str(e))
            span.set_attribute("success", False)
            logger.error(f"Traced request failed: {e}")
            raise

# Test with tracing
result = traced_generate_content("What is observability?")
print(result)
```

#### ✅ Checkpoint 3: View Traces

1. Go to the **[Trace Explorer](https://console.cloud.google.com/traces/list)**.
2. Find traces with the span name "gemini_generation".
3. Click on a trace to see the full request flow, including timing and attributes.

### Option B: Agent Engine Applications

Vertex AI Agent Engine (formerly Reasoning Engine) provides a managed runtime for deploying AI agents built with frameworks like LangChain, LangGraph, and others. Agent Engine automatically integrates with Google Cloud's observability suite without requiring additional setup.

#### Key Agent Engine Observability Features:

- **Automatic Integration:** Built-in logging, monitoring, and tracing with zero configuration
- **Structured Logs:** Agent logs are automatically sent to Cloud Logging with proper resource attribution
- **Built-in Metrics:** Request count, latency, CPU, and memory metrics are automatically captured
- **OpenTelemetry Support:** Native support for Cloud Trace with OpenTelemetry instrumentation
- **Dashboard Integration:** Pre-built dashboards in the Google Cloud Console

#### 1. Create a Simple Agent Engine Application (10 minutes) 🛠️

Let's create a simple agent using LangChain and deploy it to Agent Engine with built-in observability.

**Create the agent code (`langchain_agent.py`):**

```python
from typing import Union, List, Dict
import vertexai
from vertexai.preview import reasoning_engines
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_vertexai import ChatVertexAI
import logging

# The Agent Engine automatically handles logging setup
logger = logging.getLogger(__name__)

class ObservableAgent:
    def __init__(self, project: str, location: str) -> None:
        self.project_id = project
        self.location = location

    def set_up(self) -> None:
        """Initialize the LangChain components."""
        system = (
            "You are a helpful assistant that answers questions "
            "about Google Cloud services. Be concise and helpful."
        )
        human = "{text}"
        prompt = ChatPromptTemplate.from_messages(
            [("system", system), ("human", human)]
        )
        chat = ChatVertexAI(
            project=self.project_id,
            location=self.location,
            model_name="gemini-2.0-flash-001"
        )
        self.chain = prompt | chat

    def query(self, question: str) -> Union[str, List[Union[str, Dict]]]:
        """Query the agent with observability logging."""
        # Agent Engine automatically adds request tracing and logging
        logger.info(f"Processing query: {question}")

        try:
            response = self.chain.invoke({"text": question})
            logger.info(f"Query completed successfully")
            return response.content
        except Exception as e:
            logger.error(f"Query failed: {str(e)}")
            raise

# Test locally first
if __name__ == "__main__":
    import os
    PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT", "your-project-id")

    agent = ObservableAgent(project=PROJECT_ID, location="us-central1")
    agent.set_up()
    print(agent.query("What is Vertex AI?"))
```

#### 2. Deploy to Agent Engine (5 minutes) 🚀

Deploy your agent to the managed runtime with automatic observability:

```python
import vertexai
from vertexai.preview import reasoning_engines

# Initialize Vertex AI
PROJECT_ID = "your-project-id"  # Replace with your project ID
LOCATION = "us-central1"
vertexai.init(project=PROJECT_ID, location=LOCATION)

# Deploy the agent
reasoning_engine = reasoning_engines.ReasoningEngine.create(
    ObservableAgent(project=PROJECT_ID, location=LOCATION),
    requirements=[
        "google-cloud-aiplatform[langchain,reasoningengine]",
        "langchain-google-vertexai>=2.0.0",
        "cloudpickle==3.0.0",
        "pydantic==2.7.4",
    ],
    display_name="Observable LangChain Agent",
    description="A LangChain agent with built-in observability",
)

print(f"Agent deployed: {reasoning_engine.resource_name}")
```

#### 3. Test the Deployed Agent

```python
# Query the deployed agent
response = reasoning_engine.query(
    input={"question": "What are the benefits of using Agent Engine?"}
```

#### ✅ Checkpoint 4: View Agent Engine Observability

1. **View Logs in Cloud Logging:**

   - Go to [Logs Explorer](https://console.cloud.google.com/logs/query)
   - Filter by resource type: `Vertex AI Reasoning Engine`
   - You'll see structured logs for each query automatically

2. **View Metrics in Cloud Monitoring:**

   - Go to [Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer)
   - Search for "Vertex AI Reasoning Engine" metrics
   - View request count, latency, CPU, and memory metrics

3. **View Traces in Cloud Trace:**
   - Go to [Trace Explorer](https://console.cloud.google.com/traces/list)
   - Find traces with spans showing LangChain execution
   - View detailed timing for each component

**Sample Log Entry:**

```json
{
  "textPayload": "Processing query: What is Vertex AI?",
  "resource": {
    "type": "aiplatform.googleapis.com/ReasoningEngine",
    "labels": {
      "location": "us-central1",
      "reasoning_engine_id": "your-engine-id",
      "resource_container": "your-project-id"
    }
  },
  "timestamp": "2025-06-25T10:30:15.123Z",
  "logName": "projects/your-project-id/logs/python"
}
```

**Built-in Metrics Available:**

- `aiplatform.googleapis.com/reasoning_engine/request_count`
- `aiplatform.googleapis.com/reasoning_engine/request_latencies`
- `aiplatform.googleapis.com/reasoning_engine/cpu/allocation_time`
- `aiplatform.googleapis.com/reasoning_engine/memory/allocation_time`

#### Key Benefits of Agent Engine Observability

- **Zero Configuration:** Observability works out-of-the-box without any additional setup
- **Managed Infrastructure:** Google handles all the observability infrastructure
- **Integrated Dashboard:** Pre-built dashboards available in Google Cloud Console
- **Automatic Resource Attribution:** All logs and metrics are properly tagged with agent information
- **Enterprise Security:** VPC-SC support and enterprise-grade security features

---

## Advanced Observability with OpenTelemetry and Datadog

For organizations that require multi-platform observability or want to standardize on a vendor-neutral solution, **OpenTelemetry** is the industry standard. It provides a unified way to collect metrics, logs, and traces from your applications and export them to various backends, including Google Cloud, Datadog, and others.

### OpenTelemetry Architecture with Google Cloud

When you use OpenTelemetry, your application code is instrumented with the OpenTelemetry SDK. This SDK collects telemetry data and exports it. For Google Cloud, you can use an OTLP (OpenTelemetry Protocol) exporter that sends data directly to Cloud Monitoring, Cloud Trace, and Cloud Logging.

```mermaid
flowchart TB
    subgraph "Your Application"
        ADK[ADK Agent Code]
        OTEL_SDK[OpenTelemetry SDK]
    end

    subgraph "Google Cloud Observability"
        CL[Cloud Logging]
        CM[Cloud Monitoring]
        CT[Cloud Trace]
    end

    ADK --> OTEL_SDK
    OTEL_SDK --> CL
    OTEL_SDK --> CM
    OTEL_SDK --> CT

    style ADK fill:#e1f5fe,stroke:#0277bd
    style OTEL_SDK fill:#d5e8d4,stroke:#82b366
    style CL fill:#e8f0fe,stroke:#4285f4
    style CM fill:#e6f4ea,stroke:#5bb974
    style CT fill:#fef7e0,stroke:#fbbc04
```

### Multi-Platform Observability with Datadog

OpenTelemetry's real power comes from its flexibility. You can configure it to send telemetry data to multiple destinations simultaneously. This is ideal for organizations that use Datadog for their primary observability platform but still want to leverage Google Cloud's native integration.

A common pattern is to use the **OpenTelemetry Collector**, a standalone service that receives telemetry data, processes it, and exports it to one or more backends.

```mermaid
flowchart TB
    subgraph "Your Application"
        ADK[ADK Agent Code]
        OTEL_SDK[OpenTelemetry SDK]
    end

    subgraph "Data Processing"
        OTEL_COLLECTOR[OpenTelemetry Collector]
    end

    subgraph "Observability Backends"
        GCP[Google Cloud Observability]
        DATADOG[Datadog]
    end

    ADK --> OTEL_SDK
    OTEL_SDK --> OTEL_COLLECTOR
    OTEL_COLLECTOR --> GCP
    OTEL_COLLECTOR --> DATADOG

    style ADK fill:#e1f5fe,stroke:#0277bd
    style OTEL_SDK fill:#d5e8d4,stroke:#82b366
    style OTEL_COLLECTOR fill:#dae8fc,stroke:#6c8ebf
    style GCP fill:#e8f0fe,stroke:#4285f4
    style DATADOG fill:#632ca6,stroke:#632ca6,color:#fff
```

### Exporting to Datadog: Two Primary Approaches

#### Approach 1: OpenTelemetry Collector with Datadog Exporter

This approach uses the standard OpenTelemetry Collector with Datadog's exporter component.

**Benefits:**

- Complete vendor neutrality and flexibility.
- Centralized processing, batching, and sampling.
- Works without needing to install the Datadog Agent on every host.

**Conceptual Configuration (`collector.yaml`):**

```yaml
receivers:
  otlp:
    protocols:
      grpc:
      http:

exporters:
  datadog:
    api:
      key: ${DD_API_KEY}
  googlecloud:
    project: ${GCP_PROJECT_ID}

service:
  pipelines:
    traces:
      receivers: [otlp]
      exporters: [datadog, googlecloud]
    metrics:
      receivers: [otlp]
      exporters: [datadog, googlecloud]
```

#### Approach 2: Datadog Agent with OTLP Ingestion

This approach leverages the Datadog Agent's built-in OTLP support. Your application sends OTLP data to the Datadog Agent, which then forwards it to Datadog and potentially other backends.

**Benefits:**

- Access to all of Datadog's features, including 850+ integrations.
- Unified agent for metrics, logs, traces, and application security.
- Simplified fleet management through Datadog.

**Conceptual Configuration (`datadog.yaml`):**

```yaml
otlp_config:
  receiver:
    protocols:
      grpc:
        endpoint: "0.0.0.0:4317"
      http:
        endpoint: "0.0.0.0:4318"

logs_enabled: true
```

### Recommendations

- **For Google Cloud-first teams:** Start with the direct Google Cloud exporters. Add the OpenTelemetry Collector and Datadog exporter if you need to integrate with Datadog for specific use cases.
- **For Datadog-centric teams:** Use the OpenTelemetry Collector with dual exporters to get the best of both worlds. This gives you a unified view in Datadog while retaining deep integration with Google Cloud services.
- **For simplicity:** If you are already using the Datadog Agent for other monitoring, using its OTLP ingestion capabilities is often the easiest path.

By leveraging OpenTelemetry, you can build a flexible and future-proof observability strategy for your Vertex AI and ADK applications.

---

## 📚 References and Additional Resources

### Google Cloud Documentation

- **Vertex AI:**
  - [Vertex AI Documentation](https://cloud.google.com/vertex-ai/docs)
  - [Generative AI on Vertex AI](https://cloud.google.com/vertex-ai/docs/generative-ai/learn/overview)
  - [Vertex AI Pricing](https://cloud.google.com/vertex-ai/pricing)
- **ADK (Application Development Kit):**
  - [ADK Overview](https://cloud.google.com/adk/docs) (Note: Link is conceptual as ADK may be in private preview)
- **Observability:**
  - [Google Cloud's operations suite](https://cloud.google.com/products/operations)
  - [Cloud Logging Documentation](https://cloud.google.com/logging/docs)
  - [Cloud Monitoring Documentation](https://cloud.google.com/monitoring/docs)
  - [Cloud Trace Documentation](https://cloud.google.com/trace/docs)
- **Compute:**
  - [Cloud Run Documentation](https://cloud.google.com/run/docs)
  - [AI Agent Engine](https://cloud.google.com/vertex-ai/docs/agent-engine/overview) (Note: Link is conceptual as Agent Engine may be in private preview)

### OpenTelemetry

- [OpenTelemetry Project](https://opentelemetry.io/)
- [OpenTelemetry Python SDK](https://opentelemetry.io/docs/instrumentation/python/)
- [OTLP Exporter Specification](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/protocol/otlp.md)

### Third-Party Integrations

- [Datadog Documentation](https://docs.datadoghq.com/)
- [Datadog OpenTelemetry Integration](https://docs.datadoghq.com/opentelemetry/)

### Code and Libraries

- [google-cloud-python on GitHub](https://github.com/googleapis/google-cloud-python)
- [OpenTelemetry Python on GitHub](https://github.com/open-telemetry/opentelemetry-python)
