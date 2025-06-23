# Basic Contact Extraction Agent

This agent extracts contact information from text documents and emails using the Google ADK framework.

## Features

- Extracts names (first, last, full)
- Identifies email addresses  
- Finds phone numbers
- Detects company names and job titles
- Locates addresses
- Returns structured, formatted output

## Structure

```
basic_contact_extraction/
├── agent.py              # Main ADK agent definition (root_agent)
├── agents/               # Agent definitions
│   └── __init__.py      # Contact extraction agent
├── schemas/             # Data models
│   └── __init__.py      # ContactInfo schema
├── cli.py               # Standalone Python CLI script
├── .env.example         # Environment variable template
└── README.md           # This file
```

## Setup

1. Ensure you have a `.env` file with your API key:
```bash
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY
```

2. Install dependencies (from project root):
```bash
make install
```

## Usage

### 1. ADK Web UI (Recommended)

From the project root, start the web interface:
```bash
make adk_web
```

Then open http://localhost:8000 and select "basic_contact_extraction" from the dropdown.

### 2. ADK Command Line

From the project root:
```bash
make adk_test_basic
```

Or directly from examples directory:
```bash
cd src/adk_data_extraction/examples
adk run basic_contact_extraction
```

### 3. Python CLI Script

Run the standalone Python CLI script:

```bash
# From project root
make python_cli_basic

# Or directly from the agent directory  
cd src/adk_data_extraction/examples/basic_contact_extraction
python cli.py --text "John Doe, john@example.com, 555-1234"
python cli.py --file path/to/document.txt
```

#### Python CLI Examples

```bash
# Extract from text
python cli.py --text "Contact: Jane Smith, CTO at TechCorp, jane.smith@techcorp.com, +1-555-999-8888"

# Extract from file
python cli.py --file sample_contacts.txt

# Help
python cli.py --help
```

## Example Prompts

Try these examples with any interface:

- "Extract contacts from: Hi, I'm John Doe at Acme Corp. Email: john.doe@acme.com, Phone: 555-1234"
- "Find contact info: Dr. Sarah Johnson, MD, Springfield Medical Center, phone (555) 123-4567, sarah.johnson@springfieldmed.org"
- "Parse this email signature: Bob Wilson, Sales Manager, Global Industries Inc., 123 Business St, Suite 100, New York, NY 10001, Phone: +1-212-555-0123, Email: bwilson@globalind.com"

## Example Input/Output

**Input:**
```
Hi,
My name is Jane Doe, I work at Acme Corp. 
You can reach me at jane.doe@acme.com or 555-1234.
Best,
Jane
```

**Output:**
```json
{
  "name": "Jane Doe",
  "email": "jane.doe@acme.com", 
  "company": "Acme Corp",
  "phone": "555-1234",
  "position": ""
}
```

## Integration

This agent can be integrated into larger workflows or applications using either:
- ADK's `InMemoryRunner` for programmatic access
- Direct import of the `root_agent` 
- REST API via `adk api_server`
