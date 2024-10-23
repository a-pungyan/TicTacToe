

#global variables

import random
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
currentPLayer = "X"
winner = None
gameRunning = True

#printing the game board


def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
printBoard(board)

    
#take player input

def playerInput(board): 
    inp = int(input("Enter a number 1-9: "))
#checks if player's input number is valid 1-9, and if the input contains a dash, meaning a player 
#hasn't played that spot yet
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPLayer
    else:
        print("Oops, that spot is taken!")

#check for win or tie
#checking for horizontal win


def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

#checking for vertical win
def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return 
        
#checking for diagonal win

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

#checking for tie

def checkTie(board):
    if "-" not in board:
        printBoard(board)
        print("It's a tie!")
        gameRunning = False 

#switch player

def switchPlayer():
    global currentPLayer
    if currentPLayer == "X":
        currentPLayer = "O"
    else:
        currentPLayer = "X"

# computer

def computer(board):
    while currentPLayer == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


def checkWin():
    if checkDiagonal(board) or checkHorizontal(board) or checkVertical(board):
        print(f"The Winner is {winner}!")

#check for win or tie again

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)
