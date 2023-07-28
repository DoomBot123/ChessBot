class ChessPiece():
    def __init__(self):
        pass

    def move_to_legal_square(self,square):
        pass

class Pawn(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
    image = "pawn.png"

