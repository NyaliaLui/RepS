1. Capture replays path, sort option, and target directory to store replays
    - Form the **Folder_Processor** with the target directory
    
2. Organize the replays with replays path and sort option
    - form the necessary **Inspector** accounting for the sort option
    - Do a Depth First Search for .SC2Replay files, each replays is converted to our **Replay** object. Use the **Inspector** to determine where the **Replay** goes.
    - Sort the replays chronologically, this way replays in the same series appear one-after-another
    - Indiciate whether replays are in the same game series
    - Create the necessary folders and sub-folders to store the newly organized replays
        * Copy each replay from their original location to their new locations
