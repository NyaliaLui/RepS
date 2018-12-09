#Matchup Inspector - the inspector which is only concerned with
#the 1v1 matchup of a replay.
class MatchupInspector:

    def __init__(self):
        pass

    #inspect - return the matchup seen in 
    #in this replay
    def inspect(self, replay):
        return replay.matchup
