import random
import math
import numpy as np

def check_move(board, turn, col, pop):
    # implement your function here
    if pop == False:
        if board[0 , col] == 0:
            return True
        else:
            return False
    elif pop == True:
        if board[rows -1, col] == 0:
            return False
        else:
            return True

def apply_move(board, turn, col, pop):
    # implement your function here
    if pop == False:
        board[poprow][col] = turn
    elif pop == True:
        columntobepopped = board[:,col]
        popped = np.roll(columntobepopped, 1) 
        popped[0] = 0 
        board[:,col] = popped

    return board.copy()

def check_victory(board, who_played):
    # implement your function here
    def checker(board, who_played):
        for c in range(4):
            for r in range(rows):
                if board[r][c] == who_played and board[r][c+1] == who_played and board[r][c+2] == who_played and board[r][c+3] == who_played:
                    return True

        for c in range(7):
            for r in range(rows-3):
                if board[r][c] == who_played and board[r+1][c] == who_played and board[r+2][c] == who_played and board[r+3][c] == who_played:
                    return True

        for c in range(4):
            for r in range(rows-3):
                if board[r][c] == who_played and board[r+1][c+1] == who_played and board[r+2][c+2] == who_played and board[r+3][c+3] == who_played:
                    return True

        for c in range(4):
            for r in range(3, rows):
                if board[r][c] == who_played and board[r-1][c+1] == who_played and board[r-2][c+2] == who_played and board[r-3][c+3] == who_played:
                    return True
    
    if checker(board, who_played) == True:
        return who_played
    else:
        return 0


def computer_move(board, turn, level):
    # implement your function here
    return (0,False)
    
def display_board(board):
    # implement your function here
    print(board)
    pass

def menu():
    # implement your function here
    print("Hello! Welcome to this game of Connect 4. :)\nPlease configure the following settings (type ex to exit the game)")
    print("")

    turn = 0
    global rows
    global poprow
    while True:
        try:
            rows = input("Please input the number of rows you want. Default is 6 (press enter without entering anything to get this), min is 4 and max is 10\nRows: ")
            if rows == "":
                rows = int(6)
                break
            else:
                rows = int(rows)
            break
        except:
            print("That's not funny. Please type in a number between 4 and 10 or just press enter")

    while rows < 4 or rows > 10:
        print("Please enter a valid number between 4 and 10")
        while True:
            try:
                rows = input("Please input the number of rows you want. Default is 6 (press enter without entering anything to get this), min is 4 and max is 10\nRows: ")
                if rows == "":
                    rows = int(6)
                    break
                else:
                    rows = int(rows)
                break
            except:
                print("That's not funny. Please type in a number between 4 and 10 or just press enter")
    
    col = 7
    board = np.zeros((rows, col))
    display_board(board)
    while True:
        move1 = input("Player 1: Which column do you want to drop your piece into or pop a piece from?\nAlternatively, type ex to quit the game: ")
        if move1 == "ex":
            break

        while True:
            try:
                move1 = int(move1) - 1 
                break
            except:
                print("Please type in an acceptable answer")
                move1 = input("Player 1: Which column do you want to drop your piece into or pop a piece from?")

        while True:
            if move1 < 0 or move1 > 6:
                print("Please type in an acceptable answer. It must be between 1 and 7")
                move1 = input("Player 1: Which column do you want to drop your piece into or pop a piece from?")
                try:
                    move1 = int(move1) - 1
                except:
                    print("Please type in an acceptable answer")
                    move1 = input("Player 1: Which column do you want to drop your piece into or pop a piece from?")
            else:
                break
        
        while True:
            pop = input("Do you want to pop the column or drop the piece into the column? Type P for pop and D to drop\nAnswer:")
            if pop == "P":
                pop = True
                break
            elif pop == "D":
                pop = False
                break
            else:
                print("Please type D or P only")
       
        while True:
            if check_move(board,turn,move1,pop) == True:
                if pop == False:
                    for r in range(rows):
                        if board[r][move1] == 0:
                            poprow = r
                    apply_move(board, 1, move1, pop)
                    display_board(board)
                    break
                if pop == True:
                    apply_move(board,1, move1, pop)
                    display_board(board)
                    break
            elif check_move(board,turn,move1,pop) == False:
                print("Invalid Move")
                move1 = input("Player 1: Which column do you want to drop your piece into or pop a piece from?")
                while True:
                    try:
                        move1 = int(move1) - 1 
                        break
                    except:
                        print("Please type in an acceptable answer")
                        move1 = input("Player 1: Which column do you want to drop your piece into or pop a piece from?")
                while move1 < 0 or move1 > 6:
                    print("Please type in an acceptable answer")
                    move1 = input("Player 1: Which column do you want to drop your piece into or pop a piece from?")
                    try:
                        move1 = int(move1) - 1
                    except:
                        print("Please type in an acceptable answer")
                        move1 = input("Player 1: Which column do you want to drop your piece into or pop a piece from?")
                while True:
                    pop = input("Do you want to pop the column or drop the piece into the column? Type P for pop and D to drop\nAnswer:")
                    if pop == "P":
                        pop = True
                        break
                    elif pop == "D":
                        pop = False
                        break
                    else:
                        print("Please type D or P only")
        
        if check_victory(board, 2) == 2:
            print("Player 2 Wins!")
            print("Thank you for playing!")
            break
        elif check_victory(board, 1) == 1:
            print("Player 1 Wins!")
            print("Thank you for playing!")
            break


