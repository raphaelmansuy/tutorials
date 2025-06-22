"""
Example 1: Basic Contact Extraction (Beginner Level)
See tutorial for details.
"""
from google.adk.agents import LlmAgent
from google.adk.runtime import Runner
from google.adk.sessions import InMemorySessionService
from pydantic import BaseModel, Field
from google.genai import types
import asyncio

class ContactInfo(BaseModel):
    name: str = Field(description="Full name of the contact")
    email: str = Field(description="Email address")
    company: str = Field(description="Company name")
    phone: str = Field(description="Phone number if available", default="")
    position: str = Field(description="Job title or position", default="")

contact_extractor = LlmAgent(
    model="gemini-2.0-flash",
    name="contact_extractor",
    description="Extracts contact information from text",
    instruction="""Extract contact information from the provided text.\nFocus on accuracy and completeness. If information is unclear or missing,\nleave those fields empty rather than guessing.""",
    output_schema=ContactInfo,
    output_key="extracted_contacts"
)

session_service = InMemorySessionService()
runner = Runner(
    agent=contact_extractor,
    app_name="contact_extraction_app",
    session_service=session_service
)

async def extract_contacts(text_content):
    user_content = types.Content(role='user', parts=[types.Part(text=text_content)])
    async for event in runner.run_async(
        user_id="user_001",
        new_message=user_content
    ):
        if event.is_final_response() and event.content and event.content.parts:
            if event.content.parts[0].text:
                return event.content.parts[0].text
    return None

if __name__ == "__main__":
    sample_email = """Hi,\nMy name is Jane Doe, I work at Acme Corp. You can reach me at jane.doe@acme.com or 555-1234.\nBest,\nJane\n"""
    result = asyncio.run(extract_contacts(sample_email))
    print(result)
