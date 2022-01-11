
def display_board(b,bap):
    print()
    print(b[0] + " | " + b[1] + " | "+b[2] + "    *   " + str(bap[0]) + " | " + str(bap[1]) + " | "+ str(bap[2]))
    print(b[3] + " | " + b[4] + " | "+b[5] + "    *   " + str(bap[3]) + " | " + str(bap[4]) + " | "+ str(bap[5]))
    print(b[6] + " | " + b[7] + " | "+b[8] + "    *   " + str(bap[6]) + " | " + str(bap[7]) + " | "+ str(bap[8]))
    print()



def check_win(sign, board):
    
    
    #check rows
    if board[0] == board[1] == board[2] == sign :
        return True
    
    elif board[3] == board[4] == board[5] == sign:
        return True

    
    elif board[6] == board[7] == board[8] == sign:
        return True

    
    
    
    
    #columns
    elif board[0] == board[3] == board[6] == sign:
        return True
    
    elif board[1] == board[4] == board[7] == sign:
        return True
    
    elif board[2] == board[5] == board[8] == sign:
        return True
    
    
    #Diagonals
    elif board[0] == board[4] == board[8] == sign:
        return True
    
    elif board[2] == board[4] == board[6] == sign:
        return True
    
    
    
    else:
        return False



player_X = input("You are playing X's. Please enter your name: ") 
player_O = input("You are playing O's. Please enter your name: ")

n_sets = int(input("choose how many sets in the game: "))
score_X =0
score_O =0
#make  function check_winner(board, player )
#this function checks all different 8 possibilities for a player to win
# if a player wins then return True, if not return False

for count in range(n_sets):
    
    #print the number of round we are playing in
    print()
    print()
    print("ROUND NUMBER " + str(count+1))
    
    #SET/ROUND STARTS HERE
    
    board= ["-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"]


    board_available_positions = [1,2,3,4,5,6,7,8,9]

    counter=0

    while True:

       
        print()
        print()
        display_board(board,board_available_positions)
        print("It is " +player_X + "'s turn. sign:X")
        position = input("position:")
        
        #check that the move/input is valid
        
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("please choose a position from 1 to 9 :")
        
        while int(position) not in board_available_positions:
            position = input("that position is taken, please choose another one: ")
            
            while position not in ["1","2","3","4","5","6","7","8","9"]:
                position = input("please choose a position from 1 to 9 :")
        
        
        
        board[int(position) -1 ]= "X"
        board_available_positions[int(position) -1 ] = " "
        
        counter = counter +1
        
        if check_win("X",board):
            display_board(board,board_available_positions)
            print(player_X + " WON THE GAME. X'S WIN")
            score_X = score_X+1
            break
        
        #check if X won
        #check_win(sign, board)
        #return True if the player that has sign won
        #false otherwise(if he didnt win )
        
        
      
        if counter ==9:
            print("It is a tie")
            break
        print()
        print()
        display_board(board,board_available_positions)
        print("It is " +player_O + "'s turn. sign:O")
        position = input("position:")
        
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("please choose a position from 1 to 9 :")
        
        while int(position) not in board_available_positions:
            position = input("that position is taken, please choose another one: ")
            
            while position not in ["1","2","3","4","5","6","7","8","9"]:
                position = input("please choose a position from 1 to 9 :")
        
        
        
      
        board_available_positions[int(position) -1 ] = " "
        
        board[int(position) -1 ]= "O"
        counter = counter +1
        
        #check if O won
        if check_win("O",board):
            display_board(board,board_available_positions)
            print(player_O + " WON THE GAME. O'S WIN")
            score_O = score_O+1
            break

    #SET/ROUND END HERE
        
    #DISPLAY THE SCORE
    print()
    print(player_X +": " + str(score_X))
    print(player_O +": " + str(score_O))
    print("============================================")
    #CHECK IF THERE IS A PLAYER WHO WON THE WHOLE GAME
    
    sets_to_win_the_game = n_sets//2 +1
    
    if score_X == sets_to_win_the_game:
        print("============================================")
        print(player_X + " WON  THE WHOLE GAME. CONGRATS")
        break
    elif score_O == sets_to_win_the_game:
        print("============================================")
        print(player_O + " WON  THE WHOLE GAME. CONGRATS")
        break
    
    

