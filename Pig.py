#! src/bin/python3

from Player import Player
from Die import Die
from Game import Game
from random import randrange


class Pig (object):

    game = None
    p1 = None
    p2 = None
    active_player = None
    players = []

    def initializer(self):

        msg = "##################\n" \
            "# WELCOME TO PIG #\n" \
            "##################\n"

        print(msg)

        player1_name = input("Please enter player1 name: ")
        player2_name = input("Please enter player2 name: ")

        die = Die()

        self.p1 = Player(player1_name, die)
        self.p2 = Player(player2_name, die)

        self.game = Game(self.p1, self.p2, die)

    def run(self):

        self.initializer()

        self.players = self.game.players

        self.active_player = self.players[0]

        running_total = 0

        while self.p1.count <= 100 or self.p2.count <= 100:

            print("Player {} is up \n".format(self.active_player.name))

            self.game.display_selection_menu()

            selection = input("Roll or Hold")

            if selection == '1':
                throw = self.active_player.roll()

                if throw == 1:
                    running_total = 0
                    self.switch_player(self.active_player, running_total)
                else:
                    running_total += throw
                    print("Current total = {}".format(str(running_total)))

            elif selection == '2':
                self.switch_player(self.active_player, running_total)
                running_total = 0
            else:
                self.game.clear_screen()
                print("Invalid selection")

        if self.p1.count == 100:
            print("Player {} is the WINNER".format(self.p1.name))
        else:
            print("Player {} is the WINNER".format(self.p2.name))

    def switch_player(self, player, runningTotal):

        # Switch from player 1 to player 2
        if player is self.players[0]:
            player.count += runningTotal
            self.active_player = self.players[1]
        # switch player from p2 to p1
        elif player is self.players[1]:
            player.count += runningTotal
            self.active_player = self.players[0]

        self.display_score()

    def display_score(self):
        title = "#########\n# SCORE #\n#########\n"
        print(title)

        print("P1: {} = {}".format(self.p1.name, str(self.p1.count)))
        print("P2: {} = {}".format(self.p2.name, str(self.p2.count)))


if __name__ == '__main__':
    Pig().run()





