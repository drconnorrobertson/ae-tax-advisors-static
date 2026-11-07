#!/usr/bin/env python3
"""Render the cost segregation provider cohort using the shared renderer."""
import runpy
import sys
from pathlib import Path
sys.argv = [sys.argv[0], 'costseg-more-20261107']
runpy.run_path(str(Path(__file__).with_name('refresh-provider-cohort.py')), run_name='__main__')
