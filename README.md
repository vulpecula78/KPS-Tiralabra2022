# KPS-Tiralabra2022
## Gorn-KPS

![GitHub Actions](https://github.com/vulpecula78/KPS-Tiralabra2022/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/vulpecula78/KPS-tiralabra2022/branch/main/graph/badge.svg?token=977I3Z6IMH)](https://codecov.io/gh/vulpecula78/KPS-tiralabra2022)
-----
### Sovelluksen käyttö
1. Kloonaa repositorio

2. Suorita riippuvuuksien asennus komennolla:

    ```
    poetry install
    ```

3. Peli käynnistyy komennolla:

    ```
    poetry run invoke start
    ```
-----
### Dokumentaatio:

- [Määrittelydokumentti](https://github.com/vulpecula78/KPS-Tiralabra2022/blob/main/dokumentaatio/maarittelydokumentti.md)
- [1. Viikkoraportti](https://github.com/vulpecula78/KPS-Tiralabra2022/blob/main/dokumentaatio/viikkoraportti_1.md)
- [2. Viikkoraportti](https://github.com/vulpecula78/KPS-Tiralabra2022/blob/main/dokumentaatio/viikkoraportti_2.md)

### Testaus ja koodin laatu

Sovelluksen yksikkötestit ajetaan komennolla:

```
poetry run invoke test
```

Testiraportti tulostuu komennolla:

```
poetry run invoke coverage-report
```

Testiraportin voi myös tehdä selaimella tarkasteltavaksi komennolla:

```
poetry run invoke coverage-html
```


Koodin laatu tarkastuksen voi suorittaa pylintillä komennolla:

```
poetry run invoke lint
```
