# Määrittelydokumentti
-----
### Tietorakenteet ja algoritmit harjoitustyö
### Opinto-ohjelma: Tietojenkäsittelytieteen kandidaatti
-----
## Projektin aihe
Projektin aiheena on kivi-sakset-paperi-peli (Gorn-KPS), jossa pelaaja pelaa tietokonetta vastaan. Peliin voidaan mahdollisesti lisätä myös lisko ja Spock vaihtoehdot, joka tekee pelistä hieman haastavamman. Tarkoituksena luoda koneoppimista käyttävä algoritmi, joka pystyy suoriutumaan pelissä ihmistä vastaan hyvin voittaen suurimman osan peleistä. Peliin toteutetaan myös täysin satunnaisesti toimiva algoritmi, jotta saadaan vertailtua oppivan algoritmin tehokkuutta täysin satunnaisesti toimivaan peliin.
 
Ohjelmointikielenä projektissa käytetään Pythonia. Projekti ja sen dokumentaatio toteutetaan suomeksi. Pelin käyttöliittymä toteutetaan tekstipohjaisella käyttöliittymällä. Pelissä valitaan pelimoodi: satunnaisesti pelaavaa algoritmiä tai oppivaa algoritmiä vastaan. Syötteinä pelille annetaan kivi, sakset tai paperi. Algoritmi tallentaa syötteet muistiin ja laskee tehtyjen siirtojen perusteella todennäköisyydet seuraavista mahdollisista siirroista.
  
## Algoritmit ja tietorakenteet
Projektin algoritmi toteutetaan käyttämällä Markovin ketjuja ja mahdollisesti myös jotain muuta algoritmiä. Algoritmin oppimisen toteutuksessa käytetään eri asteisia Markovin ketjuja. 1. asteen huomioi vain yhden aikaisemman siirron, 2. asteen kaksi aikaisempaa siirtoa jne..  Näitä voidaan käyttää yksittäin, tai algoritmin kanssa, joka vaihtelee astetta sen mukaan mikä parhaiten menestyy. Tietorakenteina pythonin listoista muodostettuja matriiseja, joiden aikavaativuus on enintään O(mn) ja tilavaativuus on O(mn), sekä Trie puu.
 
-----
## Lähteet
        
* [Introduction to Markov chains](https://towardsdatascience.com/brief-introduction-to-markov-chains-2c8cab9c98ab)
* [Essays on Data Science: Markov Models From The Bottom Up, with Python](https://ericmjl.github.io/essays-on-data-science/machine-learning/markov-models/)
* [Multi‑Ai competing and winning against humans in iterated Rock‑paper‑Scissors game](https://arxiv.org/pdf/2003.06769.pdf)
* [Towards an AI for Rock, Paper, Scissors](https://towardsai.net/p/artificial-intelligence/towards-an-ai-for-rock-paper-scissors-3fb05780271f)
* [Trie](https://www.geeksforgeeks.org/trie-insert-and-search/)
* [Wikipedia: Markov chain](https://en.wikipedia.org/wiki/Markov_chain)
* [Wikipedia: Rock paper scissors](https://en.wikipedia.org/wiki/Rock_paper_scissors)
* [Wikipedia: Trie](https://en.wikipedia.org/wiki/Trie)



    
