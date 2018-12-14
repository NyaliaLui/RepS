#Developed by Nyalia "Noticals" Lui
#Contact info:
#   email: noticalsesports@gmail.com
#   twitter: @noticals

import sys
import argparse
from os import getcwd
from reps import FolderProcessor

parser = argparse.ArgumentParser(description='A python script that searches a folder and its sub-folders for SC2 replays and then sorts them!')
parser.add_argument('folder', type=str, help='path to folder of replays')
parser.add_argument('-s', '--sort', type=str, choices=['p','m'], required=True, help='sort replays by player name (p) or by matchup (m)')

args = parser.parse_args()
if args.sort is 'p':
    print("sort by player name enabled")

if args.sort is 'm':
    print("sort by matchup enabled")

fp = FolderProcessor()
fp.organize_replays(args.folder, args.sort)
