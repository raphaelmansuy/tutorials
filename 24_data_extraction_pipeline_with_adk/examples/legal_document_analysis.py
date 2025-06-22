"""
Example 2: Advanced Document Analysis (Intermediate Level)
See tutorial for details.
"""
from typing import List, Optional
from enum import Enum
from pydantic import BaseModel, Field
from google.adk.agents import LlmAgent
from google.adk.runtime import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import FunctionTool
from google.genai import types
import asyncio

class DocumentType(str, Enum):
    CONTRACT = "contract"
    INVOICE = "invoice"
    AGREEMENT = "agreement"
    PROPOSAL = "proposal"
    LEGAL_BRIEF = "legal_brief"
    UNKNOWN = "unknown"

class FinancialTerm(BaseModel):
    amount: float = Field(description="Monetary amount")
    currency: str = Field(description="Currency code (USD, EUR, etc.)", default="USD")
    description: str = Field(description="Description of what this amount represents")
    due_date: Optional[str] = Field(description="When payment is due", default=None)

class LegalExtraction(BaseModel):
    document_type: DocumentType
    parties: List[str] = Field(description="All parties involved in the document")
    key_dates: List[str] = Field(description="Important dates mentioned (contracts, deadlines, etc.)")
    financial_terms: List[FinancialTerm] = Field(description="All monetary amounts and terms")
    obligations: List[str] = Field(description="Key obligations and responsibilities listed")
    governing_law: str = Field(description="Jurisdiction or governing law", default="")
    effective_date: Optional[str] = Field(description="When the document becomes effective")
    expiration_date: Optional[str] = Field(description="When the document expires")

async def read_document_content(file_path: str, tool_context):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return {"status": "success", "content": content}
    except Exception as e:
        return {"status": "error", "message": f"Failed to read document: {str(e)}"}

document_reader_tool = FunctionTool(
    name="document_reader",
    description="Read document content from file path",
    func=read_document_content
)

legal_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="legal_analyzer",
    description="Specialized agent for analyzing legal documents",
    instruction="""You are an expert legal document analyzer. Extract structured information\nfrom legal documents with extreme precision. Pay special attention to:\n1. All parties mentioned (individuals, companies, entities)\n2. Financial terms including amounts, payment schedules, and penalties\n3. Critical dates including effective dates, deadlines, and renewal terms\n4. Legal obligations and responsibilities for each party\n5. Governing law and jurisdiction clauses\nIf information is unclear or ambiguous, mark it as 'unclear' rather than guessing.\nFor dates, use ISO format (YYYY-MM-DD) when possible.\nFor amounts, include currency and context.""",
    output_schema=LegalExtraction,
    tools=[document_reader_tool]
)

async def analyze_legal_document(document_path: str):
    session_service = InMemorySessionService()
    runner = Runner(
        agent=legal_agent,
        app_name="legal_analysis_app",
        session_service=session_service
    )
    user_content = types.Content(
        role='user',
        parts=[types.Part(text=f"Please analyze the legal document at: {document_path}")]
    )
    async for event in runner.run_async(
        user_id="legal_user",
        session_id="legal_session",
        new_message=user_content
    ):
        if hasattr(event, 'content') and event.content:
            if hasattr(event.content, 'parts') and event.content.parts:
                for part in event.content.parts:
                    if hasattr(part, 'text'):
                        return part.text
    return "No analysis result available"

if __name__ == "__main__":
    # Example usage: asyncio.run(analyze_legal_document("sample_contract.txt"))
    pass
