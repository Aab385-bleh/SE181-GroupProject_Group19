# Filename: GameManager.py
# Description: Back-End to Chess Game Term Project
# Created: 8/17/2020
# Updated: 8/21/2020
# SE181 - Group 19
import socket
import copy

# Function: StartGame
# Description: Initializes Chess Board with starting positions
# Arguements:
# Return: moves[]
def startGame():
    startingBoard=[]
    #STANDARD BOARD
    #Square Structure -> [<piece>,<Moved Yet>] (0- not moved, 1- moved, 2- no piece)
    startingBoard.append([["r",0],[".",0],[".",0],[".",0],["k",0],[".",0],[".",0],["r",0]])
    #startingBoard.append([["r",0],["n",0],["b",0],["q",0],["k",0],["b",0],["n",0],["r",0]])
    startingBoard.append([["p",0],["p",0],["p",0],["p",0],["p",0],["p",0],["p",0],["p",0]])
    i = 0
    while i<4:
       startingBoard.append([[".",2],[".",2],[".",2],[".",2],[".",2],[".",2],[".",2],[".",2]])
       i+=1
    startingBoard.append([["P",0],["P",0],["P",0],["P",0],["P",0],["P",0],["P",0],["P",0]])
    #startingBoard.append([["R",0],["N",0],["B",0],["Q",0],["K",0],["B",0],["N",0],["R",0]])
    startingBoard.append([["R",0],[".",0],[".",0],[".",0],["K",0],[".",0],[".",0],["R",0]])
    return(startingBoard)

