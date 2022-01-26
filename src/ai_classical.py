import random

class AiClassical:
    '''Palauttaa k, p tai s. Huomioi pelaajan 10 viimeistä siirtoa.
    Laskee todennäköisyydet seuraavalle siirrolle ja arpoo valinnan
    todennäköisyyteen perustuen. Jos todennäköisin oletus on, että
    pelaaja valitsee kiven, niin suurimmalla todennäköisyydellä
    arvotaan paperi'''

    def __init__(self):
        self._siirto = ["k", "p", "s"]
        self._probs = []
        self._history = [[], [], []]
        self._last_rounds = 10

    def choice(self):
        #Huomioidaan vain 10 viimeisintä siirtoa.
        if len(self._history[0]) <= self._last_rounds:
            history = 0
        else:
            history = len(self._history[0]) - self._last_rounds

        #lasketaan todennäköisyydet joilla pelaaja pelaa kiven, paperin tai sakset
        k_prob = (1 + self._history[0][history:].count("k")) / (3 + len(self._history[0][history:]))
        p_prob = (1 + self._history[0][history:].count("p")) / (3 + len(self._history[0][history:]))
        s_prob = (1 + self._history[0][history:].count("s")) / (3 + len(self._history[0][history:]))
        self._probs = [k_prob, p_prob, s_prob]
        #print(self._probs)

        #arvotaan tulos ja huomioidaan todennäköisyydet
        select = random.random()
        if select <= k_prob:
            return "p"
        if select <= p_prob + k_prob:
            return "s"
        return "k"

    def add_round(self, player, computer, result):
        self._history[0].append(player)
        self._history[1].append(computer)
        self._history[2].append(result)

    def get_history(self):
        return self._history, self._probs
