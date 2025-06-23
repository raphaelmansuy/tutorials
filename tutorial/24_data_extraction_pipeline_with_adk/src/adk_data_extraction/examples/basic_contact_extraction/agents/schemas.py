"""
Schema definitions for contact extraction agent.

This module defines the structured data schemas used by the contact extraction agent
to ensure consistent and validated output.
"""

from pydantic import BaseModel, Field


class ContactInfo(BaseModel):
    """
    Schema for individual contact information.
    
    This schema defines the structure for extracted contact information,
    ensuring consistent output format for downstream processing.
    """
    
    name: Optional[str] = Field(
        default=None,
        description="Full name of the contact person"
    )
    
    email: Optional[str] = Field(
        default=None,
        description="Email address of the contact"
    )
    
    phone: Optional[str] = Field(
        default=None,
        description="Phone number of the contact"
    )
    
    company: Optional[str] = Field(
        default=None,
        description="Company or organization name"
    )
    
    title: Optional[str] = Field(
        default=None,
        description="Job title or position"
    )
    
    address: Optional[str] = Field(
        default=None,
        description="Physical address"
    )
    
    notes: Optional[str] = Field(
        default=None,
        description="Additional notes or context about the contact"
    )


class ContactExtractionResult(BaseModel):
    """
    Schema for the complete contact extraction result.
    
    This schema wraps the extracted contacts and provides metadata
    about the extraction process.
    """
    
    contacts: List[ContactInfo] = Field(
        default_factory=list,
        description="List of extracted contact information"
    )
    
    source_text_length: int = Field(
        description="Length of the source text processed"
    )
    
    extraction_confidence: Optional[str] = Field(
        default=None,
        description="Confidence level of the extraction (high/medium/low)"
    )
    
    processing_notes: Optional[str] = Field(
        default=None,
        description="Notes about the extraction process or any issues encountered"
    )
