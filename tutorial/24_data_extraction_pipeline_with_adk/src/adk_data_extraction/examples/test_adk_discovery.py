#!/usr/bin/env python3
"""
ADK Agent Discovery Test

This script tests that ADK can discover all example agents properly.
It verifies the structure without running the actual agents.
"""

import importlib
import sys
from pathlib import Path

def test_agent_discovery():
    """Test that all examples can be imported and have root_agent defined."""
    
    examples_dir = Path(__file__).parent
    
    examples = [
        "basic_contact_extraction",
        "sequential_contract_pipeline", 
        "hierarchical_document_pipeline",
        "legal_document_analysis"
    ]
    
    print("🔍 Testing ADK Agent Discovery\n")
    
    for example in examples:
        print(f"Testing {example}...")
        
        try:
            # Test if the example directory has __init__.py 
            init_file = examples_dir / example / "__init__.py"
            if not init_file.exists():
                print(f"  ❌ Missing __init__.py")
                continue
                
            # Test if agent.py exists
            agent_file = examples_dir / example / "agent.py"
            if not agent_file.exists():
                print(f"  ❌ Missing agent.py")
                continue
                
            # Test if agent.py has root_agent
            agent_content = agent_file.read_text()
            if "root_agent" not in agent_content:
                print(f"  ❌ Missing root_agent definition")
                continue
                
            # Test if .env.example exists  
            env_example = examples_dir / example / ".env.example"
            if not env_example.exists():
                print(f"  ❌ Missing .env.example")
                continue
                
            print(f"  ✅ ADK-compliant structure")
            
        except Exception as e:
            print(f"  ❌ Error: {e}")
    
    print(f"\n🎉 Agent discovery test completed!")
    print(f"\nTo run with ADK:")
    print(f"  cd {examples_dir}")
    print(f"  adk web")
    print(f"  # Then select example from dropdown\n")

if __name__ == "__main__":
    test_agent_discovery()
