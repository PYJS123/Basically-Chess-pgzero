"""
Attempt at chess in python. (2nd time)
"""

import math

WIDTH = 500
HEIGHT = 500

LIGHTBLUE = (240, 240, 240)
DARKBLUE = (0, 47, 47)
cellSize = WIDTH / 8

# Code for piece class
class Piece:
    def __init__(self, pieceInfo, ex):
        self.x = findPos(pieceInfo, ex)[0]
        self.y = findPos(pieceInfo, ex)[1]
        self.colour = pieceInfo[0]
        self.parsedPiece = parsePiece(pieceInfo)
        self.body = Actor(self.parsedPiece, center=(self.x+(cellSize/2), self.y+(cellSize/2)))

def findPos(piece, ex):
    oppX = None
    oppY = None
    newpiecee = parsePiece(piece)
    if newpiecee == 'blackpawn': # Black
        oppX = ex - 1
        oppY = 1
    elif newpiecee == 'blackrook':
        oppY = 0
        oppX = (ex - 1) * 7
    elif newpiecee == 'blackknight':
        oppY = 0
        oppX = ((ex - 1) * 5) + 1
    elif newpiecee == 'blackbishop':
        oppY = 0
        oppX = ((ex - 1) * 3) + 2
    elif newpiecee == 'blackqueen':
        oppY = 0
        oppX = 3
    elif newpiecee == 'blackking':
        oppY = 0
        oppX = 4
    if newpiecee == 'whitepawn': # White
        oppY = 6
        oppX = ex - 1
    elif newpiecee == 'whiterook':
        oppY = 7
        oppX = (ex - 1) * 7
    elif newpiecee == 'whiteknight':
        oppY = 7
        oppX = ((ex - 1) * 5) + 1
    elif newpiecee == 'whitebishop':
        oppY = 7
        oppX = ((ex - 1) * 3) + 2
    elif newpiecee == 'whitequeen':
        oppY = 7
        oppX = 3
    elif newpiecee == 'whiteking':
        oppY = 7
        oppX = 4

    oppX *= cellSize
    oppY *= cellSize
    return (oppX, oppY)

def parsePiece(piece):
    newString = ''
    if piece[0] == 'B':
        newString += 'black'
    else:
        newString += 'white'

    pic = piece[1]
    if pic == 'p':
        newString += 'pawn'
    elif pic == 'r':
        newString += 'rook'
    elif pic == 'n':
        newString += 'knight'
    elif pic == 'b':
        newString += 'bishop'
    elif pic == 'q':
        newString += 'queen'
    elif pic == 'k':
        newString += 'king'

    return newString





pieces = []
# Adding pieces
for i in range(1, 17, 1):  # Pawns
    if i <= 8: # White
        newstr = 'Wp'
        pieces.append(Piece(newstr, i))
    else: # Black
        newstr = 'Bp'
        pieces.append(Piece(newstr, i - 8))

pieces.append(Piece('Wr', 1)) # Rooks
pieces.append(Piece('Wr', 2))
pieces.append(Piece('Br', 1))
pieces.append(Piece('Br', 2))

pieces.append(Piece('Wn', 1)) # Knights
pieces.append(Piece('Wn', 2))
pieces.append(Piece('Bn', 1))
pieces.append(Piece('Bn', 2))

pieces.append(Piece('Wb', 1)) # Bishops
pieces.append(Piece('Wb', 2))
pieces.append(Piece('Bb', 1))
pieces.append(Piece('Bb', 2))

pieces.append(Piece('Wq', 1)) # Kings and Queens
pieces.append(Piece('Wk', 1))
pieces.append(Piece('Bq', 1))
pieces.append(Piece('Bk', 1))


eventManager = {
    'stage': 0,         # Different stages: immobile(piece already moved), first piece selected, second selected
    'places': []
}



def draw():
    screen.clear()
    drawBoard()

    for x in range(len(eventManager['places'])):
        if x == 0:
            # print(pieces[eventManager['places'][0]])
            screen.draw.filled_rect(Rect((pieces[eventManager['places'][x]].x, pieces[eventManager['places'][x]].y), (cellSize, cellSize)), (247, 247, 0))

    # Draw the pieces
    for piece in pieces:
        piece.body = Actor(piece.parsedPiece, center=(piece.x+(cellSize/2), piece.y+(cellSize/2)))
        piece.body.draw()

def drawBoard():
    for rank in range(0, 8, 1):
        for file in range(0, 8, 1):
            newColour = None
            num = (file + (rank*8)) + rank
            if num % 2 == 0:
            #   print('True') # White
                newColour = LIGHTBLUE
            else:
            #   print('False') # Black
                newColour = DARKBLUE
            screen.draw.filled_rect(Rect((file*cellSize, rank*cellSize), (cellSize, cellSize)), newColour)

def on_mouse_down(pos):
    if eventManager['stage'] == 0 or eventManager['stage'] == 1:
        eventManager['stage'] += 1
        if eventManager['stage'] == 1:
            temp = (findIndex(pos[0], cellSize), findIndex(pos[1], cellSize))
            for piece in range(len(pieces)):
                if (pieces[piece].x == temp[0] * cellSize) and (pieces[piece].y == temp[1] * cellSize):
                    eventManager['places'].append(piece)
                    break
        else:
            eventManager['places'].append((findIndex(pos[0], cellSize), findIndex(pos[1], cellSize)))
            pieces[eventManager['places'][0]].x = eventManager['places'][1][0] * cellSize
            pieces[eventManager['places'][0]].y = eventManager['places'][1][1] * cellSize
            for pyce in range(len(pieces) - 1, -1, -1):
                if pieces[pyce] == pieces[eventManager['places'][0]]:
                    continue
                else:
                    if (pieces[pyce].x == pieces[eventManager['places'][0]].x) and (pieces[pyce].y == pieces[eventManager['places'][0]].y):
                        pieces.pop(pyce)
            clock.schedule(emptyEvs, 0.5)
            # eventManager['places'] = []
            eventManager['stage'] = 0

def findIndex(num1, num2):
    return math.floor(num1 / num2)

def emptyEvs():
    eventManager['places'] = []