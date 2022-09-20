import re

def main():
    f = open("puzzle.txt", "r")
    g = open("puzzle 2.txt", "w")
    for x in f:
        if(contains(x,"equality") and threefold(x)):
            g.write("lichess.org/training/"+x[0:5]+"\n")

def threefold(x):
    n = 0
    for i in range(len(x)):
        if x[i] == ',':
            n+=1
            if n == 2:
                start = i
            if n==3:
                end = i
    x = x[start+1:end]
    for i in range(4,len(x)-7,10):
        if x[i] == " ":
            if(x[i+1:i+5]==x[-4:]):
                return True
    return False

def countMoves(x):
    n = 0
    for i in range(len(x)):
        if x[i] == ',':
            n+=1
            if n == 2:
                start = i
            if n==3:
                end = i
    x = x[start+1:end]
    n = 0
    for i in range(len(x)):
        if x[i] == ' ':
            n+=1
    return (n+1)//2

def halfMoves(x):
    n = 0
    for i in range(len(x)):
        if x[i] == ' ':
            n+=1
            if n == 4:
                start = i
            if n==5:
                end = i
    return int(x[start+1:end])
    

def popularity(x):
    n = 0
    for i in range(len(x)):
        if x[i] == ',':
            n+=1
            if n == 5:
                start = i
            if n==6:
                end = i
    return int(x[start+1:end])

def moves(x):
    n = 0
    for i in range(len(x)):
        if x[i] == ',':
            n+=1
            if n == 2:
                start = i
            if n==3:
                end = i
    return x[start+1:end]


def numberOfPlays(x):
    n = 0
    for i in range(len(x)):
        if x[i] == ',':
            n+=1
            if n == 6:
                start = i
            if n==7:
                end = i
    return int(x[start+1:end])

def contains(x, regex):
    return len(re.findall(regex,x))>0

def numberOfPieces(x):
    end = x.index(" ")
    y = x[6:end]
    y = re.sub("[1-8]|\/","",y)
    return len(y)

def fenUpdate(fen, moves):
    moves = " "+moves+" "
    fen = re.sub("2","11",fen)
    fen = re.sub("3","111",fen)
    fen = re.sub("4","1111",fen)
    fen = re.sub("5","11111",fen)
    fen = re.sub("6","111111",fen)
    fen = re.sub("7","1111111",fen)
    fen = re.sub("8","11111111",fen)
    color = fen[73]
    fen = fen[0:71]
    for i in range(len(moves)-4):
        if(moves[i]==" "):
            if(moves[i+5]==" "):
                fen = doMove(fen,moves[i+1:i+5])
            elif(moves[i+5]==" "):
                fen = doMove(fen,moves[i+1:i+6])
    if color == "w":
        fen = fen+" b - - 0 1"
    else:
        fen = fen+" w - - 0 1"
    fen = re.sub("11111111","8",fen)
    fen = re.sub("1111111","7",fen)
    fen = re.sub("111111","6",fen)
    fen = re.sub("11111","5",fen)
    fen = re.sub("1111","4",fen)
    fen = re.sub("111","3",fen)
    fen = re.sub("11","2",fen)
    return fen

def doMove(board, move):
    print(move)
    fromSquare = move[0:2]
    toSquare = move[2:4]
    fromSquare = (ord(fromSquare[0])-96)+9*(8-int(fromSquare[1]))-1
    toSquare = (ord(toSquare[0])-96)+9*(8-int(toSquare[1]))-1
    promotion = None
    if len(move)>4:
        promotion = move[4]
    piece = board[fromSquare]
    board = board[:fromSquare]+"1"+board[fromSquare+1:]
    if promotion == None:
        board = board[:toSquare]+piece+board[toSquare+1:]
    else:
        board = board[:toSquare]+promotion+board[toSquare+1:]
    return board
    

main()
'''
        x = re.sub("\,https\:\/\/lichess\.org\/.+\,",",",x)
        x = re.sub("\,(([0-9]|\-)*\,)*",",",x)
        x = re.sub("\,(([a-h][1-8][a-z]?){2}\s?)*\,",",",x)
        x = re.sub("\,.*?\/.*?\/.*?[0-9]\,",",",x)
        x = re.sub("\,([a-zA-Z]|[0-9]|\_|\-)*?\n","\n",x)
        
        x = re.sub("opening|middlegame|endgame|rookEndgame|bishopEndgame|pawnEndgame|knightEndgame|queenEndgame|queenRookEndgame","",x)
        x = re.sub("advancedPawn|attackingF2F7|attraction|capturingDefender|discoveredAttack|doubleCheck|exposedKing|fork|hangingPiece|kingsideAttack|pin|queensideAttack|sacrifice|skewer|trappedPiece","",x)
        x = re.sub("attraction|clearance|defensiveMove|deflection|interference|intermezzo|xRayAttack|zugzwang","",x)
        x = re.sub("mateIn1|mateIn2|mateIn3|mateIn4|mateIn5|anastasiaMate|arabianMate|backRankMate|bodenMate|doubleBishopMate|dovetailMate|hookMate|smotheredMate","",x)
        x = re.sub("castling|enPassant|promotion|underPromotion|equality|advantage|crushing|oneMove|short|long|veryLong|master|VsMaster|superGM","",x)
        x = re.sub(" ","",x)
        x = re.sub("matequietMove","AAAAAAA",x)
        x = re.sub("mate|quietMove","",x)
        if(len(x)>2 and x[-2] != ','):
            g.write(x)
        '''
