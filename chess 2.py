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
