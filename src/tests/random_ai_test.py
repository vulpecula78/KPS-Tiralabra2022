import unittest
from ai.ai_random import AiRandom

class TestAiRandom(unittest.TestCase):
    def setUp(self):
        self.rocks = ["k", "s", -1]
        self.scissors = ["s", "s", 0]
        self.ai = AiRandom()
        
    def test_all_items_will_be_chosen_in_kps(self):
        #Testi epäonnistuu jos ei kaikkia vaihtoehtoja tule 100 yrityksellä.
        allitems = []
        i = 0
        while len(allitems) < 3 or i < 100: 
            x = self.ai.choose()
            i += 1
            if x not in allitems:
                allitems.append(x)
        self.assertListEqual(sorted(allitems), ['k', 'p', 's'])
        
    def test_get_history_and_stats_in_kps(self):
        self.ai.add_round(self.rocks[0], self.rocks[1], self.rocks[2])
        self.ai.add_round(self.scissors[0], self.scissors[1], self.scissors[2])
        hist, probs = self.ai.get_history()
        self.assertListEqual(hist[0], ['k', 's'])
        
    def test_all_items_will_be_chosen_in_kpslv(self):
        self.ai = AiRandom(True)
        #Testi epäonnistuu jos ei kaikkia vaihtoehtoja tule 100 yrityksellä.
        allitems = []
        i = 0
        while len(allitems) < 3 or i < 100: 
            x = self.ai.choose()
            i += 1
            if x not in allitems:
                allitems.append(x)
        self.assertListEqual(sorted(allitems), ['k', 'l', 'p', 's', 'v'])
        
    def test_get_history_and_stats_in_kpslv(self):
        self.ai = AiRandom(True)
        self.ai.add_round('v', self.rocks[1], self.rocks[2])
        self.ai.add_round(self.scissors[0], self.scissors[1], self.scissors[2])
        hist, probs = self.ai.get_history()
        self.assertListEqual(hist[0], ['v', 's'])
