#!/usr/bin/env python3
"""
Test script for the multi-agent extraction pipeline.

This script demonstrates how to use the multi-agent pipeline
with sample documents to show the complete workflow.
"""

import asyncio
import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from examples.multi_agent_pipeline import (
    MultiAgentExtractionPipeline,
    run_contract_example,
    run_invoice_example,
    run_general_document_example,
    run_pipeline_comparison
)

async def test_individual_examples():
    """Test each example individually"""
    print("Testing Multi-Agent Pipeline Examples")
    print("=" * 50)
    
    try:
        # Test contract processing
        print("1. Testing Contract Processing...")
        await run_contract_example()
        
        print("\n" + "=" * 50)
        
        # Test invoice processing
        print("2. Testing Invoice Processing...")
        await run_invoice_example()
        
        print("\n" + "=" * 50)
        
        # Test general document processing
        print("3. Testing General Document Processing...")
        await run_general_document_example()
        
        print("\n🎉 All individual tests completed successfully!")
        
    except Exception as e:
        print(f"❌ Error in individual tests: {e}")
        return False
    
    return True

async def test_pipeline_comparison():
    """Test the complete pipeline comparison"""
    print("\n" + "=" * 50)
    print("Testing Complete Pipeline Comparison")
    print("=" * 50)
    
    try:
        results = await run_pipeline_comparison()
        
        print("\n🎉 Pipeline comparison completed successfully!")
        print(f"Processed {len(results) - 1} document types") # -1 for averages
        
        return True
        
    except Exception as e:
        print(f"❌ Error in pipeline comparison: {e}")
        return False

async def test_pipeline_directly():
    """Test the pipeline directly with custom content"""
    print("\n" + "=" * 50)
    print("Testing Pipeline Directly")
    print("=" * 50)
    
    pipeline = MultiAgentExtractionPipeline()
    
    # Test with a simple email
    test_email = """
    From: john.doe@company.com
    To: team@company.com
    Subject: Project Update - Q1 2024
    
    Hi Team,
    
    I wanted to provide a quick update on our Q1 2024 project status:
    
    - Development milestone reached on March 15th
    - Testing phase starts March 20th
    - Deployment scheduled for March 30th
    
    Please let me know if you have any questions.
    
    Best regards,
    John Doe
    Project Manager
    Phone: 555-123-4567
    """
    
    try:
        print("Processing test email...")
        result = await pipeline.process_document(test_email)
        
        print(f"✅ Email processed successfully!")
        print(f"Document Type: {result.classification.document_type}")
        print(f"Processing Time: {result.processing_time_ms}ms")
        print(f"Confidence: {result.validation.confidence_score:.2f}")
        print(f"Status: {result.pipeline_status}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error in direct pipeline test: {e}")
        return False

def main():
    """Main test function"""
    print("Multi-Agent Extraction Pipeline Test Suite")
    print("=" * 60)
    print("This test suite demonstrates the multi-agent pipeline capabilities")
    print("with various document types and processing scenarios.")
    print()
    
    async def run_all_tests():
        """Run all test scenarios"""
        results = []
        
        # Test 1: Individual examples
        results.append(await test_individual_examples())
        
        # Test 2: Pipeline comparison
        results.append(await test_pipeline_comparison())
        
        # Test 3: Direct pipeline test
        results.append(await test_pipeline_directly())
        
        return results
    
    try:
        # Run all tests
        test_results = asyncio.run(run_all_tests())
        
        # Summary
        print("\n" + "=" * 60)
        print("TEST SUMMARY")
        print("=" * 60)
        print(f"Total Tests: {len(test_results)}")
        print(f"Passed: {sum(test_results)}")
        print(f"Failed: {len(test_results) - sum(test_results)}")
        
        if all(test_results):
            print("\n🎉 ALL TESTS PASSED!")
            print("The multi-agent pipeline is working correctly.")
        else:
            print("\n❌ SOME TESTS FAILED!")
            print("Please check the error messages above.")
            
    except KeyboardInterrupt:
        print("\n\n🛑 Tests interrupted by user")
    except Exception as e:
        print(f"\n❌ Test suite failed: {e}")
        print("Please ensure your Google API key is configured properly.")

if __name__ == "__main__":
    main()
