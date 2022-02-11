import unittest
from gorn_trie import TrieTree

class TestTrieTree(unittest.TestCase):
    def setUp(self):
        self.trie = TrieTree()
        self.trie.insert('karhu')
        self.trie.insert('karjala')
    
    def test_words_are_inserted_correctly_and_finds_correct_nodes_after_r(self):
        nodes = self.trie.get_values('kar')
        self.assertEqual(nodes, [('h', 0), ('j', 0)])
    
    def test_get_value_for_non_excistent_index_adds_it(self):
         nodes = self.trie.get_values('karpalo')
         self.assertEqual(nodes, [])
         nodes = self.trie.get_values('karpal')
         self.assertEqual(nodes, [('o', 0)])
         
    def test_update_value_of_string(self):
        self.trie.add_played_item('karh')
        nodes = self.trie.get_values('kar')
        self.assertEqual(nodes, [('h', 1), ('j', 0)])
        
    def test_temporary_not_a_real_test(self):
        self.trie.print_tree()
        
         
        
