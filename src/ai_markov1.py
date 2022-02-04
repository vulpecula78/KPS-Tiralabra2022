import random

class AiMarkov1:
    '''Gorn ai, joka käyttää siirtonsa valitsemiseen 1. asteen Markovin ketjua.
    Pelaajan tekemät siirrot tallennetaan matriisiin sen mukaan, mikä oli pelaajan
    edellinen siirto. AI tekee oletuksen arvioi pelaajan seuraavasta siirrosta
    sen mukaan mitä pelaaja valitsi viimeisimmällä kierroksella ja tekee valintansa
    sen mukaan. Mikäli kaikilla vaihtoehdolla sama todennäköisyys tai tilastoa ei
    vielä ole, niin arvotaan.'''

    def __init__(self):
        self._siirto = ["k", "p", "s"]
        self._probs =  [[0,   0,   0],       #kivi
                        [0,   0,   0],       #paperi
                        [0,   0,   0]]       #sakset
        self._history = [[], [], []]
        self._rounds = 1
        self._selection = {'k':0, 'p':1, 's':2}

    def update_probs(self):
        if self._rounds > 1:
            earlier = self._history[0][-2]   #earlier choice, pelaajan aiempi valinta
            latest = self._history[0][-1]   #current choice, pelaajan viimeisin valinta
            self._probs[self._selection[earlier]][self._selection[latest]] += 1

    def choice(self):
        if self._rounds > 1:    #kun mitään tilastoja ei vielä ole, niin arvotaan...
            highest = max(self._probs[self._selection[self._history[0][-1]]])

            # Jos todennäköisyys on sama kaikilla vaihtoehdoilla, niin arvotaan
            if highest == min(self._probs[self._selection[self._history[0][-1]]]):
                return random.choice(self._siirto)

            assume = self._probs[self._selection[self._history[0][-1]]].index(highest)
            if assume == 0:
                return "p"
            if assume == 1:
                return "s"
            return "k"
        return random.choice(self._siirto)

    def add_round(self, player, computer, result):
        self._history[0].append(player)
        self._history[1].append(computer)
        self._history[2].append(result)
        self._rounds = len(self._history[0])
        self.update_probs()

    def get_history(self):
        return self._history, self._probs