# Function: FindMoves
# Description: Determines all the legal moves that can be made for a given piece (Follows Piece Movement, Does Not Attack Own Piece)
# Arguements: board, currentPosX, currentPosY
# Return: moves[]
def findMoves(board, currentPosX, currentPosY):
    moves=[]

    if (board[currentPosX][currentPosY][0]) in ('p'):
        moves.append([currentPosX+1,currentPosY])
        if (board[currentPosX][currentPosY][1] == 0):   #If in Starting Position
            moves.append([currentPosX+2,currentPosY])
        if (currentPosY < 7 and board[currentPosX+1][currentPosY+1][0] != "."): #If attacking to left
            moves.append([currentPosX+1,currentPosY+1])
        if (currentPosY > 0 and board[currentPosX+1][currentPosY-1][0] != "."): #If attacking to Right
            moves.append([currentPosX+1,currentPosY-1])
    elif (board[currentPosX][currentPosY][0]) in ('P'):
        moves.append([currentPosX-1,currentPosY])
        if (board[currentPosX][currentPosY][1] == 0):   #If in Starting Position
            moves.append([currentPosX-2,currentPosY])
        if (currentPosY < 7 and board[currentPosX-1][currentPosY+1][0] != "."): #If attacking to Right
            moves.append([currentPosX-1,currentPosY+1])
        if (currentPosY > 0 and board[currentPosX-1][currentPosY-1][0] != "."): #If attacking to left
            moves.append([currentPosX-1,currentPosY-1])
    elif (board[currentPosX][currentPosY][0]) in ('r', 'R'):
        #Move Along X
        i=currentPosX
        while (i < 7):
            if (board[i+1][currentPosY][0] == "."):
                moves.append([i+1,currentPosY])
                i += 1
            else:
                moves.append([i+1,currentPosY])
                break
        i=currentPosX
        while (i > 0):
            if (board[i-1][currentPosY][0] == "."):
                moves.append([i-1,currentPosY])
                i -= 1
            else:
                moves.append([i-1,currentPosY])
                break
        #Move Along Y
        i=currentPosY
        while (i < 7):
            if (board[currentPosX][i+1][0] == "."):
                moves.append([currentPosX,i+1])
                i += 1
            else:
                moves.append([currentPosX,i+1])
                break
        i=currentPosY
        while (i > 0):
            if (board[currentPosX][i-1][0] == "."):
                moves.append([currentPosX,i-1])
                i -= 1
            else:
                moves.append([currentPosX,i-1])
                break
    elif (board[currentPosX][currentPosY][0]) in ('n', 'N'):
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
        i=0
        while (0 <= currentPosX + i < 7 and 0 <= currentPosY + i < 7):
            if (board[currentPosX + i + 1][currentPosY + i + 1][0] == "."):
                moves.append([currentPosX + i + 1,currentPosY + i + 1])
                i += 1
            else:
                moves.append([currentPosX + i + 1,currentPosY + i + 1])
                break
        i=0
        while (0 < currentPosX - i <= 7 and 0 <= currentPosY + i < 7):
            if (board[currentPosX - i - 1][currentPosY + i + 1][0] == "."):
                moves.append([currentPosX - i - 1,currentPosY + i + 1])
                i += 1
            else:
                moves.append([currentPosX - i - 1,currentPosY + i + 1])
                break
        i=0
        while (0 <= currentPosX + i < 7 and 0 < currentPosY - i <= 7):
            if (board[currentPosX + i + 1][currentPosY - i - 1][0] == "."):
                moves.append([currentPosX + i + 1,currentPosY - i - 1])
                i += 1
            else:
                moves.append([currentPosX + i + 1,currentPosY - i - 1])
                break
        i=0
        while (0 < currentPosX - i <= 7 and 0 < currentPosY - i <= 7):
            if (board[currentPosX - i - 1][currentPosY - i - 1][0] == "."):
                moves.append([currentPosX - i - 1,currentPosY - i - 1])
                i += 1
            else:
                moves.append([currentPosX - i - 1,currentPosY - i - 1])
                break
    elif (board[currentPosX][currentPosY][0]) in ('q', 'Q'):
        i=0
        while (0 <= currentPosX + i < 7 and 0 <= currentPosY + i < 7):
            if (board[currentPosX + i +1][currentPosY + i + 1][0] == "."):
                moves.append([currentPosX + i + 1,currentPosY + i + 1])
                i += 1
            else:
                moves.append([currentPosX + i + 1,currentPosY + i + 1])
                break
        i=0
        while (0 < currentPosX - i <= 7 and 0 <= currentPosY + i < 7):
            if (board[currentPosX - i - 1][currentPosY + i + 1][0] == "."):
                moves.append([currentPosX - i - 1,currentPosY + i + 1])
                i += 1
            else:
                moves.append([currentPosX - i - 1,currentPosY + i + 1])
                break
        i=0
        while (0 <= currentPosX + i < 7 and 0 < currentPosY - i <= 7):
            if (board[currentPosX + i + 1][currentPosY - i - 1][0] == "."):
                moves.append([currentPosX + i + 1,currentPosY - i - 1])
                i += 1
            else:
                moves.append([currentPosX + i + 1,currentPosY - i - 1])
                break
        i=0
        while (0 < currentPosX - i <= 7 and 0 < currentPosY - i <= 7):
            if (board[currentPosX - i - 1][currentPosY - i - 1][0] == "."):
                moves.append([currentPosX - i - 1,currentPosY - i - 1])
                i += 1
            else:
                moves.append([currentPosX - i - 1,currentPosY - i - 1])
                break
        #Move Forward/Backward
        i=currentPosX
        while (i < 7):
            if (board[i+1][currentPosY][0] == "."):
                moves.append([i+1,currentPosY])
                i += 1
            else:
                moves.append([i+1,currentPosY])
                break
        i=currentPosX
        while (i > 0):
            if (board[i-1][currentPosY][0] == "."):
                moves.append([i-1,currentPosY])
                i -= 1
            else:
                moves.append([i-1,currentPosY])
                break
        #Move Left/Right
        i=currentPosY
        while (i < 7):
            if (board[currentPosX][i+1][0] == "."):
                moves.append([currentPosX,i+1])
                i += 1
            else:
                moves.append([currentPosX,i+1])
                break
        i=currentPosY
        while (i > 0):
            if (board[currentPosX][i-1][0] == "."):
                moves.append([currentPosX,i-1])
                i -= 1
            else:
                moves.append([currentPosX,i-1])
                break
    elif (board[currentPosX][currentPosY][0]) in ('k', 'K'):
        if (currentPosX > 0):
            moves.append([currentPosX - 1,currentPosY])
            if (currentPosY > 0):
                moves.append([currentPosX - 1,currentPosY - 1])
            if (currentPosY < 7):
                moves.append([currentPosX - 1,currentPosY + 1])
        if (currentPosX < 7):
            moves.append([currentPosX + 1,currentPosY])
            if (currentPosY > 0):
                moves.append([currentPosX + 1,currentPosY - 1])
            if (currentPosY < 7):
                moves.append([currentPosX + 1,currentPosY + 1])
        if (currentPosY > 0):
            moves.append([currentPosX,currentPosY - 1])
        if (currentPosY < 7):
            moves.append([currentPosX ,currentPosY + 1])
        #Castling
        if (board[currentPosX][currentPosY][1] == 0):
            if(board[currentPosX][5][0] == '.' and board[currentPosX][6][0] == '.' and board[currentPosX][7][1] == 0): #add [curx,5] and [curX,6] cannot put king in check
                moves.append([currentPosX,2])
            if (board[currentPosX][3][0] == '.' and board[currentPosX][2][0] == '.' and board[currentPosX][1][0] == '.' and board[currentPosX][0][1] == 0): #add [curx,3] and [curX,2] cannot put king in check
                moves.append([currentPosX,6])
    return(moves)

