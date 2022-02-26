
## Toteutusdokumentti

-----
### Sovelluksen yleisrakenne

Sovellus koostuu pääohjelmasta, tekstipohjaisesta käyttöliittymästä ja erilaisista AI-luokista ja Trie-tietorakenteesta. 

#### Pääohjelma

Pääohjelma yhdistää kaikki osat toisiinsa ja pitää sisällään pelilogiikan. Se myös hoitaa tilastotietojen käsittelyn (Tämä mahdollisesti eriytetään omaksi luokaksi).

#### Käyttöliittymä

Käyttöliittymänä on yksinkertainen tekstipohjainen malli, joka pitää sisällään päävalikon, pelivalikon ja tilastojen tulostamisen. käyttöliittymä vastaan ottaa pelaajan antamat syötteet ja antaa ne pääohjelmalle, sekä tulostaa ruudulle pelitapahtumat pääohjelmalta saadun tiedon mukaan.

#### AI luokat

AI luokkia on 4: Täysin satunnaisesti toimiva, klassista todennäköisyyttä käyttävä luokka, 1. asteen Markovia käyttävä luokka, sekä eripituisia Markovin-ketjuja käyttävä luokka, joka vaihtelee käytettävän ketjun pituutta sen mukaan minkälainen ketju olisi tuonut parhaan tuloksen aiemmilla kierroksilla.

#### Trie 

Sovelluksessa on sen tarpeita varten rakennettu Trie-tietorakenne. Eripituisia Markovin-ketjuja käyttävä luokka tallentaa pelitapahtumat Trie puuhun, josta se saa helposti selvitetty eripituisten ketjujen todennäköisyydet.
