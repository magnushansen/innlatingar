"""Tic Tac Toe"""


import numpy as np
import random


board1 = np.full((3, 3), " ", dtype = str)


def intro():
    """This  function introduces the rules of the game Tic Tac Toe"""

    print("Welcome to Tic Tac Toe!!")
    
    print("The rules are simple, get 3 of your marks aligned up either in a row, "
          "column or diagonal manner to win the game.")
    
    play = input("Would you like to play a game of Tic Tac Toe? (Y/N): ")

    print('\nBelow board indicates how to choose your position')
    
    if play.lower() == "y":
    
        return True
    
    else:
    
        return False
    



def create_board():
    """Creates the board"""

    print(board1[0][0] + ' | ' + board1[0][1] + ' | ' + board1[0][2] + '     ' + '1' + ' | ' + '2' + ' | ' + '3')
    print('---------     ' + '---------')
    print(board1[1][0] + ' | ' + board1[1][1] + ' | ' + board1[1][2] + '     ' + '4' + ' | ' + '5' + ' | ' + '6')
    print('---------     ' + '---------')
    print(board1[2][0] + ' | ' + board1[2][1] + ' | ' + board1[2][2] + '     ' + '7' + ' | ' + '8' + ' | ' + '9')
    print('\n')



def playerinput(board,player):
    """Checks and places the marker on the position for the player"""

    while True:
        
        position = input("Which position would you like to choose? ")

        create_board()

        mapping = {
                "1": (0, 0), "2": (0, 1), "3": (0, 2),
                "4": (1, 0), "5": (1, 1), "6": (1, 2),
                "7": (2, 0), "8": (2, 1), "9": (2, 2),
            }


        if position in mapping:
            
            row, col = mapping[position]
            
            if board1[row][col] == " ":
                
                board1[row][col] = player
                                
                return True
                break
            
            else:
            
                print("Cell already taken. Try again.")
                
                continue
                return(False)



def computer_choice(board,player):
    """Checks and places the marker on the position for the computer"""


    mapping = {
            "1": (0, 0), "2": (0, 1), "3": (0, 2),
            "4": (1, 0), "5": (1, 1), "6": (1, 2),
            "7": (2, 0), "8": (2, 1), "9": (2, 2),
        }


    while True:
        position = str(random.randint(1,9)) 

        if position in mapping:
            
            row, col = mapping[position]


        if board[row][col] == " ":
                
            board[row][col] = player
            
            
            print('CPU moves')
            
            
            return True
            break
            
        else:
            
            continue


def check_win(player):
    """Check for a win by using np.any"""

    if np.any(np.all(board1 == player, axis=1)):
            
            create_board()
            
            print(f'The winner is {player}')
            
            return True

    
    if np.any(np.all(board1 == player, axis=0)):
        
        create_board()
        
        print(f'The winner is {player}')
        
        return True

    
    if np.all(np.diag(board1) == player) or np.all(np.diag(np.fliplr(board1)) == player):
        
        create_board()
        
        print(f'The winner is {player}')
        
        return True

    return False
        

def check_tie():
    """Checks if there's a tie"""

    create_board()

    return np.all(board1 != " ")

    

player1=None
player2=None

def play_game():
    """plays the game of tic tac toe involving two humans or a computer and a human"""
    
    global player1, player2
    
    player = 'X'
    
    start = intro()
    
    create_board()

    if start:
        
        game_mode = int(input("Please enter 1 or 2, whether " 
                              "you wanna play against a person or a computer "))

        if game_mode == 1:
            
            player1 = 'X'
            player2 = 'O'

            current_player = player1
            
            create_board()

            while True:
                
                
                
                playerinput(board1, current_player)
                
                if check_win(current_player):
                   
                    break

                if check_tie():
                    
                    print("It's a tie")
                   
                    break

                current_player = player2 if current_player == player1 else player1




        elif game_mode == 2:

            order_choice = input("Do you want to go first? (Y/N): ").lower()

            if order_choice == 'y':
                
                player1 = 'X'               
                player2 = 'O'
                current_player = player1
            
            else:
                
                player1 = 'O'
                player2 = 'X'
                current_player = player2

            create_board()
                    
            while True:
                
                      
                if current_player == player1:
                    
                    playerinput(board1, current_player)
                    
                    
                else:
                    computer_choice(board1, current_player)  
                   
                    

                if check_win(current_player):
                    
                    break

                if check_tie():
                    
                    print("It's a tie")
                    
                    break

                current_player = player2 if current_player == player1 else player1
                

play_game()



