class Piece:
    def __init__(self, pieceInfo):
        self.x = findPos(pieceInfo)[0]
        self.y = findPos(pieceInfo)[1]
        self.parsedPiece = parsePiece(pieceInfo)
        self.body = Actor(self.parsedPiece)

def findPos(piece):
    return (0, 0)

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