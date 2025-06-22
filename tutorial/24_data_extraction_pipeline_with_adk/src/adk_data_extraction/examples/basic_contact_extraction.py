"""
Example 1: Basic Contact Extraction (Beginner Level)
See tutorial for details.
"""

import asyncio

from google.adk.agents import LlmAgent
from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from pydantic import BaseModel, Field


class ContactInfo(BaseModel):
    """Schema for extracted contact information."""

    name: str = Field(description="Full name of the contact")
    email: str = Field(description="Email address")
    company: str = Field(description="Company name")
    phone: str = Field(description="Phone number if available", default="")
    position: str = Field(description="Job title or position", default="")


contact_extractor = LlmAgent(
    model="gemini-2.0-flash",
    name="contact_extractor",
    description="Extracts contact information from text",
    instruction="""Extract contact information from the provided text.
Focus on accuracy and completeness. If information is unclear or missing,
leave those fields empty rather than guessing.""",
    output_schema=ContactInfo,
    output_key="extracted_contacts",
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
)

session_service = InMemorySessionService()
runner = Runner(
    agent=contact_extractor,
    app_name="contact_extraction_app",
    session_service=session_service,
)


async def extract_contacts(text_content):
    """
    Extract contact information from the given text content using the contact_extractor agent.
    Creates a session, sends the text to the agent, and returns the extracted contact info as a string.

    Args:
        text_content (str): The text to extract contact information from.

    Returns:
        str or None: The extracted contact information as a string, or None if not found.
    """
    # Create a session first
    _session = await session_service.create_session(
        app_name="contact_extraction_app", user_id="user_001", session_id="session_001"
    )

    user_content = types.Content(
        role="user", 
        parts=[types.Part.from_text(text=text_content)]
    )
    async for event in runner.run_async(
        user_id="user_001",
        session_id="session_001",
        new_message=user_content,
    ):
        if event.is_final_response() and event.content and event.content.parts:
            if event.content.parts[0].text:
                return event.content.parts[0].text
    return None


def main():
    """CLI entry point for contact extraction."""
    SAMPLE_EMAIL = """Hi,\nMy name is Jane Doe, I work at Acme Corp. You can reach me at jane.doe@acme.com or 555-1234.\nBest,\nJane\n"""
    result = asyncio.run(extract_contacts(SAMPLE_EMAIL))
    print(result)


if __name__ == "__main__":
    main()
