import unittest
from reps import FolderProcessor

class FolderProcessorTestCase(unittest.TestCase):
    def setUp(self):
        self.fp = FolderProcessor('bling')

    def test_isten(self):
        self.assertTrue(True)