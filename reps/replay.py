from s2protocol import versions
import mpyq
import sys

#Replay - a wrapper around S2 protocol replay files
class Replay:

    #names - list of player names in the replay lobby
    #matchup - the matchup which this replay has.
    #       Only looks at the first two players in list currently
    #       So, this does not mean anything for team game replays
    #archive - the mpyq archive of the replay
    #baseBuild - the base build of the replay according to s2protocol
    #header - the replay header information
    #protocol - the protocol for this replay
    #details - the list of details in JSON formation for this replay
    names = []
    matchup = ''
    archive = None
    baseBuild = None
    header = None
    protocol = None
    details = None

    def __init__(self, replay_file):
        self.names = []
        self.matchup = ''

        #generate MPQ archive
        self.archive = mpyq.MPQArchive(replay_file)
        
        #get the replays protocol version
        contents = self.archive.header['user_data_header']['content']
        self.header = versions.latest().decode_replay_header(contents)

        # The header's baseBuild determines which protocol to use
        #part of this code was modified from 
        #s2_cli.py @ https://github.com/Blizzard/s2protocol/tree/master/s2protocol
        self.baseBuild = self.header['m_version']['m_baseBuild']
        try:
            self.protocol = versions.build(self.baseBuild)
        except Exception, e:
            print >> sys.stderr, 'Unsupported base build: {0} ({1})'.format(self.baseBuild, str(e))
            sys.exit(1)

        #replay details
        contents = self.archive.read_file('replay.details')
        self.details = self.protocol.decode_replay_details(contents)

        #pre process for matchup and names
        num_players = len(self.details['m_playerList'])
        for i in range(num_players):
            info = self.__beautify_name(self.details['m_playerList'][i]['m_name'])
            race = self.details['m_playerList'][i]['m_race']

            self.names.append(info)

            if i < (num_players-1):
                self.matchup = self.matchup + race + ' vs. '
            else:
                self.matchup = self.matchup + race

    #beautify_name - strips a name of CSS/HTML intended characters
    #returns the clan tag and player name in an easier to read format
    def __beautify_name(self, name):
        info = name

        #only strip if they have a clan tag
        # the '<' or '>' signs are how we tell clan tag (&lt or &gt)
        if name.find('&lt;') > 0:
            infos = name.split('<sp/>')
            infos[0] = infos[0].replace('&lt;', '')
            infos[0] = infos[0].replace('&gt;', '')

            info = '[' + infos[0] + '] ' + infos[1]

        return info
