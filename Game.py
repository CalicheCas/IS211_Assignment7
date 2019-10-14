from Player import Player
import platform
import os


class Game:

    def __init__(self, player1, player2, die):
        self.player1 = Player(player1, die)
        self.player2 = Player(player2, die)
        self.players = [player1, player2]

    def clear_screen(self):

        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')


    def display_selection_menu(self):

        menu = "Roll: 1\n" \
               "Hold: 2\n"
        print(menu)
