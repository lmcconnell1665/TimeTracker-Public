"""
Unit tests for the main function
"""

import pytest
import main

def test_main_output():
    """
    Confirms that the main function returns something
    """
    assert main.main() is not None
