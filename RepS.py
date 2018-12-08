#Developed by Nyalia "Noticals" Lui
#Contact info:
#   email: noticalsesports@gmail.com
#   twitter: @noticals

import sys
import argparse

from reps.inspector import NameInspector, MatchupInspector
from reps import Replay, FolderProcessor

parser = argparse.ArgumentParser(description='A python script that searches a folder and its sub-folders for SC2 replays and then sorts them!')
parser.add_argument('folder', type=str, help='path to folder of replays')
parser.add_argument('-s', '--sort', type=str, choices=['p','m'], required=True, help='sort replays by player name (p) or by matchup (m)')

args = parser.parse_args()
if args.sort is 'p':
    print("sort by player name enabled")
    nis = NameInspector()
    nis.inspect('replay')

if args.sort is 'm':
    print("sort by matchup enabled")
    mis = MatchupInspector()
    mis.inspect('replay')

print(args.folder)

replay = Replay('sample.SC2Replay')
print(replay.names)

fp = FolderProcessor()
