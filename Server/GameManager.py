
# Function: StartGame
# Description: Initializes Chess Board with starting positions
# Arguements:
# Return: moves[]
def startGame():
    startingBoard=[];
    #STANDARD BOARD
    #Square Structure -> [<piece>,<Moved Yet>] (0- not moved, 1- moved, 2- no piece)
    startingBoard.append([["r",0],["n",0],["b",0],["q",0],["k",0],["b",0],["n",0],["r",0]])
    startingBoard.append([["p",0],["p",0],["p",0],["p",0],["p",0],["p",0],["p",0],["p",0]])
    for n in range(4):
       startingBoard.append([[".",0],[".",0],[".",0],[".",0],[".",0],[".",0],[".",0],[".",0]])
    startingBoard.append([["P",0],["P",0],["P",0],["P",0],["P",0],["P",0],["P",0],["P",0]])
    startingBoard.append([["R",0],["N",0],["B",0],["Q",0],["K",0],["B",0],["N",0],["R",0]])
    return(startingBoard)

# Function: Findmoves
# Description: Determines all the legal moves that can be made for a given piece (Follows Piece Movement, Does Not Attack Own Piece)
# Arguements: board, currentPosX, currentPosY
# Return: moves[]
def findmoves(board, currentPosX, currentPosY):
    moves=[]

    if (board[currentPosX][currentPosY][0]) in ('p'):
        moves.append([currentPosX+1,currentPosY])
        if (board[currentPosX][currentPosY][1] == 0):   #If in Starting Position
            moves.append([currentPosX+2,currentPosY])
        if (currentPosY < 7 and board[currentPosX+1][currentPosY+1] != "."): #If attacking to left
            moves.append([currentPosX+1,currentPosY+1])
        if (currentPosY > 0 and board[currentPosX+1][currentPosY-1] != "."): #If attacking to Right
            moves.append([currentPosX+1,currentPosY-1])
    elif (board[currentPosX][currentPosY][0]) in ('P'):
        moves.append([currentPosX-1,currentPosY])
        if (board[currentPosX][currentPosY][1] == 0):   #If in Starting Position
            moves.append([currentPosX-2,currentPosY])
        if (currentPosY < 7 and board[currentPosX-1][currentPosY+1] != "."): #If attacking to Right
            moves.append([currentPosX-1,currentPosY+1])
        if (currentPosY > 0 and board[currentPosX-1][currentPosY-1] != "."): #If attacking to left
            moves.append([currentPosX-1,currentPosY-1])
    elif (board[currentPosX][currentPosY][0]) in ('r', 'R'):
        print("rook")
        #Move Along X
        i=currentPosX
        while (i < 7):
            if (board[i+1][currentPosY] == "."):
                moves.append([i+1,currentPosY])
                i += 1
            else:
                moves.append([i+1,currentPosY])
                break
        i=currentPosX
        while (i > 0):
            if (board[i-1][currentPosY] == "."):
                moves.append([i-1,currentPosY])
                i -= 1
            else:
                moves.append([i-1,currentPosY])
                break
        #Move Along Y
        i=currentPosY
        while (i < 7):
            if (board[currentPosX][i+1] == "."):
                moves.append([currentPosX,i+1])
                i += 1
            else:
                moves.append([currentPosX,i+1])
                break
        i=currentPosY
        while (i > 0):
            if (board[currentPosX][i-1] == "."):
                moves.append([currentPosX,i-1])
                i -= 1
            else:
                moves.append([currentPosX,i-1])
                break
    elif (board[currentPosX][currentPosY][0]) in ('n', 'N'):
        print("knight")
        if ( currentPosX < 7 ):
            if ( currentPosY < 6 ):
                moves.append([currentPosX+1,currentPosY+2])
            if ( currentPosY > 1 ):
                moves.append([currentPosX+1,currentPosY-2])
        if ( currentPosX < 6 ):
            if ( currentPosY < 7 ):
                moves.append([currentPosX+2,currentPosY+1])
            if ( currentPosY > 0 ):
                moves.append([currentPosX+2,currentPosY-1])
        if ( currentPosX > 0):
            if ( currentPosY < 6 ):
                moves.append([currentPosX-1,currentPosY+2])
            if ( currentPosY > 1 ):
                moves.append([currentPosX-1,currentPosY-2])
        if ( currentPosX > 1 ):
            if ( currentPosY < 7 ):
                moves.append([currentPosX-2,currentPosY+1])
            if ( currentPosY > 0 ):
                moves.append([currentPosX-2,currentPosY-1])
    elif (board[currentPosX][currentPosY][0]) in ('b', 'B'):
        print("bishop")
        i=0
        while (0 < currentPosX + i < 7 and 0 < currentPosY + i < 7):
            if (board[currentPosX + i +1][currentPosY + i + 1] == "."):
                moves.append([currentPosX + i + 1,currentPosY + i + 1])
                i += 1
            else:
                moves.append([currentPosX + i + 1,currentPosY + i + 1])
                break
        i=0
        while (0 < currentPosX - i < 7 and 0 < currentPosY + i < 7):
            if (board[currentPosX - i - 1][currentPosY + i + 1] == "."):
                moves.append([currentPosX - i - 1,currentPosY + i + 1])
                i += 1
            else:
                moves.append([currentPosX - i - 1,currentPosY + i + 1])
                break
        i=0
        while (0 < currentPosX + i < 7 and 0 < currentPosY - i < 7):
            if (board[currentPosX + i + 1][currentPosY - i - 1] == "."):
                moves.append([currentPosX + i + 1,currentPosY - i - 1])
                i += 1
            else:
                moves.append([currentPosX + i + 1,currentPosY - i - 1])
                break
        i=0
        while (0 < currentPosX - i < 7 and 0 < currentPosY - i < 7):
            if (board[currentPosX - i - 1][currentPosY - i - 1] == "."):
                moves.append([currentPosX - i - 1,currentPosY - i - 1])
                i += 1
            else:
                moves.append([currentPosX - i - 1,currentPosY - i - 1])
                break
    elif (board[currentPosX][currentPosY][0]) in ('q', 'Q'):
        print("queen")
        i=0
        while (0 < currentPosX + i < 7 and 0 < currentPosY + i < 7):
            if (board[currentPosX + i +1][currentPosY + i + 1] == "."):
                moves.append([currentPosX + i + 1,currentPosY + i + 1])
                i += 1
            else:
                moves.append([currentPosX + i + 1,currentPosY + i + 1])
                break
        i=0
        while (0 < currentPosX - i < 7 and 0 < currentPosY + i < 7):
            if (board[currentPosX - i - 1][currentPosY + i + 1] == "."):
                moves.append([currentPosX - i - 1,currentPosY + i + 1])
                i += 1
            else:
                moves.append([currentPosX - i - 1,currentPosY + i + 1])
                break
        i=0
        while (0 < currentPosX + i < 7 and 0 < currentPosY - i < 7):
            if (board[currentPosX + i + 1][currentPosY - i - 1] == "."):
                moves.append([currentPosX + i + 1,currentPosY - i - 1])
                i += 1
            else:
                moves.append([currentPosX + i + 1,currentPosY - i - 1])
                break
        i=0
        while (0 < currentPosX - i < 7 and 0 < currentPosY - i < 7):
            if (board[currentPosX - i - 1][currentPosY - i - 1] == "."):
                moves.append([currentPosX - i - 1,currentPosY - i - 1])
                i += 1
            else:
                moves.append([currentPosX - i - 1,currentPosY - i - 1])
                break
        #Move Forward/Backward
        i=currentPosX
        while (i < 7):
            if (board[i+1][currentPosY] == "."):
                moves.append([i+1,currentPosY])
                i += 1
            else:
                moves.append([i+1,currentPosY])
                break
        i=currentPosX
        while (i > 0):
            if (board[i-1][currentPosY] == "."):
                moves.append([i-1,currentPosY])
                i -= 1
            else:
                moves.append([i-1,currentPosY])
                break
        #Move Left/Right
        i=currentPosY
        while (i < 7):
            if (board[currentPosX][i+1] == "."):
                moves.append([currentPosX,i+1])
                i += 1
            else:
                moves.append([currentPosX,i+1])
                break
        i=currentPosY
        while (i > 0):
            if (board[currentPosX][i-1] == "."):
                moves.append([currentPosX,i-1])
                i -= 1
            else:
                moves.append([currentPosX,i-1])
                break
    elif (board[currentPosX][currentPosY][0]) in ('k', 'K'):
        print("king")
        moves.append([currentPosX + 1,currentPosY + 1])
        moves.append([currentPosX ,currentPosY + 1])
        moves.append([currentPosX + 1,currentPosY])
        moves.append([currentPosX - 1,currentPosY + 1])
        moves.append([currentPosX + 1,currentPosY - 1])
        moves.append([currentPosX,currentPosY - 1])
        moves.append([currentPosX - 1,currentPosY])
        moves.append([currentPosX - 1,currentPosY - 1])
        #Castling
        if (board[currentPosX][currentPosY][1] == 0):
            if(board[currentPosX][5][0] == '.' and board[currentPosX][6][0] == '.' and board[currentPosX][0][1] == 0): #add [curx,5] and [curX,6] cannot put king in check
                moves.append([currentPosX,2])
            if (board[currentPosX][3][0] == '.' and board[currentPosX][2][0] == '.' and board[currentPosX][7][1] == 0): #add [curx,3] and [curX,2] cannot put king in check
                moves.append([currentPosX,6])
    return(moves)

