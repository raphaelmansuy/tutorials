"""
Example 2: Advanced Document Analysis (Intermediate Level)
See tutorial for details.
"""

import asyncio
from enum import Enum

from google.adk import Runner
from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService
from google.genai import types
from pydantic import BaseModel, Field


class DocumentType(str, Enum):
    """Enum representing different types of legal documents."""

    CONTRACT = "contract"
    INVOICE = "invoice"
    AGREEMENT = "agreement"
    PROPOSAL = "proposal"
    LEGAL_BRIEF = "legal_brief"
    UNKNOWN = "unknown"


class FinancialTerm(BaseModel):
    """Represents financial terms and amounts in a legal document."""

    amount: float = Field(description="Monetary amount")
    currency: str = Field(description="Currency code (USD, EUR, etc.)", default="USD")
    description: str = Field(description="Description of what this amount represents")
    due_date: str | None = Field(description="When payment is due", default=None)


class LegalExtraction(BaseModel):
    """Schema for extracted legal document information."""

    document_type: DocumentType
    parties: list[str] = Field(description="All parties involved in the document")
    key_dates: list[str] = Field(
        description="Important dates mentioned (contracts, deadlines, etc.)"
    )
    financial_terms: list[FinancialTerm] = Field(
        description="All monetary amounts and terms"
    )
    obligations: list[str] = Field(
        description="Key obligations and responsibilities listed"
    )
    governing_law: str = Field(description="Jurisdiction or governing law", default="")
    effective_date: str | None = Field(
        description="When the document becomes effective"
    )
    expiration_date: str | None = Field(description="When the document expires")


legal_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="legal_analyzer",
    description="Specialized agent for analyzing legal documents",
    instruction="""You are an expert legal document analyzer. Extract structured information
from legal documents with extreme precision. Pay special attention to:
1. All parties mentioned (individuals, companies, entities)
2. Financial terms including amounts, payment schedules, and penalties
3. Critical dates including effective dates, deadlines, and renewal terms
4. Legal obligations and responsibilities for each party
5. Governing law and jurisdiction clauses
If information is unclear or ambiguous, mark it as 'unclear' rather than guessing.
For dates, use ISO format (YYYY-MM-DD) when possible.
For amounts, include currency and context.""",
    output_schema=LegalExtraction,
    disallow_transfer_to_parent=True,
    disallow_transfer_to_peers=True,
)


async def analyze_legal_document(document_path: str):
    """
    Analyze a legal document at the given path using the legal_agent.
    Creates a session, reads the document content, sends it to the agent,
    and returns the extracted legal info as a string.

    Args:
        document_path (str): The path to the legal document to analyze.

    Returns:
        str: The extracted legal information as a string, or a message if not found.
    """
    # Read the document content first
    try:
        with open(document_path, encoding="utf-8") as file:
            document_content = file.read()
    except FileNotFoundError:
        return f"Error: Document not found at {document_path}"
    except PermissionError:
        return f"Error: Permission denied to read {document_path}"
    except UnicodeDecodeError:
        return f"Error: Cannot decode document at {document_path}"

    session_service = InMemorySessionService()
    _session = await session_service.create_session(
        app_name="legal_analysis_app", user_id="legal_user", session_id="legal_session"
    )
    runner = Runner(
        agent=legal_agent,
        app_name="legal_analysis_app",
        session_service=session_service,
    )

    # Send the document content directly to the agent
    user_content = types.Content(
        role="user",
        parts=[
            types.Part.from_text(
                text=f"Please analyze this legal document:\n\n{document_content}"
            )
        ],
    )
    async for event in runner.run_async(
        user_id="legal_user", session_id="legal_session", new_message=user_content
    ):
        if hasattr(event, "content") and event.content:
            if hasattr(event.content, "parts") and event.content.parts:
                for part in event.content.parts:
                    if hasattr(part, "text") and part.text:
                        return part.text
    return "No analysis result available"


def main():
    """CLI entry point for legal document analysis."""
    import os

    # Path to the sample contract
    sample_document_path = "sample_contract.txt"

    # Check if sample document exists
    if not os.path.exists(sample_document_path):
        print(f"Sample document not found at: {sample_document_path}")
        print(
            "Please ensure the sample_contract.txt file exists in the current directory."
        )
    else:
        print("Analyzing legal document...")
        print(f"Document path: {sample_document_path}")
        print("-" * 50)

        try:
            result = asyncio.run(analyze_legal_document(sample_document_path))
            print("Analysis Result:")
            print(result)
        except Exception as e:
            print(f"Error during analysis: {e}")
            print("This might be due to API authentication issues.")
            print("Please ensure your Google API credentials are properly configured.")


if __name__ == "__main__":
    main()
