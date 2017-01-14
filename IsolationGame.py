class IsolationGame:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player1.hasmoved = False
        self.player2.hasmoved = False
        self.grid = [[" "]*5 for i in range(5)]

    def playGame(self):
        player1turn = True
        while(self.moveIsPossible(player1turn)):
            self.printboard(player1turn)
            player = self.player1 if player1turn else self.player2

            #X instead of number on the old move
            position = ""
            if player.hasmoved:
                position = player.position
                self.grid[position[0]][position[1]] = "X"

            #make the move
            move = player.move(self)
            while (not self.isMoveValid(player, move)):
                print "Invalid move!"
                move = player.move(self)
            player.hasmoved = True
            self.grid[move[0]][move[1]] = "1" if player1turn else "2"
            player.position = move
            player1turn = not player1turn

        if (player1turn):
            print "player 2 won!"
        else:
            print "player 1 won!"

    def isMoveValid(self, player, move):
        if not (move[0] >= 0 and
            move[0] <= 4 and
            move[1] >= 0 and
            move[1] <= 4):
            return False


        #Move is in bounds
        if not player.hasmoved:
            return True

        if player.position == move:
            return False
        if (move[0] == player.position[0]):
            for i in range(move[1], player.position[1], 1 if move[1] < player.position[1] else -1):
                if (self.grid[move[0]][i] != " "):
                    return False
            return True
        if (move[1] == player.position[1]):
            for i in range(move[0], player.position[0], 1 if move[0] < player.position[0] else -1):
                if (self.grid[i][move[1]] != " "):
                    return False
            return True
        #If we got to here, it's diagonal (or invalid)
        if not abs(move[0] - player.position[0]) == abs(move[1] - player.position[1]):
            return False

        #So it's a valid diagonal
        xdirection = 1 if move[0] - player.position[0] > 0 else -1
        ydirection = 1 if move[1] - player.position[1] > 0 else -1
        movecopy = [0,0]
        movecopy[0] = player.position[0] + xdirection
        movecopy[1] = player.position[1] + ydirection
        while (movecopy != move):
            if (self.grid[movecopy[0]][movecopy[1]] != " "):
                return False
            movecopy[0] += xdirection
            movecopy[1] += ydirection
        return True


    def printboard(self, player1turn):
        boardstring = "  0  1  2  3  4"
        for i in range(5):
            boardstring += "\n"
            boardstring += str(i)
            for j in range(5):
                boardstring += '[' + self.grid[j][i] + ']'
        print boardstring
        print "Player " + ("1" if player1turn else "2") + "'s turn"
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
