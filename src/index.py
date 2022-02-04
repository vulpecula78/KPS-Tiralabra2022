from gorn import Gorn
from gorn_ui import GornUi

def main():
    """Käynnistää Gorn-KPS pelin"""
    gornui = GornUi()
    gorn = Gorn(gornui)

    gorn.main()

if __name__ == '__main__':
    main()
