import unittest
from gorn_stats import GornStatistics

class Testgornstats(unittest.TestCase):
    def setUp(self):
        self.stats = GornStatistics()
        player = ['k' for i in range(26)]
        ai = ["p" for i in range(26)]
        points = [1 for i in range(26)]
        self.history = [player, ai, points]
        
    def test_points_by_rounds(self):
        result = self.stats.stats_by_nrounds(self.history)
        self.assertEqual(result, [(0.0, 100.0, 0.0)])
