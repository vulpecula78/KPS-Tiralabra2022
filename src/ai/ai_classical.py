import random

class AiClassical:
    '''Ai, joka painottaa valinnassa klassista todennäköisyyslaskentaa. Lähtö arvona kaikille
    vaihtoehdoille on 1/3 tai 1/5. Ai huomioi enintään pelaajan 10 viimeistä valintaa. Minkään
    valinnan todennäköisyys ei voi laskea nollaan. pienin todennäköisyys on 1/13(1/15) ja suurin
    11/13(13/15). Jos todennäköisin oletus on, että pelaaja valitsee kiven, niin suurimmalla
    todennäköisyydellä arvotaan paperi.'''

    def __init__(self, mode = False):
        if mode:
            self.__choices = ["p", "s", "v", "k", "l"]
            self.__rconst = 5
        else:
            self.__choices = ["k", "p", "s"]
            self.__rconst = 3
        self.__mode = mode
        self.__probs = []
        self.__history = [[], [], []]
        self.__last_rounds = 10

    def choose(self):
        '''Laskee pelattujen kierrosten perusteella todennäköisyydet
        pelaajan valinnoille ja tekee valinnan satunnaisesti
        painottaen todennäköisyyksiä.

        returns:
            k, p, s, l tai v
        '''

        #Huomioidaan vain 10 viimeisintä siirtoa.
        if len(self.__history[0]) <= self.__last_rounds:
            len_history =  self.__rconst + len(self.__history[0])
            history = 0
        else:
            len_history = self.__last_rounds + self.__rconst
            history = len(self.__history[0]) - self.__last_rounds

        #lasketaan todennäköisyydet joilla pelaaja pelaa kiven, paperin tai sakset
        k_prob = (1 + self.__history[0][history:].count("k")) / len_history
        p_prob = (1 + self.__history[0][history:].count("p")) / len_history
        s_prob = (1 + self.__history[0][history:].count("s")) / len_history
        if self.__mode:
            l_prob = (1 + self.__history[0][history:].count("l")) / len_history
            v_prob = (1 + self.__history[0][history:].count("v")) / len_history
            self.__probs = [k_prob, p_prob, s_prob, l_prob, v_prob]
        else:
            self.__probs = [k_prob, p_prob, s_prob]

        #arvotaan tulos ja huomioidaan todennäköisyydet
        select = random.random()
        if self.__mode:
            probability = 0
            for i in range(5):
                probability += self.__probs[i]
                if select <= probability:
                    return self.__choices[i]
        else:
            if select <= k_prob:
                return "p"
            if select <= p_prob + k_prob:
                return "s"
            return "k"

    def add_round(self, player, computer, result):
        '''Tallentaa pelatun kierroksen tiedot self._history
        taulukkoon: Pelaajan ja AI:n valinnat "k, p tai s",
        sekä kierroksen tuloksen.

        args:
            player: Pelaajan tekemä valinta.
            computer: AI:n valinta.
            result: 1: AI voitto, -1: pelaajan voitto, 0: tasapeli'''
        self.__history[0].append(player)
        self.__history[1].append(computer)
        self.__history[2].append(result)

    def get_history(self):
        '''Palauttaa pelihistorian ja todennäköisyydet.

        returns:
            self._history: Kaikkien kierrosten valinnat ja lopputulokset.
            self._probs: Todennäköisyydet laskettuna 10 viime kierrokselta.'''
        return self.__history, self.__probs
