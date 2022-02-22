import random

class AiMarkov1:
    '''Gorn ai, joka käyttää siirtonsa valitsemiseen 1. asteen Markovin ketjua.
    Pelaajan tekemät siirrot tallennetaan matriisiin sen mukaan, mikä oli pelaajan
    edellinen siirto. AI tekee oletuksen arvioi pelaajan seuraavasta siirrosta
    sen mukaan mitä pelaaja valitsi viimeisimmällä kierroksella ja tekee valintansa
    sen mukaan. Mikäli kaikilla vaihtoehdolla sama todennäköisyys tai tilastoa ei
    vielä ole, niin arvotaan.'''

    def __init__(self, mode = False):
        if mode:
            self.__choices = ["k", "p", "s", "l", "v"]
            self.__probs =  [[0,   0,   0,   0,   0],       #kivi
                            [0,   0,   0,   0,   0],       #paperi
                            [0,   0,   0,   0,   0],       #sakset
                            [0,   0,   0,   0,   0],       #lisko
                            [0,   0,   0,   0,   0]]       #spock
        else:
            self.__choices = ["k", "p", "s"]
            self.__probs =   [[0,   0,   0],      #kivi
                              [0,   0,   0],       #paperi
                              [0,   0,   0]]       #sakset
                            
        self.__mode = mode
        
        self._history = [[], [], []]
        self._rounds = 1
        self._selection = {'k':0, 'p':1, 's':2, 'v':4, 'l':3, 0:'k', 1:'p', 2:'s', 3:'l', 4:'v'}

    def update_probs(self):
        '''Lisää tehdyn siirron self._probs matriisiin'''
        if self._rounds > 1:
            earlier = self._history[0][-2]   #earlier choice, pelaajan aiempi valinta
            latest = self._history[0][-1]   #current choice, pelaajan viimeisin valinta
            self.__probs[self._selection[earlier]][self._selection[latest]] += 1

    def choose(self):
        '''Palauttaa k, p tai s sen mukaan minkälaisen valinnan
        pelaaja on aiemmalla kierroksella tehnyt tai valitsee
        satunnaisesti, mikäli todennäköisyydet ovat yhtä suuria.

        returns:
            'k','p', tai 's'
        '''
        if self._rounds > 1:    #kun mitään tilastoja ei vielä ole, niin arvotaan...
            highest = max(self.__probs[self._selection[self._history[0][-1]]])

            # Jos todennäköisyys on sama kaikilla vaihtoehdoilla, niin arvotaan
            if highest == min(self.__probs[self._selection[self._history[0][-1]]]):
                return random.choice(self.__choices)

            highest_index = self.__probs[self._selection[self._history[0][-1]]].index(highest)
            assumed = self._selection[highest_index]

            if self.__mode:
                if assumed == 'k':
                    return random.choice(['p', 'v'])
                if assumed == 'p':
                    return random.choice(['s', 'l'])
                if assumed == 's':
                    return random.choice(['k', 'v'])
                if assumed == 'l':
                    return random.choice(['k', 's'])
                return random.choice(['p', 'l'])

            if assumed == 'k':
                return "p"
            if assumed == 'p':
                return "s"
            return "k"
        return random.choice(self.__choices)

    def add_round(self, player, computer, result):
        '''Tallentaa pelatun kierroksen tiedot self._history
        taulukkoon: Pelaajan ja AI:n valinnat "k, p tai s",
        sekä kierroksen tuloksen.

        args:
            player: Pelaajan tekemä valinta.
            computer: AI:n valinta.
            result: 1: AI voitto, -1: pelaajan voitto, 0: tasapeli'''
        self._history[0].append(player)
        self._history[1].append(computer)
        self._history[2].append(result)
        self._rounds = len(self._history[0])
        self.update_probs()

    def get_history(self):
        '''Palauttaa pelihistorian ja todennäköisyydet.

        returns:
            self._history: Kaikkien kierrosten valinnat ja lopputulokset.
            self._probs: Todennäköisyysmatriisi'''
        return self._history, self.__probs
