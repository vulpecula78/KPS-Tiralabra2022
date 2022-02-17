import random

class AiClassical:
    '''Ai, joka painottaa valinnassa klassista todennäköisyyslaskentaa. Lähtö arvona kaikille
    vaihtoehdoille on 1/3. Ai huomioi enintään pelaajan 10 viimeistä valintaa. Minkään valinnan
    todennäköisyys ei voi laskea nollaan. pienin todennäköisyys on 1/13 ja suurin 11/13.
    Jos todennäköisin oletus on, että pelaaja valitsee kiven, niin suurimmalla todennäköisyydellä
    arvotaan paperi.'''

    def __init__(self):
        self._siirto = ["k", "p", "s"]
        self._probs = []
        self._history = [[], [], []]
        self._last_rounds = 10

    def choose(self):
        '''Laskee pelattujen kierrosten perusteella todennäköisyydet
        pelaajan valinnoille ja tekee valinnan satunnaisesti
        painottaen todennäköisyyksiä.

        returns:
            k, p tai s'''

        #Huomioidaan vain 10 viimeisintä siirtoa.
        if len(self._history[0]) <= self._last_rounds:
            len_history = 3 + len(self._history[0])
            history = 0
        else:
            len_history = self._last_rounds + 3
            history = len(self._history[0]) - self._last_rounds

        #lasketaan todennäköisyydet joilla pelaaja pelaa kiven, paperin tai sakset
        k_prob = (1 + self._history[0][history:].count("k")) / len_history
        p_prob = (1 + self._history[0][history:].count("p")) / len_history
        s_prob = (1 + self._history[0][history:].count("s")) / len_history
        self._probs = [k_prob, p_prob, s_prob]

        #arvotaan tulos ja huomioidaan todennäköisyydet
        select = random.random()
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
        self._history[0].append(player)
        self._history[1].append(computer)
        self._history[2].append(result)

    def get_history(self):
        '''Palauttaa pelihistorian ja todennäköisyydet.

        returns:
            self._history: Kaikkien kierrosten valinnat ja lopputulokset.
            self._probs: Todennäköisyydet laskettuna 10 viime kierrokselta.'''
        return self._history, self._probs
