# RepS
A python script that searches a folder and its sub-folders for SC2 replays and then sorts them!
RepS can sort by player name or by match up.

# Installation steps
* Must have [Python](https://www.python.org/downloads/) installed on your system. It was tested with Python2 but also works with Python3. Download Python [here](https://www.python.org/downloads/)
* This code uses [S2 Protocol](https://github.com/Blizzard/s2protocol) which is a python 2.X library for reading SC2 replays
* Download RepS via git or click green download button to get as .zip file
* extract the contents to anywhere on your machine
* __Success!__ You have downloaded and installed RepS!

# How to use RepS
1. Run `python RepS.py <replay folder> --sort {p|m} --target <destination folder>`
    - `--sort p` means sort the replays by player name
    - `--sort m` means sort the replays by match up
    - `--target <destination folder>` path to a folder where organized replays will be written to (optional)
2. The sorted replays will be in a newly created folder named **Replays**. If a target directory is given, then the replays will be in **target/Replays**

# Known Bugs/Issues
1. Replays that are not from the latest SC2 patch tend to have issues with [S2 Protocol](https://github.com/Blizzard/s2protocol).
2. sort by **matchup up** currently does not work for team game replays such as 2v2, 3v3, or 4v4.

# FAQ
1. RepS will create the folders in the given directory and will not modify or move the original copies.
2. sort by **player name** will result in the same replay appearing in the folders for every player in the game lobby.
3. sort by **player name** is case sensitive, so a player name __NoticALs__ and __noticals__ will have their own folders of replays.
4. Currently, running RepS on a collection that was already RepS'd will result in duplicates or undefined behaviour.

# SC2 Race Translations

### In proper language characters
| English | Chinese | Korean   |
|---------|---------|----------|
| Protoss | 星灵    | 프로토스 |
| Terran  | 人类    |     테란 |
| Zerg    | 异虫    | 저그     |

### In UTF-8 Format
| English | Chinese                  | Korean                                           |
|---------|--------------------------|--------------------------------------------------|
| Protoss | \xe6\x98\x9f\xe7\x81\xb5 | \xed\x94\x84\xeb\xa1\x9c\xed\x86\xa0\xec\x8a\xa4 |
| Terran  | \xe4\xba\xba\xe7\xb1\xbb |                         \xed\x85\x8c\xeb\x9e\x80 |
| Zerg    | \xe5\xbc\x82\xe8\x99\xab | \xec\xa0\x80\xea\xb7\xb8                         |