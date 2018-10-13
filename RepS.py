#Developed by Nyalia "Noticals" Lui
#Contact info:
#   email: noticalsesports@gmail.com
#   twitter: @noticals

import sys
from os import listdir, chdir, mkdir
from os.path import isfile, isdir, join
from shutil import copy as cp

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

#if len(sys.argv) != 3:
#    print('invalid args')
#    print('python RepS.py <player name> <destination folder>')
#    sys.exit(1)

player_name = 'ShoWTimE'
start_path = 'C:\\Users\\Nyalia Lui\\Documents\\StarCraft II\\Accounts\\75195470\\1-S2-1-2948360\\Replays\\Multiplayer\\2018 WCS Montreal'
inter_path = ''
desti_path = 'C:\\Users\\Nyalia Lui\\Documents\\StarCraft II\\Accounts\\75195470\\1-S2-1-2948360\\Replays\\Multiplayer\\2018-WCS-Montreal-Analysis'
dirs_to_move = []

search(start_path, inter_path, 'ShoWTimE')

# files = [f for f in listdir(start_path) if isfile(join(start_path, f))]
# dirs = [d for d in listdir(start_path) if isdir(join(start_path, f))]

# print(files)
# print('')
# print(dirs)
