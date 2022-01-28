import unittest
from ai_random import AiRandom

class TestAiRandom(unittest.TestCase):
    def setUp(self):
        self.rocks = ["k", "s", -1]
        self.scissors = ["s", "s", 0]
        self.ai = AiRandom()
        
    def test_all_items_will_be_chosen(self):
        #Testi epäonnistuu jos ei kaikkia vaihtoehtoja tule 100 yrityksellä.
        allitems = []
        i = 0
        while len(allitems) < 3 or i < 100: 
            x = self.ai.choice()
            i += 1
            if x not in allitems:
                allitems.append(x)
        self.assertListEqual(sorted(allitems), ['k', 'p', 's'])
        
    def test_get_history_and_stats(self):
        self.ai.add_round(self.rocks[0], self.rocks[1], self.rocks[2])
        self.ai.add_round(self.scissors[0], self.scissors[1], self.scissors[2])
        hist, probs = self.ai.get_history()
        self.assertListEqual(hist[0], ['k', 's'])
