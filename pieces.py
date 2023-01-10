
class Piece:

    def __init__(self, currentSquare, player) -> None:
        
        self.alive = True
        self.square = currentSquare
        self.value = 0
        self.player = player
        pass

    def get_alive(self):
        return self.alive
    
    def get_square(self):
        return self.square
    
    def set_dead(self):
        self.alive = False
        return 
    

class Knight(Piece):

    def __init__(self, currentSquare) -> None:
        super().__init__(currentSquare)
        self.value = 3
        self.symbol = "k"
        return

class Bishop(Piece):

    def __init__(self, currentSquare) -> None:
        super().__init__(currentSquare)
        self.value = 3
        self.symbol = "B"
        return

class Rook(Piece):

    def __init__(self, currentSquare) -> None:
        super().__init__(currentSquare)
        self.value = 5
        self.symbol = "R"
        return

class Pawn(Piece):

    def __init__(self, currentSquare) -> None:
        super().__init__(currentSquare)
        self.value = 1
        self.symbol = "P"
        return
    
class Queen(Piece):

    def __init__(self, currentSquare) -> None:
        super().__init__(currentSquare)
        self.value = 9
        self.symbol = "Q"
        return

class King(Piece):

    def __init__(self, currentSquare) -> None:
        super().__init__(currentSquare)
        self.value = 100
        self.symbol = "K"
        return

