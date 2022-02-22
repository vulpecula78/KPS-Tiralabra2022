import random
from gorn_trie import TrieTree

class GornAi:
    '''GornAi käyttää eripituisia Markovin ketjuja ennakoidakseen pelaajan siirrot.
    Se seuraa eri pituisten ketjujen menestystä ja vaihtaa sitä sen mukaan, mikä
    parhaiten menestyy.'''
    def __init__(self, mode = False, models = 6, focus = -4):
        if mode:
            self._selection = {"k":0, "s":2, "p":1, "l":4, "v":3}
            self._choices = ['k', 'p', 's', 'l', 'v']
        else:
            self._selection = {'k':0, 'p':1, 's':2}
            self._choices = ['k', 'p', 's']
        self.__gorn = mode
        self.trie = TrieTree()
        self._history = [[], [], []]
        self._rounds = 1
        self.focus = focus  #AI mallin huomioimat aikaisemmat siirrot siirrot.
        #Käytössä olevat AI mallit.
        self._models = self.create_models(models)
        #Mahdolliset eri AI mallien tekemät siirrot.
        self._ai_alt_history = [[] for i in range(len(self._models))]
        self._model_in_use = 0  #Aluksi käytössä malli 0
        self.create(self.trie)

    def create(self, tree):
        '''Alustetaan trie-puuhun 3 ensimmäistä tasoa'''
        for item in 'kps':
            for item2 in 'kps':
                for item3 in 'kps':
                    tree.insert(item + item2 + item3)

    def create_models(self, models):
        '''Luo listan käytössä olevista AI-malleista, eli
        kuinka monta asteisia Markovin ketjuja käytetään.

        args:
            models: int, käytettävien mallien määrä

        returns:
            model_list: list, lista malleista 2-tupleina
                        sisältäen mallin nimen ja kuinka
                        pitkiä sarjoja tutkitaan'''
        model_list =[]
        for model in range(models):
            mod_name = "Markov" + str(model + 1)
            hist = (model * -1) - 1
            model_list.append((mod_name, hist))
        return model_list

    def update_moves(self):
        '''Päivitetään tehdyt siirrot käytössä olevien eri mallien mukaan'''
        for model in self._models:
            if self._rounds >= (model[1] * -1):
                #print("siirto mallin ", model[0], " mukaan lisätty")
                played = ''
                for i in range(model[1], 0):    #Mallin pituuden mukaan määritelty sarja
                    played = played + self._history[0][i]  #esim 'kkps'
                #print("siirto: ", played)
                self.trie.add_played_item(played)

    def get_probabilities(self, model):
        '''hakee todennäköisyydet pelatun merkkijonon perusteella.

        args:
            model: Käytettävä AI malli

        returns:
            prob: lista tupleja, joissa pelattu merkki ja määrä.
        '''
        hist_len = model[1] + 1
        played = ''
        for item in range(hist_len, 0): #rakennetaan merkkijono
            played = played + self._history[0][item]
        prob = self.trie.get_values(played)
        return prob

    def choose(self):
        '''Suorittaa valinnan sen mukaan, minkä
        siirron olettaa pelaajan tekevän.

        returns:
            str: k, p tai s'''

        if self._rounds > 1:    #ensimmäinen kierros arvotaan
            # Määritetään käytössä olevien mallien määrä kierrosten mukaan.
            if self._rounds > len(self._models):
                models = len(self._models)
            else:
                models = self._rounds - 1
            for model in range(models): #Käydään läpi käytössä olevat mallit
                probabilities = self.get_probabilities(self._models[model])
                best_prob = 0
                assume = None
                for prob in probabilities:
                    print(prob[1])
                    if prob[1] > best_prob:
                        best_prob = prob[1]
                        assume = prob[0]
                if assume is None: # jos ei todennäköisyyksiä vielä ole, niin arvotaan.
                    choice = self.rselect()
                elif max(probabilities) == min(probabilities) and len(probabilities) > 1:
                    choice = random.choice(probabilities)
                    choice = choice[1]
                else:
                    choice = self.select(assume)
                self._ai_alt_history[model].append(choice)
            print("MODEL IN USE: ", self._models[self._model_in_use][0])
            if self._rounds > 10 and self._rounds % 1 == 0: #kuinka usein malli tarkastetaan
                self.check_model() # Tarkastetaan eri mallien suorituminen 10 erän jälkeen.
            return self._ai_alt_history[self._model_in_use][-1]
        choice = self.rselect()
        return choice

    def select(self, assumed):
        '''Suorittaa valinnan sen mukaan, minkä
        siirron olettaa pelaajan tekevän.

        returns:
            str: k, p, s, l tai v'''

        if self.__gorn:
            if assumed == 'k':
                return random.choice(['v', 'p'])
            if assumed == 'p':
                return random.choice(['s', 'l'])
            if assumed == 's':
                return random.choice(['v', 'k'])
            if assumed == 'l':
                return random.choice(['k', 's'])
            return random.choice(['l', 'p'])

        if assumed == 'k':
            choice = "p"
        elif assumed == 'p':
            choice = "s"
        else:
            choice = "k"
        return choice

    def rselect(self):
        '''Valitsee satunnaisesti k, p tai s'''
        return random.choice(self._choices)

    def check_model(self):
        ''' Tarkastaa eri mallien aiempien kierrosten suoriutumiset
        ja valitsee sen mukaan parhaiten menestyneen mallin.
        Malleja otetaan lisää käyttöön 20 ja 30 pelikierroksen
        jälkeen.'''
        mod_points = []
        if self._rounds < 20 and len(self._models) > 1:
            in_use = 2
        elif self._rounds < 30 and len(self._models) >= 3:
            in_use = 3
        else:
            in_use = len(self._models)

        for model in range(in_use):
            points = 0
            for hist in range(self.focus, 0):
                human = self._history[0][hist]
                ai_item = self._ai_alt_history[model][hist-1]
                winner = self._selection[human] - self._selection[ai_item]
                if winner in (-4, -2, 1, 3):
                    points -= 1
                elif winner != 0:
                    points += 1
            mod_points.append(points)
            print("Mallin ", self._models[model][0], "pisteet: ", points)
        best = max(mod_points)
        self._model_in_use = mod_points.index(best)

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
        self._rounds = len(self._history[1])
        self.update_moves()

    def get_history(self):
        '''Palauttaa pelihistorian ja todennäköisyydet.

        returns:
            self._history: Kaikkien kierrosten valinnat ja lopputulokset.
            self._probs: Todennäköisyydet laskettuna 10 viime kierrokselta.'''
        return self._history, [1/3, 1/3, 1/3] #self.trie
