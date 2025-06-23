"""
Contact Extraction Agent - ADK Compliant Implementation

This module defines the contact extraction agent following ADK best practices:
- Clear agent name and description for routing
- Focused instruction for specialized task
- Output schema for structured data extraction
- Proper transfer control settings
"""

from google.adk.agents import LlmAgent

from ..schemas import ContactInfo


def create_contact_extractor() -> LlmAgent:
    """
    Create and configure the contact extraction agent.
    
    Returns:
        LlmAgent: Configured contact extraction agent
    """
    return LlmAgent(
        model="gemini-2.0-flash",
        name="contact_extractor",
        description="Extracts contact information from text documents and emails",
        instruction="""You are a contact information extraction specialist.

Your task is to extract structured contact information from the provided text.

Focus on:
- Accuracy and completeness
- Proper field mapping
- Data validation

If information is unclear or missing, leave those fields empty rather than guessing.
Always provide structured output following the ContactInfo schema.""",
        output_schema=ContactInfo,
        output_key="extracted_contacts",
        disallow_transfer_to_parent=True,
        disallow_transfer_to_peers=True,
    )
