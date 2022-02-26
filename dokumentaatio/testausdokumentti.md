# Testausraportti

### Testaus

 Sovellusta on testattu 2 eri koneella Linuxilla(OpenSuse tumbleweed), sekä windows 10 koneella. Sovellus toimii oikein kaikilla testialustoilla, mutta poetryn asentama termcolor kirjasto ei toiminut ja se piti asentaa itse. Termcolor kirjaston toiminta vaati pienen lisäyksen käyttöliittymä-luokkaan.

### Yksikkötestaus ja suorituskyky
 Sovelluksen Yksikkötestaus on suoritettu unittestillä ja se kattaa tällä hetkellä kaiken muun paitsi käyttöliittymän. 
 
 ![testausraportti](./kuvat/testiraportti_vk4.png)
 
 Testikattavuudesta puuttuu kohtia, jotka eivät ole valmiina tai niille ei ole mielekästä lähteä kirjoittamaan testejä. Esimerkkinä pääohjelmasta jää pari riviä testaamatta, sillä ne sulkevat sovelluksen. 
 
 ![testaamatta](./kuvat/testaamatta_1.png)
 
 Sovellukseen on lisätty testausta varten omavaihtoehto sovelluksen sulkemisen sijaan. Sovelluksen testit ajetaan automaattisesti aina, kun githubiin tehdään muutoksia ja testiraportit ovat nähtävillä codecovissa.

#### suorituskyky

Sovelluksen suorituskykyä mitataan siten, miten se pärjää pelissä ihmistä vastaan. Kuitenkin Trie tietorakenteen suorituskyky on mitattu yksinkertaisella python-skriptillä. Sovellus tallentaa Triehen Aleksis Kiven Seitsemän veljestä kirjan, joka on ladattu osoitteesta https://www.gutenberg.org/ebooks/11940. Se mittaa kuinka kauan menee tallentaa joka sana, sekä prosessin muistinvarauksen muutoksen trie-rakenteeseen tallentamisen jälkeen. Testin tulos omalla koneella (ryzen 3700x, 32gb ram, openSuse linux, kernel 5.16.10) oli seuraavanlainen:

![testaamatta](./kuvat/trie_test.png)

Trie tyyppinen rakenne toimii siis melko nopeasti, mutta muistin varauksen muutos vain n. 680kt kokoisen kirjan kanssa on huomattavan suuri.
 
### Koodin laatu

Koodin laatua tarkastetaan ja ylläpidetään pylintin avulla. Viimeisin pylint tarkastus antoi arvosanan 9.84/10. 

### Pelin testaus

 Sovelluksella on vasta hieman testattu siten, että tuloksia on otettu talteen. Testauksen toteutuksen määrittely ei ole vielä valmis. Peliä on testattu vain KPS moodissa.
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
    - pelaaja:   34,33%
    - Tietokone: 33,38%
    - tasapeli:  32,29%
    
 Vaihtelevan pituisia Markovin-ketjuja käyttävä AI:n suoritusta mitattu 150, 175 ja 200 erän sarjoilla. Peliä ei ole tilastoitu Lisko ja Spock vaihtoehdoilla. Joitain testejä on tehty ja todettu, että pelisarjojen pitää olla huomattavasti pidempiä, kuin KPS moodissa, jotta AI alkaa suoriutumaan paremmin. Kaavioissa pystyakselilla voitot prosentteina ja vaaka-akselilla pelatut erät:

![testaamatta](./kuvat/voitto_suhteet_gornai.png)
    

 Näitä on ehkä syytä testata vielä pidemmillä peleillä. AI:n suoritumisessa on jonkin verran eroja kun focusta, eli kuinka monen kierroksen ajalta menestystä seurataan, ja mallien määrää muutetaan:

![testaamatta](./kuvat/voittosuhteet_eri_mallit.png)

Testejä on suoritettu eri malleilla ja fokuksilla. Vaikuttaisi siltä, että parhaiten AI suoriutuu kun focus on 4 - 5 ja malleja käytössä 4 - 6. 
