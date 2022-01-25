import sys
from ai_random import AiRandom
from gorn_ui import GornUi


class Gorn:
    def __init__(self):
        self._ai = None
        self._ai_random = AiRandom()
        self._ui = GornUi()

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

            if siirto == ai_siirto:
                result = 0
                tasapelit += 1
            elif (siirto == "k" and ai_siirto == "p") or (siirto == "p" and ai_siirto == "s"):
                result = 1
                ai_voitot += 1
            elif  (siirto == "s" and ai_siirto == "k"):
                result = 1
                ai_voitot += 1
            else:
                voitot += 1
                result = -1

            self._ai.add_round(siirto, ai_siirto, result)
            self._ui.move(siirto, ai_siirto, result)


    def statistics(self):
        history = self._ai.get_history()

        games_played = len(history[0])
        player_won = history[2].count(-1)
        ai_won = history[2].count(1)
        tie = history[2].count(0)

        win_p = player_won / games_played * 100
        ai_win_p = ai_won / games_played * 100
        tie_p = tie / games_played * 100

        stats = (games_played, player_won, ai_won, tie, win_p, ai_win_p, tie_p)
        self._ui.print_stats(stats)
