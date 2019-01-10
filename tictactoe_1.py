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

        self.pieces = ['X', 'O']
        self.players = ['player', 'comp']
        self.validMoves = set(range(1,10))

    def printBoard(self):
        # print each row, with margins and borders
        for row in self.numpadOrder:
            print('   |   |   ')
            print('', ' | '.join(self.board[col] for col in row))
            if row == (1,2,3): # if it is the last row, do not print the horizontal border
                print('   |   |   ')
            else:
                print('___|___|___')
        # print('\n')

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
        while True:
            print('Input next move location (1-9):')
            loc = int(input())
            if loc not in self.validMoves or not self.board[loc] == ' ':
                print(loc, 'is not a valid move.')
            else:
                return loc

    def compInputRandom(self):
        # pick random empty spot
        while True:
            loc = random.randint(1,9)
            if self.board[loc] == ' ':
                return loc

    def compInput(self):
        # first move
        if set(self.board) == {' '}:
            return 1

        # second move
        if len(set(self.board)) == 1:
            return 5

        # TODO: not complete


    def checkIfWin(self, piece):
        b = self.board

        if any(b[i]==piece and b[j]==piece and b[k]==piece \
               for i,j,k in self.winningCombs):
            return True
        else:
            return False

    def switchTurnAndPiece(self, playerInd, pieceInd):
        return not(playerInd), not(pieceInd)

    def getFirstPlayerAndPiece(self):
        # Pick randomly who goes first, and randomly which piece
        playerInd = random.randint(0, 1)  # 0 is player, 1 is comp
        pieceInd = random.randint(0, 1)   # 0 is X, 1 is O
        if playerInd:
            print('Computer is going first, using piece', self.pieces[pieceInd])
        else:
            print('Player is going first, using piece', self.pieces[pieceInd])

        return playerInd, pieceInd

    def playGame(self):

        print('Begin Tic-Tac-Toe')
        # who goes first, and with which piece is picked randomly
        curPlayerInd, curPieceInd = self.getFirstPlayerAndPiece()

        while not self.isFull():
            print('Current board:')
            self.printBoard()
            curPlayer = self.players[curPlayerInd]
            curPiece = self.pieces[curPieceInd]

            if curPlayer == 'player':
                print('Player\'s turn')
                loc = self.playerInput()
                self.placePiece(curPiece, loc)
            else:
                print('Computer\'s turn')
                loc = self.compInputRandom()
                print('Computer places ' + curPiece + ' at ' + str(loc))
                self.placePiece(curPiece, loc)

            # check if someone has won
            if self.checkIfWin(curPiece):
                self.printBoard()
                print(curPiece, " is the winner")
                break

            # switch piece/turn
            curPlayerInd, curPieceInd = self.switchTurnAndPiece(curPlayerInd, curPieceInd)

        print('Game is over')
        print('Play again? (y/n)')

        if input().lower().startswith('y'):
            self.resetBoard()
            self.playGame()

b1 = TicTacToeGame()
b1.playGame()