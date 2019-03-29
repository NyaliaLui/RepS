#Developed by Nyalia "Noticals" Lui
#Contact info:
#   email: noticalsesports@gmail.com
#   twitter: @noticals

import sys
import argparse
from reps import Dispatcher
import os

parser = argparse.ArgumentParser(description='A python script that extracts SC2 replays from zip and sorts them!')
parser.add_argument('archive', type=str, help='path to zip archive of replays')
parser.add_argument('-s', '--sort', type=str, choices=['p','m'], required=True, help='sort replays by player name (p) or by matchup (m)')
parser.add_argument('--enable-rename', action='store_true', help='enable replay renaming. off by default')

args = parser.parse_args()

#annonce which sort option was chosen
if args.sort is 'p':
    print("sort by player name enabled")

if args.sort is 'm':
    print("sort by matchup enabled")

try:
    ARCHIVE_MANAGER = Dispatcher(os.path.dirname(os.path.abspath(__file__)))
    name = ARCHIVE_MANAGER.dispatch(args.archive, args.sort, args.enable_rename)
    print(name)
except Exception as ex:
    print('Something went wrong: {0}'.format(ex))
