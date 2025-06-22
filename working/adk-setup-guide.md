# Google ADK Setup Guide: Complete Installation and Configuration

## Overview

This comprehensive guide covers all the setup requirements for Google's Agent Development Kit (ADK) for structured data extraction. Choose the approach that best fits your needs and environment.

## Choose Your Approach

**🚀 Quick Start (Google AI Studio)**: Best for experimentation, prototyping, and personal projects  
**🏢 Production Ready (Vertex AI)**: Recommended for enterprise applications, team collaboration, and production deployments

---

## Approach 1: Google AI Studio Setup (Quickstart)

### Installation Requirements

```bash
# Install Google ADK and dependencies
pip install google-generativeai google-adk pydantic asyncio

# For additional document processing (optional)
pip install PyMuPDF python-docx pandas openpyxl
```

### API Key Configuration

1. Get your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Set your environment variable:

```bash
export GOOGLE_API_KEY="your-api-key-here"
```

Or in Python:

```python
import os
os.environ["GOOGLE_API_KEY"] = "your-api-key-here"
```

### Quick Test

```python
from google.adk.agents import LlmAgent
from google.adk.runtime import Runner
from google.adk.sessions import InMemorySessionService

# Test your setup with a simple agent
test_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="test_agent", 
    instruction="You are a helpful assistant."
)

print("✅ ADK setup successful!")
```

---

## Approach 2: Vertex AI Setup (Production Ready)

### Prerequisites

