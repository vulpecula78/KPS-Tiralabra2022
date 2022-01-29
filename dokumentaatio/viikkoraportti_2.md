# Viikkoraportti 2
-----

### Mitä on tehty

 - Projektin alustus poetryllä ja Ohjelmointia (12h)
 - Opiskelua Markovin ketjuista. (3h)
 - Github actions ja codecov virittely. (1,5h)
 - Raporttien kirjoitus ja tiedonhakua ym (2,5h)
 
 Tämä viikko on mennyt pääasiassa ohjelman suunnittelun ja ohjelmoinnin merkeissä. Ohjelmaa pystyy jo käyttämään ja siinä on kaksi ai-mallia joiden pelituloksia on tarkoitus verrata Markovin-ketjulla toteutun ai:n tuloksiin. Olen hieman hahmotellut jo miten vertailua eri pelitapojen välillä tehdään. Ohjelmiston testaus on aloitettu kirjoittamalla joitain unittestejä. Github actions suorittaa testit automaattisesti. 
 
-----
### Ohjelmoinnin edistyminen
 
 Ohjelmointityö on lähtenyt melko hyvin käyntiin. Ohjelmalle on tehty perustoiminnot ja tekstikäyttöliittymä on melko pitkällä. Peliin on tehty kaksi ai-mallia, joista toinen toimii täysin satunnaisesti arpoen kivi, sakset tai paperi. Toinen malli huomioi 10 viimeisintä siirtoa ja laskee klassista todennäköisyyttä käyttäen todennäköisyyden siitä mitä pelaaja tulee valitsemaan ja arpoo näiden todennäköisyyksien pohjalta kiven, paperin tai sakset. Ai luokille on tehty unittestit. Koodin laatua on tarkasteltu pylintillä. Pääohjelman toteutus on vielä aika pahasti keskeneräinen, eikä sille ole vielä tehty testejä.
 
-----
### Mitä olen oppinut

Olen oppinut lisää Markovin ketjuista. Githubin käyttöä tullut hieman kertailtua. Hieman yleistä ohjelmoinnista ja yksikkötestauksesta.

-----
### Mitä seuraavaksi

Seuraavaksi on tarkoituksena jatkaa opiskelua Markovin ketjuista ja ohjelmoida 1. asteen Markovin-ketjuun perustuva ai. Tämän lisäksi korjailla pääohjelmaa, käyttöliittymää ja tuottaa jonkinlaista tilastointia peleistä. Yritän myös saada pylint tarkastuksen toimimaan githubissa.

-----
### Mitä jäi epäselväksi, ollut vaikeaa tai tuottanut ongelmia?
 
 Ohjelmointityö lähti liikkeelle hieman kankeasti, mutta kun sain erittäin yksinkertaisen rungon tehtyä, niin työ alkoi edistymään. Tällä hetkellä ei ole ollut suurempia ongelmia. Pylint tarkastusta en saanut ainakaan heti toimimaan oikein github actionssissa, jotain ongelmia termcolor importin kanssa. En kuitenkaan vielä paljoa aikaa tämän ongelman tutkimiseen käyttänyt.

