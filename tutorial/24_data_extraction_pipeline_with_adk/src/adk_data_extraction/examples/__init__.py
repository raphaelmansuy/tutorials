"""
Examples package for ADK data extraction tutorials.

This package contains example scripts demonstrating various data extraction
capabilities using Google's Agent Development Kit (ADK).
"""

from .basic_contact_extraction import ContactInfo, extract_contacts
from .legal_document_analysis import (
    DocumentType,
    FinancialTerm,
    LegalExtraction,
    analyze_legal_document,
)

__all__ = [
    "ContactInfo",
    "extract_contacts",
    "DocumentType",
    "FinancialTerm",
    "LegalExtraction",
    "analyze_legal_document",
]
