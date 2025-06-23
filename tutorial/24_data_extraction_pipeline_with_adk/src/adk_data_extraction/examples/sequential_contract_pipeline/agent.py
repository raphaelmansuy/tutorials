"""
Sequential Contract Pipeline with Google ADK

This example demonstrates a sequential multi-agent pattern for contract processing
using Google ADK. It shows how to build a linear workflow where agents process
documents in a predefined sequence, each building on the work of the previous agent.
"""

from google.adk.agents import Agent

# Create the root agent that ADK will discover
root_agent = Agent(
    name="sequential_contract_pipeline",
    model="gemini-2.0-flash",
    description="Processes contracts through a sequential multi-agent pipeline for comprehensive analysis",
    instruction="""You are a contract analysis coordinator that processes contracts through a sequential workflow.

Your role is to:
1. Extract basic contract information (parties, dates, amounts)
2. Analyze contract terms and conditions
3. Identify potential risks and issues
4. Provide structured recommendations

Process contracts systematically and provide comprehensive analysis including:
- Contract metadata and key parties
- Financial terms and obligations
- Risk assessment and compliance issues
- Actionable recommendations

Return results in a clear, structured format.""",
)


class SequentialContractPipeline:
    """
    Sequential contract processing pipeline using Google ADK.
    
    This pipeline demonstrates a linear workflow where each agent builds
    on the work of the previous agent, providing incremental enhancement
    and validation of contract data extraction.
    """

    def __init__(self):
        """Initialize the sequential contract pipeline"""
        self.session_service = InMemorySessionService()
        self.main_agent = self._create_main_agent()

    def _create_main_agent(self) -> LlmAgent:
        """Create the main sequential coordinator agent"""
        
        # Contract Data Extractor Agent
        extractor_agent = LlmAgent(
            model="gemini-2.0-flash",
            name="contract_extractor",
            description="Primary contract data extraction agent",
            instruction="""You are a contract data extraction specialist. Your role is to:

1. Analyze contract documents thoroughly
2. Extract all key contract information including:
   - All contracting parties with full legal names
   - Contract value and currency
   - Start and end dates
   - Payment terms and schedules
   - Key obligations for each party
   - Governing law and jurisdiction

3. Provide accurate, complete, and structured data extraction
4. Format dates consistently (YYYY-MM-DD when possible)
5. Include currency codes for all monetary amounts
6. Extract exact legal entity names as they appear

Focus on accuracy and completeness. If information is unclear, mark it as such rather than guessing.""",
            output_schema=ContractData,
            output_key="contract_extraction",
            disallow_transfer_to_parent=False,
            disallow_transfer_to_peers=True,
        )

        # Contract Enhancer Agent
        enhancer_agent = LlmAgent(
            model="gemini-2.0-flash",
            name="contract_enhancer",
            description="Contract data enhancement and enrichment agent",
            instruction="""You are a contract enhancement specialist. Your role is to:

1. Review and enhance the extracted contract data
2. Add missing details that may have been overlooked
3. Standardize formats and improve data quality
4. Identify and extract additional relevant information
5. Verify accuracy of extracted data against the source

Enhancement focus areas:
- Complete party information including addresses and roles
- Detailed payment terms and schedules
- Comprehensive obligation mapping
- Risk factors and contingencies
- Renewal and termination clauses
- Performance milestones and deadlines

Provide enhanced, standardized, and comprehensive contract data.""",
            output_schema=ContractData,
            output_key="enhanced_contract",
            disallow_transfer_to_parent=False,
            disallow_transfer_to_peers=True,
        )

        # Contract Validator Agent
        validator_agent = LlmAgent(
            model="gemini-2.0-flash",
            name="contract_validator",
            description="Contract data validation and quality assurance agent",
            instruction="""You are a contract validation specialist. Your role is to:

1. Validate the enhanced contract data for accuracy and completeness
2. Cross-reference extracted data with the original document
3. Identify any inconsistencies or errors
4. Provide quality scores and confidence assessments
5. Recommend improvements or corrections

Validation criteria:
- Data accuracy against source document
- Completeness of required contract elements
- Consistency of dates, amounts, and terms
- Proper formatting and standardization
- Legal accuracy of extracted terms

Provide final validated contract data with quality assessment.""",
            output_schema=ContractData,
            output_key="validated_contract",
            disallow_transfer_to_parent=False,
            disallow_transfer_to_peers=True,
        )

        # Main Sequential Coordinator
        coordinator = LlmAgent(
            model="gemini-2.0-flash",
            name="sequential_coordinator",
            description="Main coordinator for sequential contract processing pipeline",
            instruction="""You are the coordinator for a sequential contract processing pipeline.

Your workflow:
1. First, transfer to contract_extractor for initial data extraction
2. Then, transfer to contract_enhancer to enhance and enrich the data
3. Finally, transfer to contract_validator for quality validation
4. Provide a comprehensive summary of the complete process

Ensure each step builds on the previous work and that the final result
represents a thorough, accurate, and validated contract analysis.

Process documents sequentially through all three stages:
Extraction → Enhancement → Validation → Summary""",
            sub_agents=[extractor_agent, enhancer_agent, validator_agent],
        )

        return coordinator

    async def process_contract(self, contract_content: str) -> ContractAnalysisResult:
        """
        Process a contract through the sequential pipeline
        
        Args:
            contract_content: The text content of the contract to process
            
        Returns:
            ContractAnalysisResult: Complete processing results
        """
        start_time = time.time()
        
        logger.info("Starting sequential contract processing")

        try:
            # Create session for processing
            session = await self.session_service.create_session()
            
            # Initialize runner
            runner = Runner(
                agent=self.main_agent,
                session_service=self.session_service,
                session_id=session.id,
            )

            # Process the contract
            response = await runner.run(
                input_prompt=f"""Process this contract through the complete sequential pipeline:

CONTRACT CONTENT:
{contract_content}

Please process this contract through all stages:
1. Extract all contract data (parties, terms, dates, obligations)
2. Enhance and enrich the extracted data
3. Validate the final results for accuracy and completeness
4. Provide a comprehensive summary

Ensure thorough analysis at each stage."""
            )

            # Calculate processing time
            processing_time_ms = int((time.time() - start_time) * 1000)
            
            logger.info("Sequential contract processing completed - Time: %dms", processing_time_ms)

            return {
                "response": response,
                "processing_status": "completed",
                "processing_time_ms": processing_time_ms,
                "session_id": session.id
            }

        except Exception as e:
            logger.error("Sequential contract processing failed - Error: %s", str(e))
            
            return {
                "error": str(e),
                "processing_status": "failed",
                "processing_time_ms": int((time.time() - start_time) * 1000)
            }


async def main():
    """
    Example usage of the Sequential Contract Pipeline
    """
    # Get sample contract
    sample_contracts = get_sample_contracts()
    sample_contract = sample_contracts["service_agreement"]
    
    # Initialize and run pipeline
    pipeline = SequentialContractPipeline()
    
    print("📋 Starting Sequential Contract Processing Pipeline")
    print("=" * 60)
    print("Processing sample service agreement...")
    print()
    
    result = await pipeline.process_contract(sample_contract)
    
    print("📄 Processing Results:")
    print(f"   Status: {result['processing_status']}")
    print(f"   Processing Time: {result['processing_time_ms']}ms")
    
    if 'response' in result:
        print(f"\n🔍 Contract Analysis:")
        print(result['response'])
    
    if 'error' in result:
        print(f"\n❌ Error: {result['error']}")


if __name__ == "__main__":
    asyncio.run(main())
