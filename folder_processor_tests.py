import unittest
from reps import FolderProcessor

class FolderProcessorTestCase(unittest.TestCase):
    def setUp(self):
        self.fp = FolderProcessor('bling')
        print('setup folder processor test case')

    def tearDown(self):
        print('teardown folder processor test case')

    def test_isten(self):
        self.assertTrue(True)