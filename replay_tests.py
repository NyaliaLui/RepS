import unittest
from reps import Replay


class ReplayTestCase(unittest.TestCase):
    def setUp(self):
        self.replay = Replay()
        print('setup replay test case')

    def tearDown(self):
        print('teardown replay test case')

    def test_isten(self):
        self.assertTrue(self.replay.series_flag == -1)