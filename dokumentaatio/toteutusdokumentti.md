
## Toteutusdokumentti

-----

Sovellus on tekstipohjainen kivi, paperi ja sakset peli, jossa myös mahdollista pelata muunnosta kivi, paperi, sakset, lisko ja Spock. Päätarkoituksena sovelluksessa on kuitenkin ollut toteuttaa Markovin ketjuihin pohjautuva koneoppimista käyttävä tekoäly. Jotta tekoälyn suoriutumista voitaisiin vertailla, niin toteutettiin sovellukseen myös täysin satunnaisesti ja klassisella todennäköisyydellä toimivat tekoälyt.

#### Sovelluksen yleisrakenne

Sovellus koostuu pääohjelmasta, tekstipohjaisesta käyttöliittymästä ja erilaisista AI-luokista ja Trie-tietorakenteesta. Sovelluksen kansiorakenne on seuraavanlainen:

    Gorn-KPS
    ├── dokumentaatio
    │   └── kuvat
    └── src
        ├── ai
        ├── tests
        │   └── test_Trie
        └── ui

Dokumentaatio pitää sisällään tämän ja muut dokumentit. Dokumentteihin liittyvät kuvat ovat omassa kansiossaan. Itse sovellus ja siihen liittyvät testit ovat src kansiossa. Käyttöliittymä löytyy ui kansiosta, tekoälyluokat ai-kansiosta. Tests kansiossa sijaitsee yksikkötestit ja Test_Trie kansio, joka pitää sisällään Trie-tietorakenteen testin.

#### Pääohjelma ja muut src kansion luokat

Index.py käynnistää sovelluksen ja määrittelee käyttöliittymän antamalla sen parametrinä gorn.py:lle. Gorn.py on pääohjelma, joka pitää sisällään pelilogiikan ja yhdistää muut luokat kokonaisuudeksi. Siinä on pääsilmukka joka kutsuu käyttöliittymää, joka palauttaa luvut 0-4 tai 6 ja pelimoodin. Tämän perusteella, valinnoilla 1-4, se valitsee tekoälymallin ja aloittaa pelin tai valinnalla 6 se kutsuu stats.py luomaan viimeisen pelin tilastot. Valinnalla 0 poistutaan pelistä. Stats.py käsittelee gorn.py:ltä saamansa pelihistorian ja palauttaa pyydetyt tilastot, jotka ohjataan käyttöliittymälle.

##### Trie

Src kansiosta löytyy myös gorn_trie.py tiedosto, joka on sovelluksen tarpeita varten rakennettu ja yksinkertaistettu Trie-tietorakenne. Eripituisia Markovin-ketjuja käyttävä AI-luokka tallentaa pelaajan tekemät siirtosarjat Trie puuhun, josta se saa helposti selvitetty eripituisten ketjujen todennäköisyydet.

#### Käyttöliittymä

Käyttöliittymänä on yksinkertainen tekstipohjainen malli, joka pitää sisällään päävalikon, pelivalikon ja tilastojen tulostamisen. käyttöliittymä vastaan ottaa pelaajan antamat syötteet ja antaa ne pääohjelmalle, sekä tulostaa ruudulle pelitapahtumat pääohjelmalta saadun tiedon mukaan.

#### AI luokat

AI luokkia on 4: Täysin satunnaisesti toimiva, klassista todennäköisyyttä käyttävä luokka, 1. asteen Markovia käyttävä luokka, sekä eripituisia Markovin-ketjuja käyttävä Gorn_ai luokka, joka vaihtelee käytettävän ketjun pituutta sen mukaan minkälainen ketju olisi tuonut parhaan tuloksen aiemmilla kierroksilla. Kaikilla luokilla on samannimiset funktiot: choose, add_round ja get_history joita kutsutaan pääohjelmasta. 

Ai_markov1.py käyttää tietorakenteena matriisia, 3x3 tai 5x5, mihin se tallentaa pelaajan tekemät siirrot. Tämän käyttäminen on suoraviivaista ja sinne tallentaminen ja lukeminen ovat aikavaativuudeltaan O(n). Taulukon kaikkiin soluihin alustetaan 0, joten tilavaativuus pysyy muuttumattomana. Gorn_ai käyttää pelaajan siirtojen tallentamiseen Trie rakennetta, jonka kokoa kasvatetaan tehtyjen siirtojen mukaan. Hakeminen ja lisääminen Triehen ovat aikavaativuudeltaan luokkaa O(n).

#### Testit

Yksikkötestit sijaitsevat kansiossa src/tests. Käyttöliittymälle ei ole testejä. Kansio test_Trie sisältää pienen suorituskyky testin gorn_trie luokalle, joka tallentaa siihen kansiossa olevan Seitsemän veljestä kirjan sanat erikseen, mitaten siihen kuluneen ajan ja muistin varauksen muutoksen. Se myös testaa hakunopeutta. Testitulokset löytyvät testausraportista.

#### Parannettavaa

Sovelluksessa olisi vielä hyvin paljon parannettavaa. Algoritmien toimintaa voisi varmasti vielä parantaa, sekä olisi hyvä tehdä mahdollisuus gorn_ai:n focus ja models asetusten valitseminen käyttöliittymästä. Käyttöliittymän käyttämät sanakirjat voisi siirtää omaksi luokaksi, ja tehdä myös graafinen käyttöliittymä esim. tkinterillä. Mahdollisuus tallentaa peli, pelihistoria tai tilastot helpottaisivat tulosten analysointia.

### Liitteet:

[Trie](https://www.geeksforgeeks.org/trie-insert-and-search/)

[Wikipedia: Markov chain](https://en.wikipedia.org/wiki/Markov_chain)

[Wikipedia: Trie](https://en.wikipedia.org/wiki/Trie)





