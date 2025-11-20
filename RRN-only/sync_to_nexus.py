#!/usr/bin/env python3
"""
Sync notebook from data-challenge-notebooks to roman_notebooks repository.

This script copies the nexus_microlensing_data_challenge_workflow.ipynb notebook
from the data-challenge-notebooks repo to the roman_notebooks repo, maintaining
separate formatting and contributing rules while keeping the content in sync.

Usage:
    python sync_to_nexus.py [--dry-run] [--target-dir TARGET_DIR]

Options:
    --dry-run          Show what would be copied without actually copying
    --target-dir DIR   Override the default target directory
"""

import argparse
import json
import shutil
import sys
from pathlib import Path


def get_repo_paths():
    """Get the source and target repository paths."""
    # Get the script's directory (should be in data-challenge-notebooks)
    script_dir = Path(__file__).parent.resolve()
    
    # Source is the current repo
    source_repo = script_dir
    
    # Target is the roman_notebooks repo (sibling directory)
    target_repo = source_repo.parent / "roman_notebooks"
    
    if not target_repo.exists():
        raise FileNotFoundError(
            f"Target repository not found at {target_repo}. "
            "Please ensure roman_notebooks is a sibling directory."
        )
    
    return source_repo, target_repo


def get_notebook_paths(source_repo, target_repo):
    """Get source and target notebook paths."""
    source_notebook = source_repo / "nexus_microlensing_data_challenge_workflow.ipynb"
    target_dir = target_repo / "content" / "notebooks" / "microlensing_data_challenge"
    target_notebook = target_dir / "nexus_microlensing_data_challenge_workflow.ipynb"
    
    return source_notebook, target_notebook, target_dir


def validate_paths_in_notebook(notebook_path, target_repo):
    """
    Validate that relative paths in the notebook are correct for roman_notebooks.
    
    Parameters
    ----------
    notebook_path : Path
        Path to the notebook file
    target_repo : Path
        Path to the roman_notebooks repository root
        
    Returns
    -------
    list
        List of warnings about potentially incorrect paths
    """
    warnings = []
    
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Check all markdown cells for relative paths
    for cell in notebook.get('cells', []):
        if cell.get('cell_type') == 'markdown':
            source = ''.join(cell.get('source', []))
            
            # Look for relative paths (../../ or ../)
            import re
            # Match markdown links and image tags with relative paths
            relative_path_pattern = r'(?:src|href)=["\'](\.\.\/[^"\']+)["\']'
            matches = re.findall(relative_path_pattern, source)
            
            for match in matches:
                # Check if path would be valid from target location
                target_notebook_dir = target_repo / "content" / "notebooks" / "microlensing_data_challenge"
                test_path = (target_notebook_dir / match).resolve()
                
                # Check if it's within the repo
                try:
                    test_path.relative_to(target_repo.resolve())
                except ValueError:
                    warnings.append(
                        f"Path '{match}' may be invalid from target location"
                    )
    
    return warnings


def sync_notebook(dry_run=False, target_dir_override=None):
    """
    Sync the notebook from data-challenge-notebooks to roman_notebooks.
    
    Parameters
    ----------
    dry_run : bool
        If True, show what would be done without actually copying
    target_dir_override : str, optional
        Override the default target directory path
    """
    try:
        source_repo, target_repo = get_repo_paths()
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    
    source_notebook, target_notebook, target_dir = get_notebook_paths(
        source_repo, target_repo
    )
    
    if target_dir_override:
        target_dir = Path(target_dir_override)
        target_notebook = target_dir / source_notebook.name
    
    # Check if source exists
    if not source_notebook.exists():
        print(f"Error: Source notebook not found at {source_notebook}", file=sys.stderr)
        sys.exit(1)
    
    # Validate paths in source notebook
    warnings = validate_paths_in_notebook(source_notebook, target_repo)
    if warnings:
        print("Warnings about paths in notebook:")
        for warning in warnings:
            print(f"  - {warning}")
        print()
    
    # Show what will be done
    print(f"Source: {source_notebook}")
    print(f"Target: {target_notebook}")
    print()
    
    if dry_run:
        print("DRY RUN: Would copy notebook (no changes made)")
        return
    
    # Create target directory if it doesn't exist
    target_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy the notebook
    shutil.copy2(source_notebook, target_notebook)
    print(f"✓ Copied notebook to {target_notebook}")
    
    # Check if there's a requirements.txt to copy as well
    source_requirements = source_repo / "requirements.txt"
    if source_requirements.exists():
        target_requirements = target_dir / "requirements.txt"
        shutil.copy2(source_requirements, target_requirements)
        print(f"✓ Copied requirements.txt to {target_requirements}")
    
    print("\nNext steps:")
    print(f"  1. cd {target_repo}")
    print("  2. Review the changes: git diff")
    print("  3. Add to git: git add content/notebooks/microlensing_data_challenge/")
    print("  4. Commit and push as needed")
    print("  5. Create PR to roman_notebooks repository")


def main():
    """Main entry point for the sync script."""
    parser = argparse.ArgumentParser(
        description="Sync notebook from data-challenge-notebooks to roman_notebooks"
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be copied without actually copying'
    )
    parser.add_argument(
        '--target-dir',
        type=str,
        help='Override the default target directory path'
    )
    
    args = parser.parse_args()
    sync_notebook(dry_run=args.dry_run, target_dir_override=args.target_dir)


if __name__ == '__main__':
    main()

