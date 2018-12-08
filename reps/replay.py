from s2protocol import versions
import mpyq
import sys

#beautify_name - strips a name of CSS/HTML intended characters
#returns the clan tag and player name in an easier to read format
def beautify_name(name):
    infos = name.split('<sp/>')
    infos[0] = infos[0].replace('&lt;', '')
    infos[0] = infos[0].replace('&gt;', '')

    info = '[' + infos[0] + '] ' + infos[1]

    return info

#Replay - a wrapper around S2 protocol replay files
class Replay:

    names = []
    matchup = 'xvx'
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
        for i in range(len(self.details['m_playerList'])):
            info = beautify_name(self.details['m_playerList'][i]['m_name'])
            self.names.append(info)
