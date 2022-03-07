class GornStatistics:

    def __init__(self):
        pass

    def victories(self, history):
        '''Palauttaa pelin tulokset

        args:
            history: pelin historia matriisi

        returns:
            7-tuple pelin tuloksista
        '''

        if len(history[0]) > 0:
            games_played = len(history[0])
            player_won = history[2].count(-1)
            ai_won = history[2].count(1)
            tie = history[2].count(0)

            win_p = player_won / games_played * 100
            ai_win_p = ai_won / games_played * 100
            tie_p = tie / games_played * 100

            return (games_played, player_won, ai_won, tie, win_p, ai_win_p, tie_p)
        return (0,0,0,0,0,0,0)

    def stats_by_nrounds(self, history):
        '''
        Palauttaa voittoprosentit 25 kierroksen välein.

        args:
            history: Pelatuin pelin tapahtumat, joista tilasto luodaan.

        returns:
            3-tuple: pelaajan-, AI:n voitto % ja tasapeli %
        '''

        games_played = len(history[0])
        sets = games_played // 25

        #Luodaan tilastot 25 kierroksen voittoprosenteista.
        win_stats = []
        for i in range(sets):
            pwins = (history[2][i*25:i*25+25].count(-1) / 25) *100
            cwins = (history[2][i*25:i*25+25].count(1) / 25) *100
            ties = (history[2][i*25:i*25+25].count(0) / 25) *100
            win_stats.append((pwins, cwins, ties))
        return win_stats