# Function: FindAttacks
# Description: Determines all the legal attacks that can be made for a given piece on a board
# Arguements: board, currentPosX, currentPosY
# Return: attacks[]
def findAttacks(board, currentPosX, currentPosY):
    attacks=[]

    if (board[currentPosX][currentPosY][0]) in ('p'):
        if (currentPosY < 7 and board[currentPosX+1][currentPosY+1][0] != "."): #If attacking to left
            attacks.append([currentPosX+1,currentPosY+1])
        if (currentPosY > 0 and board[currentPosX+1][currentPosY-1][0] != "."): #If attacking to Right
            attacks.append([currentPosX+1,currentPosY-1])
    elif (board[currentPosX][currentPosY][0]) in ('P'):
        if (currentPosY < 7 and board[currentPosX-1][currentPosY+1] != "."): #If attacking to Right
            attacks.append([currentPosX-1,currentPosY+1])
        if (currentPosY > 0 and board[currentPosX-1][currentPosY-1] != "."): #If attacking to left
            attacks.append([currentPosX-1,currentPosY-1])
    elif (board[currentPosX][currentPosY][0]) in ('r', 'R'):
        #Move Along X
        i=currentPosX
        while (i < 7):
            if (board[i+1][currentPosY][0] == "."):
                attacks.append([i+1,currentPosY])
                i += 1
            else:
                attacks.append([i+1,currentPosY])
                break
        i=currentPosX
        while (i > 0):
            if (board[i-1][currentPosY][0] == "."):
                attacks.append([i-1,currentPosY])
                i -= 1
            else:
                attacks.append([i-1,currentPosY])
                break
        #Move Along Y
        i=currentPosY
        while (i < 7):
            if (board[currentPosX][i+1][0] == "."):
                attacks.append([currentPosX,i+1])
                i += 1
            else:
                attacks.append([currentPosX,i+1])
                break
        i=currentPosY
        while (i > 0):
            if (board[currentPosX][i-1][0] == "."):
                attacks.append([currentPosX,i-1])
                i -= 1
            else:
                attacks.append([currentPosX,i-1])
                break
    elif (board[currentPosX][currentPosY][0]) in ('n', 'N'):
        if ( currentPosX < 7 ):
            if ( currentPosY < 6 ):
                attacks.append([currentPosX+1,currentPosY+2])
            if ( currentPosY > 1 ):
                attacks.append([currentPosX+1,currentPosY-2])
        if ( currentPosX < 6 ):
            if ( currentPosY < 7 ):
                attacks.append([currentPosX+2,currentPosY+1])
            if ( currentPosY > 0 ):
                attacks.append([currentPosX+2,currentPosY-1])
        if ( currentPosX > 0):
            if ( currentPosY < 6 ):
                attacks.append([currentPosX-1,currentPosY+2])
            if ( currentPosY > 1 ):
                attacks.append([currentPosX-1,currentPosY-2])
        if ( currentPosX > 1 ):
            if ( currentPosY < 7 ):
                attacks.append([currentPosX-2,currentPosY+1])
            if ( currentPosY > 0 ):
                attacks.append([currentPosX-2,currentPosY-1])
    elif (board[currentPosX][currentPosY][0]) in ('b', 'B'):
        i=0
        while (0 < currentPosX + i < 7 and 0 < currentPosY + i < 7):
            if (board[currentPosX + i +1][currentPosY + i + 1][0] == "."):
                attacks.append([currentPosX + i + 1,currentPosY + i + 1])
                i += 1
            else:
                attacks.append([currentPosX + i + 1,currentPosY + i + 1])
                break
        i=0
        while (0 < currentPosX - i < 7 and 0 < currentPosY + i < 7):
            if (board[currentPosX - i - 1][currentPosY + i + 1][0] == "."):
                attacks.append([currentPosX - i - 1,currentPosY + i + 1])
                i += 1
            else:
                attacks.append([currentPosX - i - 1,currentPosY + i + 1])
                break
        i=0
        while (0 < currentPosX + i < 7 and 0 < currentPosY - i < 7):
            if (board[currentPosX + i + 1][currentPosY - i - 1][0] == "."):
                attacks.append([currentPosX + i + 1,currentPosY - i - 1])
                i += 1
            else:
                attacks.append([currentPosX + i + 1,currentPosY - i - 1])
                break
        i=0
        while (0 < currentPosX - i < 7 and 0 < currentPosY - i < 7):
            if (board[currentPosX - i - 1][currentPosY - i - 1][0] == "."):
                attacks.append([currentPosX - i - 1,currentPosY - i - 1])
                i += 1
            else:
                attacks.append([currentPosX - i - 1,currentPosY - i - 1])
                break
    elif (board[currentPosX][currentPosY][0]) in ('q', 'Q'):
        i=0
        while (0 < currentPosX + i < 7 and 0 < currentPosY + i < 7):
            if (board[currentPosX + i +1][currentPosY + i + 1][0] == "."):
                attacks.append([currentPosX + i + 1,currentPosY + i + 1])
                i += 1
            else:
                attacks.append([currentPosX + i + 1,currentPosY + i + 1])
                break
        i=0
        while (0 < currentPosX - i < 7 and 0 < currentPosY + i < 7):
            if (board[currentPosX - i - 1][currentPosY + i + 1][0] == "."):
                attacks.append([currentPosX - i - 1,currentPosY + i + 1])
                i += 1
            else:
                attacks.append([currentPosX - i - 1,currentPosY + i + 1])
                break
        i=0
        while (0 < currentPosX + i < 7 and 0 < currentPosY - i < 7):
            if (board[currentPosX + i + 1][currentPosY - i - 1][0] == "."):
                attacks.append([currentPosX + i + 1,currentPosY - i - 1])
                i += 1
            else:
                attacks.append([currentPosX + i + 1,currentPosY - i - 1])
                break
        i=0
        while (0 < currentPosX - i < 7 and 0 < currentPosY - i < 7):
            if (board[currentPosX - i - 1][currentPosY - i - 1][0] == "."):
                attacks.append([currentPosX - i - 1,currentPosY - i - 1])
                i += 1
            else:
                attacks.append([currentPosX - i - 1,currentPosY - i - 1])
                break
        #Move Forward/Backward
        i=currentPosX
        while (i < 7):
            if (board[i+1][currentPosY][0] == "."):
                attacks.append([i+1,currentPosY])
                i += 1
            else:
                attacks.append([i+1,currentPosY])
                break
        i=currentPosX
        while (i > 0):
            if (board[i-1][currentPosY][0] == "."):
                attacks.append([i-1,currentPosY])
                i -= 1
            else:
                attacks.append([i-1,currentPosY])
                break
        #Move Left/Right
        i=currentPosY
        while (i < 7):
            if (board[currentPosX][i+1][0] == "."):
                attacks.append([currentPosX,i+1])
                i += 1
            else:
                attacks.append([currentPosX,i+1])
                break
        i=currentPosY
        while (i > 0):
            if (board[currentPosX][i-1][0] == "."):
                attacks.append([currentPosX,i-1])
                i -= 1
            else:
                attacks.append([currentPosX,i-1])
                break
    elif (board[currentPosX][currentPosY][0]) in ('k', 'K'):
        if (currentPosX > 0):
            attacks.append([currentPosX - 1,currentPosY])
            if (currentPosY > 0):
                attacks.append([currentPosX - 1,currentPosY - 1])
            if (currentPosY < 7):
                attacks.append([currentPosX - 1,currentPosY + 1])
        if (currentPosX < 7):
            attacks.append([currentPosX + 1,currentPosY])
            if (currentPosY > 0):
                attacks.append([currentPosX + 1,currentPosY - 1])
            if (currentPosY < 7):
                attacks.append([currentPosX + 1,currentPosY + 1])
        if (currentPosY > 0):
            attacks.append([currentPosX,currentPosY - 1])
        if (currentPosY < 7):
            attacks.append([currentPosX ,currentPosY + 1])
    return(attacks)

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
def moveValidation(board, currentPosX, currentPosY, newPositionX,  newPositionY, player):
    #Make sure you are moving your piece
    if player == 'w':
        if board[currentPosX][currentPosY][0] in ('p','r','n','b','q','k','.'):
            return (False)

    if player == 'b':
        if board[currentPosX][currentPosY][0] in ('P','R','N','B','Q','K','.'):
            return (False)

    #Find Possible Moves/Attacks
    possibleMoves = findMoves(board, currentPosX, currentPosY)

    #Remove Attacks Against Own Pieces
    legalMoves = friendlyFire(board, currentPosX, currentPosY, possibleMoves)

    #Remove Spots that would put in check
    testCheckboard = makeMove(board, currentPosX, currentPosY, newPositionX, newPositionY)
    if (board[currentPosX][currentPosY][0].isupper()):
        if (isCheck(testCheckboard, 'w')):
            return(False)
    else:
        if (isCheck(testCheckboard, 'b')):
            return(False)

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
    updateBoard = copy.deepcopy(board)
    tmpPiece = updateBoard[currentPosX][currentPosY][0]
    updateBoard[currentPosX][currentPosY] = ['.',2]
    updateBoard[newPositionX][newPositionY] = [tmpPiece, 1]
    return(updateBoard)

