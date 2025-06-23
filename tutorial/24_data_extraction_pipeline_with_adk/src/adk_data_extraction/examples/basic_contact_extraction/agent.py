"""
Basic Contact Extraction - ADK Agent

This module defines the root agent for basic contact extraction.
It follows ADK conventions for agent discovery and execution.
"""

from google.adk.agents import Agent

from .agents import create_contact_extractor

# Create the root agent that ADK will discover
root_agent = Agent(
    name="basic_contact_extraction",
    model="gemini-2.0-flash",
    description="Extracts contact information from text documents and emails",
    instruction="""You are a contact information extraction specialist.

Your task is to extract structured contact information from the provided text.

Focus on:
- Names (first, last, full)
- Email addresses
- Phone numbers
- Company names
- Job titles
- Addresses

Return the information in a clear, structured format.""",
)

# For backwards compatibility, keep the pipeline class
class ContactExtractionPipeline:
    """Simple contact extraction pipeline following ADK patterns."""
    
    def __init__(self):
        self.contact_extractor = create_contact_extractor()

# Development/testing functions
def main():
    """CLI entry point for contact extraction testing."""
    print("This agent is designed to be run with 'adk web' or 'adk run'.")
    print("To test the agent, run from the examples directory:")
    print("  adk web")
    print("Then select 'basic_contact_extraction' from the dropdown.")


if __name__ == "__main__":
    main()
