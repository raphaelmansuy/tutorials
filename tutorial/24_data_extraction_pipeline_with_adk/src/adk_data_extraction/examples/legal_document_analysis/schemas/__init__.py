"""
Schemas for Legal Document Analysis Pipeline

This module contains Pydantic schemas for legal document analysis,
providing comprehensive type safety and validation for legal data extraction.
"""

from enum import Enum
from typing import List, Optional

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


class LegalAnalysisResult(BaseModel):
    """Complete result of legal document analysis"""

    document_path: str = Field(description="Path to the analyzed document")
    extraction: LegalExtraction = Field(description="Extracted legal information")
    analysis_status: str = Field(description="Status of the analysis process")
    processing_time_ms: int = Field(description="Time taken for analysis in milliseconds")
    confidence_score: float = Field(
        description="Confidence in extraction quality (0-1)", ge=0.0, le=1.0
    )
