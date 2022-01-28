import random

class AiRandom:
    '''Palauttaa k, p tai s satunnaisesti arvottuna.
    Kaikilla tuloksilla yhtäsuuri todennäköisyys.'''

    def __init__(self):
        self._siirto = ["k", "p", "s"]
        self._history = [[], [], []]

    def choice(self):
        '''Palauttaa listalta arvotun k, p tai s.'''
        return random.choice(self._siirto)

    def get_history(self):
        '''palauttaa historian, todennäköisyydet.
        Todennäköisyys on aina sama kaikilla vaihtoehdoilla:
        1/3'''
        return self._history, 1/3

    def add_round(self, player, computer, result):
        '''Lisää pelatun kierroksen muistiin'''
        self._history[0].append(player)
        self._history[1].append(computer)
        self._history[2].append(result)
