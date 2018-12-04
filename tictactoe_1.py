class TicTacToeGame:

    def __init__(self):
        # board numbering is organized like the numpad
        # 7 8 9
        # 4 5 6
        # 1 2 3
        self.numpadOrder = ((7,8,9),(4,5,6),(1,2,3))
        self.board = ['_'] * 10


    def printBoard(self):
        for row in self.numpadOrder:
            print(' | '.join(self.board[col] for col in row))
            print('__|___|__')
        print('\n')

    def placePiece(self, piece, loc):
        self.board[loc] = piece

b1 = TicTacToeGame()
b1.printBoard()
b1.placePiece('X',1)
b1.placePiece('O',5)
b1.printBoard()