from IsolationGame import *
from HumanPlayer import *
from RandomAI import *

game = IsolationGame(HumanPlayer(), RandomAI())
game.playGame()