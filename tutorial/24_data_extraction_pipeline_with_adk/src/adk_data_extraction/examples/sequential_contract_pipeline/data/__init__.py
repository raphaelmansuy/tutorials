"""
Sample Contract Data for Sequential Pipeline Testing

This module contains sample contract data for testing the sequential contract
processing pipeline.
"""

"""
Sample Contract Data for Sequential Pipeline Testing

This module contains sample contract data for testing the sequential contract
processing pipeline.
"""

# Sample contracts for testing
SAMPLE_CONTRACTS = {
    "service_agreement": """
CLOUD MIGRATION SERVICES AGREEMENT

This Professional Services Agreement is effective March 1, 2024, between:

SERVICE PROVIDER: CloudTech Solutions Inc.
Principal Office: 789 Tech Plaza, Austin, TX 78701

CLIENT: Innovation Corp LLC
Business Address: 456 Business Center, Dallas, TX 75201

SERVICES: Cloud infrastructure consulting and migration services including:
• Current infrastructure assessment and analysis
• AWS cloud migration strategy and planning
• Cloud infrastructure implementation
• Data migration and system integration
• Staff training and knowledge transfer
• 3 months post-migration support

FINANCIAL TERMS:
Total Contract Value: $85,000 USD

Payment Schedule:
• $25,000 upon contract execution (March 1, 2024)
• $35,000 upon migration planning completion (May 1, 2024)
• $25,000 upon successful cloud deployment (July 15, 2024)

PROJECT TIMELINE:
Start Date: March 15, 2024
Planning Phase: March 15 - May 1, 2024
Migration Phase: May 1 - July 15, 2024
Support Period: July 16 - October 15, 2024
Contract End Date: October 15, 2024

LEGAL TERMS:
Governing Law: State of Texas
Termination Notice: 15 days written notice
Liability Cap: Total contract value ($85,000)

Parties:
- CloudTech Solutions Inc. (Service Provider)
- Innovation Corp LLC (Client)

Key Obligations:
- CloudTech: Deliver migration services, provide support, maintain timeline
- Innovation Corp: Provide access, make timely payments, participate in training

Signatures:
CloudTech Solutions Inc.: _________________ Date: _______
Innovation Corp LLC: _________________ Date: _______
""",

    "simple_service": """
    Simple Service Agreement
    
    This agreement is between ABC Corp and XYZ Services.
    Service fee: $5,000 per month
    Term: 12 months starting January 1, 2024
    Payment: Net 30 days
    """,
    
    "consulting_agreement": """
    Consulting Agreement
    
    Client: Global Enterprises Inc.
    Consultant: Tech Advisory LLC
    Fee: $200/hour, $10,000 retainer
    Period: 6 months from March 1, 2024
    Obligations: Monthly reports, 40 hours minimum
    Governing Law: New York
    """
}

SAMPLE_SERVICE_CONTRACT = SAMPLE_CONTRACTS["service_agreement"]


def get_sample_contracts() -> dict[str, str]:
    """Get sample contracts for testing"""
    return SAMPLE_CONTRACTS


def get_sample_service_contract() -> str:
    """Return the primary sample service contract for testing"""
    return SAMPLE_SERVICE_CONTRACT
