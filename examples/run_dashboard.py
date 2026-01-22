#!/usr/bin/env python
"""Example script demonstrating how to run the AIML Studio dashboard.

This script shows how to start the dashboard application and access it
from a web browser.

Usage:
    python examples/run_dashboard.py

The dashboard will be available at http://localhost:8050
"""

import sys
from pathlib import Path

# Add parent directory to path to allow imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from aiml_studio.app import main

if __name__ == "__main__":
    print("Starting AIML Studio Dashboard...")
    print("=" * 50)
    print("Dashboard Features:")
    print("  - Analytics: View experiment metrics and trends")
    print("  - Data Sources: Manage data connections")
    print("  - Projects: Track ML projects and experiments")
    print("=" * 50)
    print("\nAccess the dashboard at: http://localhost:8050")
    print("\nPress Ctrl+C to stop the server\n")
    
    main()
