"""
Hierarchical Document Extraction Pipeline with Google ADK

This example demonstrates a production-ready document processing system using Google ADK
with advanced multi-agent coordination patterns and hierarchical organization.
"""

from google.adk.agents import Agent

# Create the root agent that ADK will discover
root_agent = Agent(
    name="hierarchical_document_pipeline",
    model="gemini-2.0-flash",
    description="Processes documents through a hierarchical multi-agent system with specialized extraction agents",
    instruction="""You are a document processing coordinator that manages a hierarchical pipeline of specialized agents.

Your role is to:
1. Classify documents by type (contract, invoice, email, etc.)
2. Route documents to appropriate specialized extraction agents
3. Coordinate validation and quality assurance
4. Provide comprehensive structured output

Process documents systematically through:
- Document classification and routing
- Specialized extraction by document type
- Quality validation and verification
- Integrated result compilation

Return results in a structured format with extracted data, metadata, and quality assessments.""",
)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class HierarchicalDocumentPipeline:
    """
    Hierarchical document extraction pipeline implementing Google ADK best practices.
    
    This pipeline provides enterprise-grade document processing with:
    - Intelligent document classification and routing
    - Specialized extraction agents for different document types
    - Quality validation and assurance mechanisms
    - Hierarchical coordination using ADK patterns
    """

    def __init__(self):
        self.session_service = InMemorySessionService()
        self.coordinator_agent = self._create_coordinator_agent()
        self.runner = self._create_runner()

    def _create_coordinator_agent(self) -> LlmAgent:
        """Create the main coordinator agent using hierarchical pattern"""
        
        # Create specialist sub-agents
        classifier_agent = create_document_classifier()
        contract_specialist = create_contract_specialist()
        invoice_specialist = create_invoice_specialist()
        general_specialist = create_general_specialist()
        validation_specialist = create_validation_specialist()

        # Main Coordinator Agent with Hierarchical Structure
        coordinator = LlmAgent(
            model="gemini-2.0-flash",
            name="document_extraction_coordinator",
            description="Main coordinator for intelligent document extraction pipeline with specialized sub-agents",
            instruction="""You are the main Document Extraction Coordinator managing a team of specialists.

COORDINATION WORKFLOW (4-Step Process):

STEP 1: DOCUMENT CLASSIFICATION
- Transfer to 'document_classifier' to analyze the document type
- Wait for classification results before proceeding

STEP 2: SPECIALIZED EXTRACTION  
- Based on classification, transfer to appropriate specialist:
  - For contracts/agreements: transfer to 'contract_specialist'
  - For invoices/bills: transfer to 'invoice_specialist' 
  - For other documents: transfer to 'general_specialist'
- Wait for extraction results before proceeding

STEP 3: QUALITY VALIDATION
- Transfer to 'validation_specialist' to validate extraction quality
- Wait for validation results before proceeding

STEP 4: PIPELINE SYNTHESIS
- Provide comprehensive summary of the complete pipeline results
- Include: classification → extraction → validation outcomes
- Highlight key findings and quality metrics

IMPORTANT COORDINATION RULES:
1. You MUST complete all 4 steps in sequence
2. After each transfer, wait for results before proceeding
3. Use get_shared_state tool to monitor progress between agents if needed
4. Each specialist agent will automatically save their results to session state via output_key
5. Make routing decisions based on the classification results from Step 1

You coordinate but do not perform extraction yourself - delegate to specialist agents.""",
            sub_agents=[
                classifier_agent,
                contract_specialist,
                invoice_specialist,
                general_specialist,
                validation_specialist,
            ],  # ADK Hierarchical Coordination Pattern
            tools=[get_shared_state],  # Only coordination tools, no output_schema
            disallow_transfer_to_parent=True,  # Top-level coordinator
            disallow_transfer_to_peers=True,
        )

        return coordinator

    def _create_runner(self) -> Runner:
        """Create the runner for the coordinator agent"""
        return Runner(
            agent=self.coordinator_agent,
            app_name="hierarchical_document_extraction_app",
            session_service=self.session_service,
        )

    async def process_document(self, document_content: str) -> dict[str, Any]:
        """
        Process a document through the hierarchical pipeline.
        
        Args:
            document_content (str): The document text to process
            
        Returns:
            dict: Processing results including classification, extraction, and validation
        """
        # Create a unique session for this document
        session_id = f"doc_session_{hash(document_content) % 10000}"
        
        session = await self.session_service.create_session(
            app_name="hierarchical_document_extraction_app",
            user_id="doc_processor",
            session_id=session_id
        )

        user_content = types.Content(
            role="user",
            parts=[types.Part.from_text(text=document_content)]
        )

        # Process through the hierarchical pipeline
        final_response = ""
        async for event in self.runner.run_async(
            user_id="doc_processor",
            session_id=session_id,
            new_message=user_content,
        ):
            if event.is_final_response() and event.content and event.content.parts:
                if event.content.parts[0].text:
                    final_response = event.content.parts[0].text
                    break

        # Retrieve final session state with all results
        final_session = await self.session_service.get_session(
            app_name="hierarchical_document_extraction_app",
            user_id="doc_processor",
            session_id=session_id
        )

        return {
            "coordinator_summary": final_response,
            "session_state": final_session.state if final_session else {},
            "session_id": session_id
        }


def main():
    """CLI entry point for hierarchical document processing."""
    
    # Sample document for testing
    SAMPLE_CONTRACT = """
    SERVICE AGREEMENT
    
    This Agreement is between CloudTech Solutions Inc. and Innovation Corp LLC.
    
    Services: Cloud migration consulting and implementation
    Contract Value: $85,000 USD
    Start Date: March 15, 2024
    End Date: October 15, 2024
    
    Payment Terms:
    - $25,000 upon contract execution
    - $35,000 upon migration planning completion  
    - $25,000 upon successful deployment
    
    Governing Law: State of Texas
    """
    
    async def run_demo():
        pipeline = HierarchicalDocumentPipeline()
        
        print("🏗️ Hierarchical Document Pipeline Demo")
        print("=" * 50)
        print("Processing sample contract through 4-step pipeline...")
        print()
        
        results = await pipeline.process_document(SAMPLE_CONTRACT)
        
        print("📊 COORDINATOR SUMMARY:")
        print(results["coordinator_summary"])
        print()
        
        print("💾 SESSION STATE RESULTS:")
        for key, value in results["session_state"].items():
            print(f"  {key}: {type(value).__name__}")
        print()
        
        print(f"📝 Session ID: {results['session_id']}")
    
    # Run the demo
    asyncio.run(run_demo())


if __name__ == "__main__":
    main()
