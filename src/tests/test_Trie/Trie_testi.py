import sys
import psutil
import timeit

sys.path.insert(0,'../..')

from gorn_trie import TrieTree

trie = TrieTree()

file = open('11940-8.txt', 'r')
read_data = file.read()
per_word = read_data.split()

print('Sanoja yhteensä:', len(per_word))

#Tallennustesti
mem1 = psutil.Process().memory_info().rss
starttime = timeit.default_timer()

for sana in per_word:
    trie.insert(sana)
    
print("Sanojen tallentamiseen meni :", timeit.default_timer() - starttime)

mem2 = psutil.Process().memory_info().rss
print("Prosessin muistin varaus kasvoi: ", (mem2 - mem1) / (1024*1024))

#Haku testi
print("Haetaan sana: Pikipallero")

starttime = timeit.default_timer()
a = trie.get_values('Pikipallero')
print("Sanan hakemiseen meni :", (timeit.default_timer() - starttime) * (10*5))
print(a)