# Function: IsCheck
# Description: Determine if a player is in Check
# Arguements: board, player
# Return: True/False
def isCheck(board, player):
    checkSquares=[]
    row=0
    col=0
    # Find if White in Check
    if player == 'w':
        while row < 8:
            while col < 8:
                if (board[row][col][0] in ['p','r','n','b','q']):
                    checkSquares.append(findAttacks(board, row, col ))
                col+=1
            row+=1
            col=0
        for check in checkSquares:
            for c in check:
                if (board[c[0]][c[1]][0] == 'K'):
                    return(True) #Is in Check
        return(False) #Is not in Check
    # Find if Black in Check
    if player == 'b':
        while row < 8:
            while col < 8:
                if (board[row][col][0] in ['P','R','N','B','Q']):
                    checkSquares.append(findAttacks(board, row, col))
                col+=1
            row+=1
            col=0
        for check in checkSquares:
            for c in check:
                if (board[c[0]][c[1]][0] == 'k'):
                    return(True) #Is in Check
        return(False) #Is not in Check

# Function: IsCheckMate
# Description: Determine if a player is in Checkmate given a board that has a player in check
# Arguements: board, player
# Return: True/False
def isCheckMate(board, player):
    possibleMoves = []
    currentBoard = copy.deepcopy(board)
    if (player == 'w'):
        # Can King move out of Check?
        row=0
        col=0
        while row < 8 and col < 8:
            if (board[row][col][0] in ['K']):
                possibleMoves = (findMoves(board, row, col ))
                break
            else:
                col+=1
            if col == 8 and row < 8:
                row+=1
                col=0
        legalMoves = friendlyFire(board, row, col, possibleMoves)
        testBoard = copy.deepcopy(currentBoard)
        for m in legalMoves:
            testMove = makeMove(testBoard, row, col, m[0], m[1])
            if (isCheck(testMove, player)):
                testBoard = copy.deepcopy(currentBoard)
            else:
                return(False) #Is not in Checkmate
        # Can Other Piece move out of Check?
        row=0
        col=0
        possibleMoves = []
        allies=[]
        while row < 8 and col < 8:
            if (board[row][col][0] in ['R','N','B','Q','P']):
                allies.append([row, col]) #Get location of Piece
                possibleMoves.append((findMoves(board, row, col ))) #Get Moves for that Piece
            col+=1
            if col == 8 and row < 8:
                row+=1
                col=0
        testBoard = copy.deepcopy(currentBoard)
        i = 0
        while i < len(allies):
            for m in possibleMoves[i]:
                print(m)
                testMove = makeMove(testBoard, allies[i][0], allies[i][1], m[0], m[1])
                if (isCheck(testMove, player)):
                    testBoard = copy.deepcopy(currentBoard)
                else:
                    return(False) #Is not in Checkmate
         #Is in Checkmate
        return(True)

