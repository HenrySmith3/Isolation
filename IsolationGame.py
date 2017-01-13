class IsolationGame:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.grid = [[" "]*5 for i in range(5)]

    def playGame(self):
        player1turn = True
        while(self.moveIsPossible(player1turn)):
            self.printboard()
            player = self.player1 if player1turn else self.player2

            #X instead of number on the old move
            if hasattr(player, 'position'):
                oldmove = player.position
                self.grid[oldmove[0]][oldmove[1]] = "X"

            #make the move
            move = player.move(self)
            self.grid[move[0]][move[1]] = "1" if player1turn else "2"
            player.position = move
            player1turn = not player1turn

        if (player1turn):
            print "player 2 won!"
        else:
            print "player 1 won!"

    def printboard(self):
        boardstring = ""
        for i in range(5):
            boardstring += "\n"
            for j in range(5):
                boardstring += '[' + self.grid[i][j] + ']'
        print boardstring
    def moveIsPossible(self, player1turn):
        player = self.player1 if player1turn else self.player2
        if not hasattr(player, 'position'):
            return True
        position = player.position
        for i in [position[0]-1, position[0], position[0]+1]:
            for j in [position[1]-1, position[1], position[1]+1]:
                if (i >= 0 and i < 5 and j >= 0 and j < 5):
                    if self.grid[i][j] == " ":
                        return True
        return False