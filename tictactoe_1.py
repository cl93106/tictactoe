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
        return not ' ' in self.board[1:]

    def resetBoard(self):
        # initialize all spaces to blank
        self.board = [' '] * 10

    def playerInput(self):
        # player inputs move location
        loc = -1
        while True:
            print('Input next move location (1-9):')

            try:
                loc = int(input())
            except ValueError:
                print('Invalid input.')
                continue

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

    @property
    def compInput(self):
        curPiece = self.pieces[self.pieceInd]


        # first to move on empty board, go corner
        if set(self.board) == {' '}:
            return 1

        # find vacant spots
        vacant = set([i for i in range(1,10) if self.board[i] == ' '])

        # pick winning move
        for loc in vacant:
            self.board[loc] = curPiece
            if self.checkIfWin(curPiece):
                self.board[loc] = ' '
                return loc
            self.board[loc] = ' '

        # block opponent winning move
        oppPiece = self.pieces[self.pieceInd ^ 1]
        for loc in vacant:
            self.board[loc] = oppPiece
            if self.checkIfWin(oppPiece):
                self.board[loc] = ' '
                return loc
            self.board[loc] = ' '

        # pick center
        if 5 in vacant:
            return 5

        # play defensive move if opponent captures 2 opposite corners
        if (self.board[1] == self.board[9] == oppPiece) or \
           (self.board[1] == self.board[9] == oppPiece):
            if self.board[4] == self.board[6] == ' ':
                return 4
            elif self.board[2] == self.board[8] == ' ':
                return 2

        # pick corner
        for i in (1,3,7,9):
            if i in vacant:
                return i

        # pick edge
        return vacant.pop()


    def checkIfWin(self, piece):
        b = self.board

        if any(b[i]==piece and b[j]==piece and b[k]==piece \
               for i,j,k in self.winningCombs):
            return True
        else:
            return False

    def switchTurnAndPiece(self):
        self.playerInd ^= 1
        self.pieceInd ^= 1

    def getFirstPlayerAndPiece(self):
        # Pick randomly who goes first, and randomly which piece
        self.playerInd = random.randint(0, 1)  # 0 is player, 1 is comp
        self.pieceInd = random.randint(0, 1)   # 0 is X, 1 is O
        if self.playerInd:
            print('Computer is going first, using piece', self.pieces[self.pieceInd])
        else:
            print('Player is going first, using piece', self.pieces[self.pieceInd])

    def getPlayerAndPiece(self):
        return self.players[self.playerInd], self.pieces[self.pieceInd]

    def talkTrash(self):
        lines = ['How you like them apples?',
                 'Computer is wicked smaht!']

        return random.choice(lines)

    def playGame(self):

        print('Begin Tic-Tac-Toe')
        # who goes first, and with which piece is picked randomly
        self.getFirstPlayerAndPiece()

        while not self.isFull():
            print('Current board:')
            self.printBoard()
            curPlayer, curPiece = self.getPlayerAndPiece()

            if curPlayer == 'player':
                print('Player\'s turn')
                loc = self.playerInput()
                self.placePiece(curPiece, loc)
            else:
                print('Computer\'s turn')
                # loc = self.compInputRandom()
                loc = self.compInput
                print('Computer places ' + curPiece + ' at ' + str(loc))
                self.placePiece(curPiece, loc)

            # check if someone has won
            if self.checkIfWin(curPiece):
                self.printBoard()
                print(curPlayer, ' using ', curPiece, ' is the winner')
                break

            # switch piece/turn
            self.switchTurnAndPiece()
        else:
            print('Draw')

        self.printBoard()
        if curPlayer == 'comp':
            print(self.talkTrash())
        print('Game is over')
        print('Play again? (y/n)')

        if input().lower().startswith('y'):
            self.resetBoard()
            self.playGame()

b1 = TicTacToeGame()
b1.playGame()