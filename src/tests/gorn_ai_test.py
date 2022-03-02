import unittest
from ai.gorn_ai import GornAi

class TestGornAi(unittest.TestCase):
    def setUp(self):
        self.rocks = ["k", "s", -1]
        self.scissors = ["s", "s", 0]
        self.papers = ["p", "r", 0]
        self.ai = GornAi(False, 3, -3)
        
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
        
    def test_update_moves_and_get_correct_probabilities(self):
        self.ai.add_round('s', 'p', 1)
        self.ai.add_round('s', 'p', 1)
        self.ai.add_round('s', 'p', 1)
        self.ai.add_round('k', 'p', 1)
        self.ai.add_round('s', 'p', 1)        
        prob = self.ai.get_probabilities(('m1', -2))
        self.assertEqual(prob, [('k', 1), ('p', 0), ('s', 2)])
        
    def test_after_played_rounds_ai_should_choose_rock(self):
        self.ai.add_round('s', 'p', 1)
        self.ai.add_round('s', 'p', 1)
        self.ai.add_round('s', 'p', 1)
        self.ai.add_round('k', 'p', 1)
        self.ai.add_round('s', 'p', 1)
        item = self.ai.choose()
        self.assertEqual(item, 'k')
        
    def test_after_played_rounds_ai_should_choose_scissors(self):
        self.ai.add_round('p', 'p', 1)
        self.ai.add_round('p', 'p', 1)
        self.ai.add_round('p', 'p', 1)
        item = self.ai.choose()
        self.assertEqual(item, 's')
        
    def test_after_played_rounds_ai_should_choose_rock_with_another_model(self):
        for i in range(6):
            self.ai.add_round('s', 'p', 1)
        self.ai._model_in_use = 2
        
        item = self.ai.choose()
        self.assertEqual(item, 'k')
        
    def test_ai_changes_model(self):
        player = 'sskspskspskksskkps'
        ai =     'pspspppssspkppkppk'#'pspspppkpkpkp'
        points = [-1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, -1, -1, 0, 1, 1]
        for x in range(12):
            i = player[x]
            j = ai[x]
            p = points[x]
            self.ai.add_round(i, j, p)
            choice = self.ai.choose()
        self.ai.check_model()
        model = self.ai._model_in_use
        self.assertEqual(model,  1)
        
    def test_with_lizard_and_spock(self):
        self.ai = GornAi(True, 4, -4)
        self.ai.add_round('s', 'p', 1)
        self.ai.add_round('s', 'p', 1)
        self.ai.add_round('l', 's', -1)
        self.ai.add_round('v', 'v', 0)
        choice = self.ai.choose()
        self.assertIn(choice, ['v', 'k'])
        
    def test_models_and_focus_set_correctly(self):
        self.ai = GornAi(True, 4, -4)
        self.ai.add_round('s', 'p', 1)
        self.ai.add_round('l', 's', -1)
        self.ai.add_round('s', 'p', 1)
        choice = self.ai.choose()
        hist, model = self.ai.get_history()
        self.assertEqual(model, ["models:", 4, "focus:", -4])
        
