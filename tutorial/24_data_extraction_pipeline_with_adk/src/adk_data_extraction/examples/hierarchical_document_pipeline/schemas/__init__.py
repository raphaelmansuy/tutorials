"""
Schemas for Hierarchical Document Pipeline

This module contains all Pydantic schemas used by the hierarchical document 
extraction pipeline, following ADK best practices for type safety and validation.
"""

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class DocumentType(str, Enum):
    """Document types that can be processed by the pipeline"""

    CONTRACT = "contract"
    INVOICE = "invoice"
    AGREEMENT = "agreement"
    PROPOSAL = "proposal"
    REPORT = "report"
    EMAIL = "email"
    UNKNOWN = "unknown"


class DocumentClassification(BaseModel):
    """Schema for document classification results"""

    document_type: DocumentType = Field(description="Primary document type")
    complexity_level: str = Field(description="simple, medium, complex")
    estimated_processing_time: int = Field(description="Estimated seconds to process")
    recommended_extractor: str = Field(description="Which specialized agent to use")
    confidence_score: float = Field(
        description="Confidence in classification (0-1)", ge=0.0, le=1.0
    )
    key_indicators: list[str] = Field(
        description="Text indicators that led to this classification"
    )


class ContractData(BaseModel):
    """Schema for contract extraction results"""

    parties: list[str] = Field(description="All parties involved in the contract")
    contract_value: float | None = Field(
        description="Total contract value", default=None
    )
    currency: str = Field(description="Currency code", default="USD")
    start_date: str | None = Field(description="Contract start date", default=None)
    end_date: str | None = Field(description="Contract end date", default=None)
    payment_terms: list[str] = Field(description="Payment terms and schedules")
    key_obligations: list[str] = Field(description="Main obligations for each party")
    governing_law: str | None = Field(
        description="Governing law jurisdiction", default=None
    )


class InvoiceData(BaseModel):
    """Schema for invoice extraction results"""

    invoice_number: str = Field(description="Invoice number")
    vendor_name: str = Field(description="Vendor/supplier name")
    customer_name: str = Field(description="Customer name")
    invoice_date: str | None = Field(description="Invoice date", default=None)
    due_date: str | None = Field(description="Payment due date", default=None)
    total_amount: float = Field(description="Total invoice amount")
    currency: str = Field(description="Currency code", default="USD")
    line_items: list[str] = Field(
        description="List of line items with quantities and prices"
    )
    tax_amount: float | None = Field(description="Tax amount", default=None)


class GeneralData(BaseModel):
    """Schema for general document extraction"""

    document_title: str = Field(description="Document title or subject")
    main_entities: list[str] = Field(
        description="Key entities mentioned (people, companies, etc.)"
    )
    key_dates: list[str] = Field(description="Important dates mentioned")
    summary: str = Field(description="Brief summary of the document content")
    action_items: list[str] = Field(description="Action items or next steps mentioned")
    contact_info: list[str] = Field(description="Contact information found")


class ValidationSummary(BaseModel):
    """Schema for validation summary"""

    is_valid: bool = Field(description="Whether extraction passed validation")
    confidence_score: float = Field(
        description="Confidence in extraction quality (0-1)", ge=0.0, le=1.0
    )
    completeness_score: float = Field(
        description="How complete the extraction is (0-1)", ge=0.0, le=1.0
    )
    issues: list[str] = Field(description="Quality issues identified")
    recommendation: str = Field(description="Recommended next action")


class PipelineResult(BaseModel):
    """Complete pipeline result"""

    extraction_id: str = Field(description="Unique identifier for this extraction")
    classification: DocumentClassification
    extracted_data: ContractData | InvoiceData | GeneralData
    validation: ValidationSummary
    processing_time_ms: int = Field(description="Total processing time in milliseconds")
    pipeline_status: str = Field(description="Overall pipeline status")
