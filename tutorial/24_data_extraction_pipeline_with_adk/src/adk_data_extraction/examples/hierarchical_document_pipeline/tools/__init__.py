"""
Tools for Hierarchical Document Pipeline State Management

This module contains tools for managing shared state between agents
in the hierarchical document extraction pipeline, following ADK patterns.
"""

import logging
from datetime import datetime
from typing import Any

logger = logging.getLogger(__name__)


def save_classification_to_state(
    document_type: str,
    complexity: str,
    confidence: float,
    recommended_extractor: str,
    key_indicators: str,
) -> dict[str, Any]:
    """Tool to save classification results to shared state"""

    # This will be available to all agents in the session
    classification = {
        "document_type": document_type,
        "complexity_level": complexity,
        "confidence_score": confidence,
        "recommended_extractor": recommended_extractor,
        "key_indicators": key_indicators.split(",") if key_indicators else [],
        "estimated_processing_time": 30,  # Default estimate
        "timestamp": datetime.now().isoformat(),
    }

    logger.info(f"Classification saved: {document_type} (confidence: {confidence})")
    return {"status": "saved", "classification": classification}


def save_extraction_to_state(
    extraction_type: str, extraction_data: str
) -> dict[str, Any]:
    """Tool to save extraction results to shared state"""

    extraction_result = {
        "type": extraction_type,
        "data": extraction_data,
        "timestamp": datetime.now().isoformat(),
    }

    logger.info(f"Extraction saved: {extraction_type}")
    return {"status": "saved", "extraction": extraction_result}


def save_validation_to_state(
    is_valid: bool,
    confidence: float,
    completeness: float,
    issues: str,
    recommendation: str,
) -> dict[str, Any]:
    """Tool to save validation results to shared state"""

    validation_result = {
        "is_valid": is_valid,
        "confidence_score": confidence,
        "completeness_score": completeness,
        "issues": issues.split(",") if issues else [],
        "recommendation": recommendation,
        "timestamp": datetime.now().isoformat(),
    }

    logger.info(f"Validation completed: valid={is_valid}, confidence={confidence}")
    return {"status": "saved", "validation": validation_result}


def create_extraction_id(document_content: str) -> str:
    """Create a unique extraction ID based on document content hash"""
    import hashlib
    
    content_hash = hashlib.md5(document_content.encode()).hexdigest()[:8]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"extract_{timestamp}_{content_hash}"


def log_pipeline_step(step: str, status: str, details: str = "") -> dict[str, Any]:
    """Log pipeline step execution for monitoring and debugging"""
    
    log_entry = {
        "step": step,
        "status": status,
        "details": details,
        "timestamp": datetime.now().isoformat(),
    }
    
    logger.info(f"Pipeline step: {step} - {status}")
    if details:
        logger.debug(f"Step details: {details}")
    
    return {"status": "logged", "entry": log_entry}
