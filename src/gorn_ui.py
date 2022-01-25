from termcolor import colored, cprint

class GornUi:
    def __init__(self):
        self.items = {"k":"kiven", "p":"paperin", "s":"sakset"}
        self.results = {-1:"Pelaajan voitto", 0:"Tasapeli", 1:"Tietokoneen voitto"}

    def start_menu(self):
        menu_items = ['1', '6', '0']
        print (colored("\nTervetuloa pelaamaan Gorn: kivi, paperi ja sakset peliä!\n", 'green'))

        while True:
            cprint("Valitse vastustaja tai tulosta tilastot:", 'green')
            cprint("1) Satunnaisesti pelaava AI", 'cyan')
            cprint("2) 1. asteen Markov", 'cyan')
            print("6) tilastot")
            print("0) lopeta")

            selection = input("\nValintasi: ")

            if selection in menu_items:
                return selection

    def game_menu(self, round_, won, ai_won, ties):
        choices = ('x', 'k', 's', 'p')
        while True:
            print()
            print(f"Kierros: {round_}.")
            print(colored(f"Pelaaja: {won}", 'green'), colored(f" Tietokone: {ai_won}", 'red'),
                  colored(f" Tasapelit: {ties}", 'blue'))
            cprint("Valitse k)ivi, s)akset tai p)aperi. \nx) lopettaa pelin: ", 'cyan', end='')
            choice = input('')

            if choice in choices:
                return choice
            cprint('Virheellinen valinta!', 'red')

    def move(self, player, computer, result):
        print("Valitsit " + self.items[player] + " ja tietokone valitsi " + self.items[computer])
        print(self.results[result] + "!")

    def print_stats(self, data):
        '''Tulostaa pelin tilastot.
            data on lista, jossa
            0: pelatut kierrokset, 1: pelaajan voitot,
            2: tietokoneen voitot, 3: tasapelit,
            4: Pelaajan voitto %,  5: tietokoneen voitto %,
            6: tasapeli %'''

        cprint("Tilastot:", 'green')
        cprint(f"Kierroksia pelattu: {data[0]}, joista pelaaja voittanut {data[1]}" +
               f" ({data[4]:.2f}%) ja tietokone {data[2]} ({data[5]:.2f}%)." +
               f" Tasapelejä pelattu: {data[3]} ({data[6]:.2f}%)", 'green')
