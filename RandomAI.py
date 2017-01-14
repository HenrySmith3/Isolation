import random
class RandomAI:

    def __init__(self):
        pass
    def move(self, game):
        moves = game.generatePossibleMoves()
        return random.choice(moves)