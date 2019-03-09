import unittest
from reps.inspector import NameInspector, MatchupInspector

class InspectorTestCase(unittest.TestCase):
    def setUp(self):
        self.namer = NameInspector()
        self.matchupper = MatchupInspector()
        print('setup inspector test case')

    def tearDown(self):
        print('teardown inspector test case')

    def test_isten(self):
        self.assertTrue(True)