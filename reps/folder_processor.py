from os import listdir, chdir, mkdir
from os.path import isfile, isdir, join
from shutil import copy as cp

#FolderProcessor - a singleton which
#traverses a directory tree, organizes the replays using inspectors,
#and creates the proper subfolders
class FolderProcessor:

    _folders = {}

    def __init__(self):
        self._folders = {'reps': 'RepS'}

    #create necessary subfolders from path
    def __create_folders(self, folder_path):
        all_folders = folder_path.split('\\')

        for folder in all_folders:
            try:
                mkdir(folder)
            except FileExistsError:
                pass

            chdir(folder)


    #organize_replays - conduct a depth first search on the given replay folder
    #and organize the replays.
    def organize_replays(self, start_path, inter_path, player_name):
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
