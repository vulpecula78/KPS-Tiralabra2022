## Gorn-KPS Käyttöohje

#### Sisältö:
1. Sovelluksen asennus ja käynnistäminen
2. Testien suorittaminen

_____

### Sovelluksen asennus ja käynnistäminen

1. Kloonaa repositorio
2. Siirry kansioon KPS-Tiralabra2022.

3. Suorita riippuvuuksien asennus komennolla:

    ```
    poetry install
    ```

    Joissain tapauksissa riippuvuuksien asennus ei täysin toimi, jolloin termcolor kirjasto pitää asentaa käsin:
    
    ```
    pip3 install termcolor
    ```
    
4. Sovellus voidaan käynnistää komennolla:

    ```
    poetry run invoke start
    ```

    tai

    ```
    python3 src/index.py
    ```

-----

### Testien suorittaminen

#### Yksikkötestit

Yksikkötestit testaavat sovelluksen eri osat, käyttöliittymää lukuunottamatta. Testit sijaitsevat kansiossa src/tests
Sovellukseen sisältyvät yksikkötestit saadaan ajettua käskyllä:

   ```
    poetry run invoke test
   ```

Kattavuusraportti saadaan käskyllä:

   ```
    poetry run invoke coverage-report
   ```

Ja se saadaan myös html muodossa käskyllä:

   ```
    poetry run invoke coverage-html
   ```

#### Trie-tietorakenteen suorituskykytesti

Trie tietorakennetta varten on tehty yksinkertainen pieni testi, joka tallentaa trie-puuhun "seitsemän veljestä"-kirjan sanat.
Testi mittaa kirjan tallentamiseen kuluneen ajan, sekä muistinvarauksen muutoksen. Tämän jälkeen testi suorittaa haun sanalle "pikipallero" ja mittaa sen hakemiseen kuluneen ajan. Testi sijaitsee kansiossa src/tests/test_Trie.

Testin voi suorittaa käskyllä:


   ```
    python3 src/tests/test_Trie/Trie_testi.py
   ```

#### Koodin laatu


Koodin laatua on seurattu pylintillä ja se voidaan tarkastaa seuraavasti:

   ```
    poetry run invoke lint
   ```

_____

