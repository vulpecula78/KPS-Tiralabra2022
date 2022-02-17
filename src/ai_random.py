import random

class AiRandom:
    '''Palauttaa k, p tai s satunnaisesti arvottuna.
    Kaikilla tuloksilla yhtäsuuri todennäköisyys.'''

    def __init__(self):
        self._siirto = ["k", "p", "s"]
        self._history = [[], [], []]

    def choose(self):
        '''Palauttaa listalta arvotun k, p tai s.'''
        return random.choice(self._siirto)

    def get_history(self):
        '''palauttaa historian, todennäköisyydet.
        Todennäköisyys on aina sama kaikilla vaihtoehdoilla:
        1/3

        returns:
            self._history: Pelin kaikkien kierrosten tapahtumat.
        '''
        return self._history, [1/3, 1/3, 1/3]

    def add_round(self, player, computer, result):
        '''Lisää pelatun kierroksen muistiin.

        args:
            player: Pelaajan tekemä valinta.
            computer: AI:n valinta.
            result: 1: AI voitto, -1: pelaajan voitto, 0: tasapeli'''
        self._history[0].append(player)
        self._history[1].append(computer)
        self._history[2].append(result)
