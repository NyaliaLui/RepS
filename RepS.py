#Developed by Nyalia "Noticals" Lui
#Contact info:
#   email: noticalsesports@gmail.com
#   twitter: @noticals

import sys
import argparse
from reps import FolderProcessor

parser = argparse.ArgumentParser(description='A python script that searches a folder and its sub-folders for SC2 replays and then sorts them!')
parser.add_argument('folder', type=str, help='path to folder of replays')
parser.add_argument('-s', '--sort', type=str, choices=['p','m'], required=True, help='sort replays by player name (p) or by matchup (m)')
parser.add_argument('-t', '--target', type=str, help='target folder for the replays')
parser.add_argument('--enable-rename', action='store_true', help='enable replay renaming. off by default')

args = parser.parse_args()

#annonce which sort option was chosen
if args.sort is 'p':
    print("sort by player name enabled")

if args.sort is 'm':
    print("sort by matchup enabled")

try:
    #put organized replays in target directory if enabled
    fp = (FolderProcessor(args.target) if args.target else FolderProcessor())
    fp.organize_replays(args.folder, args.sort, args.enable_rename)
except Exception as ex:
    print('Something went wrong: {0}'.format(ex))
