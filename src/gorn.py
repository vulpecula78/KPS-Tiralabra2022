import sys
from ai_random import AiRandom
from ai_classical import AiClassical
from gorn_ui import GornUi


class Gorn:
    def __init__(self):
        self._ai = None
        self._ai_random = AiRandom()
        self._ai_classic = AiClassical()
        self._ui = GornUi()
        self._items = {"k":5, "s":3, "p":1}

    def main(self):
        while True:
            selection = self._ui.start_menu()

            if selection == "0":
                sys.exit()
            if selection == "6":
                self.statistics()
            if selection == "1":
                self._ai = self._ai_random
                self.kps_peli()
            if selection == "2":
                self._ai =  self._ai_classic
                self.kps_peli()

    def kps_peli(self):
        kierros = 0
        voitot = 0
        ai_voitot = 0
        tasapelit = 0

        while True:
            kierros = kierros + 1
            siirto = self._ui.game_menu(kierros, voitot, ai_voitot, tasapelit)
            ai_siirto = self._ai.choice()

            if siirto == "x":
                break

            winner = self._items[siirto] - self._items[ai_siirto]
            if winner == 0:
                tasapelit += 1
                result = 0
            elif winner in (2, -4):
                voitot += 1
                result = -1
            else:
                ai_voitot += 1
                result = 1

            self._ai.add_round(siirto, ai_siirto, result)
            self._ui.move(siirto, ai_siirto, result)


    def statistics(self):
        '''Viimeisempänä käytetyn ai:n tilastot. '''
        try:
            history, probabilities = self._ai.get_history()
        except AttributeError:
            print("Virhe! Tilastoja ei vielä ole.\n")
            return

        print(probabilities)
        games_played = len(history[0])
        player_won = history[2].count(-1)
        ai_won = history[2].count(1)
        tie = history[2].count(0)

        win_p = player_won / games_played * 100
        ai_win_p = ai_won / games_played * 100
        tie_p = tie / games_played * 100

        stats = (games_played, player_won, ai_won, tie, win_p, ai_win_p, tie_p)
        self._ui.print_stats(stats)
