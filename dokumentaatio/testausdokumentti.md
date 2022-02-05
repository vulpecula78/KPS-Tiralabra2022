# Testausraportti

### Testaus

 Sovellusta on testattu 2 eri koneella Linuxilla(OpenSuse tumbleweed), sekä windows 10 koneella. Sovellus toimii oikein kaikilla testialustoilla, mutta poetryn asentama termcolor kirjasto ei toiminut ja se piti asentaa itse. Termcolor kirjaston toiminta vaati pienen lisäyksen käyttöliittymä luokkaan.

### Yksikkötestaus
 Sovelluksen Yksikkötestaus on suoritettu unittestillä ja se kattaa tällä hetkellä kaiken muun paitsi käyttöliittymän. 
 
 ![testausraportti](./kuvat/testiraportti.png)
 
 Pääohjelmasta jää pari riviä testaamatta, sillä ne sulkevat sovelluksen. 
 ![testaamatta](./kuvat/testaamatta_1.png)
 
 Sovellukseen on lisätty testausta varten omavaihtoehto sovelluksen sulkemisen sijaan. Sovelluksen testit ajetaan automaattisesti aina, kun githubiin tehdään muutoksia ja testiraportit ovat nähtävillä codecovissa.
 
### Koodin laatu

Koodin laatu tarkastetaan ja ylläpidetään pylintin avulla.

### Pelin testaus

 Sovelluksella on vasta hieman testattu siten, että tuloksia on otettu talteen. 
 Pelitulokset ovat jakautuneet seuraavasti:
 
* Satunnainen AI, kun pelejä pelattu 7 ja pelin keskimääräinen pituus 45 kierrosta:
    - pelaaja:   31,43%
    - Tietokone: 32,24%
    - tasapeli:  36,33% 
* Klassista todennäköisyyttä käyttävä AI, kun pelejä 7 ja keskimääräinen pituus 50 kierrosta:
    - pelaaja:   35,37%
    - Tietokone: 34,50%
    - tasapeli:  30,13%
* 1.asteen Markov, kun pelejä 3 ja keskimääräinen pituus 43 kierrosta:
    - pelaaja:   32,44%
    - Tietokone: 33,56%
    - tasapeli:  34,00%
