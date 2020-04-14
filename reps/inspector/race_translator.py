#Race Translator
# @purpose - translate the SC2 race from any language into english
class RaceTranslator:

    #conversion_table - the table of race conversions

    def __init__(self):
        self.__conversion_table = {}

        #english
        self.__conversion_table['Protoss'] = 'Protoss'
        self.__conversion_table['Terran'] = 'Terran'
        self.__conversion_table['Zerg'] = 'Zerg'
        self.__conversion_table[b'Protoss'] = 'Protoss'
        self.__conversion_table[b'Terran'] = 'Terran'
        self.__conversion_table[b'Zerg'] = 'Zerg'

        #chinese
        self.__conversion_table['\xe6\x98\x9f\xe7\x81\xb5'] = 'Protoss'
        self.__conversion_table['\xe4\xba\xba\xe7\xb1\xbb'] = 'Terran'
        self.__conversion_table['\xe5\xbc\x82\xe8\x99\xab'] = 'Zerg'
        self.__conversion_table[b'\xe6\x98\x9f\xe7\x81\xb5'] = 'Protoss'
        self.__conversion_table[b'\xe4\xba\xba\xe7\xb1\xbb'] = 'Terran'
        self.__conversion_table[b'\xe5\xbc\x82\xe8\x99\xab'] = 'Zerg'

        #korean
        self.__conversion_table['\xed\x94\x84\xeb\xa1\x9c\xed\x86\xa0\xec\x8a\xa4'] = 'Protoss'
        self.__conversion_table['\xed\x85\x8c\xeb\x9e\x80'] = 'Terran'
        self.__conversion_table['\xec\xa0\x80\xea\xb7\xb8'] = 'Zerg'
        self.__conversion_table[b'\xed\x94\x84\xeb\xa1\x9c\xed\x86\xa0\xec\x8a\xa4'] = 'Protoss'
        self.__conversion_table[b'\xed\x85\x8c\xeb\x9e\x80'] = 'Terran'
        self.__conversion_table[b'\xec\xa0\x80\xea\xb7\xb8'] = 'Zerg'

        #german
        # Protoss and Zerg in German is still Protoss and Zerg (according to google translate)
        self.__conversion_table['Terraner'] = 'Terran'
        self.__conversion_table[b'Terraner'] = 'Terran'


    #translate
    # @params - a SC2 race as english, chinese (mandarin), or korean characters.
    #   all non-english representations must be in utf-8 form
    # @return - the SC2 race as english characters
    # @purpose - translate non-english SC2 races into their english forms
    def translate(self, sc2race):
        return self.__conversion_table[sc2race]
