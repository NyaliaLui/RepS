from os import listdir, chdir, mkdir
from os.path import isdir, join
from shutil import copy as cp
from reps.inspector import NameInspector, MatchupInspector
from replay import Replay, is_replay

#FolderProcessor - a singleton which
#traverses a directory tree, organizes the replays using inspectors,
#and creates the proper subfolders
class FolderProcessor:

    __folders = {}
    __inspector = None

    def __init__(self):
        self.__folders = {}
        self.__inspector = None

    #create necessary subfolders from path
    def __create_folders(self):
        all_folders = folder_path.split('\\')

        for folder in all_folders:
            try:
                mkdir(folder)
            except FileExistsError:
                pass

            chdir(folder)


    #depth_first_search - recurssively search the folder structure for all replays
    #call the inspector to form and add to necessary buckets after reading a replay
    def __depth_first_search(self, start_path, inter_path):
        current_path = join(start_path, inter_path)
        dirs_and_files = listdir(current_path)
        dirs = []
        files = []

        for df in dirs_and_files:
            # print(current_path)

            if is_replay(join(current_path, df)):
                files.append(df)

            if isdir(join(current_path, df)):
                dirs.append(df)

        for i in range(len(dirs)):
            inter = join(inter_path, dirs[i])
            # print('recurse', inter)
            self.__depth_first_search(start_path, inter)


        #finished recursive steps, now we read replays found
        key = ''
        for i in range(len(files)):

            src_file = join(start_path, inter_path, files[i])
            replay = Replay(src_file)
            keys = self.__inspector.inspect(replay)
            
            #go through each key
            for j in range(len(keys)):
                key = keys[j]

                #place replays in proper folders
                if key in self.__folders.keys():
                    self.__folders[key].append(replay.names)
                else:
                    self.__folders[key] = []
                    self.__folders[key].append(replay.names)



    #organize_replays - conduct a depth first search on the given replay folder
    #and organize the replays.
    def organize_replays(self, folder_path, sort_type):
        
        #form the proper inspector
        if sort_type is 'p':
            self.__inspector = NameInspector()
        else:
            self.__inspector = MatchupInspector()
        
        #perform depth first search for replays
        self.__depth_first_search(folder_path, '')

        #create the necessary subfolders
        # self.__create_folders()

    def folders(self):
        return self.__folders
        
