#Controls the game, tells the GUI what to do

from player import Player

class ChessGame():
    def __init__(self):
        #Any settings will be set here
        self.black_player = Player()
        self.white_player = Player()

    def start_game(self):
        pass

    def has_legal_moves(self, player):
        #Checks if player class has any legal moves
        pass