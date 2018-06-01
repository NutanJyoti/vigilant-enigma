board = ['','','','','','','','','','']

class project1():
    
    def display_board(self,passing_Num,player):
        t = int(passing_Num)
        if(player == 'player1'):
          board[t] = "x"
        if(player == 'player2'):
           board[t] = "o"
          
    
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
        
        
    def display_number(self,Name):
            a = input(Name + " enter a number") 
            return a
        
    def display_exit(self):
             b = input("Do you want to exit")
             print(b)
             
    def win_check(self,alp):
         return ((board[7] == alp and board[8] == alp and board[9] == alp) or # across the top
    (board[4] == alp and board[5] == alp and board[6] == alp) or # across the middle
    (board[1] == alp and board[2] == alp and board[3] == alp) or # across the bottom
    (board[7] == alp and board[4] == alp and board[1] == alp) or # down the middle
    (board[8] == alp and board[5] == alp and board[2] == alp) or # down the middle
    (board[9] == alp and board[6] == alp and board[3] == alp) or # down the right side
    (board[7] == alp and board[5] == alp and board[3] == alp) or # diagonal
    (board[9] == alp and board[5] == alp and board[1] == alp)) # diagonal
    
    
def main ():
    p = project1()
    store_win_value1=None
    store_win_value2=None
    choice=input("Do you want to play. Press yes or no 1")
    var =choice
    while var == 'yes':
     store_num1 = p.display_number("player1")
     p.display_board(store_num1,"player1")
     #logic for winner1
     store_win_value1 = p.win_check('x')
     if(store_win_value1):
      print("Player 1 You Won The game ")
      continue
   # passing_Num = p.display_number()
     store_num2 = p.display_number("player2")
     p.display_board(store_num2,"player2")
     
      #logic for winner2
     store_win_value2 = p.win_check('o')
     if(store_win_value2):
      print("Player 2 You Won The game ")
      continue
     
     choice=input("Do you want to play. Press yes or no 2")
     var = choice         
    print("exit from game")
    #p.display_bord(store_win_value)
    
    #p.display_exit('yes','no')
if __name__=="__main__":
    main()