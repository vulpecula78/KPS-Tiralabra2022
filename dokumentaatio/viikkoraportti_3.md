# Viikkoraportti 3
-----

### Mitä on tehty

 - Ohjelmointia ja testausta (12h)
 - Opiskelua, tiedonhakua. (2h)
 - Github actions ja codecov virittely. (1h)
 - Raporttien kirjoitus (2h)
 
 Tällä viikolla ohjelmointityö on edennyt melko hyvin. On saatu toteutettua 1. versio Markovin ketjua käyttävästä luokasta, sekä pohdittua 2. asteen ketjun toteutusta. Sovellusta tuli myös testattua muilla koneilla ja Windows järjestelmässä, jolloin löytyi pieniä ongelmia. Nämä kuitenkin sain ratkaistua melko helposti. Testausraportin tekeminen on nyt aloitettu ja jonkin verran testipelejä on tilastoituna.
 
-----
### Ohjelmoinnin edistyminen
 
 Ohjelmointityö on edistynyt aika hyvin. Pääohjelman kirjoitin melkein kokonaan uusiksi, ja tein sille unittestit, jotka taisivat olla tämän viikon yksi haastavin osuus. Käyttöliittymään tuli pieniä korjauksia, sekä Windows yhteen sopivuuden vaatima korjaus. Lisäksi sain toteutettua 1. asteen Markovin ketjulla toimivan mallin ja suunniteltua jo seuraavan mallin toteutusta. Tähän tehtiin myös kattavat unittestit. Githubissa sain myös pylintin toimimaan oikein, ja se antaa koodin laaduksi 10/10. Lisäksi olen kokeillut miten helposti saisin laajennettua peliin lisko ja Spock vaihtoehdot.
 
-----
### Mitä olen oppinut

 Tällä viikolla en ole oppinut mitään tiettyä asiaa, mutta paljon pieniä juttua pääosin ohjelmointiin liittyen. Pääosin unittestien tekeminen on vaatinut paljon kertausta ja mieleenpaluttamista.

-----
### Mitä seuraavaksi

 Seuraava tavoite on saada tehtyä 2. asteen Markovin ketju. Samalla pitää saada päätettyä miten toteutan AI:n joka voi pelin edistymisen mukaan vaihdella eri asteita. Teenkö tästä yhden vai useamman luokan, tms. Mietittävänä on myös huomioidaanko vain pelaajan siirtoja vai pelaajan ja tietokoneen tekemiä siirtopareja. Myös käytettävien näppäinten muuttaminen on käynyt mielessä.

-----
### Mitä jäi epäselväksi, ollut vaikeaa tai tuottanut ongelmia?
 
 Termcolor kirjasto on tuottanut hieman harmia, mutta siitä en halunnut luopua. Huomasin, että vaikka poetry asentaa sen, niin se ei toimi. Ratkaisuna tähän on asentaa se itse uusiksi käyttäen pip. Tämä myös auttoi kun github workflow:n lisäsi erikseen asennuksen termcolorille.  Windowsin powershellissä termcolor tulosti vain koodisarjat väreille tms. Tähän löytyi ratkaisu pienellä vaivalla. Pääohjelman rakenne uudelleenkirjoituksenkin jälkeen tuotti hieman vaivaa testien kirjoittamiselle. Tähän asiaan joudun ehkä vielä jossain kohtaa palaamaan.

