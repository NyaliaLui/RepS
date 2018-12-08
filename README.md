# RepS
A python script that searches a folder and its sub-folders for SC2 replays and then sorts them!
RepS can sort by player name or by match up.

# Installation steps
* Must have [Python2](https://www.python.org/downloads/) installed on your system. Download Python2 [here](https://www.python.org/downloads/)
* This code uses [S2 Protocol](https://github.com/Blizzard/s2protocol) which is a python 2.X library for reading SC2 replays
* Download RepS via git or click green download button to get as .zip file
* extract the contents to anywhere on your machine
* __Success!__ You have downloaded and installed RepS!

# How to use RepS
1. Run `python RepS.py <replay folder> --sort {p|m}`
    - `--sort p` means sort the replays by player name
    - `--sort m` means sort the replays by match up
2. The sorted replays will be in **folder/RepS**


# FAQ
1. RepS will create the folders in the given directory and will not modify or move the original copies.
2. sort by **player name** will result in the same replay appearing in both player's folders.
2. sort by **player name** is case sensitive, so a player name __NoticALs__ and __noticals__ will have their own folders of replays
