import unittest
from ai.ai_markov1 import AiMarkov1

class TestAiClassical(unittest.TestCase):
    def setUp(self):
        self.rocks = ["k", "s", -1]
        self.scissors = ["s", "s", 0]
        self.papers = ["p", "r", 0]
        self.ai = AiMarkov1()
        
    def test_add_round_and_update_probabilities(self):
        self.ai.add_round(self.rocks[0], self.rocks[1], self.rocks[2])
        self.ai.add_round(self.scissors[0], self.scissors[1], self.scissors[2])
        hist, probs = self.ai.get_history()
        self.assertEqual(probs[0][2], 1)
        
    def test_ai_should_play_paper_after_2_rocks_by_player(self):
        self.ai.add_round(self.rocks[0], self.rocks[1], self.rocks[2])
        self.ai.add_round(self.rocks[0], self.rocks[1], self.rocks[2])
        ai_move = self.ai.choose()
        self.assertEqual(ai_move, "p")
    '''    
    def test_ai_should_play_rock_after_2_scissors_played_by_player(self):
        self.ai.add_round(self.scissors[0], self.scissors[1], self.scissors[2])
        self.ai.add_round(self.scissors[0], self.scissors[1], self.scissors[2])
        ai_move = self.ai.choose()
        self.assertEqual(ai_move, "k")
        
    def test_ai_should_play_scissors_after_2_papers_played_by_player(self):
        self.ai.add_round(self.papers[0], self.papers[1], self.papers[2])
        self.ai.add_round(self.papers[0], self.papers[1], self.papers[2])
        ai_move = self.ai.choose()
        self.assertEqual(ai_move, "s")
        
    def test_any_item_possible_if_all_probabilities_same(self):
        self.ai.add_round(self.rocks[0], self.rocks[1], self.rocks[2])          #taulukko näyttää:
        self.ai.add_round(self.rocks[0], self.rocks[1], self.rocks[2])          #   k   p   s    
        self.ai.add_round(self.papers[0], self.papers[1], self.papers[2])       # k 1   1   1
        self.ai.add_round(self.rocks[0], self.rocks[1], self.rocks[2])          # p 1   0   0
        self.ai.add_round(self.scissors[0], self.scissors[1], self.scissors[2]) # s 1   0   0
        self.ai.add_round(self.rocks[0], self.rocks[1], self.rocks[2])  
        #Seuraavan siirron oletusarvo on sama kaikille vaihtoehdoille.
        allitems = []
        i = 0
        while len(allitems) < 3 or i < 100:
            x = self.ai.choose()
            i += 1
            if x not in allitems:
                allitems.append(x)
        self.assertListEqual(sorted(allitems), ['k', 'p', 's'])
     '''   
    def test_in_first_round_all_items_will_be_possible(self):
        #Testi epäonnistuu jos ei kaikkia vaihtoehtoja tule 100 yrityksellä.
        allitems = []
        i = 0
        while len(allitems) < 3 or i < 100:
            x = self.ai.choose()
            i += 1
            if x not in allitems:
                allitems.append(x)
        self.assertListEqual(sorted(allitems), ['k', 'p', 's'])
        