# player 2 move
        move2 = input("Player 2: Which column do you want to drop your piece into or pop a piece from?\nAlternatively, type ex to quit the game: ")
        if move2 == "ex":
            break

        while True:
            try:
                move2 = int(move2) - 1 
                break
            except:
                print("Please type in an acceptable answer")
                move2 = input("Player 2: Which column do you want to drop your piece into or pop a piece from?")

        while True:
            if move2 < 0 or move2 > 6:
                print("Please type in an acceptable answer. It must be between 1 and 7")
                move2 = input("Player 2: Which column do you want to drop your piece into or pop a piece from?")
                try:
                    move2 = int(move2) - 1
                except:
                    print("Please type in an acceptable answer")
                    move2 = input("Player 2: Which column do you want to drop your piece into or pop a piece from?")
            else:
                break
        
        while True:
            pop = input("Do you want to pop the column or drop the piece into the column? Type P for pop and D to drop\nAnswer:")
            if pop == "P":
                pop = True
                break
            elif pop == "D":
                pop = False
                break
            else:
                print("Please type D or P only")
       
        while True:
            if check_move(board,turn,move2,pop) == True:
                if pop == False:
                    for r in range(rows):
                        if board[r][move2] == 0:
                            poprow = r
                    apply_move(board, 2, move2, pop)
                    display_board(board)
                    break
                if pop == True:
                    apply_move(board,2, move2, pop)
                    display_board(board)
                    break
            elif check_move(board,turn,move2,pop) == False:
                print("Invalid Move")
                move2 = input("Player 2: Which column do you want to drop your piece into or pop a piece from?")
                while True:
                    try:
                        move2 = int(move2) - 1 
                        break
                    except:
                        print("Please type in an acceptable answer")
                        move2 = input("Player 2: Which column do you want to drop your piece into or pop a piece from?")
                while move2 < 0 or move2 > 6:
                    print("Please type in an acceptable answer")
                    move2 = input("Player 2: Which column do you want to drop your piece into or pop a piece from?")
                    try:
                        move2 = int(move2) - 1
                    except:
                        print("Please type in an acceptable answer")
                        move2 = input("Player 2: Which column do you want to drop your piece into or pop a piece from?")
                while True:
                    pop = input("Do you want to pop the column or drop the piece into the column? Type P for pop and D to drop\nAnswer:")
                    if pop == "P":
                        pop = True
                        break
                    elif pop == "D":
                        pop = False
                        break
                    else:
                        print("Please type D or P only")
        
        if check_victory(board, 2) == 2:
            print("Player 2 Wins!")
            print("Thank you for playing!")
            break
        elif check_victory(board, 1) == 1:
            print("Player 1 Wins!")
            print("Thank you for playing!")
            break
        turn += 1


if __name__ == "__main__":
    menu()




    
