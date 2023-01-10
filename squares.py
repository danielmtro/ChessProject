from pieces import Piece
import pieces

class Square:

    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col
        self.empty = True
        self.currentpiece = None
        
        pass

    def get_coord(self):
        return (self.row, self.col)
    
    def get_empty(self):
        return self.empty
    
    def show_current_piece(self):
        
        if self.currentpiece == None:
            return " "

        return self.currentpiece.symbol
    
    def get_current_piece(self):
        return self.currentpiece
    
    def remove_piece(self):
        self.currentpiece = None
        self.empty = True
    
    def set_piece(self, piece: Piece):
        
        if self.get_current_piece() == None:
            raise AttributeError("Square currently filled")
        
        self.currentpiece = Piece
        self.empty = False

        return
    
    def __str__(self) -> str:
        return str(self.get_coord())

