import unittest
from ai.ai_classical import AiClassical

class TestAiClassical(unittest.TestCase):
    def setUp(self):
        self.rocks = ["k", "s", -1]
        self.scissors = ["s", "s", 0]
        self.ai = AiClassical()
        
    def test_all_items_will_be_chosen(self):
        #Testi epäonnistuu jos ei kaikkia vaihtoehtoja tule 100 yrityksellä.
        allitems = []
        i = 0
        while len(allitems) < 3 or i < 100:
            x = self.ai.choose()
            i += 1
            if x not in allitems:
                allitems.append(x)
        self.assertListEqual(sorted(allitems), ['k', 'p', 's'])
        
    def test_probability_to_player_to_play_rock_when_5_rocks_played(self):
        for i in range(5):
            self.ai.add_round(self.rocks[0], self.rocks[1], self.rocks[2])
        s = self.ai.choose()
        hist, probs = self.ai.get_history()
        self.assertEqual(probs[0], 0.75)
        
    def test_test_probability_player_to_play_scissors_when_10_rocks_played(self):
        for i in range(10):
            self.ai.add_round(self.rocks[0], self.rocks[1], self.rocks[2])
        s = self.ai.choose()
        hist, probs = self.ai.get_history()
        self.assertAlmostEqual(probs[2], 0.0769, 3)
        
    def test_test_probability_player_to_play_scissors_doesnt_go_worse(self):
        for i in range(15):
            self.ai.add_round(self.rocks[0], self.rocks[1], self.rocks[2])
        s = self.ai.choose()
        hist, probs = self.ai.get_history()
        self.assertAlmostEqual(probs[2], 0.0769, 3)
        
    def test_test_probability_player_to_play_scissors_gets_better(self):
        for i in range(12):
            self.ai.add_round(self.rocks[0], self.rocks[1], self.rocks[2])
        self.ai.add_round(self.scissors[0], self.scissors[1], self.scissors[2])
        s = self.ai.choose()
        hist, probs = self.ai.get_history()
        self.assertAlmostEqual(probs[2], 0.154, 3)
        
    def test_all_items_will_be_chosen_in_kpslv(self):
        self.ai = AiClassical(True)
        #Testi epäonnistuu jos ei kaikkia vaihtoehtoja tule 100 yrityksellä.
        allitems = []
        i = 0
        while len(allitems) < 3 or i < 100:
            x = self.ai.choose()
            i += 1
            if x not in allitems:
                allitems.append(x)
        self.assertListEqual(sorted(allitems), ['k', 'l', 'p', 's', 'v'])
