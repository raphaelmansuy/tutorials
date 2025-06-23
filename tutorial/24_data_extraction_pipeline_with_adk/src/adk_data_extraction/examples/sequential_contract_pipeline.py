"""
Service Contract Processing Pipeline - Sequential Pattern Example

This educational example demonstrates Google ADK's Sequential Pipeline Pattern
following the official documentation and LLM Auditor sample:
- https://google.github.io/adk-docs/agents/multi-agents/#sequential-pipeline-pattern
- https://github.com/google/adk-samples/tree/main/python/agents/llm-auditor

Key Educational Points:
1. SequentialAgent as the root_agent (main orchestrator)
2. Communication via conversation flow (NOT session state)
3. Each agent processes the cumulative conversation history
4. Fixed 3-step process: Extract → Validate → Report
5. Assumes input is always a service contract (no classification needed)
6. CRITICAL: Agents must NOT use output_schema to avoid transfer conflicts

Sequential Pipeline Pattern Implementation:
- Step 1: Service Data Extractor → extracts contract data
- Step 2: Quality Validator → validates the extraction from conversation history
- Step 3: Summary Reporter → creates report based on all previous conversation

This follows the official ADK pattern exactly like the LLM Auditor sample:
```python
sequential_agent = SequentialAgent(
    name="pipeline",
    sub_agents=[step1_agent, step2_agent, step3_agent]
)
root_agent = sequential_agent
```

Benefits of Sequential Pipeline Pattern:
✅ Pure SequentialAgent workflow orchestration
✅ Simple conversation flow communication
✅ Direct implementation from ADK documentation and samples
✅ Educational clarity and simplicity
✅ No complex coordination logic needed

Educational Focus:
❌ No document classification (assumes service contracts only)
❌ No conditional branching or routing
❌ No complex multi-agent coordination
❌ Simplified for learning purposes only

IMPORTANT BUG FIX:
The key issue was using `output_schema` with agents in a SequentialAgent.
The ADK framework automatically disables agent transfer when both `output_schema`
and agent transfer configurations are present, which breaks the sequential flow.
The solution is to format outputs as structured text instead of using schemas.

IMPORTANT: Unlike some documentation examples, this follows the actual working
pattern used in ADK samples where agents communicate through conversation flow
rather than explicit session state management.
"""

import asyncio

from google.adk.agents import LlmAgent, SequentialAgent
from pydantic import BaseModel, Field

# =============================================================================
# SCHEMAS FOR SERVICE CONTRACT DATA
# =============================================================================


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


# =============================================================================
# SEQUENTIAL PIPELINE AGENTS (Following Official ADK Pattern)
# =============================================================================

# Step 1: Service Contract Data Extractor
# Extracts structured data from service contracts
service_data_extractor = LlmAgent(
    model="gemini-2.0-flash",
    name="ServiceDataExtractor",
    description="Extracts structured data from service contracts",
    instruction="""You are a Service Contract Data Extraction specialist.

Your task is to extract key information from the service contract provided by the user.

EXTRACTION FOCUS:
• Service Provider and Client company names
• Contract value and financial terms
• Service description and scope
• Start date, end date, and duration
• Payment schedule and terms
• Legal jurisdiction and termination clauses

Please extract dates in YYYY-MM-DD format when possible.
Extract monetary values as numbers (e.g., 85000.0 for $85,000).
Be precise and accurate with all extracted information.

FORMAT YOUR RESPONSE AS:
=== SERVICE CONTRACT DATA EXTRACTION ===

SERVICE PROVIDER: [Provider Company Name]
CLIENT COMPANY: [Client Company Name]
CONTRACT VALUE: [Total USD value]
SERVICE DESCRIPTION: [Brief service description]

TIMELINE:
- Start Date: [YYYY-MM-DD]
- End Date: [YYYY-MM-DD]
- Duration: [X months]

PAYMENT INFORMATION:
- Payment Terms: [List payment schedule/terms]
- Total Payments: [Number of payment milestones]

LEGAL FRAMEWORK:
- Governing Law: [Jurisdiction]
- Termination Notice: [Notice period required]

Provide a clear, structured extraction of all contract data."""
)

