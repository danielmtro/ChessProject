from squares import Square

class Board():

    def __init__(self) -> None:
        self.board = []

        for i in range(8):
            self.board.append([])
            for j in range(8):
                self.board[-1].append(Square(i, j))
        pass
    
    def __str__(self) -> str:
        str = ""

        for i in range(33):
            str += "-"
        str += "\n"

        for i in chess.board:
            for j in i:
                str += "| "
                str += j.show_current_piece()
                str += " "
                
            str += "|"
            str += "\n"
            for i in range(33):
                str += "-"
            str += "\n"

        return str

chess = Board()

print(chess)