# Initialize Chess Board
# Initialize Pieces
board1 = []

#STANDARD BOARD
#Square Structure -> [<piece>,<Moved Yet>]
board1.append([["r",0],["n",0],["b",0],["q",0],["k",0],["b",0],["n",0],["r",0]])
board1.append([["p",0],["p",0],["p",0],["p",0],["p",0],["p",0],["p",0],["p",0]])
for n in range(4):
   board1.append([[".",0] *8])
board1.append([["P",0],["P",0],["P",0],["P",0],["P",0],["P",0],["P",0],["P",0]])
board1.append([["R",0],["N",0],["B",0],["Q",0],["K",0],["B",0],["N",0],["R",0]])

#NOT STANDARD BOARD

#board1.append([[".",0],[".",0],[".",0],[".",0],[".",0],[".",0],[".",0],[".",0]])
#board1.append(['.','.','.','.','.','.','.','.'])
#board1.append(['.','.','.','.','k','.','.','.'])
#board1.append(['.','.','.','.','.','p','.','.'])
#board1.append(['.','.','.','r','k','.','r','.'])
#board1.append(['.','.','.','.','k','.','.','.'])
#board1.append(['.','.','p','.','.','.','p','.'])
#board1.append(['.','.','.','.','.','.','.','.'])


def moveValidation(board, currentPosX, currentPosY, newPositionX,  newPositionY):
    legalMoves=[]

    if (board[currentPosX][currentPosY][0]) in ('p'):
        legalMoves.append([currentPosX+1,currentPosY])
        if (currentPosX == 1):   #If in Starting Position
            legalMoves.append([currentPosX+2,currentPosY])
        if (currentPosY < 7 and board[currentPosX+1][currentPosY+1] != "."): #If attacking to left
            legalMoves.append([currentPosX+1,currentPosY+1])
        if (currentPosY > 0 and board[currentPosX+1][currentPosY-1] != "."): #If attacking to Right
            legalMoves.append([currentPosX+1,currentPosY-1])
    elif (board[currentPosX][currentPosY][0]) in ('P'):
        legalMoves.append([currentPosX-1,currentPosY])
        if (currentPosX == 6):   #If in Starting Position
            legalMoves.append([currentPosX-2,currentPosY])
        if (currentPosY < 7 and board[currentPosX-1][currentPosY+1] != "."): #If attacking to Right
            legalMoves.append([currentPosX-1,currentPosY+1])
        if (currentPosY > 0 and board[currentPosX-1][currentPosY-1] != "."): #If attacking to left
            legalMoves.append([currentPosX-1,currentPosY-1])
    elif (board[currentPosX][currentPosY][0]) in ('r', 'R'):
        print("rook")
        #Move Along X
        i=currentPosX
        while (i < 7):
            if (board[i+1][currentPosY] == "."):
                legalMoves.append([i+1,currentPosY])
                i += 1
            else:
                legalMoves.append([i+1,currentPosY])
                break
        i=currentPosX
        while (i > 0):
            if (board[i-1][currentPosY] == "."):
                legalMoves.append([i-1,currentPosY])
                i -= 1
            else:
                legalMoves.append([i-1,currentPosY])
                break
        #Move Along Y
        i=currentPosY
        while (i < 7):
            if (board[currentPosX][i+1] == "."):
                legalMoves.append([currentPosX,i+1])
                i += 1
            else:
                legalMoves.append([currentPosX,i+1])
                break
        i=currentPosY
        while (i > 0):
            if (board[currentPosX][i-1] == "."):
                legalMoves.append([currentPosX,i-1])
                i -= 1
            else:
                legalMoves.append([currentPosX,i-1])
                break
    elif (board[currentPosX][currentPosY][0]) in ('n', 'N'):
        print("knight")
        if ( currentPosX < 7 ):
            if ( currentPosY < 6 ):
                legalMoves.append([currentPosX+1,currentPosY+2])
            if ( currentPosY > 1 ):
                legalMoves.append([currentPosX+1,currentPosY-2])
        if ( currentPosX < 6 ):
            if ( currentPosY < 7 ):
                legalMoves.append([currentPosX+2,currentPosY+1])
            if ( currentPosY > 0 ):
                legalMoves.append([currentPosX+2,currentPosY-1])
        if ( currentPosX > 0):
            if ( currentPosY < 6 ):
                legalMoves.append([currentPosX-1,currentPosY+2])
            if ( currentPosY > 1 ):
                legalMoves.append([currentPosX-1,currentPosY-2])
        if ( currentPosX > 1 ):
            if ( currentPosY < 7 ):
                legalMoves.append([currentPosX-2,currentPosY+1])
            if ( currentPosY > 0 ):
                legalMoves.append([currentPosX-2,currentPosY-1])
    elif (board[currentPosX][currentPosY][0]) in ('b', 'B'):
        print("bishop")
        i=0
        while (0 < currentPosX + i < 7 and 0 < currentPosY + i < 7):
            if (board[currentPosX + i +1][currentPosY + i + 1] == "."):
                legalMoves.append([currentPosX + i + 1,currentPosY + i + 1])
                i += 1
            else:
                legalMoves.append([currentPosX + i + 1,currentPosY + i + 1])
                break
        i=0
        while (0 < currentPosX - i < 7 and 0 < currentPosY + i < 7):
            if (board[currentPosX - i - 1][currentPosY + i + 1] == "."):
                legalMoves.append([currentPosX - i - 1,currentPosY + i + 1])
                i += 1
            else:
                legalMoves.append([currentPosX - i - 1,currentPosY + i + 1])
                break
        i=0
        while (0 < currentPosX + i < 7 and 0 < currentPosY - i < 7):
            if (board[currentPosX + i + 1][currentPosY - i - 1] == "."):
                legalMoves.append([currentPosX + i + 1,currentPosY - i - 1])
                i += 1
            else:
                legalMoves.append([currentPosX + i + 1,currentPosY - i - 1])
                break
        i=0
        while (0 < currentPosX - i < 7 and 0 < currentPosY - i < 7):
            if (board[currentPosX - i - 1][currentPosY - i - 1] == "."):
                legalMoves.append([currentPosX - i - 1,currentPosY - i - 1])
                i += 1
            else:
                legalMoves.append([currentPosX - i - 1,currentPosY - i - 1])
                break
    elif (board[currentPosX][currentPosY][0]) in ('q', 'Q'):
        print("queen")
        i=0
        while (0 < currentPosX + i < 7 and 0 < currentPosY + i < 7):
            if (board[currentPosX + i +1][currentPosY + i + 1] == "."):
                legalMoves.append([currentPosX + i + 1,currentPosY + i + 1])
                i += 1
            else:
                legalMoves.append([currentPosX + i + 1,currentPosY + i + 1])
                break
        i=0
        while (0 < currentPosX - i < 7 and 0 < currentPosY + i < 7):
            if (board[currentPosX - i - 1][currentPosY + i + 1] == "."):
                legalMoves.append([currentPosX - i - 1,currentPosY + i + 1])
                i += 1
            else:
                legalMoves.append([currentPosX - i - 1,currentPosY + i + 1])
                break
        i=0
        while (0 < currentPosX + i < 7 and 0 < currentPosY - i < 7):
            if (board[currentPosX + i + 1][currentPosY - i - 1] == "."):
                legalMoves.append([currentPosX + i + 1,currentPosY - i - 1])
                i += 1
            else:
                legalMoves.append([currentPosX + i + 1,currentPosY - i - 1])
                break
        i=0
        while (0 < currentPosX - i < 7 and 0 < currentPosY - i < 7):
            if (board[currentPosX - i - 1][currentPosY - i - 1] == "."):
                legalMoves.append([currentPosX - i - 1,currentPosY - i - 1])
                i += 1
            else:
                legalMoves.append([currentPosX - i - 1,currentPosY - i - 1])
                break
        #Move Forward/Backward
        i=currentPosX
        while (i < 7):
            if (board[i+1][currentPosY] == "."):
                legalMoves.append([i+1,currentPosY])
                i += 1
            else:
                legalMoves.append([i+1,currentPosY])
                break
        i=currentPosX
        while (i > 0):
            if (board[i-1][currentPosY] == "."):
                legalMoves.append([i-1,currentPosY])
                i -= 1
            else:
                legalMoves.append([i-1,currentPosY])
                break
        #Move Left/Right
        i=currentPosY
        while (i < 7):
            if (board[currentPosX][i+1] == "."):
                legalMoves.append([currentPosX,i+1])
                i += 1
            else:
                legalMoves.append([currentPosX,i+1])
                break
        i=currentPosY
        while (i > 0):
            if (board[currentPosX][i-1] == "."):
                legalMoves.append([currentPosX,i-1])
                i -= 1
            else:
                legalMoves.append([currentPosX,i-1])
                break
    elif (board[currentPosX][currentPosY][0]) in ('k', 'K'):
        print("king")
        legalMoves.append([currentPosX + 1,currentPosY + 1])
        legalMoves.append([currentPosX ,currentPosY + 1])
        legalMoves.append([currentPosX + 1,currentPosY])
        legalMoves.append([currentPosX - 1,currentPosY + 1])
        legalMoves.append([currentPosX + 1,currentPosY - 1])
        legalMoves.append([currentPosX,currentPosY - 1])
        legalMoves.append([currentPosX - 1,currentPosY])
        legalMoves.append([currentPosX - 1,currentPosY - 1])
    print(legalMoves)

def makeMove (board, currentPosX, currentPosY, newPositionX,  newPositionY):
    print("Move Made")
    #Update board
    #Update Piece Move Yet

def sendBoard (board):
    print("Board Sent to Client")

# General
    # If new position is occupied by own Piece
        #illegal
    # Else
        # Pawn
            # If blocked?
                # Illegal
            # Else
                # If starting position:
                    # If attacking:
                        # [x+1][y+1] or [x-1][y+1]
                    # Else:
                        # [x][y+1] or [x][y+2]
                # Else
                    # If attacking
                        # If En Passant
                            # [x+1][y] or [x-1][y]
                        # Else
                            # [x+1][y+1]
                    # Else
                        # [x][y+1]

        # Rook
            #[x+n][y] or [x-n][y] or [x][y+n][]

        # Knight
            # [x+2][y+1] or [x+2][y-1] or [x-2][y+1] or [x-2][y-1] or [x+1][y+2] or [x-1][y+2] or [x+1][y-2] or [x-1][y-2]

        # Bishop
        # Queen
        # King
#############################################################################
x=0
y=0
moveValidation(board1, x,y,1,1)

#print(board[x][y])