# Step 2: Quality Validator
# Validates the extracted data quality and completeness
quality_validator = LlmAgent(
    model="gemini-2.0-flash",
    name="QualityValidator",
    description="Validates extraction quality and completeness",
    instruction="""You are a Contract Data Quality Validator.

Your task is to review the contract data extracted by the previous agent and assess its quality.

VALIDATION APPROACH:
1. Review the extracted contract data from the conversation above
2. Check data format and consistency
3. Assess overall data quality
4. Provide recommendations

VALIDATION CRITERIA:
• Completeness: Are all critical fields populated with meaningful data?
• Accuracy: Do the extracted values appear reasonable and consistent?
• Format: Are dates, amounts, and other structured data properly formatted?
• Consistency: Do related fields align logically (e.g., dates, payment terms)?

QUALITY LEVELS:
• EXCELLENT: Complete, accurate, well-formatted data (confidence > 0.9)
• GOOD: Minor gaps or formatting issues, generally reliable (confidence 0.7-0.9)
• FAIR: Some missing data or inconsistencies, needs review (confidence 0.5-0.7)
• POOR: Significant gaps, errors, or formatting problems (confidence < 0.5)

RECOMMENDATIONS:
• APPROVE: Data quality is sufficient for processing
• REVIEW: Data needs human review before processing
• REJECT: Data quality is too poor, requires re-extraction

FORMAT YOUR RESPONSE AS:
=== QUALITY VALIDATION REPORT ===

COMPLETENESS CHECK:
- Is Complete: [Yes/No]
- Missing Fields: [List any missing fields]

DATA QUALITY ASSESSMENT:
- Overall Quality: [EXCELLENT/GOOD/FAIR/POOR]
- Data Issues: [List any identified issues]
- Confidence Score: [0.0-1.0]

RECOMMENDATION: [APPROVE/REVIEW/REJECT]

VALIDATION SUMMARY:
[Provide detailed assessment of the extracted data quality]"""
)

# Step 3: Summary Reporter
# Creates final comprehensive summary report
summary_reporter = LlmAgent(
    model="gemini-2.0-flash",
    name="SummaryReporter",
    description="Creates comprehensive contract summary report",
    instruction="""You are a Contract Summary Report Generator.

Your task is to create a comprehensive summary report based on the contract data extracted and validated by the previous agents.

Review the conversation history to access:
• The original contract document provided by the user
• The structured contract data extracted by the ServiceDataExtractor
• The validation assessment provided by the QualityValidator

Use all this information to create your comprehensive summary.

FORMAT YOUR RESPONSE AS:
=== COMPREHENSIVE CONTRACT SUMMARY REPORT ===

CONTRACT TITLE: [Descriptive title based on service and parties]

EXECUTIVE SUMMARY:
[Concise overview of the contract purpose and scope]

KEY HIGHLIGHTS:
• [Most important contract point 1]
• [Most important contract point 2]
• [Most important contract point 3]
• [Additional highlights as needed]

FINANCIAL OVERVIEW:
[Summary of contract value, payment terms, and schedule]

TIMELINE OVERVIEW:
[Summary of key dates, duration, and important milestones]

RISK FACTORS:
• [Potential risk or concern 1]
• [Potential risk or concern 2]
• [Additional risks as identified]

NEXT ACTIONS:
• [Recommended follow-up action 1]
• [Recommended follow-up action 2]
• [Recommended follow-up action 3]
• [Additional actions as needed]

Provide a comprehensive, professional summary report."""
)


# =============================================================================
# SEQUENTIAL PIPELINE DEFINITION (Following ADK Samples Pattern)
# =============================================================================

# Create the Sequential Pipeline following ADK pattern exactly like LLM Auditor sample
# This is the core of the Sequential Pipeline Pattern
service_contract_pipeline = SequentialAgent(
    name="ServiceContractPipeline",
    description=(
        "Sequential pipeline for processing service contracts. "
        "Extracts contract data, validates the extraction quality, "
        "and generates a comprehensive summary report."
    ),
    sub_agents=[
        service_data_extractor,  # Step 1: Extract → state['contract_data']
        quality_validator,       # Step 2: Validate → state['validation_report']
        summary_reporter         # Step 3: Report → state['final_report']
    ]
)

# For ADK compatibility, the root agent must be the SequentialAgent
# This follows the exact pattern from ADK samples (e.g., LLM Auditor)
root_agent = service_contract_pipeline


# =============================================================================
# DEMONSTRATION FUNCTION (Optional - for testing)
# =============================================================================

