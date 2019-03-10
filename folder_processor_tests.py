import unittest
import os
from reps import FolderProcessor
from shutil import rmtree
import traceback

class FolderProcessorTestCase(unittest.TestCase):
    def setUp(self):
        self.root_path = 'SampleReplays'
        self.fp = FolderProcessor(dest=self.root_path)

    def test_sortby_matchup(self):
        self.fp.organize_replays(self.root_path, 'm')

        #Replays must be a directory
        self.assertTrue(os.path.isdir(os.path.join(self.root_path, 'Replays')))

        #the matchup folder must be a directory
        temp_path = os.path.join(self.root_path, 'Replays', 'Protoss vs Terran')
        self.assertTrue(os.path.isdir(temp_path))

        #all 4 sample files must be in the directory
        files = os.listdir(temp_path)
        self.assertTrue(len(files) == 4)

        #remove the directory for further testing
        rmtree(os.path.join(self.root_path, 'Replays'))

    def test_sortby_player(self):
        self.fp.organize_replays('SampleReplays', 'p')

        #Replays must be a directory
        replays_path = os.path.join(self.root_path, 'Replays')
        self.assertTrue(os.path.isdir(replays_path))

        #the player folders must be directories
        fs = os.listdir(replays_path)
        temp_path1 = os.path.join(replays_path, fs[0])
        temp_path2 = os.path.join(replays_path, fs[1])
        self.assertTrue(os.path.isdir(temp_path1))
        self.assertTrue(os.path.isdir(temp_path2))

        #both plater folders must have all 4 sample replays
        files1 = os.listdir(temp_path1)
        files2 = os.listdir(temp_path2)
        self.assertTrue(len(files1) == 4)
        self.assertTrue(len(files2) == 4)

        #remove the directory for further testing
        rmtree(replays_path)

    def test_sort_twice(self):
        self.fp.organize_replays('SampleReplays', 'p')

        try:
            self.fp.organize_replays('SampleReplays', 'p')
        except Exception as ex:
            self.assertTrue('Replays folder is already formed' == str(ex))

        #remove the directory for further testing
        rmtree(os.path.join('SampleReplays', 'Replays'))