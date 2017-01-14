class HumanPlayer:

    def __init__(self):
        pass
    def move(self, game):
        print "Input x,y"
        move = input()
        return [move[0], move[1]]