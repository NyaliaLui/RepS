#Developed by Nyalia "Noticals" Lui
#Contact info:
#   email: noticalsesports@gmail.com
#   twitter: @noticals

import sys
from os import listdir, chdir, mkdir
from os.path import isfile, isdir, join
from shutil import copy as cp
import argparse
from s2protocol import versions
import mpyq

#create necessary subfolders from path
def create_folders(folder_path):
    all_folders = folder_path.split('\\')

    for folder in all_folders:
        try:
            mkdir(folder)
        except FileExistsError:
            pass

        chdir(folder)

#this search is looking at the directory names
def search(start_path, inter_path, player_name):
    current_path = join(start_path, inter_path)
    dirs_and_files = listdir(current_path)
    dirs = []
    files = []

    for df in dirs_and_files:
        # print(current_path)

        if isfile(join(current_path, df)):
            files.append(df)

        if isdir(join(current_path, df)):
            dirs.append(df)

    for i in range(len(dirs)):
        inter = join(inter_path, dirs[i])
        # print('recurse', inter)
        search(start_path, inter, player_name)

    #we are now down recursing. So, create files if applicable

    if player_name in inter_path:

        #make CWD the destination root
        chdir(desti_path)
        create_folders(inter_path)

        dst_dir = join(desti_path, inter_path)

        for i in range(len(files)):
            #copy the file to necessary folder.
            #I might need to re-create the directory structure right away.
            #I'll need a check to see if the directory is already created,
            #if so, just copy the file over, otherwise create it.
            src_file = join(start_path, inter_path, files[i])
            cp(src_file, dst_dir)
            print('create--> ', inter_path+'\\'+files[i])

#process_replay - processes a SC2 replay and returns replay archive
def process_replay(replay):
    return mpyq.MPQArchive(replay)

#get_details - returns the SC2 details listing of a SC2 replay archive
#part of this code was modified from 
#s2_cli.py @ https://github.com/Blizzard/s2protocol/tree/master/s2protocol
def get_details(archive):
    contents = archive.header['user_data_header']['content']
    header = versions.latest().decode_replay_header(contents)

    # The header's baseBuild determines which protocol to use
    baseBuild = header['m_version']['m_baseBuild']
    try:
        protocol = versions.build(baseBuild)
    except Exception, e:
        print >> sys.stderr, 'Unsupported base build: {0} ({1})'.format(baseBuild, str(e))
        sys.exit(1)

    contents = archive.read_file('replay.details')
    details = protocol.decode_replay_details(contents)

    return details

#beautify_name - strips names of CSS/HTML intended characters
#returns the clan tag and player name in an easier to read format
def beautify_name(name):
    infos = name.split('<sp/>')
    infos[0] = infos[0].replace('&lt;', '')
    infos[0] = infos[0].replace('&gt;', '')

    info = '[' + infos[0] + '] ' + infos[1]

    return info

#player_names - returns a list with the names of all
#the players in the SC2 game lobby
def player_names(details):
    names = []

    for i in range(len(details['m_playerList'])):
        info = beautify_name(details['m_playerList'][i]['m_name'])
        names.append(info)

    return names

parser = argparse.ArgumentParser(description='A python script that searches a folder and its sub-folders for SC2 replays and then sorts them!')
parser.add_argument('folder', type=str, help='path to folder of replays')
parser.add_argument('-s', '--sort', type=str, choices=['p','m'], required=True, help='sort replays by player name (p) or by matchup (m)')

args = parser.parse_args()
if args.sort is 'p':
    print("sort by player enabled")

if args.sort is 'm':
    print("sort by matchup enabled")

print(args.folder)

try:
    archive = process_replay('sample.SC2Replay')
    details = get_details(archive)
    names = player_names(details)

    print(names)
except Exception, e:
    print('something went wrong.\n', str(e))
    sys.exit(1)
