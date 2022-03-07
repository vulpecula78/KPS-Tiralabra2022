import sys
from ai.ai_random import AiRandom
from ai.ai_classical import AiClassical
from ai.ai_markov1 import AiMarkov1
from ai.gorn_ai import GornAi
from gorn_stats import GornStatistics

class Gorn:
    def __init__(self, gornui):
        self._ai = None
        self._ui = gornui
        self._items = {"k":0, "s":2, "p":1, "l":4, "v":3} # lisko 4, spock 2
        self.stats = (0, 0, 0, 0, 0, 0, 0)
        self._statistics = GornStatistics()

    def main(self):
        '''Päävalikon toiminta logiikka. Kutsuu ui:lta
        valintaa, jonka mukaan valitaan toiminto.'''
        while True:
            selection, mode = self._ui.start_menu()
            if selection == "0":
                sys.exit()
            if selection == "0x0x": #Tämä vaihtoehto on unittestiä varten.
                return self.stats
            if selection == "6":
                self.statistics()
            if selection in ('1', '2', '3', '4'):
                self.setai(selection, mode)

    def setai(self, selection, mode):
        '''Valitaan tekoälymalli ja aloitetaan peli.

        args:
            selection: str: 1, 2, 3 tai 4 '''
        if selection == "2":
            self._ai =  AiClassical(mode)
        elif selection == "3":
            self._ai =  AiMarkov1(mode)
        elif selection == "4":
            self._ai = GornAi(mode)
        else:
            self._ai = AiRandom(mode)
        self.kps_peli()

    def kps_peli(self):
        '''pelilogiikka. Pyytää ui:lta pelaajan valinnan ja
        valitulta tekoälyltä AI valinnan. Tarkastaa tuloksen
        ja palauttaa tiedot ui:lle ja AI:lle. Funktio on silmukassa,
        kunnes saa syötteen "x", jonka jälkeen palataan pääsilmukkaan.

        Ensin pyydetään pelaajan valinta kutsumalla ui:n game_menu,
        siten AI:n valinta. Tämän jälkeen tarkastetaan tulos,
        päivitetään historia ja pyydetään ui:tä tulostamaan tapahtumat.
        '''
        round_ = 0
        win = 0
        ai_win = 0
        ties = 0

        while True:
            choice = self._ui.game_menu(round_, win, ai_win, ties)
            if choice == "x":
                break
            ai_choice = self._ai.choose()

            round_ += 1
            winner = self._items[choice] - self._items[ai_choice]
            if winner == 0:
                ties += 1
                result = 0
            elif winner in (-4, -2, 1, 3):
                win += 1
                result = -1
            else:
                ai_win += 1
                result = 1

            self._ai.add_round(choice, ai_choice, result)
            self._ui.move(choice, ai_choice, result)

    def statistics(self):
        '''Viimeisempänä käytetyn ai:n tilastot.
        Mikäli tilastoja ei ole, niin palautetaan virhe.
        Muutoin pyydetään AI:ltä historia ja todennäköisyydet,
        annetaan ne gorn_stats luokalle ja pyydentään ui:tä
        tulostamaan ne.'''
        if self._ai is None:
            print("Virhe! Tilastoja ei vielä ole.\n")
            return

        history, probabilities = self._ai.get_history()

        self.stats = self._statistics.victories(history)
        win_stats = self._statistics.stats_by_nrounds(history)

        self._ui.print_stats(self.stats, win_stats, probabilities)
