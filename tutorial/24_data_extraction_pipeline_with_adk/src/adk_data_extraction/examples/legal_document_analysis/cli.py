#!/usr/bin/env python3
"""
Legal Document Analysis - Python CLI

This script demonstrates how to use the legal document analysis agent
programmatically outside of the ADK CLI interface.

Usage:
    python cli.py --text "LEGAL DOCUMENT: ..."
    python cli.py --file path/to/legal_document.txt
"""

import argparse
import asyncio
import sys
from pathlib import Path

# Add the parent directory to the path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from google.adk.runners import InMemoryRunner
from google.genai.types import Part, UserContent

# Import the agent
try:
    from .agent import root_agent
except ImportError:
    from agent import root_agent


async def analyze_legal_document(text: str) -> None:
    """
    Analyze legal document using the ADK agent.
    
    Args:
        text: The legal document text to analyze
    """
    print("🔍 Analyzing legal document...")
    print(f"📄 Input: {text[:100]}{'...' if len(text) > 100 else ''}")
    print("-" * 50)
    
    # Create runner
    runner = InMemoryRunner(agent=root_agent)
    
    # Create a session
    session = await runner.session_service.create_session(
        app_name=runner.app_name,
        user_id="cli_user"
    )
    
    # Create user content
    content = UserContent(parts=[Part(text=text)])
    
    # Run the agent
    print("🤖 Running legal document analysis...")
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
    
    print(f"\n✅ Analysis complete! Processed {event_count} events.")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Analyze legal documents using ADK agent",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cli.py --text "LEGAL AGREEMENT: This contract..."
  python cli.py --file legal_document.txt
        """
    )
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--text",
        help="Legal document text to analyze"
    )
    group.add_argument(
        "--file",
        help="File containing legal document text to analyze"
    )
    
    args = parser.parse_args()
    
    # Get the text to process
    if args.text:
        text = args.text
    else:
        try:
            with open(args.file, encoding='utf-8') as f:
                text = f.read()
        except FileNotFoundError:
            print(f"❌ Error: File '{args.file}' not found.")
            sys.exit(1)
        except OSError as e:
            print(f"❌ Error reading file: {e}")
            sys.exit(1)
    
    # Run the analysis
    try:
        asyncio.run(analyze_legal_document(text))
    except KeyboardInterrupt:
        print("\n🛑 Analysis cancelled by user.")
        sys.exit(1)
    except RuntimeError as e:
        print(f"❌ Error during analysis: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
