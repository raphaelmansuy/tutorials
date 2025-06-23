#!/usr/bin/env python3
"""
Contact Extraction Demo - Python CLI

This script demonstrates how to use the basic contact extraction functionality
directly using the ADK framework without complex module imports.

Usage:
    python contact_demo.py "Contact text to analyze..."
"""

import asyncio
import os
import sys
from pathlib import Path

# Ensure we can import google.adk
try:
    from google.adk import Agent
    from google.adk.runners import InMemoryRunner
    from google.genai.types import Part, UserContent
except ImportError as e:
    print(f"❌ Error: Could not import ADK modules. Make sure you have activated the virtual environment.")
    print(f"Details: {e}")
    print("Run: source .venv/bin/activate")
    sys.exit(1)


def create_contact_extraction_agent():
    """Create a simple contact extraction agent."""
    return Agent(
        name="contact_extraction_demo",
        model="gemini-2.0-flash",
        description="Extracts contact information from text",
        instruction="""You are a contact information extraction specialist.

Extract structured contact information from the provided text, including:
- Names (first, last, full)
- Email addresses
- Phone numbers  
- Company names
- Job titles
- Addresses

Return the information in a clear, structured format.""",
    )


async def extract_contacts(text: str) -> None:
    """
    Extract contacts from text using a simple ADK agent.
    
    Args:
        text: The text to extract contacts from
    """
    print("🔍 Extracting contacts from text...")
    print(f"📄 Input: {text[:100]}{'...' if len(text) > 100 else ''}")
    print("-" * 50)
    
    # Create agent
    agent = create_contact_extraction_agent()
    
    # Create runner
    runner = InMemoryRunner(agent=agent)
    
    # Create a session
    session = await runner.session_service.create_session(
        app_name=runner.app_name,
        user_id="demo_user"
    )
    
    # Create user content
    content = UserContent(parts=[Part(text=text)])
    
    # Run the agent
    print("🤖 Running contact extraction agent...")
    event_count = 0
    
    async for event in runner.run_async(
        user_id=session.user_id,
        session_id=session.id,
        new_message=content,
    ):
        event_count += 1
        print(f"\n📋 Event {event_count} (Author: {event.author}):")
        
        if event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    print(f"   {part.text}")
    
    print(f"\n✅ Extraction complete! Processed {event_count} events.")


def main():
    """Main CLI entry point."""
    if len(sys.argv) != 2:
        print("Usage: python contact_demo.py \"Contact text to analyze...\"")
        print("\nExample:")
        print('python contact_demo.py "John Doe, john@example.com, 555-1234"')
        sys.exit(1)
    
    text = sys.argv[1]
    
    # Check for API key
    if not os.getenv("GOOGLE_API_KEY") and not os.getenv("GOOGLE_GENAI_USE_VERTEXAI"):
        print("❌ Error: No API key found.")
        print("Please set GOOGLE_API_KEY environment variable or configure Vertex AI.")
        print("You can copy .env.example to .env and add your API key.")
        sys.exit(1)
    
    # Run the extraction
    try:
        asyncio.run(extract_contacts(text))
    except KeyboardInterrupt:
        print("\n🛑 Extraction cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error during extraction: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
