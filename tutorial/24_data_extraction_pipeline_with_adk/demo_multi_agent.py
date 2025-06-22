#!/usr/bin/env python3
"""
Simple Multi-Agent Pipeline Demo

This script demonstrates the multi-agent pipeline with a simple example
that matches the patterns used in the working examples.
"""

import asyncio
import os
import sys

# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from adk_data_extraction.examples.multi_agent_pipeline import MultiAgentExtractionPipeline
except ImportError:
    print("❌ Could not import multi_agent_pipeline module")
    print("Make sure you're running this from the tutorial directory")
    print("and that you've installed the dependencies with 'make install'")
    sys.exit(1)


async def simple_demo():
    """Simple demonstration of the multi-agent pipeline"""
    print("🚀 Multi-Agent Pipeline Simple Demo")
    print("=" * 50)
    
    # Initialize the pipeline
    pipeline = MultiAgentExtractionPipeline()
    
    # Sample business email for testing
    sample_email = """
    From: sarah.johnson@techcorp.com
    To: project-team@techcorp.com
    Subject: Q1 Project Status Update
    Date: March 15, 2024
    
    Hi Team,
    
    I wanted to share our Q1 project progress:
    
    Key Milestones Completed:
    - Requirements gathering: February 28, 2024
    - System design: March 10, 2024
    - Initial development phase: March 15, 2024
    
    Financial Update:
    - Budget allocation: $50,000
    - Spent to date: $32,000
    - Remaining budget: $18,000
    
    Team Updates:
    - John Smith (john@techcorp.com) - Lead Developer
    - Lisa Chen (lisa@techcorp.com) - QA Engineer  
    - Mike Rodriguez (mike@techcorp.com) - Project Manager
    
    Next Steps:
    1. Complete testing phase by March 30, 2024
    2. User acceptance testing in April
    3. Production deployment by April 15, 2024
    
    Please reach out if you have any questions.
    
    Best regards,
    Sarah Johnson
    Project Director
    Phone: (555) 123-4567
    """
    
    try:
        print("📄 Processing sample business email...")
        print("Content preview:", sample_email[:100] + "...")
        
        # Process the document through the pipeline
        result = await pipeline.process_document(sample_email)
        
        print("\n✅ Processing completed!")
        print(f"📊 Results Summary:")
        print(f"  - Document ID: {result.extraction_id[:8]}...")
        print(f"  - Document Type: {result.classification.document_type}")
        print(f"  - Complexity: {result.classification.complexity_level}")
        print(f"  - Processing Time: {result.processing_time_ms}ms")
        print(f"  - Pipeline Status: {result.pipeline_status}")
        print(f"  - Requires Review: {'Yes' if result.requires_review else 'No'}")
        
        print(f"\n🔍 Classification Details:")
        print(f"  - Confidence: {result.classification.confidence_score:.2f}")
        print(f"  - Recommended Extractor: {result.classification.recommended_extractor}")
        print(f"  - Key Indicators: {', '.join(result.classification.key_indicators[:3])}")
        
        print(f"\n📊 Extracted Data Summary:")
        if hasattr(result.extracted_data, 'document_title'):
            print(f"  - Title: {result.extracted_data.document_title}")
            print(f"  - Main Entities: {len(result.extracted_data.main_entities)} found")
            print(f"  - Key Dates: {len(result.extracted_data.key_dates)} found")
            print(f"  - Action Items: {len(result.extracted_data.action_items)} found")
            print(f"  - Contact Info: {len(result.extracted_data.contact_info)} found")
        
        print(f"\n✅ Validation Results:")
        print(f"  - Valid: {result.validation.is_valid}")
        print(f"  - Confidence: {result.validation.confidence_score:.2f}")
        print(f"  - Completeness: {result.validation.completeness_score:.2f}")
        print(f"  - Recommendation: {result.validation.recommendation}")
        
        if result.validation.quality_issues:
            print(f"  - Quality Issues: {', '.join(result.validation.quality_issues[:2])}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error processing document: {e}")
        print("This might be due to API configuration issues.")
        print("Please ensure your GOOGLE_API_KEY is set in your environment.")
        return False


async def quick_classification_demo():
    """Quick demonstration of just the classification step"""
    print("\n🎯 Quick Classification Demo")
    print("=" * 30)
    
    pipeline = MultiAgentExtractionPipeline()
    
    # Different document types for classification testing
    test_documents = {
        "Contract": "This Service Agreement is entered into between Company A and Company B for software development services...",
        "Invoice": "Invoice #INV-2024-001\nBill To: Customer Name\nAmount Due: $1,500.00\nDue Date: March 30, 2024",
        "Meeting Notes": "Meeting minutes from March 15, 2024\nAttendees: John, Sarah, Mike\nAction items: Complete testing by month end",
        "Email": "From: user@company.com\nSubject: Project Update\nHi team, here's the latest status..."
    }
    
    print("Testing document classification...")
    
    for doc_type, content in test_documents.items():
        try:
            classification = await pipeline.classify_document(content)
            print(f"  📄 {doc_type:12} → {classification.document_type:10} (confidence: {classification.confidence_score:.2f})")
        except Exception as e:
            print(f"  ❌ {doc_type:12} → Error: {str(e)[:50]}")
    
    return True


def main():
    """Main demo function"""
    print("Multi-Agent Pipeline Demo")
    print("=" * 30)
    print("This demo shows the multi-agent pipeline in action")
    print("with document classification, extraction, and validation.")
    print()
    
    # Check environment
    if not os.getenv('GOOGLE_API_KEY'):
        print("⚠️  Warning: GOOGLE_API_KEY not found in environment")
        print("The demo may fail without proper API credentials.")
        print("Please set your API key with: export GOOGLE_API_KEY='your-key-here'")
        print()
    
    async def run_demos():
        """Run all demonstration scenarios"""
        try:
            # Demo 1: Complete pipeline
            success1 = await simple_demo()
            
            # Demo 2: Classification only
            success2 = await quick_classification_demo()
            
            return success1 and success2
            
        except KeyboardInterrupt:
            print("\n🛑 Demo interrupted by user")
            return False
        except Exception as e:
            print(f"\n❌ Demo failed: {e}")
            return False
    
    # Run the demos
    try:
        success = asyncio.run(run_demos())
        
        print("\n" + "=" * 50)
        if success:
            print("🎉 Demo completed successfully!")
            print("The multi-agent pipeline is working correctly.")
            print("\nNext steps:")
            print("- Try with your own documents")
            print("- Explore the full examples with: make run_multi_agent_example")
            print("- Check out the complete test suite: make test_multi_agent")
        else:
            print("❌ Demo encountered issues.")
            print("Please check your API configuration and try again.")
            
    except Exception as e:
        print(f"❌ Demo failed to start: {e}")
        print("Please ensure dependencies are installed: make install")


if __name__ == "__main__":
    main()
