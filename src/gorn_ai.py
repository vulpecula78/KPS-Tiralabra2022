import random
from gorn_trie import TrieTree

class GornAi:
    '''GornAi käyttää eripituisia Markovin ketjuja ennakoidakseen pelaajan siirrot.
    Se seuraa eri pituisten ketjujen menestystä ja vaihtaa sitä sen mukaan, mikä
    parhaiten menestyy.'''
    def __init__(self):
        self._selection = {'k':5, 'p':3, 's':1}
        self.trie = TrieTree()
        self._history = [[], [], []]
        self._rounds = 1
        self.focus = -5  #AI mallin huomioimat aikaisemmat siirrot siirrot.
        #Käytössä olevat AI mallit.
        self._models = [('m1', -2), ('m2', -3), ('m3', -4), ('m4', -5), ('m', -6)]
        #Mahdolliset eri AI mallien tekemät siirrot.
        self._ai_alt_history = [[] for i in range(len(self._models))]
        self._model_in_use = 0  #Aluksi käytössä malli 0 ('m1', -2)
        self.create(self.trie)

    def create(self, tree):
        '''Alustetaan trie-puuhun 3 ensimmäistä tasoa'''
        for item in 'kps':
            for item2 in 'kps':
                for item3 in 'kps':
                    tree.insert(item + item2 + item3)

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
        '''hakee todennäköisyydet pelatun merkkijonon perusteella'''
        hist_len = model[1] + 1
        played = ''
        for item in range(hist_len, 0): #rakennetaan merkkijono
            played = played + self._history[0][item]
        #print("pelattu sarja :", played)
        prob = self.trie.get_values(played)
        return prob

    def choose(self):
        if self._rounds > 1:    #ensimmäinen kierros arvotaan
            #5 kierroksen jälkeen aletaan tilastoimaan siirtoja kaikille 5 ai mallille.
            if self._rounds > 5:
                models = len(self._models)
            else:
                models = 1
            for x in range(models): #Käydään läpi käytössä olevat mallit
                probabilities = self.get_probabilities(self._models[x])
                s = 0
                assume = None
                #print("MALLI:", x)
                #print('oletukset ovat:', probabilities)
                for i in probabilities:
                    if i[1] > s:
                        s = i[1]
                        assume = i[0]
                if assume is None: # jos ei todennäköisyyksiä vielä ole, niin arvotaan.
                    choice = self.rselect()
                elif max(probabilities) == min(probabilities) and len(probabilities) > 1:
                    choice = random.choice(probabilities)
                    choice = choice[1]
                else:
                    choice = self.select(assume)
                self._ai_alt_history[x].append(choice)
            print("MODEL IN USE: ", self._model_in_use)
            if self._rounds > 10 and self._rounds % 1 == 0:
                self.check_model() # Tarkastetaan eri mallien suorituminen 10 erän jälkeen.
            return self._ai_alt_history[self._model_in_use][-1]
        choice = self.rselect()
        return choice

    def select(self, assumed):
        if assumed == 'k':
            return "p"
        if assumed == 'p':
            return "s"
        return "k"

    def rselect(self):
        return random.choice(['k', 'p', 's'])

    def check_model(self):
        ''' Tarkastaa eri mallien muokaiset suoriutumiset
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
                if winner in (-2, 4):
                    points -= 1
                elif winner in (-4, 2):
                    points += 1
            mod_points.append(points)
            print("Mallin ", model, "pisteet: ", points)
        best = max(mod_points)
        self._model_in_use = mod_points.index(best)

    def add_round(self, player, computer, result):
        '''lisää pelatun kierroksen tiedot muistiin'''
        self._history[0].append(player)
        self._history[1].append(computer)
        self._history[2].append(result)
        self._rounds = len(self._history[1])
        self.update_moves()

    def get_history(self):
        #self.trie.print_tree()
        return self._history, [1/3, 1/3, 1/3]
