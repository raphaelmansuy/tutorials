"""
Sequential Contract Pipeline Schemas

This module defines the data models for the sequential contract processing pipeline.
Following ADK best practices, schemas are separated from agent logic.
"""

from pydantic import BaseModel, Field


class ContractData(BaseModel):
    """Schema for contract data extraction"""

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


class ContractAnalysisResult(BaseModel):
    """Complete result of contract analysis"""

    contract_data: ContractData | None = Field(
        description="Extracted contract data", default=None
    )
    processing_status: str = Field(description="Status of the processing workflow")
    processing_time_ms: int = Field(description="Time taken for processing in milliseconds")
    quality_score: float = Field(
        description="Quality assessment score (0-1)", ge=0.0, le=1.0, default=0.0
    )
    validation_notes: list[str] = Field(
        description="Validation notes and recommendations", default_factory=list
    )


class ServiceContractData(BaseModel):
    """Schema for service contract extraction results"""

    # Core Contract Information
    service_provider: str = Field(description="Name of the service provider company")
    client_company: str = Field(description="Name of the client company")
    contract_value: float = Field(description="Total contract value in USD")
    service_description: str = Field(description="Brief description of services provided")

    # Timeline Information
    start_date: str = Field(description="Contract start date")
    end_date: str = Field(description="Contract end date")
    duration_months: int = Field(description="Contract duration in months")

    # Payment Information
    payment_terms: list[str] = Field(description="Payment schedule and terms")
    total_payments: int = Field(description="Number of payment milestones")

    # Legal Framework
    governing_law: str = Field(description="Governing law jurisdiction")
    termination_notice: str = Field(description="Required termination notice period")


class ValidationReport(BaseModel):
    """Schema for contract validation results"""

    is_complete: bool = Field(description="Whether all required fields are extracted")
    data_quality: str = Field(description="Overall data quality: excellent, good, fair, poor")
    missing_fields: list[str] = Field(description="List of missing or incomplete fields")
    data_issues: list[str] = Field(description="Data quality issues identified")
    confidence_score: float = Field(description="Confidence in extraction (0-1)", ge=0.0, le=1.0)
    recommendation: str = Field(description="Processing recommendation: approve, review, reject")


class ContractSummary(BaseModel):
    """Schema for final contract summary report"""

    contract_title: str = Field(description="Descriptive title for the contract")
    executive_summary: str = Field(description="Brief executive summary")
    key_highlights: list[str] = Field(description="Most important contract points")
    financial_overview: str = Field(description="Summary of financial terms")
    timeline_overview: str = Field(description="Summary of key dates and milestones")
    risk_factors: list[str] = Field(description="Potential risks or concerns identified")
    next_actions: list[str] = Field(description="Recommended follow-up actions")
