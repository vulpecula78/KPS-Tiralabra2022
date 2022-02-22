import unittest
from gorn import Gorn

class StubUI:
    def __init__(self, commands, moves):
        self.menu_commands = commands
        self.moves = moves
        
    def start_menu(self):
        return self.menu_commands.pop(0), False

    def game_menu(self, round_, won, ai_won, ties):
        return self.moves.pop(0)
        
    def move(self, player, computer, result):
        pass
    
    def print_stats(self, data, probabilities):
        return data[0]


class TestGorn(unittest.TestCase):
    def test_game_against_random_ai(self):
        ui = StubUI(['1', '6', '0x0x'], ['k', 'p', 's', 'x'])
        gorn = Gorn(ui)
        
        stats = gorn.main()
        self.assertEqual(stats[0], 3)
        
    def test_game_against_classical_ai(self):
        ui = StubUI(['2', '6', '0x0x'], ['k', 'p', 's', 'p', 'p', 'x'])
        gorn = Gorn(ui)
        
        stats = gorn.main()
        self.assertEqual(stats[0], 5) #pelatut kierrokset

    def test_game_against_markov1_ai(self):
        ui = StubUI(['3', '6', '0x0x'], ['s', 's', 's', 's', 's', 's', 's', 'x'])
        gorn = Gorn(ui)
        
        stats = gorn.main()
        self.assertEqual(stats[0], 7) #pelatut kierrokset
        self.assertGreater(stats[2], 4)
        
    def test_statistics_when_no_games_started(self):
        ui = StubUI(['6', '0x0x'], [])
        gorn = Gorn(ui)
        
        stats = gorn.main()
        self.assertEqual(stats[1], 0)
        
    def test_statistics_when_game_started_but_0_rounds_played(self):
        ui = StubUI(['1', '6', '0x0x'], ['x'])
        gorn = Gorn(ui)
        
        stats = gorn.main()
        self.assertEqual(stats[1], 0)
        
