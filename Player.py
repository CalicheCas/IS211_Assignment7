from PlayerType import PlayerType


class Player:

    count = 0
    pt = PlayerType().human
    active = False

    def __init__(self, name, die):

        self.name = name
        self.die = die

    def roll(self):

        self.active = True
        val = self.die.spin()
        print("You rolled a {}".format(str(val)))

        return val

    def hold(self, total):

        self.count += total
        self.active = False

    def print_score(self):

        print("{} = []".format(self.name, str(self.count)))
