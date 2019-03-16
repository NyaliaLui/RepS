# Basic Sorting Code

1. Capture replays path, sort option, and target directory to store replays
    - Form the **Folder_Processor** with the target directory
    
2. Organize the replays with replays path and sort option
    - form the necessary **Inspector** accounting for the sort option
    - Do a Depth First Search for .SC2Replay files, each replays is converted to our **Replay** object. Use the **Inspector** to determine where the **Replay** goes.
    - Sort the replays chronologically, this way replays in the same series appear one-after-another
    - Indiciate whether replays are in the same game series
    - Create the necessary folders and sub-folders to store the newly organized replays
        * Copy each replay from their original location to their new locations

# Multithreaded Sorting Code

1. Capture zip archive of replays

2. Dispatch archive to one of several **Sorters** available with **__Dispatcher.dispatch(archive_name)__**

3. Internal to Dispatcher, maintains a [ThreadPool](https://docs.python.org/2/library/multiprocessing.html) and a record of available **Sorters.**

4. When a **Sorter** is available, call **__pool.apply_async(sort_archive, archive_name)__** which will extract archive contents, sort, and re-zipp. Once complete, the result should be the path to sorted archive.