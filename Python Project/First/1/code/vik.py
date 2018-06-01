
a = input( " enter a number") 
player="player1"            
board = ['','','','','','','','','','']

def display_board(self,passing_Num,player):
       #board=['','','','','','','','','','']
       t = int(passing_Num)
       if(player == 'player1'):
          board[t] = "x"
       if(player == 'player2'):
          board[t] = "y"
    
       print("   |   |")
       print(' ' + str(board[7]) +'  | ' + str(board[8]) + '  | ' + str(board[9]) )
       print("   |   |")
       print('--------------')
       print("   |   |")
       print(' ' + str(board[4]) +'  | ' + str(board[5]) + '  | ' + str(board[6]) )
       print("   |   |")
       print('--------------')
       print("   |   |")
       print(' ' + str(board[1]) +'  | ' + str(board[2]) + '  | ' + str(board[3]) )
       print("   |   |")
        
        
