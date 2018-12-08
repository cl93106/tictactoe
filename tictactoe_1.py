import random

class TicTacToeGame:

    def __init__(self):
        # board numbering is organized like the numpad
        # 7 8 9
        # 4 5 6
        # 1 2 3
        self.numpadOrder = ((7,8,9),(4,5,6),(1,2,3))
        # initialize blank board
        self.board = [' '] * 10
        self.winningCombs = [(1, 2, 3), (4, 5, 6), (7, 8, 9), \
                        (1, 4, 7), (2, 5, 8), (3, 6, 9), \
                        (1, 5, 9), (3, 5, 7)]

    def printBoard(self):
        # print each row, with margins and borders
        for row in self.numpadOrder:
            print('   |   |   ')
            print('', ' | '.join(self.board[col] for col in row))
            if row == (1,2,3): # if it is the last row, do not print the horizontal border
                print('   |   |   ')
            else:
                print('___|___|___')
        print('\n')

    def placePiece(self, piece, loc):
        # place piece at loc
        self.board[loc] = piece

    def isFull(self):
        # no blank spaces means full
        return not ' ' in self.board

    def resetBoard(self):
        # initialize all spaces to blank
        self.board = [' '] * 10

    def playerInput(self):
        # player inputs move location
        loc = -1
        nums = set(range(1,10))
        while loc not in nums or not self.board[loc] == ' ':
            print('Input next move location (1-9)')
            loc = int(input())
        return loc

    def compInput(self):
        # not implemented yet
        pass

    def checkIfWin(self, piece):
        b = self.board

        if any(b[i]==piece and b[j]==piece and b[k]==piece \
               for i,j,k in self.winningCombs):
            return True
        else:
            return False

    def playGame(self):
        pieces = ['X', 'O']
        players = ['player', 'comp']

        currentPlayerInd = random.randint(0,1)
        currentPieceInd = 0

        while not self.isFull():
            self.printBoard()
            curPlayer = players[currentPlayerInd]
            curPiece = pieces[currentPieceInd]

            if curPlayer == 'player':
                loc = self.playerInput()
                print(loc)
                self.placePiece(curPiece, loc)
            else:
                print('hello')

            self.printBoard()
            # check if someone has won
            if self.checkIfWin(curPiece):
                print(curPiece, " is the winner")
                break

            # switch piece
            currentPieceInd = not(currentPieceInd)
            currentPlayerInd = not(currentPlayerInd)

        print('Game is over')
        print('Play again? (y/n)')

        if input().lower().startswith('y'):
            self.resetBoard()
            self.playGame()


b1 = TicTacToeGame()
# b1.printBoard()
# b1.placePiece('X',1)
# b1.placePiece('O',5)
# b1.placePiece('X',6)
# b1.placePiece('O',9)
# b1.printBoard()
b1.playGame()