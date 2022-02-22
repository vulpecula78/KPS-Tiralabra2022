import random

class AiRandom:
    '''Palauttaa k, p, s, l tai v satunnaisesti arvottuna.
    Kaikilla tuloksilla yhtäsuuri todennäköisyys.'''

    def __init__(self, mode = False):
        if mode:
            self.__choices = ["k", "p", "s", "v", "l"]
        else:
            self.__choices = ["k", "p", "s"]
        self.__history = [[], [], []]
        self.__mode = mode

    def choose(self):
        '''Palauttaa listalta arvotun k, p, s, l tai v'''
        return random.choice(self.__choices)

    def get_history(self):
        '''palauttaa historian, todennäköisyydet.
        Todennäköisyys on aina sama kaikilla vaihtoehdoilla

        returns:
            self._history: Pelin kaikkien kierrosten tapahtumat.
        '''
        if self.__mode:
            return self.__history, [1/5, 1/5, 1/5, 1/5, 1/5]
        return self.__history, [1/3, 1/3, 1/3]

    def add_round(self, player, computer, result):
        '''Lisää pelatun kierroksen muistiin.

        args:
            player: Pelaajan tekemä valinta.
            computer: AI:n valinta.
            result: 1: AI voitto, -1: pelaajan voitto, 0: tasapeli'''
        self.__history[0].append(player)
        self.__history[1].append(computer)
        self.__history[2].append(result)