async def demonstrate_sequential_pipeline():
    """Demonstrate the Sequential Pipeline Pattern for service contract processing"""
    from google.adk import Runner
    from google.adk.sessions import InMemorySessionService
    from google.genai import types

    print("\n" + "=" * 80)
    print("SERVICE CONTRACT PROCESSING - SEQUENTIAL PIPELINE PATTERN")
    print("Following Official ADK Documentation and LLM Auditor Sample")
    print("=" * 80)

    # Sample service contract for demonstration
    sample_contract = """
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

    Signatures:
    CloudTech Solutions Inc.: _________________ Date: _______
    Innovation Corp LLC: _________________ Date: _______
    """

    print("📋 SEQUENTIAL PIPELINE PATTERN CHARACTERISTICS:")
    print("✅ SequentialAgent as root_agent (main orchestrator)")
    print("✅ Communication via conversation flow (like LLM Auditor)")
    print("✅ Each agent processes cumulative conversation history")
    print("✅ Fixed 3-step process: Extract → Validate → Report")
    print("✅ No explicit session state management needed")
    print("✅ Follows ADK samples pattern (LLM Auditor)")
    print("✅ Educational simplicity and clarity")
    print()

    print("🔄 Processing service contract through Sequential Pipeline...")

    # Create session service and runner
    session_service = InMemorySessionService()
    runner = Runner(
        agent=root_agent,  # Use the SequentialAgent directly as root_agent
        app_name="service_contract_pipeline",
        session_service=session_service,
    )

    try:
        # Create session
        session_id = "demo_session"
        await session_service.create_session(
            app_name="service_contract_pipeline",
            user_id="demo_user",
            session_id=session_id,
        )

        # Create user message with contract content
        user_content = types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text=f"Please process this service contract:\n\n{sample_contract}"
                )
            ],
        )

        # Run the sequential pipeline
        final_response = None
        step_count = 0
        all_events = []
        print("\n📊 SEQUENTIAL PIPELINE EXECUTION")
        print("=" * 60)
        
        async for event in runner.run_async(
            user_id="demo_user",
            session_id=session_id,
            new_message=user_content,
        ):
            all_events.append(event)
            
            if event.author and event.author != "user":
                step_count += 1
                print(f"\n🔸 STEP {step_count}: {event.author.upper()}")
                print("-" * 40)
                
                if event.content and event.content.parts:
                    for part in event.content.parts:
                        if part.text:
                            # Truncate very long outputs for readability
                            output = part.text
                            if len(output) > 500:
                                output = output[:500] + "... [truncated]"
                            print(output)
                            
            if event.is_final_response():
                final_response = event

        print(f"\n✅ Pipeline Status: {'completed' if final_response else 'incomplete'}")
        print(f"📈 Total Steps Executed: {step_count}")
        
        # Debug: Show all agent events
        print(f"🔍 Debug: Total events received: {len(all_events)}")
        agent_events = [e for e in all_events if e.author and e.author != "user"]
        print(f"🔍 Debug: Agent events: {len(agent_events)}")
        for i, event in enumerate(agent_events):
            print(f"   Agent {i+1}: {event.author}")

    except Exception as e:
        print(f"❌ Pipeline failed: {e}")


def main():
    """Main function demonstrating the Sequential Pipeline Pattern"""
    print("Service Contract Processing - Sequential Pipeline Pattern")
    print("=" * 60)
    print("Educational demonstration following official ADK LLM Auditor sample:")
    print("• SequentialAgent as root_agent (main orchestrator)")
    print("• Communication via conversation flow")
    print("• Each agent processes cumulative conversation history")
    print("• Fixed 3-step sequential process")
    print("• Follows ADK samples pattern (LLM Auditor)")
    print("• Pure implementation of ADK Sequential Pipeline Pattern")
    print()

    try:
        # Run the demonstration
        asyncio.run(demonstrate_sequential_pipeline())

        print("\n🎓 SEQUENTIAL PIPELINE PATTERN SUMMARY")
        print("=" * 55)
        print("This example demonstrates the official ADK Sequential Pipeline Pattern:")
        print()
        print("Pattern Structure:")
        print("✅ SequentialAgent as root_agent")
        print("✅ Agents communicate through conversation flow")
        print("✅ Each agent processes cumulative conversation history")
        print("✅ Fixed execution order with no branching")
        print("✅ Simple conversation-based communication")
        print()
        print("Educational Benefits:")
        print("✅ Direct implementation from ADK samples (LLM Auditor)")
        print("✅ Clear demonstration of workflow agent patterns")
        print("✅ Simple and focused example for learning")
        print("✅ No complex coordination or routing logic")
        print("✅ Pure Sequential Pipeline Pattern implementation")

    except (ImportError, RuntimeError, ValueError) as e:
        print(f"❌ Error running sequential pipeline: {e}")
        print("Please ensure your Google API key is configured properly.")


if __name__ == "__main__":
    main()
