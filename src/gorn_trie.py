class TrieNode:
    '''Trie tietorakenteen noodi, jolla arvona k, p, s,
    l tai v. Määrä kuinka monta kertaa valittu.

    args:
        item: Noodin nimi'''
    def __init__(self, item):
        self.item = item
        self.value = 0
        self.leafs = {}
        self.last = False

class TrieTree:
    def __init__(self):
        self.root = TrieNode('')

    def insert(self, items):
        '''Asettaa trie-puuhun merkkijonon.

        args:
            items: Asetettava merkkijono'''
        node = self.root
        for item in items:
            if item in node.leafs:
                node = node.leafs[item]
            else:
                new = TrieNode(item)
                node.leafs[item] = new
                node = new
            node.last = True

    def search(self, items):
        '''Hakee merkkijonon viimeisen merkin, ellei sitä ole,
        niin se lisätään

        args:
            items: haettava merkkijono

        returns:
            node: Haettavan merkkijonon viimeinen noodi.
        '''
        node = self.root
        for item in items:
            if item in node.leafs:
                node = node.leafs[item]
            else:
                #Ellei merkkijonoa löytynyt, niin se lisätään
                self.insert(items)
                node = node.leafs[item]
        return node

    def add_played_item(self, items):
        '''lisää halutun merkkijonon viimeisen merkin
        arvoa yhdellä.

        args:
            items: merkkijono, jonka viimeistä arvoa nostetaan yhdellä.
        '''
        node = self.search(items)
        value = node.value
        value += 1
        node.value = value

    def get_values(self, items):
        '''Palauttaa halutusta lehdestä nähtevien
        lehtien arvot, eli kuinka monta kertaa niitä
        on pelattu.

        args:
            items: merkkijono,  jonka viimeisen merkin tiedot haetaan

        returns:
            values: haetun merkkijonon viimeisen merkin lehtien nimet ja arvot.
        '''
        values = []
        node = self.search(items)
        for item in node.leafs:
            leaf_node = node.leafs[item]
            #print(item, ":", leaf_node.value)
            values.append((item, leaf_node.value))
        return values

    def print_tree(self):
        '''Nämä ovat puun tulostamista varten olevia väliaikaisia funktioita,
        joita käytetään tarkastamaan sovelluksen toimintaa.'''
        taso = 0
        node = self.root
        print("puun taso: ", taso)
        print("root:", node.value)
        print("-----------------------")
        for leaf in node.leafs:
            leaf_node = node.leafs[leaf]
            self.next_leaf(leaf_node, taso)

    def next_leaf(self, node, taso):
        taso = taso + 1
        print("puun taso: ", taso)
        print("noodi:", node.item, "Noodin arvo: ", node.value)
        print("-----------------------")
        for leaf in node.leafs:
            leaf_node = node.leafs[leaf]
            self.next_leaf(leaf_node, taso)
