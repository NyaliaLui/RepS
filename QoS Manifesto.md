# Quality of Service Manifesto
This document describes the core features and attributes which RepS must satisfy at all times.

1. When RepS is run, the necessary sub-folders must be created based on sort type
2. Sort by matchup, must create one sub-folder for each matchup in the replay collection and place all replays in their proper locations
3. Sort by player name, must create 1 sub-folder for each name in the replay collection and place all matching replays in their proper folders
4. Master branch must pass 100% of test cases
5. A branch can only be merged into master if it passes 100% of test cases
6. A branch can only be merged into master if it adheres to all points in the QoS Manifesto
7. A comment block must be written above every function and class
    - Function's must have comments which describes the constructs purpose, input parameters, and expected return value
    - Classes must have comments which describe the constructs puprose
    - the `__init__` function is excempt from this rule.
    - See `reps/folder_processor.py` for example
8. All descriptions in `Docs/` must have a readability consensus of grade 8 or lower
    - We use [Readability Formulas](http://www.readabilityformulas.com/free-readability-formula-tests.php) for this