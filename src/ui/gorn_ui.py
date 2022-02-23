import os
from termcolor import colored, cprint

class GornUi:
    def __init__(self):
        os.system('color') #Tarvitaan, jotta termcolor toimii windowsissa
        self.items = {"k":"kiven", "p":"paperin", "s":"sakset", "l":"liskon", "v":"Spockin"}
        self.results = {-1:"Pelaajan voitto", 0:"Tasapeli", 1:"Tietokoneen voitto"}
        self._sentences = {'ks':"Kivi murskaa sakset!", 'sp':"Sakset silppuaa paperin!",
                           'pk':"Paperi peittää kiven!", 'lv':"Lisko myrkyttää Spockin!",
                           'kl':"kivi murskaa liskon!", 'lp':"Lisko syö paperin!",
                           'vs':"Spock rikkoo sakset!", 'vk':"Spock höyrystää kiven!",
                           'pv':"Paperi kiistää Spockin väitteen!",
                           'sl':"Sakset katkoo liskon kaulan!"}
        self.gorn = False
        print (colored
               ("\n\n-----------------------------------------------------------------------",
                'green'))
        print (colored
               ("\nTervetuloa pelaamaan Gorn: kivi, paperi, sakset, lisko ja Spock peliä!\n",
                'green'))
        print (colored
               ("-----------------------------------------------------------------------\n",
                'green'))

    def start_menu(self):
        menu_items = ['1', '2', '3', '4', '5', '6', '0']

        while True:
            cprint("\nValitse vastustaja tai tulosta tilastot:", 'green')
            cprint("1) Satunnaisesti pelaava AI", 'cyan')
            cprint("2) Klassista todennäköisyyttä käyttävä AI", 'cyan')
            cprint("3) 1. asteen Markov käyttävä AI", 'cyan')
            cprint("4) Gorn AI", 'cyan')
            cprint("5) Vaihda pelimoodia, käytössä:  ", end='')
            if self.gorn:
                print("Kivi, paperi, sakset, lisko ja Spock.")
            else:
                print("Kivi, paperi ja sakset")
            print("6) Tilastot ")
            print("0) lopeta")

            selection = input("\nValintasi: ")

            if selection in menu_items:
                if selection == '5':
                    self.gorn = not self.gorn
                    continue
                return selection, self.gorn

    def game_menu(self, round_, won, ai_won, ties):
        if self.gorn:
            choices = ('x', 'k', 's', 'p', 'l', 'v')
        else:
            choices = ('x', 'k', 's', 'p')

        while True:
            print()
            print(f"Kierros: {round_}.")
            print(colored(f"Tilanne {round_} kierroksen jälkeen:", 'white'),
                  colored(f"Pelaaja: {won}", 'green'), colored(f" Tietokone: {ai_won}", 'red'),
                  colored(f" Tasapelit: {ties}", 'blue'))
            if self.gorn:
                cprint("Valitse k)kivi, s)sakset, p)paperi, l)lisko tai v)Spock  \nx)" +
                       "lopettaa pelin: ", 'cyan', end='')
            else:
                cprint("Valitse k)ivi, s)akset tai p)aperi. \nx) lopettaa pelin: ", 'cyan', end='')
            choice = input('')

            if choice in choices:
                return choice
            cprint('Virheellinen valinta!', 'red')

    def move(self, player, computer, result):
        print("Valitsit " + self.items[player] + " ja tietokone valitsi " + self.items[computer])
        if result == 1:
            cprint(self._sentences[computer+player], 'red')
        elif result == -1:
            cprint(self._sentences[player+computer], 'green')
        print(self.results[result] + "!")

    def print_stats(self, data, stats_by_rounds, probabilities):
        '''Tulostaa pelin tilastot.
            data on lista, jossa
            0: pelatut kierrokset, 1: pelaajan voitot,
            2: tietokoneen voitot, 3: tasapelit,
            4: Pelaajan voitto %,  5: tietokoneen voitto %,
            6: tasapeli %'''

        cprint("Tilastot:", 'green')
        cprint(f"Kierroksia pelattu: {data[0]}, joista pelaaja voittanut {data[1]}" +
               f" ({data[4]:.2f}%) ja tietokone {data[2]} ({data[5]:.2f}%)." +
               f" Tasapelejä pelattu: {data[3]} ({data[6]:.2f}%)\n", 'green')
        if len(stats_by_rounds) > 0:
            for i in range(len(stats_by_rounds)):
                print(f"Kierrokset {i+1} - {(i+1)*25}: Pelaaja: {stats_by_rounds[i][1]:.2f}%," +
                      f" AI: {stats_by_rounds[i][2]:.2f}%," +
                      f"Tasapelit: {stats_by_rounds[i][3]:.2f}%")
            print()
        if type(probabilities[0]) == float:
            print("Todennäköisyystaulukko, jonka mukaan pelaajan seuraava siirto ennakoidaan:")
            items = ['k', 'p', 's', 'l', 'v']
            for i in range(len(probabilities)):
                print(f"{items[i]}: {probabilities[i]:.2f}% ", end="")
        else:
            for i in probabilities:
                print(i)
        print()
