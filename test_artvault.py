# test_artvault.py
"""
Tests for ArtVault module.
"""

import unittest
from artvault import ArtVault

class TestArtVault(unittest.TestCase):
    """Test cases for ArtVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ArtVault()
        self.assertIsInstance(instance, ArtVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ArtVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
