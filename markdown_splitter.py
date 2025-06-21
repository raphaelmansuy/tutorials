#!/usr/bin/env python3
"""
Markdown Splitter Script

This script takes a markdown file as input and extracts each ## paragraph 
into separate files in a subfolder. The subfolder name matches the input file name.

Usage:
    python markdown_splitter.py <input_file.md>

Example:
    python markdown_splitter.py 07_develop_ai_agent_with_google_adk.md

Requirements:
    - Python 3.11+
    - Input file must be a markdown file (.md extension)
"""

import sys
import re
from pathlib import Path
from typing import List, Tuple


def sanitize_filename(filename: str) -> str:
    """
    Sanitize a string to be used as a filename by removing or replacing
    characters that are not allowed in filenames.
    
    Args:
        filename (str): The original filename string
        
    Returns:
        str: A sanitized filename safe for filesystem use
    """
    # Replace problematic characters with underscores
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    # Replace multiple spaces with single underscore
    filename = re.sub(r'\s+', '_', filename)
    # Remove leading/trailing whitespace and dots
    filename = filename.strip(' .')
    # Limit length to avoid filesystem issues
    if len(filename) > 100:
        filename = filename[:100]
    return filename


def extract_h2_sections(content: str) -> List[Tuple[str, str]]:
    """
    Extract all ## sections from markdown content.
    
    Args:
        content (str): The markdown content to parse
        
    Returns:
        List[Tuple[str, str]]: List of tuples containing (title, content) for each section
    """
    sections = []
    lines = content.split('\n')
    current_section = None
    current_content = []
    
    for line in lines:
        # Check if line starts with ## (H2 header)
        if line.strip().startswith('## '):
            # Save previous section if exists
            if current_section is not None:
                sections.append((current_section, '\n'.join(current_content)))
            
            # Start new section
            current_section = line.strip()[3:].strip()  # Remove '## ' prefix
            current_content = [line]  # Include the header in content
            
        elif current_section is not None:
            # Check if we hit another header level that should end this section
            if line.strip().startswith('# ') and not line.strip().startswith('## '):
                # This is an H1, end current section
                sections.append((current_section, '\n'.join(current_content)))
                current_section = None
                current_content = []
            else:
                # Add line to current section
                current_content.append(line)
    
    # Don't forget the last section
    if current_section is not None:
        sections.append((current_section, '\n'.join(current_content)))
    
    return sections


def create_output_directory(input_file_path: Path) -> Path:
    """
    Create output directory based on input filename.
    
    Args:
        input_file_path (Path): Path to the input markdown file
        
    Returns:
        Path: Path to the created output directory
    """
    # Get filename without extension
    base_name = input_file_path.stem
    
    # Create output directory in the same location as input file
    output_dir = input_file_path.parent / base_name
    output_dir.mkdir(exist_ok=True)
    
    return output_dir


def write_section_file(output_dir: Path, section_title: str, content: str, index: int) -> Path:
    """
    Write a section to a separate markdown file.
    
    Args:
        output_dir (Path): Directory to write the file in
        section_title (str): Title of the section (for filename)
        content (str): Content to write
        index (int): Section index for ordering
        
    Returns:
        Path: Path to the created file
    """
    # Create filename with index and sanitized title
    sanitized_title = sanitize_filename(section_title)
    filename = f"{index:02d}_{sanitized_title}.md"
    
    file_path = output_dir / filename
    
    # Write content to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return file_path


def process_markdown_file(input_file_path: str) -> None:
    """
    Main function to process a markdown file and split it into sections.
    
    Args:
        input_file_path (str): Path to the input markdown file
    """
    input_path = Path(input_file_path)
    
    # Validate input file
    if not input_path.exists():
        print(f"Error: File '{input_file_path}' does not exist.")
        sys.exit(1)
    
    if not input_path.suffix.lower() == '.md':
        print(f"Error: File '{input_file_path}' is not a markdown file (.md extension required).")
        sys.exit(1)
    
    print(f"Processing file: {input_path}")
    
    # Read the markdown file
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except (IOError, OSError, UnicodeDecodeError) as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    
    # Extract H2 sections
    sections = extract_h2_sections(content)
    
    if not sections:
        print("No ## sections found in the file.")
        return
    
    print(f"Found {len(sections)} ## sections")
    
    # Create output directory
    output_dir = create_output_directory(input_path)
    print(f"Created output directory: {output_dir}")
    
    # Write each section to a separate file
    created_files = []
    for i, (title, section_content) in enumerate(sections, 1):
        file_path = write_section_file(output_dir, title, section_content, i)
        created_files.append(file_path)
        print(f"Created: {file_path.name}")
    
    print(f"\nSuccessfully split {len(sections)} sections into {output_dir}")
    print("Created files:")
    for file_path in created_files:
        print(f"  - {file_path.name}")


def main():
    """Main entry point of the script."""
    if len(sys.argv) != 2:
        print("Usage: python markdown_splitter.py <input_file.md>")
        print("\nExample:")
        print("  python markdown_splitter.py 07_develop_ai_agent_with_google_adk.md")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    try:
        process_markdown_file(input_file)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
    except (IOError, OSError) as e:
        print(f"File system error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