1. **Google Cloud Account**: Create a [Google Cloud account](https://console.cloud.google.com/freetrial) (new customers get $300 in free credits)
2. **Python Environment**: Python 3.10+ with terminal access
3. **Local IDE**: VS Code, PyCharm, or similar with terminal support

### Step 1: Set Up Google Cloud Project

1. In the [Google Cloud Console](https://console.cloud.google.com/projectselector2/home/dashboard), select or create a Google Cloud project
2. [Enable billing](https://cloud.google.com/billing/docs/how-to/verify-billing-enabled) for your project
3. [Enable the Vertex AI API](https://console.cloud.google.com/flows/enableapi?apiid=aiplatform.googleapis.com)

### Step 2: Configure Authentication

Install and configure the Google Cloud CLI:

```bash
# Install Google Cloud CLI (if not already installed)
# Visit: https://cloud.google.com/sdk/docs/install

# Update gcloud components
gcloud components update

# Authenticate and set up Application Default Credentials
gcloud auth application-default login

# Set your default project (optional but recommended)
gcloud config set project YOUR_PROJECT_ID
gcloud config set compute/region YOUR_PREFERRED_REGION  # e.g., us-central1
```

### Step 3: Install ADK and Dependencies

```bash
# Create and activate virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# macOS/Linux:
source .venv/bin/activate
# Windows CMD:
# .venv\Scripts\activate.bat
# Windows PowerShell:
# .venv\Scripts\Activate.ps1

# Install ADK and dependencies
pip install google-adk google-generativeai pydantic asyncio

# For additional document processing (optional)
pip install PyMuPDF python-docx pandas openpyxl
```

### Step 4: Configure Environment Variables

Create a `.env` file in your project directory:

```bash
# .env file for Vertex AI configuration
GOOGLE_CLOUD_PROJECT="your-project-id"
GOOGLE_CLOUD_LOCATION="us-central1"  # or your preferred region
GOOGLE_GENAI_USE_VERTEXAI="True"

# Optional: Set additional configuration
GOOGLE_APPLICATION_CREDENTIALS="path/to/service-account-key.json"  # if using service account
```

### Step 5: Verify Vertex AI Setup

```python
import os
from google.adk.agents import Agent

# Load environment variables
os.environ["GOOGLE_CLOUD_PROJECT"] = "your-project-id"
os.environ["GOOGLE_CLOUD_LOCATION"] = "us-central1"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"

# Test Vertex AI connection
def test_connection():
    """Test Vertex AI connection and authentication"""
    try:
        test_agent = Agent(
            name="vertex_test_agent",
            model="gemini-2.0-flash",
            description="Test agent for Vertex AI connection",
            instruction="You are a test assistant for Vertex AI setup verification."
        )
        print("✅ Vertex AI ADK setup successful!")
        print(f"📍 Project: {os.environ.get('GOOGLE_CLOUD_PROJECT')}")
        print(f"🌍 Region: {os.environ.get('GOOGLE_CLOUD_LOCATION')}")
        return True
    except Exception as e:
        print(f"❌ Setup failed: {str(e)}")
        print("💡 Check your authentication and project configuration")
        return False

# Run the test
test_connection()
```

### Step 6: Available Gemini Models on Vertex AI

When using Vertex AI, you have access to the following Gemini models:

```python
# Available models for Vertex AI
VERTEX_AI_MODELS = {
    "gemini-2.0-flash": "Latest model with advanced reasoning",
    "gemini-2.0-flash-lite": "Faster, more cost-effective option", 
    "gemini-1.5-pro": "Previous generation with strong performance",
    "gemini-1.5-flash": "Fast processing for simpler tasks"
}

# Example usage with different models
extraction_agent = Agent(
    name="document_extractor",
    model="gemini-2.0-flash",  # or "gemini-2.0-flash-lite" for faster processing
    description="Specialized document extraction agent",
    instruction="Extract structured data from documents with high accuracy."
)
```

---

## Key Differences: Google AI Studio vs Vertex AI

| Feature | Google AI Studio | Vertex AI |
|---------|------------------|-----------|
| **Authentication** | API Key | Service Account / ADC |
| **Rate Limits** | Lower limits | Higher enterprise limits |
| **Data Privacy** | Shared infrastructure | Private Google Cloud |
| **Monitoring** | Basic usage tracking | Full Cloud Monitoring integration |
| **Cost** | Pay-per-use pricing | Enterprise pricing with commitments |
| **Compliance** | Standard terms | Enterprise compliance (SOC2, HIPAA, etc.) |
| **Team Collaboration** | Individual accounts | Project-based team access |
| **Production Ready** | Development/Testing | Full production workloads |

### When to Use Each Approach

**Choose Google AI Studio when**:

- Building prototypes or proof-of-concepts
- Learning ADK and experimenting with agents
- Working on personal projects
- Need quick setup without cloud infrastructure

**Choose Vertex AI when**:

- Deploying production applications
- Need enterprise security and compliance
- Working with sensitive or proprietary data
- Require advanced monitoring and logging
- Building team-based applications
- Need higher rate limits and SLA guarantees

---

## Troubleshooting Common Setup Issues

### Google AI Studio Issues

```bash
# If API key authentication fails
export GOOGLE_API_KEY="your-key-here"
python -c "import os; print('API Key set:', bool(os.environ.get('GOOGLE_API_KEY')))"
```

### Vertex AI Issues

```bash
# Check authentication status
gcloud auth list

# Verify project configuration  
gcloud config list

# Test API access
gcloud auth application-default print-access-token

# Check enabled APIs
gcloud services list --enabled | grep aiplatform
```

### Python Environment Issues

```bash
# Verify ADK installation
pip show google-adk

# Check Python version (must be 3.10+)
python --version

# Test imports
python -c "from google.adk.agents import Agent; print('ADK import successful')"
```

---

## ADK Setup Guide

This guide helps you install and configure Google ADK for both prototyping and production.

---

## 1. Environment Setup
- Python 3.9 or newer
- Recommended: Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 2. Install Google ADK

```bash
pip install google-adk
```

---

## 3. Authentication

### For Google AI Studio (Prototyping)
- Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
- Set it as an environment variable:

```bash
export GOOGLE_API_KEY="your-api-key-here"
```

### For Vertex AI (Production)
- Create a Google Cloud project
- Enable Vertex AI API
- Create a Service Account and download the JSON key
- Set the environment variable:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account.json"
```

---

## 4. Test Your Installation

Run a simple ADK agent (see [Quick Start](24-adk-quick-start.md)) to verify everything works.

---

## 5. Troubleshooting
- If you see authentication errors, check your API key or credentials
- If you get import errors, ensure your virtual environment is active and ADK is installed
- For more help, see the [official ADK docs](https://google.github.io/adk-docs/)

---

## Next Steps

Once you've completed the setup:

1. **Return to the main tutorial**: [Structured Data Extraction with Google ADK](24-data-extraction-pipeline-with-adk.md)
2. **Explore ADK documentation**: [Google ADK Official Docs](https://google.github.io/adk-docs/)
3. **Try sample agents**: [ADK Sample Repository](https://github.com/google/adk-samples)
4. **Join the community**: [Google Cloud Community](https://www.googlecloudcommunity.com/)

---

## Additional Resources

- [Vertex AI Pricing Calculator](https://cloud.google.com/products/calculator)
- [Google AI Studio Rate Limits](https://ai.google.dev/pricing)
- [ADK Best Practices Guide](https://google.github.io/adk-docs/safety/)
- [Vertex AI Security Documentation](https://cloud.google.com/vertex-ai/docs/general/data-security)

---

*Last updated: June 22, 2025*