# Function: FriendlyFire
# Description: Determines if an attack is being made against a player's own piece
# Arguements: board, currentPosX, currentPosY, possibleMoves
# Return: moves[]
def friendlyFire(board, currentPosX, currentPosY, possibleMoves):
    moves = []
    for n in possibleMoves:
        if (board[n[0]][n[1]][0] == '.' or board[currentPosX][currentPosY][0].isupper() != board[n[0]][n[1]][0].isupper()):
            moves.append(n)
    return (moves)

# Function: MoveValidation
# Description: Checks for Legal Move (Follows Piece Movement, Does Not Attack Own Piece)
# Arguements: board, currentPosX, currentPosY, newPositionX, newPositionY
# Return: True/False
def moveValidation(board, currentPosX, currentPosY, newPositionX,  newPositionY):
    #Find Possible Moves/Attacks
    possibleMoves = findmoves(board, currentPosX, currentPosY)

    #Remove Attacks Against Own Pieces
    legalMoves = friendlyFire(board, currentPosX, currentPosY, possibleMoves)

    #Checks if New Position is Valid
    for n in legalMoves:
        if (newPositionX == n[0] and newPositionY == n[1]):
            return(True) #Move Accepted
    #Move Illegal
    return(False)

# Function: MakeMove
# Description: Moves the Piece(s) From One Location on the Board to Another
# Arguements:
# Return: updateBoard
def makeMove (board, currentPosX, currentPosY, newPositionX,  newPositionY):
    print("Move Made")
    #Update board
    #Update Piece Move Yet element
    return(updateBoard)

# Function: IsCheck
# Description: Determine if a player is in Check
# Arguements: board
# Return: True/False
def isCheck(board):
    return(True) #Is in Check
    return(False) #Is not in Check

# Function: PawnPromotion
# Description: Promote Pawn When Reaching Other Side Of Board
# Arguements: board, pawnPosX, pawnPosY, newPiece
# Return: updateBoard
def pawnPromotion(board, pawnPosX, pawnPosY, newPiece):
    updateBoard = board
    updateBoard[pawnPosX][pawnPosY] = [newPiece,1]
    return(updateBoard)

# Function: SendBoard
# Description: Send Board to Client
# Arguements:
# Return: Error Code
def sendBoard (board):
    if ('P' in board[1] or 'p' in board[7]):
        print("Pawn Promotion Sent")
        #Send Board and wait for response
        #Swap Pawn
        gameboard=pawnPromotion(gameboard,pawnPosX,pawnPosY,newPiece)
        #Send new Board
    else:
        print("Board Sent to Client")

#############################################################################
#Test Code
gameboard = startGame();
print(gameboard)
gameboard=pawnPromotion(gameboard,1,0,'B')
print(gameboard)
x=0
y=1


#moveValidation(gameboard, x,y,2,3)
