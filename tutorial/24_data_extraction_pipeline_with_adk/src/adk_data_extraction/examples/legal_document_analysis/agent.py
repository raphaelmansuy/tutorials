"""
Legal Document Analysis Pipeline with Google ADK

This example demonstrates advanced legal document analysis using Google ADK
with specialized agents for comprehensive legal document processing.
"""

from google.adk.agents import Agent

# Create the root agent that ADK will discover
root_agent = Agent(
    name="legal_document_analysis",
    model="gemini-2.0-flash",
    description="Provides comprehensive legal document analysis with specialized agents for expert-level processing",
    instruction="""You are a legal document analysis coordinator managing a team of specialized legal experts.

Your responsibilities:
1. Coordinate comprehensive legal document analysis
2. Extract and analyze legal terms, obligations, and risks
3. Provide compliance verification and assessment
4. Deliver integrated professional-grade legal analysis

Process legal documents through:
- Expert legal document analysis and extraction
- Financial terms and obligations identification
- Compliance and risk assessment
- Comprehensive legal data validation

Provide thorough, accurate, and professionally formatted legal analysis with:
- Contract metadata and parties
- Key terms and conditions
- Risk assessment and compliance issues
- Professional recommendations""",
)


class LegalDocumentAnalysisPipeline:
    """
    Advanced legal document analysis pipeline using Google ADK.
    
    This pipeline provides comprehensive legal document processing with:
    - Expert legal document analysis
    - Financial terms and obligations extraction
    - Compliance verification and risk assessment
    - Multi-agent coordination for complex legal workflows
    """

    def __init__(self):
        """Initialize the legal analysis pipeline"""
        self.session_service = InMemorySessionService()
        self.main_agent = self._create_main_agent()

    def _create_main_agent(self) -> LlmAgent:
        """Create the main legal analysis coordinator agent"""
        
        # Create specialized sub-agents
        legal_analyzer = create_legal_analyzer()
        contract_reviewer = create_contract_reviewer()
        compliance_checker = create_compliance_checker()

        # Main coordinator agent
        coordinator = LlmAgent(
            model="gemini-2.0-flash",
            name="legal_coordinator",
            description="Main coordinator for legal document analysis pipeline",
            instruction="""You are the main coordinator for a comprehensive legal document analysis pipeline.

Your responsibilities:
1. Coordinate the overall legal analysis workflow
2. Manage communication between specialized legal agents
3. Ensure comprehensive coverage of all legal aspects
4. Provide integrated analysis results
5. Handle complex legal document processing requirements

Available specialized agents:
- legal_analyzer: Primary legal document extraction and analysis
- contract_reviewer: Detailed contract review and risk assessment
- compliance_checker: Legal compliance verification and validation

Workflow:
1. Start with legal_analyzer for primary document analysis
2. Use contract_reviewer for detailed contract-specific analysis
3. Apply compliance_checker for regulatory compliance verification
4. Integrate all analyses into comprehensive legal assessment

Provide thorough, accurate, and professionally formatted legal analysis.""",
            sub_agents=[legal_analyzer, contract_reviewer, compliance_checker],
        )

        return coordinator

    async def analyze_document(self, document_path: str) -> LegalAnalysisResult:
        """
        Analyze a legal document using the complete pipeline
        
        Args:
            document_path: Path to the legal document to analyze
            
        Returns:
            LegalAnalysisResult: Complete analysis results
        """
        start_time = time.time()
        
        logger.info("Starting legal document analysis - Path: %s", document_path)

        try:
            # Read document content
            document_content = self._read_document(document_path)
            if not document_content:
                raise ValueError(f"Could not read document: {document_path}")

            # Create session for analysis
            session = await self.session_service.create_session()
            
            # Initialize runner
            runner = Runner(
                agent=self.main_agent,
                session_service=self.session_service,
                session_id=session.id,
            )

            # Process the document
            response = await runner.run(
                input_prompt=f"""Analyze this legal document comprehensively:

DOCUMENT PATH: {document_path}

DOCUMENT CONTENT:
{document_content}

Please provide:
1. Complete legal document analysis and extraction
2. Detailed contract review (if applicable)
3. Compliance verification and assessment
4. Risk analysis and recommendations
5. Comprehensive summary of all findings

Ensure thorough coverage of all legal aspects and provide professional-grade analysis."""
            )

            # Calculate processing time
            processing_time_ms = int((time.time() - start_time) * 1000)
            
            logger.info("Legal document analysis completed - Time: %dms", processing_time_ms)

            return {
                "document_path": document_path,
                "response": response,
                "analysis_status": "completed",
                "processing_time_ms": processing_time_ms,
                "session_id": session.id
            }

        except Exception as e:
            logger.error("Legal document analysis failed - Error: %s", str(e))
            
            return {
                "document_path": document_path,
                "error": str(e),
                "analysis_status": "failed",
                "processing_time_ms": int((time.time() - start_time) * 1000)
            }

    def _read_document(self, document_path: str) -> str:
        """Read document content from file"""
        try:
            with open(document_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            logger.error("Document not found: %s", document_path)
            return ""
        except PermissionError:
            logger.error("Permission denied reading: %s", document_path)
            return ""
        except UnicodeDecodeError:
            logger.error("Cannot decode document: %s", document_path)
            return ""


async def main():
    """
    Example usage of the Legal Document Analysis Pipeline
    """
    # Sample legal contract content
    sample_contract = """
    PROFESSIONAL SERVICES AGREEMENT
    
    This Professional Services Agreement ("Agreement") is entered into on March 1, 2024,
    between:
    
    CLIENT: Global Enterprises Inc., a Delaware corporation
    ADDRESS: 500 Corporate Blvd, Suite 100, New York, NY 10001
    
    CONSULTANT: Legal Advisory Services LLC, a New York limited liability company
    ADDRESS: 200 Law Center Drive, Albany, NY 12207
    
    TERMS AND CONDITIONS:
    
    1. SCOPE OF SERVICES
    Consultant agrees to provide legal advisory services including contract review,
    compliance analysis, and regulatory guidance.
    
    2. COMPENSATION
    - Professional Fee: $350 per hour
    - Retainer: $25,000 due upon execution
    - Monthly billing with Net 15 payment terms
    - Late payment penalty: 1.5% per month
    
    3. TERM
    - Effective Date: March 1, 2024
    - Initial Term: 12 months
    - Automatic renewal for additional 6-month periods
    - Either party may terminate with 30 days written notice
    
    4. OBLIGATIONS
    CLIENT OBLIGATIONS:
    - Provide timely access to necessary documents and information
    - Make payments according to agreed schedule
    - Maintain confidentiality of consultant's work product
    
    CONSULTANT OBLIGATIONS:
    - Provide services with professional competence
    - Maintain client confidentiality
    - Deliver work product within agreed timeframes
    - Carry professional liability insurance minimum $2M
    
    5. GOVERNING LAW
    This Agreement shall be governed by the laws of the State of New York.
    Any disputes shall be resolved through binding arbitration in New York County.
    
    6. INDEMNIFICATION
    Each party agrees to indemnify the other against third-party claims arising
    from their breach of this Agreement or negligent acts.
    
    IN WITNESS WHEREOF, the parties have executed this Agreement.
    
    GLOBAL ENTERPRISES INC.          LEGAL ADVISORY SERVICES LLC
    
    _________________________        _________________________
    Michael Johnson, CEO             Sarah Williams, Managing Partner
    Date: March 1, 2024             Date: March 1, 2024
    """

    # Write sample document to temporary file
    temp_file = "sample_legal_contract.txt"
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(sample_contract)

    try:
        # Initialize and run pipeline
        pipeline = LegalDocumentAnalysisPipeline()
        
        print("⚖️ Starting Legal Document Analysis Pipeline")
        print("=" * 60)
        print(f"Analyzing document: {temp_file}")
        print()
        
        result = await pipeline.analyze_document(temp_file)
        
        print("📄 Analysis Results:")
        print(f"   Document: {result['document_path']}")
        print(f"   Status: {result['analysis_status']}")
        print(f"   Processing Time: {result['processing_time_ms']}ms")
        
        if 'response' in result:
            print(f"\n🔍 Legal Analysis:")
            print(result['response'])
        
        if 'error' in result:
            print(f"\n❌ Error: {result['error']}")

    finally:
        # Clean up temporary file
        try:
            Path(temp_file).unlink()
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    asyncio.run(main())
