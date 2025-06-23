"""
Contact Information Schema for Basic Contact Extraction

This module defines the data models for contact information extraction.
Following ADK best practices, schemas are separated from agent logic.
"""

from pydantic import BaseModel, Field


class ContactInfo(BaseModel):
    """Schema for extracted contact information."""

    name: str = Field(description="Full name of the contact")
    email: str = Field(description="Email address")
    company: str = Field(description="Company name")
    phone: str = Field(description="Phone number if available", default="")
    position: str = Field(description="Job title or position", default="")
