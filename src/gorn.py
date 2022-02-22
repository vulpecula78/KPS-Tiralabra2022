import sys
from ai.ai_random import AiRandom
from ai.ai_classical import AiClassical
from ai.ai_markov1 import AiMarkov1
from ai.gorn_ai import GornAi

class Gorn:
    def __init__(self, gornui):
        self._ai = None
        self._ui = gornui
        #self._items = {"k":5, "s":3, "p":1}
        self._items = {"k":0, "s":2, "p":1, "l":4, "v":3} # lisko 4, spock 2
        self.stats = (0, 0, 0, 0, 0, 0, 0)

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
        '''Valitaan tekoäly malli ja aloitetaan peli.

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
        ja palauttaa tiedot ui:lle ja AI:lle.'''
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
        Tämä on vielä kesken'''
        if self._ai is None:
            print("Virhe! Tilastoja ei vielä ole.\n")
            return

        history, probabilities = self._ai.get_history()

        if len(history[0]) > 0:
            games_played = len(history[0])
            player_won = history[2].count(-1)
            ai_won = history[2].count(1)
            tie = history[2].count(0)

            win_p = player_won / games_played * 100
            ai_win_p = ai_won / games_played * 100
            tie_p = tie / games_played * 100
            self.stats = (games_played, player_won, ai_won, tie, win_p, ai_win_p, tie_p)

            sets = games_played // 25

            #Luodaan tilastot 25 kierroksen voitto prosenteista, kesken...
            win_stats = []
            rounds = 0
            for i in range(sets):
                pwins = (history[2][i*25:i*25+25].count(-1) / 25) *100
                cwins = (history[2][i*25:i*25+25].count(1) / 25) *100
                ties = (history[2][i*25:i*25+25].count(0) / 25) *100
                rounds += 1
                win_stats.append((rounds, pwins, cwins, ties))
            print(win_stats)
        self._ui.print_stats(self.stats, probabilities)