# Function: PawnPromotion
# Description: Promote Pawn When Reaching Other Side Of Board
# Arguements: board, pawnPosX, pawnPosY, newPiece
# Return: updateBoard
def pawnPromotion(board, pawnPosX, pawnPosY, newPiece):
    updateBoard = board
    updateBoard[pawnPosX][pawnPosY] = [newPiece,1]
    return(updateBoard)

# Function: simpleBoard
# Description: Given Board[row][column][square] simplify to Board[row][column] and print
# Arguements: board
# Return: simpleBoard
def simpleBoard(board,player):
    simpleB = []
    r = 0
    c = 0
    while r < 8:
        simpleR=[]
        while c < 8:
            if player == 'w':
                simpleR.append(board[r][c][0])
            elif player == 'b':
                simpleR.append(board[7-r][c][0])
            c+=1
        c=0
        r+=1
        simpleB.append(simpleR)

    for row in simpleB:
        print(row)

# Function: gameManager
# Description: Runs the Game (Main Function)
# Arguements: None
# Return: None
def gameManager():
    winner = 'none'
    playerTurn = 'w'

    #Start Game
    gameboard = startGame()

    while winner == 'none':
        vMove = False
        simpleBoard(gameboard,'w')#Print Board
        if playerTurn == 'w':
            print("Turn: White")
        if playerTurn == 'b':
            print("Turn: Black")
        while vMove != True:
            # Take in Move (curX, curY, newX, newY)
            txt = input("Make Your Move:")
            move=txt.split()
            curX=int(move[0])
            curY=int(move[1])
            newX=int(move[2])
            newY=int(move[3])
            # Check if Move Valid
            if (moveValidation(gameboard,curX,curY,newX,newY,playerTurn) == True):
                gameboard = makeMove(gameboard, curX, curY, newX, newY)
                vMove = True
                #Handle Castling
                if (gameboard[newX][newY][0] in ('k')):
                    if curX == 0 and curY == 4 and newX == 0:
                        if newY == 2:
                            #Castle Queen's Side
                            gameboard = makeMove(gameboard, 0, 0, 0, 3)
                        elif newY == 6:
                            #Castle King Side
                            gameboard = makeMove(gameboard, 0, 7, 0, 5)
                elif (gameboard[newX][newY][0] in ('K')):
                    if curX == 7 and curY == 4 and newX == 7:
                        if newY == 2:
                            #Castle Queen's Side
                            gameboard = makeMove(gameboard, 7, 0, 7, 3)
                        elif newY == 6:
                            #Castle King Side
                            gameboard = makeMove(gameboard, 7, 7, 7, 5)

            else:
                print("Invalid Move!")

        #Check if Pawn Promotion
        for c in range(8):
            if ( gameboard[0][c] == ['P',1]):
                newPiece = input('Pawn Promotion! Choose Your Piece (R,N,B,Q):')
                gameboard=pawnPromotion(gameboard,0,c,newPiece)
        for c in range(8):
            if (gameboard[7][c] == ['p',1] ):
                newPiece = input('Pawn Promotion! Choose Your Piece (r,n,b,q):')
                gameboard=pawnPromotion(gameboard,7,c,newPiece)

        #Check for Check/CheckMate
        if playerTurn == 'w':
            if (isCheck(gameboard, 'b')):
                if (isCheckMate(gameboard, 'b')):
                    winner = 'White'
                    print("Winner: ", winner)
                else:
                    print("Check")
        elif playerTurn == 'b':
            if (isCheck(gameboard, 'w')):
                if (isCheckMate(gameboard, 'w')):
                    winner = 'Black'
                    print("Winner: ", winner)
                else:
                    print("Check")
        # Change Player Turn
        if playerTurn == 'w':
            playerTurn = 'b'
        else:
            playerTurn = 'w'

############################################################################
gameManager() #This Line Runs the game
#gameboard = startGame()
#print(findMoves(gameboard,0,4))
#print(findMoves(gameboard,7,4))