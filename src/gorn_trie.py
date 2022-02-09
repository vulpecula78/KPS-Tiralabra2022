class TrieNode:
    def __init__(self, item):
        self.item = item
        self.value = 0  
        self.leafs = {}
        self.last = False

class TrieTree:
    def __init__(self):
        self.root = TrieNode('')

    def insert(self, items):
        '''Asettaa trie-puuhun merkkijonon'''
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
        niin se lisätään'''
        node = self.root
        for item in items:
            if item in node.leafs:
                node = node.leafs[item]
            else:
                self.insert(items)
                node = node.leafs[item]
        return node

    def add_played_item(self, items):
        '''lisää halutun merkkijonon viimeisen merkin
        arvoa yhdellä'''
        node = self.search(items)
        a = node.value
        a += 1
        node.value = a

    def get_values(self, items):
        '''Palauttaa halutusta lehdestä nähtevien
        lehtien arvot, eli kuinka monta kertaa niitä
        on pelattu.'''
        values = []
        node = self.search(items)
        for item in node.leafs:
            leaf_node = node.leafs[item]
            #print(item, ":", leaf_node.value)
            values.append((item, leaf_node.value))
        return values

    '''Nämä ovat puun tulostamista varten olevia väliaikaisia funktioita'''
    def print_tree(self):
        taso = 0
        node = self.root
        print("puun taso: ", taso)
        print("root:", node.value)
        print("-----------------------")
        for item in node.leafs:
            leaf_node = node.leafs[item]
            self.next_leaf(leaf_node, taso)

    def next_leaf(self, node, taso):
        taso = taso + 1
        print("puun taso: ", taso)
        print("noodi:", node.item, "Noodin arvo: ", node.value)
        print("-----------------------")
        for item in node.leafs:
            leaf_node = node.leafs[item]
            self.next_leaf(leaf_node, taso)
            
'''
tr = TrieTree()
tr.insert("kps")
tr.insert("kpky")
tr.insert("kpke")
tr.insert("kpp")
tr.insert("kkk")
tr.insert("kks")
tr.insert("kkp")
tr.add_played_item('spsk')
tr.add_played_item('spss')
tr.add_played_item('kpk')
print(tr.get_values('kp'))
tr.add_played_item('p')
print(tr.get_values('p'))
tr.add_played_item('pk')
print(tr.get_values('p'))
print(tr.get_values('sps'))
'''
