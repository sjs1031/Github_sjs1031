class Game:
    """"""
    def __init__(self):
        """Constructor"""
        self.score = 0
        self.pins = [0 for i in range(11)]

    def roll(self, numOfRolls, pins):
        """"""
        x = 0
        for pin in pins:
            self.pins[x] = pin
            x += 1
        x = 0
        for roll in range(numOfRolls):
            if self.pins[x] == 10:
                self.score = self.pins[x] + self.pins[x+1] + self.pins[x+2]
            else:
                self.score += self.pins[x]
                x += 1
        print(self.score)